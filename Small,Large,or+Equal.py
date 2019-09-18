
# coding: utf-8

# In[9]:


def compare(a,b):
    if -1000<=a and b<=1000:
        if a<b:
            print("a<b")
        elif b<a:
            print("a>b")
        else:
            print("a==b")


# In[10]:


compare(1,2)


# In[11]:


compare(4,3)


# In[12]:


compare(5,5)

