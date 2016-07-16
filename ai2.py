#coding:utf-8

import json

prob_data_file = "prob.json"

def load(): #確率データの読み込み jsonを読み込んで返す

    f = open(prob_data_file,"r")
    p = json.load(f)

    prob = []

    for i in p:
        prob.append( {int(k):v for k,v in i.items()})

    return prob


def eval(nl,prob): #評価値を計算 高いほど良い
    ret = 0.0
    for n in nl:
        ret += prob[len(nl)-1][n]
    print ret
    return ret


def answer(nl,n): #手札のリスト 場の数字
    
    prob = load()
    
    if n is None: n=1 #もし場に何も出ていなければ
    best_nl = nl[1:]
    max_eval = eval(nl[1:],prob)

    ret = nl[0]
    
    for i in range(len(nl)-1):
        if n>nl[i+1]: #場に出ているほうが大きかったらだめ
            continue

        else: #もし場に出ている数字以上なら
            nl_=nl[:i+1]+nl[i+2:] #1つ取り除いて
            e = eval(nl_,prob) #評価関数に入れる
            if(max_eval < e): #もし評価値が大きければ上書き
                best_nl = nl_
                max_eval = e
                ret = nl[i+1]

    return(best_nl,ret)
    
