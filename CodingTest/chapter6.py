#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 선택정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
m = 0
idx = 0
for i in range(10):
    for j in range(i+1, 10):
        if(j == i+1): 
            m = array[j]
            idx = j
            continue
        if(m > array[j]): 
            m = array[j]
            idx = j
    if(array[i] > m):
        temp = array[i]
        array[i] = m
        array[idx] = temp
print(array)


# In[4]:


# 선택정렬 책 답안
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if(array[min_index] > array[j]): min_index = j
    array[i], array[min_index] = array[min_index], array[i]
print(array)


# In[3]:


# 삽입정렬 -> 잘못된 답안 : 루프를 더 돈다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    for j in range(0,i):
        if array[j] >= array[i]:
            array[i], array[j] = array[j], array[i]
print(array)


# In[7]:


# 삽입정렬 책 답안
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # range(start, end, step)
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)


# In[22]:


# 퀵 정렬
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: 
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[right], array[left] = array[left], array[right]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

    
quick_sort(array, 0, len(array)-1)
print(array)


# In[25]:


# 퀵 정렬 
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1: return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


# In[28]:


# 계수 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

m = max(array)
arr = [0]*(m+1)
for i in range(len(array)):
    arr[array[i]] += 1

for i in range(len(arr)):
    for j in range(arr[i]):
        print(i, end =" ")


# In[33]:


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)


# In[32]:


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array.sort()
print(array)


# In[35]:


array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]
result = sorted(array, key=setting)
print(result)


# In[38]:


# 위에서 아래로
n = int(input())
Sequence = []
for i in range(n):
    Sequence.append(int(input()))
Sequence.sort(reverse = True)

for i in Sequence:
    print(i, end=' ')


# In[52]:


# 성적이 낮은 순서로 학생 출력하기


n = int(input())
score = []
for i in range(n):
    score.append(input().split())

score = sorted(score, key=lambda student: int(student[1]))

for student in score:
    print(student[0], end = ' ')


# In[55]:


# 부하가 많이 걸리는 코드
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(k):
    idx_a = a.index(min(a))
    idx_b = b.index(max(b))
    a[idx_a], b[idx_b] = b[idx_b], a[idx_a]
print(sum(a))


# In[56]:


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] <= b[i]: a[i], b[i] = b[i], a[i]
print(sum(a))

