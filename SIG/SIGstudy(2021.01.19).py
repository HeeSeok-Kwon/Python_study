#!/usr/bin/env python
# coding: utf-8

# # 2021.01.19

# In[1]:


# Input()으로 입력받은 정수 계속 더해나가다가 
# 음수가 입력되면 중단
# 그 전까지 계산된 값 출력


# In[5]:


nsum = 0
while True:
    num = int(input())
    if num < 0: break
    nsum += num
print(nsum)   


# In[12]:


# 윤년
year = int(input("연도를 입력하시오.:"))
if year%4 == 0 :
    if year%100 == 0: 
        if year%400 == 0: print("%d년은 윤년이다."%(year))
        else : print("%d년은 평년이다."%(year))
    else: print("%d년은 윤년이다."%(year))
else : print("%d년은 평년이다."%(year))


# In[21]:


# 윤년
year = int(input("연도를 입력하시오.:"))
if year%4 == 0 and year%100 != 0 or year%400 == 0:
    print("%d년은 윤년이다."%(year))
else : 
    print("%d년은 평년이다."%(year))

