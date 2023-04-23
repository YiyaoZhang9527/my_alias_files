import os
from re import I


def hook_command(url):
    command = "{}{}{}{}".format("youtube-dl -F ",'"',url,'"')
    return command


if __name__ == '__main__':
    print("请输入url:")
    input_url=input()
    print("测试视频下载格式的命令是 :")
    print(hook_command(input_url))
    

    
