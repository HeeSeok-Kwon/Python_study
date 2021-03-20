#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 상하좌우(내 답안)
N = int(input()) # N*N 행렬 
direction = list(map(str,input().split()))
# print(direction)
row = 1
col = 1
for i in direction:
    if i == 'L' and col > 1: col -= 1
    elif i == 'R' and col < N: col += 1
    elif i == 'U' and row > 1: row -= 1
    elif i == 'D' and row < N: row += 1
    else: continue

print(row, col)


# In[8]:


# 예시 답안
n = int(input())
x, y = 1, 1
nx, ny = 0, 0 # 이 코드 있어야 오류가 안 남
plans = input().split()

dx = [0,0,-1,1] # 세로방향 움직임
dy = [-1,1,0,0] # 가로방향 움직임
move_types = ['L','R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)): # 4번 루프를 돌며 방향 읽음
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n: # 할당X, 무시됨
            continue
        x, y = nx, ny

print(x, y)

