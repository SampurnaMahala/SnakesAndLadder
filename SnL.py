import random as r
bo=[[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,[1,32],-1,-1,-1,-1,-1,],[-1,-1,[1,77],-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,[0,2],-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,[1,85],-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,[0,20],-1,],[-1,[1,98],[0,1],-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,[0,42],-1,]]
pos=1
while(pos<=100):
    s=""
    a=input('continue')
    d=r.randint(1,6)
    for i in range(9,-1,-1):
        for j in range(9,-1,-1):
            if((pos//10==i) and (pos%10==j+1))or((pos//10-1==i)and(pos%10==0)and(j==9)):
                print(end="💀   ")
            elif(bo[i][j]==-1):
                x=(i*10)+j+1
                print(x,end="   ")
                if(i==0):
                    print(end=' ')
            if(type(bo[i][j]) is list):
                if(bo[i][j][0]==0):
                    print(end="🐍   ")
                    if((pos//10==i) and (pos%10==j+1))or((pos//10-1==i)and(pos%10==0)and(j==9)):
                        pos=bo[i][j][1]
                        s="a snake bit you fell down to" + str(bo[i][j][1])
                elif(bo[i][j][0]==1):
                    print(end="🪜   ")
                    if((pos//10==i) and (pos%10==j+1))or((pos//10-1==i)and(pos%10==0)and(j==9)):
                        pos=bo[i][j][1]
                        s="you found a ladder and climbed to" +  str(bo[i][j][1])
                    
        print()
        print("-"*50)
    print("you rolled a :",d)
    print(s,"\n")
    if(pos==100):
        print("you won")
        break
    if(pos+d<=100):
        pos+=d
