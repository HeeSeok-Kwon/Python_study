#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:





# In[115]:


rand = np.random.randint(1, 46) # 1부터 45까지의 숫자중 하나 반환
print(rand)


# In[141]:


# 로또 번호 추출
arr = []
for i in range(0, 6): # 1부터 45까지의 숫자중 하나 생성
    rand = np.random.randint(1, 46)
    for j in arr: # list인 arr 원소 수만큼 j가 루프를 돈다.
        while(rand == j): # 같은 숫자가 나오는 것을 방지
            rand = np.random.randint(1, 46)
#     for j in range(0,i):
#         while(arr[j] == rand): # 같은 숫자가 나오는 것을 방지
#             rand = np.random.randint(1, 46)
    arr.append(rand)
    
for i in range(1,6): # 생성된 여섯자리 로또 번호 sorting (오름차순)
    for j in range(0, i):
        if(arr[j] >= arr[i]):
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

print('오늘의 당첨번호는',arr, "입니다.")


# In[136]:


import time

def hgj(sentence, timesl=0.1): # 한 글자씩 출력
    for i in range(len(sentence)):
        print(sentence[i], end="")
        time.sleep(timesl)

# 로또 구매
class buyer:
    def __init__(self):
        self.Wallet = 0
        self.chance = 1
        self.mylotto = []
    
    def initWallet(self): # 지갑 생성
        self.Wallet = 10
        print("당신의 지갑에는", self.Wallet,"만원 있습니다.")
    
    def myStatus(self): # 내 현재 잔고와 구매횟수 알아보는 함수
        print("당신의 잔고는", self.Wallet,"입니다.")
        print('기회는', self.chance,"번 남았습니다.")
        return
    
    def reset(self): # 새롭게 복권 구매할 수 있도록 하는 함수
        self.Wallet = 0
        self.chance = 1
        self.mylotto = []
        print("새롭게 복권구매가 가능합니다!")
    
    def winnings(self, arr):
        cnt = 0
        for i in arr:
            for j in range(1, 7):
                if(i == self.mylotto[j]): cnt += 1
        
        if cnt <= 2:
            print("당첨금은 아쉽게도 없습니다...")
        elif cnt == 3:
            print("당첨금은 5000원 입니다!")
        elif cnt == 4:
            print("당첨금은 10,000원 입니다!")
        elif cnt == 5:
            print("당첨금은 100,000원 입니다!")
        elif cnt == 6:
            print("축하합니다!!! 당첨금은 1,000,000,000원 입니다!")
    
    def buyLotto(self): # 로또 구매
        if(self.chance <= 0):
            print("1일 구매가능횟수를 초과하였습니다.")
            return
        
        if(self.Wallet < 10):
            print("잔고가 부족합니다.")
            return
        
        self.chance -= 1
        self.Wallet -= 10
        ############## 조 결정 ############## 
        print("Enter, q : 구매 (강제)종료")
        hgj("조를 결정하시오.(1조~7조):")
        group = input()
        if(group == '' or group == 'q'): 
            print("로또 구매가 (강제)종료됩니다.")
            self.Wallet = 0; self.chance = 1; self.mylotto = [];
            return
        group = int(group)
        while(not(group >= 1 and group <=7)):
                print("1부터 7까지의 숫자 안에서 결정하시오.:", end="")
                group = int(input())  
        self.mylotto.append(group)
                       
        print() 
        ############## 로또 번호 입력 ############## 
        for i in range(1,7): 
            hgj("%d번째 로또번호를 입력하시오.(1~45):"%i)
            r = input()
            if(r == '' or r == 'q'): 
                print("로또 구매가 (강제)종료됩니다.")
                self.Wallet = 0; self.chance = 1; self.mylotto = [];
                return
            r = int(r)
            while(not(r >= 1 and r <=45)): # 로또 번호 제한 조건1
                print("1부터 45까지의 숫자만 입력하시오.:", end="")
                r = input()
                if(r == '' or r == 'q'): 
                    print("로또 구매가 (강제)종료됩니다.")
                    self.Wallet = 0; self.chance = 1; self.mylotto = [];
                    return
                r = int(r)
                
            if(i == 1):
                self.mylotto.append(r)
                continue
            elif(i >= 2):
                for j in range(1,i): # 로또 번호 제한 조건2
                    while(r == self.mylotto[j] or not(int(r) >= 1 and int(r) <=45)): 
                        print("1부터 45까지의 각기 다른 번호를 입력해주세요.:", end="")
                        r = input()
                    if(r == '' or r == 'q'): 
                        print("로또 구매가 (강제)종료됩니다.")
                        self.Wallet = 0; self.chance = 1; self.mylotto = [];
                        return
                    r = int(r)
            self.mylotto.append(r)
#             print("디버깅", self.mylotto)
#             print("디버깅", r)
        ############## 로또 번호 sorting ############## 
        arr = self.mylotto
#         print("디버깅", arr)
        for i in range(1,7): # 생성된 여섯자리 로또 번호 sorting (오름차순)
            for j in range(1, i):
                if(arr[j] >= arr[i]):
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
        print("조:%d  로또번호: %d %d %d %d %d %d"%(arr[0],arr[1], arr[2], arr[3],
                                              arr[4], arr[5], arr[6]))
        self.mylotto = arr
        


# In[ ]:





# In[137]:


buyer1 = buyer()
buyer1.initWallet()


# In[138]:


buyer1.buyLotto()


# In[139]:


buyer1.myStatus()


# In[142]:


buyer1.winnings(arr)


# In[143]:


buyer1.reset()

