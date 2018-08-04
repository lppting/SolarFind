#!/usr/bin/python
#-*- coding:utf-8 -*-
import time

while True:
    f = open ("s.log","w+")
    now = time.asctime(time.localtime(time.time()))
    f.write(str(now))
    f.close()
    time.sleep(2)
