#!/usr/bin/env python
# coding: utf-8

# In[14]:


# 숫자 카드 게임
N, M = map(int,input().split())
arr = []
maxmin = []
for i in range(0, N):
    data = list(map(int, input().split()))
    arr.append(data)
    maxmin.append(min(arr[i]))
    
# print("디버깅", arr)
print(max(maxmin))


# In[15]:


# 답안 예시 1
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data) # 입력받은 리스트의 제일 작은 값 할당
    result = max(result, min_value) # result, min_value 중 큰 값을 계속 할당

print(result)


# In[16]:


# 답안 예시 2
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001 # 문제에 제시된 10,000 보다 1 큰 값
    for a in data: # 리스트 갯수만큼 루프
        min_value = min(a, min_value) # 리스트에서 가장 작은 값 추출
    result = max(result, min_value) # 작은 값 중 가장 큰 값을 추출
    
print(result)

