
# coding: utf-8

# In[6]:


while True:
    H,W=map(int, input().split())
    if H == 0 and W == 0:
        break
    
    for i in range(0,H):
        frame=""
        for j in range(0,W):
            if i == 0 or i == H-1 or j == 0 or j == W-1:
                frame+="#"
            else:
                frame+="."
        print(frame)
        
    print()
  

