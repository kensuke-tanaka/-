
# coding: utf-8

# In[5]:


s=list(input())
q=int(input())
m=["print","replace","reverse"]
for i in range(q):
    a=input().split()
    num1=int(a[1])
    num2=int(a[2])+1
    
    if a[0]==m[0]:
        print(*s[num1:num2],sep="")
    elif a[0]==m[1]:
        s[num1:num2]=list(a[3])
    elif a[0]==m[2]:
        s[num1:num2]=reversed(s[num1:num2])
        
    

