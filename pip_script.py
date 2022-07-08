#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   piplog.py
@Time    :   2020/09/06 11:58:15
@Author  :   JohnRain
@Contact :   iamjohnrain@163.com
@Department   :  Sun Yat-Sen University
@Desc    :   None
'''

# here put the import lib


def os_type(win=None,linux=None,Mac=None):
    platform = __import__('platform').system().lower() 
    if platform == 'windows':
        print("windows")
        return win
    elif platform == 'linux':
        print("linux")
        return linux
    elif platform == 'darwin':
        print("Mac OS")
        return Mac

def pip3install(packge=None, keyword='清华',cmd = 'pip'):
    cmd = os_type(win='pip',linux='pip3',Mac='pip3')
    if packge == None:
        return 'please input you packge name'
    else:
        source = {'阿里':' -i https://mirrors.aliyun.com/pypi/simple'
        ,'清华':' -i https://pypi.tuna.tsinghua.edu.cn/simple/'
        ,'中科大':' -i https://pypi.mirrors.ustc.edu.cn/simple/'
        ,'华中理工大':' -i http://pypi.hustunique.com/'
        ,'山东理工大':' -i http: // pypi.sdutlinux.org /'
        ,'豆瓣':' -i http://pypi.douban.com/simple/'}
        __import__('os').system(cmd + ' install ' + str(packge) + source[keyword])

print("pelace in put pkg name:")
pakname = input()
change = {1:'阿里',2:'清华',3:'中科大',4:'华中理工大',5:'山东理工大',6:'豆瓣'}
print('pelace change src:',change)
pip3install('httpx',change[int(input())])


