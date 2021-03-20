#!/usr/bin/env python
# coding: utf-8

# In[26]:


# 1이 될 때까지(내 답안)
N, K = map(int, input().split())
cnt = 0

while not(N == 1):
    if not(N%K == 0):
        N -= 1
        print("minus", N)
        cnt += 1
    elif N%K == 0:
        N //= K
        print("div", N)
        cnt += 1

print(cnt)


# In[22]:


# 예시 답안 1
n, k = map(int, input().split())
result = 0

while n >= k : # 나누어 떨어질 가능성이 있을 경우만 루프를 돈다.
    while n%k != 0: 
        n -= 1
        result += 1
    n //= k
    result += 1
    
while n > 1: # 남은 수 처리 --> n이 k로 나누어 떨어지지 않음
    n -= 1
    result += 1
    
print(result)


# In[35]:


# 예시 답안 2
n, k = map(int, input().split()) 
result = 0

while True:
    target = (n//k)*k 
#     print("디버깅 n//k", n//k,"디버깅 target", target)
#     if n < k:
#         break
    result += (n-target) # 나머지만큼 카운트 증가
#     print("디버깅 result", result)
    n = target 
#     print("디버깅 n1", n)
    if n < k:
        break
    result += 1
    n //= k 
#     print("디버깅 n2", n)
    
result += (n-1)
print(result)


# In[ ]:




