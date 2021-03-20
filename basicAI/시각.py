#!/usr/bin/env python
# coding: utf-8

# In[11]:


# # 시각 --- 틀린 답안 ---

# def find(time):
#     cnt = 0
#     for i in time:
#         if i//10 == 3 or i == 3:
#             cnt += 1
#     return cnt

# N = int(input())
# time = [0,0,0] # 시, 분, 초
# stop = N + 1
# cnt = 0

# while time[0] != stop:
   
#     if find(time) >= 1:
#         cnt += 1
#     if time[2] > 59:
#         time[1] += 1
#         time[2] = 0
#     if time[1] > 59:
#         time[0] += 1
#         time[1] = 0
        
#     time[2] += 1
    
# print(cnt)  


# In[25]:


# 시각

N = int(input())
cnt = 0
for i in range(N+1):
    if i == 3: cnt += 3600
    else : cnt+=1575

print(cnt)


# In[52]:


N = int(input())
time = [0,0] # 시, 분
stop = N + 1
cnt = 0

while stop > time[0] :
    
    if time[0]//10 == 3 or time[0]%10 == 3:
        cnt += 60
        time[0] += 1
        continue
    
    for i in time:
        if i//10 == 3 or i%10 == 3: 
            cnt += 1
            break
    time[1] += 1
    if time[1] > 59:
        time[0] += 1
        time[1] = 0
    
print(cnt)  


# In[59]:


N = int(input())
time = [0, 0, 0] # 시, 분, 초
stop = N + 1
cnt = 0

while stop > time[0] :
    
    if time[0]//10 == 3 or time[0]%10 == 3:
        cnt += 3600
        time[0] += 1
        continue
    
    if time[1]//10 == 3 or time[1]%10 == 3:
        cnt += 60
        time[1] += 1
        continue
    
    if time[2]//10 == 3 or time[2]%10 == 3: 
        cnt += 1
            
    time[2] += 1
    
    if time[2] > 59:
        time[1] += 1
        time[2] = 0
    if time[1] > 59:
        time[0] += 1
        time[1] = 0
    
print(cnt)  


# In[60]:


# 문제 해설 --- 완전 탐색 ---

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)

