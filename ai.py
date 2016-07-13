
#coding=utf-8
#2016-07-13
#5本のキュウリAI 
#ver 1.0
#評価関数を導入


def evaluation(nl): #スコアの低いほうが良い
    score = 0
    for i in nl:
        score += min(i-1,15-i)
    return score


def answer(nl, n): #nl:手持ちの数字リスト n:場に出ている数字
    if n is None: n=1 #もし場に何も出ていなければ１が出ていることにしておく
    nl.sort() 

    #一番小さいものを出すのをベストにしておく(とりあえず)
    best_nl = nl[1:]
    best_score = evaluation(nl[1:])
    ret = nl[0]
    print(best_nl,best_score,ret)
    

    for i in range(len(nl)-1):
        if n>nl[i]: #場に出ているほうが大きかったらだめ
            continue
        else: #もし場に出ている数字以上なら
            nl_=nl[:i]+nl[i+1:] #1つ取り除いて
            e = evaluation(nl_) #評価関数に入れる
            print(nl_,e,nl[i])
            if(best_score > e): #もしスコアが良ければ上書き
                best_nl = nl_
                best_score = e
                ret = nl[i]

#            print("remove"+str(i))
    return(best_nl,ret)
   





    
