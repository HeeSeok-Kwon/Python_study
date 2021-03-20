#!/usr/bin/env python
# coding: utf-8

# In[1]:


var = int(input("구구단을 나타낼 열을 입력하시오 : "))


# In[12]:


for i in range(1,10):
    print("%d*%d=%d"%(1,i,1*i))


# In[16]:


for i in range(1,10):
    for j in range(1, 4):
        print("%d*%d=%2d"%(j,i,j*i), end='  ')
    print()


# In[27]:


for x in range(0, 3):
    for i in range(1,10):
        for j in range(1, 4):
            print("%d*%d=%2d"%(j+x*3,i,(j+x*3)*i), end='  ')
        print()
    print()


# In[145]:


def gugudan(col):
    if(col > 9): # 함수 인수 조건문
        print("1부터 9까지의 숫자만 입력해주세요!") # 10 이상의 숫자는 무의미
        return # 10 이상 숫자가 함수에 들어오면 함수 종료
    loop = 9//col #전체 루프문을 위한 변수
    print() # 이쁘게 출력하기 위한 print문
    for x in range(0, loop+1): # 1단부터 9단까지 출력하기 위한 전체 루프문
        for i in range(1,10): # *1 ~ *9 까지 출력하기 위한 루프문
            for j in range(1, col+1): # var 열의 개수만큼 보여주기 위한 루프
                if(j+x*col > 9 and 9%col == 0): return #공백 print 제거
                if(j+x*col > 9): break #9단까지만 출력
                #입력된 열수만큼 print 
                print("%d*%d=%2d"%(j+x*col,i,(j+x*col)*i), end='  ')
            print() #단 안에서 개행
        print() #단수 개행

col = int(input("구구단을 나타낼 열의 수를 입력하시오(1~9) : "))
gugudan(col)


# In[ ]:




