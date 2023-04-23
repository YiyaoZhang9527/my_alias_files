
def download_command(format_code,url):
    command = "{}{}{}{}{}".format("youtube-dl -f ",format_code,' "',url,'"')
    return command


if __name__ == '__main__':
    print("请输入format code :")
    input_fromat_code = input()
    print("请输入url:")
    input_url=input()
    print(download_command(input_fromat_code,input_url))