#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 2021.02.04


# In[2]:


a = 10
b = 20
print(a,b)
temp = a
a = b
b = temp
print(a, b)

c=10
d=20
print(c,d)
c, d = d, c
print(c,d)


# In[3]:


def magu_print(x,y, *rest):
    print(x,y,rest)
    
magu_print(1,2,3,5,6,7,9,10)


# In[14]:


t = ('a','b','c')
tt = 'a','b','c'
print(t, tt)

empty = ()
print(empty)

one = 5,
print(one)

p = 1,2,3
q=p[:1]+(5,)+p[2:]
print(q)
r = p[:1],5,p[2:]
print(r)

p = 1,2,3
q = list(p)
print(q)

r = tuple(q)
print(r)


# In[19]:


dic = {}
dic['dictionary'] = '1. A reference book containing an ...'
dic['python'] = 'Any of various nonvenomous snakes of the ...'
print(dic['dictionary'])
print(dic)

smalldic = {'dictionary':'reference','python':'snake'}
print(smalldic['python'])
print(smalldic)

