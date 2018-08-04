#-*- coding:utf-8 -*-
import requests
import re
import json

headers = {"Connection": "keep-alive",
           "Pragma": "no-cache",
           "Cache-Control": "no-cache",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
           "Accept": "*/*",
           "Referer": "http://www.weather.com.cn/weather1dn/101250804.shtml",
           "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
           "Cookie": "vjuids=-1f178ca6d.164a7830b51.0.f16eeb5d32649; vjlast=1531818741.1531818741.30; UM_distinctid=164a7830bdf67c-0c72a4cf9b674a-5b193413-100200-164a7830be015a; f_city=%E5%A8%84%E5%BA%95%7C101250801%7C; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1531818740,1531818813,1531819094,1531820819; Wa_lvt_1=1531818743,1531818814,1531819094,1531820819; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1531821262; Wa_lpvt_1=1531821262",
           "Accept-Encoding": "gzip, deflate",
           }
url = "http://d1.weather.com.cn/sk_2d/101250804.html?_=1531821262009"

def weather():
    r = requests.get(url,headers=headers)
    r.encoding="utf-8"
    t1 = r.text
    pattern= r"{.*}"
    t2 = re.findall(pattern,t1)
    t3 = json.loads(t2[0])
    return t3

if __name__ == "__main__":
    weather()
