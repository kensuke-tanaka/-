
# coding: utf-8

# In[2]:


def division(a,b):
    if 1<=a and b<=10**9:
        d = int(a/b)
        r = a%b
        f = a/b
        print(d," ",r," ",f)


# In[3]:


division(3,2)


# In[4]:


division(10,3)

