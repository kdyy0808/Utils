import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from geometry_msgs.msg import PoseWithCovarianceStamped
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import transforms3d
import numpy as np
import csv
import os
import signal
import sys
import datetime
import threading
import time

class AmclPoseSubscriber(Node):
    def __init__(self):
        super().__init__('amcl_pose_subscriber')
        self.subscription = self.create_subscription(
            PoseWithCovarianceStamped,
            'amcl_pose',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.x_data = []
        self.y_data = []
        self.heading_data = []
        self.is_running = True
        self.lock = threading.Lock()
        self.data_updated = threading.Event()

    def listener_callback(self, msg):
        with self.lock:
            if not self.is_running:
                return
            print("get")
            position = msg.pose.pose.position
            x = position.x
            y = position.y

            orientation = msg.pose.pose.orientation
            quaternion = (
                orientation.w,
                orientation.x,
                orientation.y,
                orientation.z
                
            )
            euler = transforms3d.euler.quat2euler(quaternion)
            heading = euler[2]  # Yaw 값
            #heading = orientation.z # Yaw 값
            #print(f"Heading 1: {heading1}")
            print(f"Heading : {heading}")
            self.x_data.append(x)
            self.y_data.append(y)
            self.heading_data.append(heading)
            self.data_updated.set()  # 새로운 데이터가 추가되었음을 알림

    def save_data_to_file(self, filename):
        with self.lock:
            if len(self.x_data) > 0:
                with open(filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['x', 'y', 'heading'])
                    for x, y, heading in zip(self.x_data, self.y_data, self.heading_data):
                        writer.writerow([x, y, heading])

    def cleanup(self):
        with self.lock:
            self.is_running = False
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'amcl_pose_data_{timestamp}.csv'
        self.save_data_to_file(filename)
        print(f"Data saved to {filename}")
        self.destroy_node()
        plt.close('all')

def main(args=None):
    rclpy.init(args=args)
    node = AmclPoseSubscriber()
    
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    shutdown_event = threading.Event()

    def signal_handler(sig, frame):
        print("Shutdown signal received. Initiating shutdown...")
        shutdown_event.set()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    executor_thread = threading.Thread(target=executor.spin, daemon=True)
    executor_thread.start()

    try:
        while not shutdown_event.is_set():
            if node.data_updated.is_set():
                print("New data received. Press Ctrl+C to stop and save data.")
                node.data_updated.clear()
            time.sleep(0.1)
    except Exception as e:
        print(f"Exception in main thread: {e}")
    finally:
        print("Cleaning up...")
        node.cleanup()
        executor.shutdown()
        rclpy.shutdown()
        
        # 강제 종료 타이머 설정
        force_quit_timer = threading.Timer(5.0, lambda: os._exit(0))
        force_quit_timer.start()
        
        executor_thread.join(timeout=4.0)
        if executor_thread.is_alive():
            print("Warning: Executor thread did not terminate gracefully")
        
        force_quit_timer.cancel()  # 정상 종료 시 타이머 취소
        print("Shutdown complete")

if __name__ == '__main__':
    main()