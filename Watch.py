
# coding: utf-8

# In[18]:


def watch(seconds):
    if seconds<=86400 and 0<=seconds:
        print(int(seconds/3600),":",int((seconds%3600)/60),":",int(seconds%60))


# In[19]:


watch(200)

