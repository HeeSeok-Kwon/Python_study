#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 2021.02.02


# In[4]:


# 람다
(lambda x,y:x+y)(10,20)


# In[9]:


map(lambda x: x**2, range(5)) # -> map 객체가 나옴 그래서 list 함수 사용
list(map(lambda x: x**2, range(5)))


# In[11]:


from functools import reduce
reduce(lambda x,y : x + y,[0,1,2,3,4])


# In[12]:


reduce(lambda x,y: y+x,"abcde")


# In[14]:


list(filter(lambda x: x < 5, range(10)))


# In[15]:


list(filter(lambda x: x%2 == 1, range(10)))


# In[17]:


# 람다 == 이름없는 함수(익명 함수)
lambda x: x+10
# 결과 => <function __main__.<lambda>(x)> 함수 객체

# 익명함수 람다를 변수에 할당
plus_ten = lambda x: x+10
print(plus_ten(1))


# In[18]:


# 람다 자체를 호출
(lambda x: x + 10)(1)


# In[19]:


def plus_five(x):
    return x+5

list(map(plus_five, [1,2,3])) # 함수를 인자로 사용


# In[20]:


list(map(lambda x: x+5, [1,2,3])) # 익명 함수를 인자로 사용

