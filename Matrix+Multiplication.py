
# coding: utf-8

# In[6]:


n,m,l=map(int,input().split())
mat1=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    mat1[i] = [int(x) for x in input().split()]
    
mat2=[[0 for j in range(l)]for k in range(m)]
for j in range(m):
    mat2[j] = [int(x) for x in input().split()]


    
for i in range(n):
    ans=[]
    for j in range(l):
        num = 0
        for k in range(m):
            num+= mat1[i][k]*mat2[k][j]
        ans.append(str(num))
    print(" ".join(ans))

