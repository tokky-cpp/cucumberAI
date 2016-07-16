#coding=utf:8

import ai
import init
import matplotlib.pyplot as plt
import json

win=[]
lose=[]
for i in range(7):
    win.append({})
    lose.append({})

for i in range(10000):
    if(i%1000==0): print i
    a=init.deal(7)
    b=init.deal(7)
    
    a_hist=[]
    b_hist=[]
    a_hist.append(a)
    b_hist.append(b)
    n = None
    for i in range(6):
        (a,n)=ai.answer(a,n)
        a_hist.append(a)
        (b,n)=ai.answer(b,n)
        b_hist.append(b)
        


        if(a[0]<=b[0]): 
            for nl in a_hist:
                for num in nl:
                    win[len(nl)-1].setdefault(num,0)
                    win[len(nl)-1][num]+=1

            for nl in b_hist:
                for num in nl:
                    lose[len(nl)-1].setdefault(num,0)
                    lose[len(nl)-1][num]+=1
                    

print win
print lose    
        
prob=[]
for i in range(7):
    prob.append({})


for i in range(7):
    for j in range(len(win[i])):
        prob[i].setdefault(j+1, float(win[i][j+1])/(win[i][j+1]+lose[i][j+1]))

x = [i+1 for i in range(len(prob[0]))]
y = [prob[0][i+1] for i in range(len(prob[0]))]


f = open("prob.json","w")
json.dump(prob,f)

plt.plot(y,x)
plt.show()
