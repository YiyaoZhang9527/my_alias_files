import requests
import re

def DNSinfo():
    rsp_src = requests.get("http://nstool.netease.com").text
    url = re.findall("<iframe src='(.*)/' frameborder=0", rsp_src)[0]
    rsp = requests.get(url).text.split("<br>")
    return rsp[1].split(),rsp[2].split()
print(DNSinfo())
