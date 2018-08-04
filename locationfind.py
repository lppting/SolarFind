#-*- coding:utf-8 -*-
import requests
import json

def location():
    head_url = "http://api.map.baidu.com/cloudgc/v1?"
    address = "address=娄星区学院路422号&city=湖南"
    ak = "&ak=DC74lWZ0Ql5RSgL87E31KPHG36VyjxCs"
    url = head_url + address + ak
    r = requests.get(url)
    content = r.text
    baiduAddr = json.loads(content)
    addr =  baiduAddr["result"][0]["location"]
    str =  json.dumps(addr)
    t1 =  str.replace("{","").replace("}","")
    t2 = t1.split(",")
    return content

def WriteData():
    data = json.dumps(location())
    print data
    f = open("location.log","w+")
    f.write(data)
    f.close()
def ReadData():
    f = open("location.log","r+")
    text = f.read()
    local = json.loads(text)
    t1 = json.loads(local)
    t2 =  t1["result"][0]["location"]
    str =  json.dumps(t2)
    t3 =  str.replace("{","").replace("}","")
    t4 = t3.split(",")
    f.close()
    return t4

if __name__ == "__main__":
    WriteData()
