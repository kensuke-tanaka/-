
# coding: utf-8

# In[1]:


suits = ['S','H','C','D']
 
table = [[False]*14 for i in range(4)]
 
N = int(input())
 
for x in range(N):
 
    mark,num = input().split()
    num = int(num)
 
    if mark == 'S':
        table[0][num] = True
    elif mark == 'H':
        table[1][num] = True
    elif mark == 'C':
        table[2][num] = True
    else:
        table[3][num] = True
        
for i in range(4):
    for k in range(1,14):
        if table[i][k] == False:
            print("%s %d"%(suits[i],k))

