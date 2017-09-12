System wide File Descriptors(FD) limits:
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
