
# coding: utf-8

# In[ ]:


import math

n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
p1 = 0
p2 = 0
p3 = 0
pin = 0
for i in range(n):
    p1+=abs(x[i]-y[i])
    
for i in range(n):
    p2+=(abs(x[i]-y[i]))**2
    

for i in range(n):
    p3+=(abs(x[i]-y[i]))**3
    
for i in range(n):
    pin=max(pin,abs(x[i]-y[i]))

print(p1)
print(math.sqrt(p2))
print(p3**(1/3))
print(pin)

