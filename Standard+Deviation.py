
# coding: utf-8

# In[2]:


import math

while True:
    n = int(input())
    if n == 0:
        break
    
    m=list(map(int,input().split()))
    heikin=sum(m)/len(m)
    result=math.sqrt((sum([(i-heikin)**2 for i in m])/len(m)))
    print(result)

