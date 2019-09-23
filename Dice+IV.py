
# coding: utf-8

# In[2]:


n=0
n=int(input())
for i in range(n):
    if i==0:
        d1=list(map(int,input().split()))
    else:
        d2=list(map(int,input().split()))
            
        for i in range(4):
            d2[0],d2[1],d2[4],d2[5]=d2[1],d2[5],d2[0],d2[4]
            for i in range(4):
                d2[1],d2[3],d2[4],d2[2]=d2[3],d2[4],d2[2],d2[1]
                if d1[0]==d2[0] and d1[1]==d2[1] and d1[2]==d2[2] and d1[3]==d2[3] and d1[4]==d2[4] and d1[5]==d2[5]:
                    n+=1
        for i in range(4):
            d2[0],d2[3],d2[5],d2[2]=d2[3],d2[5],d2[2],d2[0]
            for i in range(4):
                d2[1],d2[3],d2[4],d2[2]=d2[3],d2[4],d2[2],d2[1]
                if d1[0]==d2[0] and d1[1]==d2[1] and d1[2]==d2[2] and d1[3]==d2[3] and d1[4]==d2[4] and d1[5]==d2[5]:
                    n+=1
if n==0:
    print('Yes')
else:
    print('No')

