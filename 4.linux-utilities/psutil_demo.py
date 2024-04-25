import psutil
import time

def monitor_system():
    print("CPU Usage:", psutil.cpu_percent())
    print("Memory Usage:", psutil.virtual_memory().percent)
    print("Disk Usage:")
    for partition in psutil.disk_partitions():
        print(f"  {partition.device}: {psutil.disk_usage(partition.mountpoint).percent}%")

if __name__ == '__main__':
    while True:
        monitor_system()
        time.sleep(5)  # Update every 5 seconds