#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 2021.01.21

# for문
family = ['mother','father','sister','brother','baby']
for x in family:
    print("%s %d"%(x,len(x)))


# In[4]:


# 문제 1
num = int(input("자연수 하나를 입력하시오. >>> "))
for i in range(num):
    print(num)


# In[15]:


# 문제 2
num = int(input("정수 하나를 입력하시오. >>> "))
if num < 0:
    for i in range(num,0):
        print(i, i**2)
elif num >= 0:
    for i in range(1,num+1):
        print(i, i**2)


# In[29]:


# 문제 3

def prime(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i == 0: cnt += 1
    if cnt == 2: return True
    else: return False

num = int(input("소수를 구하기 위한 2 이상의 자연수를 입력하시오. >>> "))

for i in range(2, num+1):
    res = prime(i)
    if res == True:
        print(i,end=" ")
    else:
        continue


# In[28]:


# 문제 3 
num = int(input("숫자를 입력하시오. >>> "))
arr = []
for i in range(1,num+1):
    arr.append(i)
# print(arr) # 범위 안 모든 수 출력
arr.remove(1) # 1 제거
res = min(arr) # 1 제외한 최소값 2
for x in arr:
    for i in arr:
        if i == res: continue
        elif i%res == 0: # 2의 배수부터 리스트에서 삭제
            arr.remove(i)
    res = x
    
print(arr)

