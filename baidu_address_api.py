# -*- encoding: utf-8 -*-
'''
@File    :   address_API.py
@Time    :   2020/09/07 15:57:42
@Author  :   DataMagician 
@Version :   1.0
@Contact :   408903228@qq.com
'''

# here put the import lib
import requests
import json

def getUrl(*address):
    '''
    调用地图API获取待查询地址专属url
    最高查询次数30w/天，最大并发量160/秒
    '''
    ak = 'Vhzgfjih2w3YY0WUPuPdKiMQKwIor9rp'
    if len(address) < 1:
        return None
    else:
        for add in address:   
            url = 'http://api.map.baidu.com/geocoding/v3/?address={inputAddress}&output=json&ak={myAk}'.format(inputAddress=add,myAk=ak)  
            yield url
            
def getPosition(url):
    '''返回经纬度信息'''
    res = requests.get(url)
    json_data = json.loads(res.text)
    
    if json_data['status'] == 0:
        lat = json_data['result']['location']['lat'] #纬度
        lng = json_data['result']['location']['lng'] #经度
        precise = json_data['result']['precise']
        confidence = json_data['result']['confidence']
        comprehension = json_data['result']['comprehension']
        level = json_data['result']['level']
    else:
        print("Error output!")
        return json_data['status']
    return lat,lng,precise,confidence,comprehension,level

def getStrings(address):
    for add in address:
        add_url = list(getUrl(add))[0]
        print(add_url)
        try:
            lat,lng,precise,confidence,comprehension,level = getPosition(add_url) 
            print("地址：{0}|经度:{1}|纬度:{2}|精度:{3}|置信度:{4}|解释性:{5}|分类等级:{6}".format(add,lat,lng,precise,confidence,comprehension,level))
        except Error as e:
            print(e)

def getDict(address):
    column = ["地址","经度","纬度","精度","置信度","解释性","分类等级"]
    addressL,latL,lngL,preciseL,confidenceL,comprehensionL,levelL = [],[],[],[],[],[],[]
    n = -1
    for add in address:
        addressL.append(add)
        lat,lng,precise,confidence,comprehension,level  = getPosition(list(getUrl(add))[0])
        latL.append(lat)
        lngL.append(lng)
        preciseL.append(precise)
        confidenceL.append(confidence)
        comprehensionL.append(comprehension)
        levelL.append(level)
                
    return {cn : data for cn , data in zip(column,(addressL,latL,lngL,preciseL,confidenceL,comprehensionL,levelL))}
if __name__ == "__main__":
    print("输入要查询的地址:")
    str_= input()
    location_info = getDict([str_])
    print(location_info)

