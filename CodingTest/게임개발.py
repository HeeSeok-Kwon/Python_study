#!/usr/bin/env python
# coding: utf-8

# In[69]:


# 게임 개발
N, M = map(int,input().split()) # N : 가로, M : 세로
A, B, d = map(int,input().split()) # A, B : 좌표 / d : 바라보는 방향
stage = []
cnt = 1 # 방문한 칸 수
vec = {0:[0,-1],1:[1,0],2:[0,1],3:[-1,0]}
for i in range(N):
    data = map(int,input().split())
    stage.append(list(data))
D = d
# 북, 서, 남, 동 --> 왼쪽 순으로 흐르게끔 하는 코드
if D == 1: D = 3 
elif D == 3: D = 1
a, b = A, B
stage[A][B] = 2
while True:
    loop = 0
    for i in range(D,D+4):
        if loop == 4: 
            dcpy = D
#             print("디버깅",i)
            break
        if i > 3: i -= 4
        try:
            stage[a+vec[i][0]][b+vec[i][1]]
        except IndexError:
            loop += 1
            continue
        else :
            opt = stage[a+vec[i][0]][b+vec[i][1]]
            if opt == 0 and a+vec[i][0]>=0 and b+vec[i][1]>=0 :
                a = a+vec[i][0]
                b = b+vec[i][1]
                stage[a][b] = 2
#                 print("디버깅",i)
                dcpy = i
                D = i
                cnt += 1
#                 print("loop",loop)
                break
#             else:
#                 dcpy = i 
        loop += 1
        
    if loop == 4:
        try:
            stage[a-vec[dcpy][0]][b-vec[dcpy][1]]
        except IndexError:
            print(cnt)
            print(stage)
            break
        else:
            opt = stage[a-vec[dcpy][0]][b-vec[dcpy][1]]
            if opt== 1 and a-vec[dcpy][0]>=0 and b-vec[dcpy][1]>=0: # 1 : 바다 
                print(cnt)
                print(stage)
#                 print("디버깅",a,b)
                break
            elif opt == 2 : # 2 : 가본 곳
                a = a-vec[dcpy][0]
                b = b-vec[dcpy][1]
#                 stage[a][b] += 1
#                 print("디버깅",dcpy,a,b)
                continue
    


# In[74]:


# 예시 답안
n,m = map(int, input().split())

d = [[0]*m for _ in range(n)]
x,y,direction = map(int,input().split())
d[x][y] = 1 #현재 좌표 방문 처리

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
dx = [-1,0,1,0] # 북,동,남,서
dy = [0,1,0,-1]

def turn_left(): # 북->서->남->동->북
    global direction
    direction -= 1
    if direction == -1:
        direction = 3 # 0->3->2->1

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
#         print(d)
        x = nx
        y = ny
        count += 1
        turn_time = 0 # 방향 도는 거 초기화
        continue
    else:
        turn_time += 1
        
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x=nx
            y=ny
        else: 
            break
        turn_time = 0
        
print(count)


# In[8]:


vec = {0:[1,-1],1:[-1,-1],2:[-1,1],3:[1,1]}
print(vec[0])

