
# coding: utf-8

# In[5]:


num=list(map(int,input().split()))
ques=int(input())
for i in range(ques):
    a=list(map(int,input().split()))
    if a in [[num[0], num[1]], [num[1], num[5]], [num[5], num[4]], [num[4], num[0]]]:
        print(num[2])
    elif a in [[num[0], num[2]], [num[2], num[5]], [num[5], num[3]], [num[3], num[0]]]:
        print(num[4])
    elif a in [[num[0], num[4]], [num[4], num[5]], [num[5], num[1]], [num[1], num[0]]]:
        print(num[3])
    elif a in [[num[0], num[3]], [num[3], num[5]], [num[5], num[2]], [num[2], num[0]]]:
        print(num[1])
    elif a in [[num[1], num[2]], [num[2], num[4]], [num[4], num[3]], [num[3], num[1]]]:
        print(num[0])
    elif a in [[num[1], num[3]], [num[3], num[4]], [num[4], num[2]], [num[2], num[1]]]:
        print(num[5])

