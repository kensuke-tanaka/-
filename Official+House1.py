
# coding: utf-8

# In[ ]:


room = [[[0 for i in range(10)] for j in range(3)] for k in range(4)] 

n = int(input())
for i in range(n):
    b, f, r, v = map(int, input().split())
    room[b-1][f-1][r-1] += v
    
for i in range(4):
    for j in range(3):
        for k in range(10):
            print(" ", room[i][j][k], sep="", end="")
        print("")
    if i <= 2:
        split_str="#"*20
        print(split_str)
