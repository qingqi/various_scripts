# find the binary file path for process
readlink -f /proc/<pid>/exe


# xargs 可以读入 stdin 的资料，并且以空白字元或断行字元作为分辨，将 stdin 的资料分隔成为 arguments
redis-cli keys "*" | xargs redis-cli del


# 每5s运行一次 free -m，就是监控该命令的执行结果
watch -n 5 free -m


"$@" # separate word
"$*" # single word
