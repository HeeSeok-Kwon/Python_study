#!/usr/bin/env python
# coding: utf-8

# In[8]:


stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력


# In[13]:


from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(list(queue)) # 먼저 들어온 순서대로 출력
queue.reverse() 
print(queue) # 나중에 들어온 순서대로 출력


# In[14]:


def recursive_function():
    print("재귀함수를 호출합니다.")
    recursive_function()
    
recursive_function()


# In[15]:


def recursive_function(i):
    if i == 100: return
    print(i, "번째 재귀함수에서", i+1,"번째 재귀 함수를 호출합니다.")
    recursive_function(i+1)
    print(i,"번째 재귀함수를 종료합니다.")
    
recursive_function(1)


# In[16]:


def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
def factorial_recursive(n):
    if n <= 1: return 1
    return n*factorial_recursive(n-1)
print("반복적으로 구현:",factorial_iterative(5))
print("재귀적으로 구현:",factorial_recursive(5))


# In[20]:


INF = 999999999
graph= [[0,7,5], [7,0,INF],[5,INF,0]]
print(graph)


# In[18]:


graph = [[] for _ in range(3)]
graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))
print(graph)


# In[21]:


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8], #1번 노드
    [1, 7], # 2번 노드
    [1, 4, 5], # 3번 노드
    [3, 5], # 4번 노드
    [3, 4], # 5번 노드
    [7], # 6번 노드
    [2, 6, 8], # 7번 노드
    [1, 7] # 8번 노드
]

visited = [False]*9

dfs(graph, 1, visited)


# In[25]:


from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
graph = [
    [],
    [2, 3, 8], #1번 노드
    [1, 7], # 2번 노드
    [1, 4, 5], # 3번 노드
    [3, 5], # 4번 노드
    [3, 4], # 5번 노드
    [7], # 6번 노드
    [2, 6, 8], # 7번 노드
    [1, 7] # 8번 노드
]

visited = [False]*9

bfs(graph, 1, visited)


# In[26]:


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1 # 한 지점이 0이면 연결된 모든 0이 1로 바뀐다.
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
    
print(result)    


# In[27]:


from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 바로 연결된 노드는 모두 1씩 더해짐
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))

