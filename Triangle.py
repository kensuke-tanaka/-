
# coding: utf-8

# In[2]:


import math
a,b,C = map(int,input().split())
rad=math.pi*C/180
S=math.sin(rad)*a*b/2
L=a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(rad))
h=b*math.sin(rad)
print(S)
print(L)
print(h)

