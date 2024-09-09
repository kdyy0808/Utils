import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime
import subprocess
import os
import signal
import argparse
import threading

# 기본적으로 제외할 토픽 목록
DEFAULT_EXCLUDED_TOPICS = [
    '/rosout', '/rosout_agg',
    '/parameter_events',
    '/input_topic'
]

class TimedBagRecorder(Node):
    def __init__(self, max_size_mb, excluded_topics):
        super().__init__('timed_bag_recorder')
        self.publisher_ = self.create_publisher(String, 'formatted_wallclock', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        
        self.max_size_bytes = int(max_size_mb * 1024 * 1024)  # Convert MB to bytes
        
        # Bag 파일 저장 경로 설정
        self.bag_path = f'timed_recording_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
        
        # 모든 토픽 가져오기
        all_topics = self.get_all_topics()
        
        # 제외할 토픽 필터링
        topics_to_record = [topic for topic in all_topics if topic not in excluded_topics]
        
        # ros2 bag record 명령어 구성
        record_command = ['ros2', 'bag', 'record', '-o', self.bag_path] + topics_to_record
        
        # 디버그: 실행할 명령어 출력
        self.get_logger().info(f'Executing command: {" ".join(record_command)}')
        
        # ros2 bag record 프로세스 시작
        self.bag_process = subprocess.Popen(
            record_command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            preexec_fn=os.setsid
        )

        print(f'Started recording to {self.bag_path}')
        print(f'Recording will stop at {max_size_mb:.2f} MB')
        print(f'Excluded topics: {", ".join(excluded_topics)}')
        print(f'Recording topics: {", ".join(topics_to_record)}')
        
        self.shutdown_flag = threading.Event()

    def get_all_topics(self):
        # 모든 토픽 목록 가져오기
        result = subprocess.run(['ros2', 'topic', 'list'], capture_output=True, text=True)
        return result.stdout.strip().split('\n')

    def timer_callback(self):
        if self.shutdown_flag.is_set():
            return

        current_time = datetime.now()
        formatted_time = current_time.strftime("%m/%d %H:%M:%S")
        msg = String()
        msg.data = formatted_time
        self.publisher_.publish(msg)
        #print(f'Publishing: {msg.data}')
        
        # 현재 bag 파일의 크기 확인
        bag_size = self.get_directory_size(self.bag_path)
        if bag_size >= self.max_size_bytes:
            print(f'Bag file reached {bag_size/1024/1024:.2f}MB. Stopping recording.')
            self.stop_recording()
            self.shutdown_flag.set()
            print('Initiating shutdown sequence...')
            # 종료 시퀀스를 별도의 스레드에서 실행
            threading.Thread(target=self.shutdown_sequence).start()

    def shutdown_sequence(self):
        self.destroy_node()
        rclpy.shutdown()
        print("Node has been shut down.")
        os._exit(0)  # 강제 종료

    def get_directory_size(self, path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def stop_recording(self):
        if self.bag_process:
            try:
                # ros2 bag record 프로세스 그룹 종료
                os.killpg(os.getpgid(self.bag_process.pid), signal.SIGINT)
                self.bag_process.wait(timeout=5)  # 5초 동안 대기
            except subprocess.TimeoutExpired:
                # 타임아웃 발생 시 강제 종료
                os.killpg(os.getpgid(self.bag_process.pid), signal.SIGKILL)
            except ProcessLookupError:
                # 프로세스가 이미 종료된 경우
                pass
            finally:
                self.bag_process = None
            print('Stopped bag recording')

    def __del__(self):
        if hasattr(self, 'bag_process') and self.bag_process:
            self.stop_recording()

def main(args=None):
    # 커맨드 라인 인자 파싱
    parser = argparse.ArgumentParser(description='ROS2 Bag Recorder with size limit and topic exclusion')
    parser.add_argument('--max-size', type=float, default=4096.0, help='Maximum bag size in MB (default: 4096.0 MB = 4GB)')
    parser.add_argument('--exclude', nargs='*', default=None, help='Additional topics to exclude from recording')
    parser.add_argument('--include-all', action='store_true', help='Include all topics, overriding default exclusions')
    parsed_args, remaining_args = parser.parse_known_args()

    if parsed_args.include_all:
        excluded_topics = []
    else:
        excluded_topics = DEFAULT_EXCLUDED_TOPICS.copy()
        if parsed_args.exclude:
            excluded_topics.extend(parsed_args.exclude)

    rclpy.init(args=remaining_args)
    timed_bag_recorder = TimedBagRecorder(parsed_args.max_size, excluded_topics)
    try:
        rclpy.spin(timed_bag_recorder)
    except KeyboardInterrupt:
        pass
    finally:
        if not timed_bag_recorder.shutdown_flag.is_set():
            timed_bag_recorder.stop_recording()
        timed_bag_recorder.destroy_node()
        try:
            rclpy.shutdown()
        except rclpy._rclpy_pybind11.RCLError:
            # 이미 셧다운된 경우 무시
            pass
        print("Program has completed.")

if __name__ == '__main__':
    main()