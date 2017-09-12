1. System Wide  
file: /etc/sysctl.conf  
Query File Descriptors(FD) limits:
```bash
cat /proc/sys/fs/file-max
sysctl fs.file-max
```
and, in file /etc/sysctl.conf

Set limits:
```bash
sysctl -w fs.file-max=100000
```
Or, append the following line in /ect/sysctl.conf:
fs.file-max = 100000
Relogin or:
```bash
sysctl -p
```

2. Per user  
file: /etc/security/limits.conf  
Hard limit:
```bash
ulimit -Hn
```
Soft limit:
```bash
ulimit -Sn
```
Edit in /etc/security/limits.conf:
```vim
# Example hard limit for max opened files
marin        hard nofile 4096
# Example soft limit for max opened files
marin        soft nofile 1024
```

