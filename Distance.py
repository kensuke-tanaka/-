
# coding: utf-8

# In[1]:


import math

x1,y1,x2,y2=map(int,input().split())
a=(x2-x1)**2+(y2-y1)**2
result=math.sqrt(a)

print(result)


