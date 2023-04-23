import subprocess
import datetime
import sys


now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(" ","")

def creat_command(key_name=now,mail_or_lab=now,key_type="ECC"):
    if key_type == "RSA":
        key_type = "rsa -b 2048"
    elif key_type == "ECC":
        key_type = "ed25519"
    command = "{}{}{}{}{}{}{}{}".format(
        'ssh-keygen -t ',key_type,' -f ~/.ssh/',key_name,' -C ' , '"',mail_or_lab,'"')
    return command



if __name__ == '__main__':
    # mail_or_lab = "408903228zyy@gmail.com"
    # key_name = "TencentServer5M"
    # key_type = "ed25519" 

    print("请输入所选的密钥类型:\n1:RSA\n2:ECC(椭圆加密)")
    change_type = {1:"RSA",2:"ECC"}
    input_type = change_type[int(input())]
    print("本次密钥的加密方式为:",input_type)

    print("\n\n请选择此密钥的命名方式:\n1:放弃命名用当前时间代替\n2.输入所用密钥名称")
    input_name = int(input())
    if input_name==1:
        print("你放弃了密钥命名，本次采用当前时间作为密钥名称")
        input_name = now
    elif input_name==2:
        print("现在请输入你为此密钥准备的名称：")
        input_name = input()
    else:
        print("必须做出操作选择！！！！")
        sys.exit()
    print("所用密钥名称：",input_name)

    print("\n\n请输选择公钥中体现标签的创建方式:\n1:放弃命名用当前时间代替\n2.输入用公钥标签名称")
    input_lab = int(input())
    if input_lab==1:
        print("你放弃了公钥标签的命名，本次采用当前时间作为密钥名称")
        input_lab=now
    elif input_lab == 2:
        print("现在请输入你为此公钥准备的标签名称：")
        input_lab=input()
    else:
        print("必须做出操作选择！！！！")
        sys.exit()

    command_str = creat_command(key_name=input_name,mail_or_lab=input_lab,key_type=input_type)
    print("生成创建命令:",command_str)
    print("{}{}".format("公钥文件地址在：~/.ssh/",input_name))
    print("{}{}".format("私钥文件地址在：~/.ssh/",input_name,".pub"))
    print(subprocess.getoutput(command_str))

    #print(creat_command)22
