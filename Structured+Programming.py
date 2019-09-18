
# coding: utf-8

# In[3]:


n=int(input())
 
list=[]
for i in range(1,n+1):
    if i%3==0:
        list.append(i)
    else:
        a=i
        for j in range(1,5):
            if a%10==3:
                list.append(i)
                break
            else:
                a=a//10
        else:
            continue
print("",*list)

