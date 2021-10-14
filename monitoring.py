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