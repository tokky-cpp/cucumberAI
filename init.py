#coding=utf:8

import random

def deal(l): #l枚ランダムに生成。リスト形式で返す。
    nl=[]
    for i in range(l):
        nl.append(random.randint(0,15))
        nl.sort()
    return nl

