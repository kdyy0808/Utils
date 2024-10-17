import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import csv
import sys

def load_data_from_file(filename):
    x_data, y_data, heading_data = [], [], []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            x, y, heading = map(float, row)
            x_data.append(x)
            y_data.append(y)
            heading_data.append(heading)
    return x_data, y_data, heading_data

def plot_trajectory(x_data, y_data, heading_data):
    fig, ax = plt.subplots(figsize=(10, 8))
    line, = ax.plot([], [], 'bo-', lw=2, markersize=4)
    arrow = ax.arrow(0, 0, 0, 0, head_width=0.05, head_length=0.1, fc='r', ec='r')

    ax.set_xlim(min(x_data) - 1, max(x_data) + 1)
    ax.set_ylim(min(y_data) - 1, max(y_data) + 1)
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_title('Robot Trajectory with Direction')
    ax.grid(True)

    def init():
        line.set_data([], [])
        arrow.set_data(x=0, y=0, dx=0, dy=0)
        return line, arrow

    def animate(frame):
        line.set_data(x_data[:frame+1], y_data[:frame+1])
        
        if frame > 0:
            x, y = x_data[frame], y_data[frame]
            heading = heading_data[frame]
            dx = 0.2 * np.cos(heading)
            dy = 0.2 * np.sin(heading)
            arrow.set_data(x=x, y=y, dx=dx, dy=dy)

        return line, arrow

    ani = animation.FuncAnimation(fig, animate, frames=len(x_data),
                                  init_func=init, blit=True, interval=100)
    plt.show()

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_csv_file>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        x_data, y_data, heading_data = load_data_from_file(filename)
        plot_trajectory(x_data, y_data, heading_data)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()