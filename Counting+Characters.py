
# coding: utf-8

# In[ ]:


letter="abcdefghijklmnopqrstuvwxyz"
table=[0]*26
while True:
    try:
        sentence=input()
    except:
        break
    for A in sentence:
        index=0
        for B in letter:
            if A == B or A == B.upper():
                table[index] += 1
                break
            index += 1
    for i in range(len(letter)):
        print("%s : %d"%(letter[i],table[i]))




