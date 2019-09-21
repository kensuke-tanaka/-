
# coding: utf-8

# In[1]:


num=[]
while True:
    n = int(input())
    if n == 0:
        break
    while n != 0:
        num.append(n%10)
        n //= 10
    num.reverse()
    print(sum(num))

