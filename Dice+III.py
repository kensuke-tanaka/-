
# coding: utf-8

# In[3]:


import random
class dice():
    def __init__(self,num):
        self.num = num

    def move(self,com):
        if com == 'E':
            self.num = [self.num[i] for i in [3,1,0,5,4,2]]
        if com == 'S':
            self.num = [self.num[i] for i in [4,0,2,3,5,1]]
        if com == 'N':
            self.num = [self.num[i] for i in [1,5,2,3,0,4]]
        if com == 'W':
            self.num = [self.num[i] for i in [2,1,5,0,4,3]]
diceNum = [int(x) for x in input().split()]
d = dice(diceNum)
s = [ "E" , "S" , "N" , "W" ]
a,b,c,g,e,f =map(int,input( ).split( ))
j = 0
while j <= 10000 :
    k = random.randrange ( 4 )
    d.move(s[k])
    if d.num[ 0 ] == a and d.num[ 1 ] == b and d.num[ 2 ] == c and d.num[ 3 ] == g and d.num[ 4 ] == e and d.num[ 5 ] == f :
        print ( "Yes" )
        break
    if j == 10000 :
        print ( "No" )
    j += 1


