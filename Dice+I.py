
# coding: utf-8

# In[1]:


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
comList = input()
d = dice(diceNum)
for c in comList:
    d.move(c)
print(d.num[0])

