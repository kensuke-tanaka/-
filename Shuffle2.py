
# coding: utf-8

# In[ ]:


while True:
    s = input() 
    m = int(input())
    
    while m > 0:
        h = int(input())
        s = s[h:] + s[:h]
        m-=1
    print(s)

