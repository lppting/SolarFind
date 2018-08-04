#-*- coding:utf-8 -*-
import numpy
import datetime
import os
import requests
import json
import re
import time
import math

#获取经纬度坐标，使用的是百度地图
def location():
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

#返回维度值
def Lat():
    local_lat = location()
    latdata = local_lat[0][7:]
    return latdata

#返回经度值
def Lng():
    local_lng = location()
    lngdata = local_lng[1][7:]
    return lngdata

#计算天数   
def date():
    now = time.localtime(time.time())
    year = now.tm_year
    month = int(now.tm_mon)
    day = now.tm_mday
    N = 0
    if year % 4 == 0:
        if month == 1:
            N = day
        if month == 2:
            month_before = 31
            N = day + month_before
        if month == 3:
            month_before = 60
            N = day + month_before
        if month == 4:
            month_before = 91
            N = day + month_before
        if month == 5:
            month_before = 121
            N = day + month_before
        if month == 6:
            month_before = 152
            N = day + month_before
        if month == 7:
            month_before = 182
            N = day + month_before
        if month == 8:
            month_before = 213
            N = day + month_before
        if month == 9:
            month_before = 244
            N = day + month_before
        if month == 10:
            month_before = 274
            N = day + month_before
        if month == 11:
            month_before = 305
            N = day + month_before
        if month == 12:
            month_before = 335
            N = day + month_before
    else:
        if month == 1:
            N = day
        if month == 2:
            month_before = 31
            N = day + month_before
        if month == 3:
            month_before = 59
            N = day + month_before
        if month == 4:
            month_before = 90
            N = day + month_before
        if month == 5:
            month_before = 120
            N = day + month_before
        if month == 6:
            month_before = 151
            N = day + month_before
        if month == 7:
            month_before = 181
            N = day + month_before
        if month == 8:
            month_before = 212
            N = day + month_before
        if month == 9:
            month_before = 243
            N = day + month_before
        if month == 10:
            month_before = 273
            N = day + month_before
        if month == 11:
            month_before = 304
            N = day + month_before
        if month == 12:
            month_before = 334
            N = day + month_before
        return N
    
#赤纬角
def sun_x():
    Pi = math.pi
    now = time.localtime(time.time())
    Year = now.tm_year
    N = date()
    s = 23.5*math.sin(2*Pi*(284+N)/365)
    N0 = 79.6764+0.2422*(Year-1985)-((Year-1985)/4)
    T = N - N0
    An = 2*Pi*T/365.2422
    S0 = 0.3723 + 23.2567*math.sin(An) +0.1149*math.sin(2*An)-0.1712*math.sin(3*An)
    S1 = -0.758*math.cos(An) + 0.356*math.cos(2*An) + 0.0201*math.cos(3*An)
    S = S0 + S1
    return S

#时角
def sun_y():
    Pi = math.pi
    now = time.localtime(time.time())
    h = now.tm_hour
    m = now.tm_min
    s = now.tm_sec
    t0 = h*60 + m
    J =  Lng()
    T = float(t0 - 4*(120-float(J)))/60.0
    An = (T-12)*Pi/12*180/Pi
    return An

#高度角
def sun_a():
    p = math.pi/180
    lat = float(Lat())
    Sin_A = math.cos(lat*p)*math.cos(sun_y()*p)*math.cos(sun_x()*p)+math.sin(lat*p)*math.sin(sun_x()*p)
    Ele =  math.asin(Sin_A)*180/math.pi
    return Ele

#方位角     
def sun_b():
    p = math.pi/180
    sin = math.sin
    cos = math.cos
    lat = float(Lat())
    Cos_A = (sin(sun_a()*p)*sin(lat*p)-sin(sun_x()*p))/(cos(sun_a()*p)*cos(lat*p))
    Azi =  math.acos(Cos_A)*180/math.pi
    return Azi

if __name__ == "__main__":
    print sun_a(),sun_b()


























