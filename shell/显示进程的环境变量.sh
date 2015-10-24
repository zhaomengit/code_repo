# 显示进程的环境变量信息

tr \\0 \\n < /proc/${PID}/environ
