
# coding: utf-8

# In[ ]:


while True:
    m,f,r=map(int, input().split())
    if m==f==r==-1:
        break
    elif m==-1 or f==-1:
        print("F")
    elif m+f>=80:
        print("A")
    elif m+f>=65 and m+f<80:
        print("B")
    elif m+f>=50 and m+f<65:
        print("C")
    elif m+f>=30 and m+f<50:
        print("D")
    elif m+f>=30 and m+f<50 and r>=50:
        print("C")
    elif m+f<30:
        print("F")
    
    

