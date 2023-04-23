printf "检查TCP连接情况"
netstat -ant | grep 'ESTABLISHED' | awk -F " " '{print $5}' | awk -F ":" '{print $1}' | sort -n | uniq -c| sort -t " " -k 1 -nr