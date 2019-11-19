"""
信号方法处理
"""

import os
import signal

pid = os.fork()

# 子进程退出时父进程忽略,子进程由系统处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

if pid < 0:
    print("Error")
elif pid == 0:
    print("child PID:", os.getppid())
else:
    while True:
        pass
