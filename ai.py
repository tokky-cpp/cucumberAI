
#coding=utf-8
#2016-07-13
#5本のキュウリAI 
#ver 1.1
#ゲームの終盤に向けてスコアを変えるように評価関数を修正
#評価関数をコスト関数に命名変更


def cost(nl): #コストを計算。低い方が良い。
    score = 0
    for i in nl:
        score += min(i-1,15-i+(7-len(nl)))
    return score


def answer(nl, n): #nl:手持ちの数字リスト n:場に出ている数字
    if n is None: n=1 #もし場に何も出ていなければ１が出ていることにしておく
    nl.sort() 

    #一番小さいものを出すのをベストにしておく(とりあえず)
    best_nl = nl[1:]
    min_cost = cost(nl[1:])
    ret = nl[0]
    print(best_nl,min_cost,ret)
    

    for i in range(len(nl)-1):
        if n>nl[i+1]: #場に出ているほうが大きかったらだめ
            continue
        else: #もし場に出ている数字以上なら
            nl_=nl[:i+1]+nl[i+2:] #1つ取り除いて
            e = cost(nl_) #コスト関数に入れる
            print(nl_,e,nl[i+1])
            if(min_cost > e): #もしコストが小さければ上書き
                best_nl = nl_
                min_cost = e
                ret = nl[i+1]

#            print("remove"+str(i))
    print("remove",ret,best_nl)
    return(best_nl,ret)
   





    
