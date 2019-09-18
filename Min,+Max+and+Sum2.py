
# coding: utf-8

# In[1]:


a = input()
box=[]
for i in range(int(a)):
    b=input()
    box.append(b)
c=0
for i in range(len(box)):
    c+=int(box[i])

min1 = min(box)
max1 = max(box)
print(min1,"",max1,"",c)

