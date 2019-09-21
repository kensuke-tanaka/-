
# coding: utf-8

# In[7]:


r,c=map(int,input().split())
sheet1=[[0 for i in range(c)] for j in range(r)]
for i in range(r):
    sheet1[i] = [int(x) for x in input().split()]

sheet2=[[0 for j in range(c+1)]for k in range(r+1)]
for i in range(r):
    for j in range(c):
        sheet2[i][j]=sheet1[i][j]

for i in range(r):
    sheet2[i][c] = sum(sheet2[i])

for i in range(c):
    for j in range(r):
        sheet2[r][j]+=sheet2[i][j]

sheet2[r][c] = sum(sheet[r])

for i in range (r + 1):
    print(" ".join(map(str,sheet2[i])))

