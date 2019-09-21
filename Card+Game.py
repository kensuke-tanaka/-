
# coding: utf-8

# In[2]:


n=int(input())
taro=[]
hanako=[]
taroP=0
hanakoP=0
for i in range(n):
    a,b=map(str,input().split())
    taro.append(a)
    hanako.append(b)

for j in range(n):
    if taro[j]>hanako[j]:
        taroP+=3
    elif hanako[j]>taro[j]:
        hanakoP+=3
    else:
        taroP+=1
        hanakoP+=1

print(taroP,hanakoP)

