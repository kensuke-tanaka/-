
# coding: utf-8

# In[ ]:


while True:
    a,op,b = input().split()
    a=int(a)
    b=int(b)
    if op=="?":
        break
    if op=="+":
        print(a+b)
    if op=="-":
        print(a-b)
    if op=="+":
        print(a*b)
    if op=="/":
        print(a//b)

