printf "检查UPD连接情况"
netstat -anu | awk -F " " '{print $5}' | awk -F ":" '{print $1}' | sort -n | uniq -c | sort -t " " -k 1 -nr