#-*- coding:utf-8 -*-
from solarfind import sun_a,sun_b,sun_x,sun_y
from weather import weather
from PiCtrl import MainControl
import time
import json

Azi = sun_b()
global T
global Wth
global solar_x
global solar_y
global t_now
T = 0

#时间判定，晚上自动关闭恢复水平位置。
def TimeNow():
    now = time.localtime(time.time())
    H = now.tm_hour
    ReadData =  float(ReadLog())
    global T
    global t_now 
    t_now = time.asctime(now)
    T = ReadData
    if H <=19 and 6 < H:
        SunEle()
    else:
        Default()

#夜间，太阳能板恢复初始位置
def Default():
    ReadData =  float(ReadLog())
    global T
    T = 0
    MainControl(-ReadData)
    WriteLog(T)
    
#追踪太阳高度角    
def SunEle():
    Ele = int(90 - sun_a())
    global T
    global solar_x
    solar_x = Ele
    T0 = 0
    if Ele <=50 and 4 <= Ele:
        if Ele == 4:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 5:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 6:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 7:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 8:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 9:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 10:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 11:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 12:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 13:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 14:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 15:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 16:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 17:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 18:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 19:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 20:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 21:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 22:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 23:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 24:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 25:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 26:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 27:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 28:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 29:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 30:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 31:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 32:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 33:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 34:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 35:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 36:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 37:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 38:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 39:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 40:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 41:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 42:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 43:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 44:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 45:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 46:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 47:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 48:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 49:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
        if Ele == 50:
            T0 = 0.5 * Ele - T
            MainControl(T0)
            T = 0.5 * Ele
            
    else:
        T0 = 24 - T
        MainControl(T0)
        T = 24
#    print Wth,T0,T,solar_x,time.asctime(t_now)
    WriteJson()
    WriteLog(T)
    
def ReadLog():
    f = open("control.log","r+")
    read = f.read()
    f.close()
    return read

def WriteLog(data):
    text = str(data)
    f = open("control.log","w+")
    f.write(text)
    f.close()

def WriteJson():
    dict = {'wearther':Wth,'time':t_now,'solarele':solar_x,'where':T}
    f = open("solar.json","w+")
    JsonData = json.dumps(dict)
    f.write(JsonData)
    f.close()

if __name__ == "__main__":
    data = weather()
    t = data["weather"] 
    Str = t.encode('utf-8')
    global Wth
    Wth = t
    while True:   
        if Str == "晴" or Str == "多云":
#            print t
            TimeNow()
            time.sleep(6)
        else:
            Default()
