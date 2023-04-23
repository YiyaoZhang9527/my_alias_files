import random
import  datetime
import os
import sys
from log_color import LogLevel, log

def sys_info():
    '''
    反馈当前层级系统信息
    '''
    date_time_p = datetime.datetime.now()
    date_strings = str(date_time_p).replace("-","") 
    os.path.abspath(sys.argv[0])#得到执行文件的绝对路径： 
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    file_path = os.path.join(dirname,filename)
    return date_strings,dirname,filename,file_path


def generate(mine_lenght=None,max_length=16,tags=None,one_range=None,add_symbols = None):
    date_strings,dirname,filename,file_path = sys_info()
    #print(date_strings,dirname,filename)
    result = []
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    number_letters ="1234567890"
    symbol = "-～@&^"
    pass_word_elements = list("{}{}{}".format(number_letters,capital_letters,lowercase_letters,symbol))
    
    if one_range:
        pass_word_elements = one_range
    elif add_symbols and isinstance(add_symbols,str):
        pass_word_elements = pass_word_elements+list(add_symbols)

    if mine_lenght == None:
        length = random.randint(12,max_length)
    elif (mine_lenght != None) and isinstance(mine_lenght,int) and (mine_lenght <= max_length):
        length = random.randint(mine_lenght,max_length)
    elif mine_lenght == max_length or mine_lenght > max_length:
        length = mine_lenght
    else:
        return "Error"
    #log(pass_word_elements,LogLevel.PASS)
    for _ in range(0,length+1):
        #print(_)
        index_ = random.randint(0,len(pass_word_elements)-1)
        result.append(pass_word_elements[index_])

    body = {"密码长度":_,"生成的密码":"".join(result),"密码标签":tags,"创建时间":date_strings}
    f = open(dirname+os.sep+"passdict",'a+')
    f.write(body.__repr__()+"\n")
    f.close()

    return body


if __name__ == '__main__':
    # generate(mine_lenght=21,max_length=30,tags="HuaweiJumpServer")
    # generate(mine_lenght=24,max_length=30,tags="AliCrawlerServer")
    # generate(mine_lenght=19,max_length=30,tags="TencentServer5M")
    # generate(mine_lenght=25,max_length=30,tags="TencentServer1M")
    # generate(mine_lenght=25,max_length=30,tags="TencentNetworkServer5M")
    # generate(mine_lenght=16,max_length=16,tags="kite")
    log("请输入本次创建密码的最大长度(小于10位则默认生成10位)",LogLevel.INFO)
    minLenght = int(input())
    log("请输入本次创建密码的最大长度(小于10位则默认生成10位)",LogLevel.INFO)
    maxLenght = int(input())
    log("请输入本次创建密码的主题",LogLevel.INFO)
    titile = input()
    for k,v in generate(mine_lenght=(minLenght <10 and 10 or minLenght)
                        ,max_length=(10 < maxLenght <60 and 10 or maxLenght)
                        ,tags=titile
                        ,add_symbols="").items():
        log((k,v),LogLevel.INFO)
    
