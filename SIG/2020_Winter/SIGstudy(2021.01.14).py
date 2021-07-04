#!/usr/bin/env python
# coding: utf-8

# # 2021.01.14

# In[14]:


# input으로 정수 한 개 입력받아, 
#그 숫자를 그 숫자 크기만큼 반복해서 출력
loop = int(input("자연수 한 개를 입력하시오.:"))
start = 0
while start < loop:
    print(loop)
    start += 1


# In[12]:


# 고무공을 100미터 높이에서 떨어뜨리는데,
# 이 공을 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오릅니다.
# 공이 열 번 튈 동안, 그때마다 공의 높이를 계산합니다.

# m = 100
# cnt = 1
# while cnt <= 10:
#     print(cnt, m*(3/5)**cnt)
#     cnt += 1
    
m = 100
cnt = 1
while cnt <= 10:
    print(cnt, round(m*(3/5)**cnt,4))
    cnt += 1
    
# m = int(input("공을 떨어뜨릴 높이를 입력하시오.:"))
# cnt = 1
# while cnt <= 10:
#     print(cnt, round(m*(3/5)**cnt,4))
#     cnt += 1

