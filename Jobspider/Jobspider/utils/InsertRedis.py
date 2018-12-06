# -*- coding: utf-8 -*-
import redis
def inserintotc(str,type):
    try:
        r = redis.Redis(host='39.106.14.176', port=6379, db=0, password='foobared')
    except:
        print("连接redis失败")
    else:
        if type == 1:
            r.lpush('start_url', str)
def inserintota(str,type):
    try:
        r = redis.Redis(host='39.106.14.176', port=6379, db=0,password='foobared')
    except:
        print("连接redis失败")
    else:
        if type == 2:
            r.lpush('requests', str)