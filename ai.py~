
#coding=utf-8
#2016-07-11
#5本のキュウリAI 
#ver 0.0
#ルールにしたがって出しているだけ。

def answer(nl, n): #nl:手持ちの数字リスト n:場に出ている数字
    if n is None: n=1 #もし場に何も出ていなければ１が出ていることにしておく
    nl.sort() 

    for i in nl:
        if n<=i: #小さい順に見ていってもし出せる数字があれば出す。
            ret = i
            nl.remove(i)
#            print("remove"+str(i))
            return(nl,ret)
   
#場の数字以上の数字を持っていなかったときの処理
    ret = nl[0]
    nl.remove(nl[0])
 #   print("remove"+str(i))
    return(nl,ret)
    
