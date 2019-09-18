
# coding: utf-8

# In[ ]:


i = 1
while True:
    x = input()
    x = int(x)
    if x < 0 or x > 10000:
        continue
    if x == 0 or i > 10000:
        break
    print('Case {0}: {1}' .format(i, x))
    i += 1

