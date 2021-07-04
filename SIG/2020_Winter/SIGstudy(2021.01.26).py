#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2021.01.26


# In[1]:


def f1(x):
    a = 3
    b = 5
    y = a*x + b
    return y

c = f1(10)
print(c)


# In[7]:


def simple_interest(p,r,t):
    return p*r*t

print(simple_interest(10000000,0.03875,5))
print(simple_interest(1100000,0.05,5/12))


# In[16]:


def simple_interest_amount(p,r,t):
    return p*(1+r*t)

print(simple_interest_amount(10000000,0.03875,5))
print(simple_interest_amount(1100000,0.05,5/12))


# In[18]:


def compound_interest_amount(p,r,t,n):
    return p*(1+r/n)**(n*t)

print(compound_interest_amount(1500000,0.043,6,4))
print(compound_interest_amount(1500000,0.043,6,1/2))

