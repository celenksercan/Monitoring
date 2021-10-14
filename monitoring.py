  import psutil


def monitor_cpu_times():
    print("\n CPU TIMES")
    cpu_times=psutil.cpu_times()
    user_time=round(cpu_times.user/3600)
    system_time=(cpu_times.system/3600)
    idle_time=round(cpu_times.idle/3600)
    print("Time spent on processes by the User: {}".format(user_time))
    print("Time spent on processes by the System: {}".format(system_time))
    print("Time spent on processes by the Idle: {}".format(idle_time))

def monitor_cpu_util():
    print("\ CPU UTIL")
    print(psutil.cpu_percent())
    
def monitor_cpu_cores():
    print("\n CPU CORES")
    print(psutil.cpu_count())
    
    
def monitor_cpu_freq():
    print("\n CPU FREQUENCIES")
    print("{} Mhz".format(psutil.cpu_freq().current))
    
    
def monitor_ram():
    print("\n RAM USAGE")
    virtual_memory=psutil.virtual_memory()
    print("Total Memory {} bytes".format(virtual_memory.total))
    print("Available Memory {} bytes".format(virtual_memory.available))
    print("Used Memory {} bytes".format(virtual_memory.used))
    print("Percent used {}% ".format(virtual_memory.percent))
    
    
    
def monitor_disk():
    print("\n DISK PARTITIONS")
    print(psutil.disk_partitions())

    
def monitor_disk_usage():
    print("\n DISK IMAGE")
    disk_usage=psutil.disk.usage('/')
    print("Total Memory {} bytes".format(disk_usage.total))
    print("Free Memory {} bytes".format(disk_usage.free))
    print("Used Memory {} bytes".format(disk_usage.used))
    print("Percent used {}% ".format(disk_usage.percent))
    
    
def monitor_network():
    print("\n NETWORK REQUESTS")
    io_stats=psutil.net_io_counters()
    print("Total Bytes Sent {} ".format(io_stats.bytes_sent))
    print("Total Bytes Received {}".format(io_stats.bytes_recv))

    
def monitor_battery():
    print("\n MONITOR BATTERY")
    battery_info=psutil.sensor_battery()
    print("Battery Percent: {}".format(battery_info.percent))
    print("Seconds left: {}".format(battery_info.secsleft))
