#!/usr/bin/env python
# coding: utf-8

# In[12]:


# 왕실의 나이트(내 답안)


def move1(row, col): # 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
    cnt = 0
    if col-2 > 0 :
        if row-1 > 0: cnt+=1
        if row+1 < 9: cnt+=1
    if col+2 < 9:
        if row-1 > 0: cnt+=1
        if row+1 < 9: cnt+=1
    return cnt

def move2(row, col): # 1. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
    cnt = 0
    if row-2 > 0:
        if col-1 > 0: cnt+=1
        if col+1 < 9: cnt+=1
    if row+2 < 9:
        if col-1 > 0: cnt+=1
        if col+1 < 9: cnt+=1
    return cnt
    
loc = input()
col = int(ord(loc[0])) - 96 # 문자열을 좌표값으로 변환
row = int(loc[1]) 
cnt = 0 # 이동 가능한 경우의 수 출력
# print(row, col) # 디버깅

cnt += move1(row, col)
cnt += move2(row, col)
print(cnt)


# In[14]:


# 답안 예시

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a')) + 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)] # 행렬

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    if next_row >= 1 and next_row <=8 and next_column>=1 and next_column <= 8:
        result += 1
        
print(result)

