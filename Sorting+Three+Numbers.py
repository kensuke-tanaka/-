
# coding: utf-8

# In[1]:


def sort(a,b,c):
    if 1<=a<=10000 and 1<=b<=10000 and 1<=c<=10000:
        if a<b and b<c:
            print(a,b,c)
        elif a<c and c<b:
            print(a,c,b)
        elif b<a and a<c:
            print(b,a,c)
        elif b<c and c<a:
            print(b,c,a)
        elif c<a and a<b:
            print(c,a,b)
        else:
            print(c,b,a)


# In[2]:


sort(3,8,1)

