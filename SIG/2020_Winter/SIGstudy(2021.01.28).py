#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 2021.01.28


# In[3]:


def hap(a, b):
    print(a+b)
def gop(a, b):
    print(a*b)
def hap_gop(a, b):
    hap(a, b)
    gop(a, b)

hap(2,3)
gop(2,3)
hap_gop(2,3)


# In[4]:


def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)
countdown(3)


# In[8]:


def sumOfDigits(n):
    if n//10 == 0: return n
    return n%10 + sumOfDigits(n//10)

result = sumOfDigits(47253)
print(result)


# In[11]:


def compound_interest_amount_withoutN(p,r,t):
    if t == 0: return p
    return (1+r)*compound_interest_amount_withoutN(p,r,t-1)
Expire_Receipt = compound_interest_amount_withoutN(3600000,0.058,2)
print(Expire_Receipt)

