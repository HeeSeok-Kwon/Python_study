#!/usr/bin/env python
# coding: utf-8

# In[1]:


N, M, K = map(int, input("자연수 3개 입력>>>").split())
print(N, M, K)


# In[29]:


# 문제 해설 -- 그리디 알고리즘 --
n ,m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째 큰 수

res = 0 # 결과 변수

while True:
    for i in range(k): # k번 더하고
        if m == 0: break
        res += first
        m -= 1
    if m == 0: break
    res += second #한 번 더하고
    m -= 1
    
print(res)


# In[30]:


# 문제 해설 2 

n ,m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m%(k+1)

res2 = 0
res2 += (count)*first 
res2 += (m-count)*second

print(res2)


# In[40]:


#동빈이의 큰 수의 법칙(내 답안)
import copy

def findsec(arr):
    cpy = copy.deepcopy(arr)
    del cpy[arr.index(max(arr))]
    return max(cpy)

result = 0
# N : N개의 리스트, M : 총 더할 횟수, K : 특정 인덱스 수가 연속해서 더해질 횟수
N, M, K = map(int, input("자연수 3개 입력>>>").split())
# N개 만큼 자연수 입력 --> N개만 입력받도록 보완 필요
arr = [int(x) for x in input("%d개의 자연수 입력>>>"%N).split()]
# print(arr)
#### 틀린 답안 #### --> 5 7 2 / 3 4 3 3 3 = 26(정답), 27(오답) 
# maxcnt = M//K # K는 항상 M보다 작거나 같다.
# seccnt = M%K

maxcnt = M//(K+1)*K+M%(K+1)
seccnt = M//(K+1)

result += max(arr)*maxcnt
# print("디버깅", max(arr), maxcnt)  
result += findsec(arr)*seccnt
# print("디버깅", findsec(arr), seccnt)

print(result)

