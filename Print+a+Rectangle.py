
# coding: utf-8

# In[6]:


a = input()
b = input()
list = [["#" for i in range(int(a))] for j in range(int(b))]
for x in list:
    print(*x)

