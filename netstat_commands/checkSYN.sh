echo "检查SYN攻击"
netstat -ant | grep 'SYN' | awk -F " " '{print $5}' | awk -F ":" '{print $1}' | sort -n | uniq -c| sort -t " " -k 1 -nr