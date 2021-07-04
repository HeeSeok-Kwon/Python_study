#!/usr/bin/env python
# coding: utf-8

# In[12]:


# 자판기
money = int(input("돈을 넣어주세요.(원단위) >>> "))
print()
print("+------------------+")
print("|     [자판기]     |")
print("|------------------|")
print("| 1.콜라   1000원  |")
print("| 2.사이다 1000원  |")
print("| 3.식혜    800원  |")
print("| 4.커피    500원  |")
print("| 5.우유    800원  |")
print("| 6.포카리 2000원  |")
print("| 7.보리차 1500원  |")
print("| 8.주스   1500원  |")
print("+------------------+")
print()
menu = {1:"콜라",2:"사이다",3:"식혜",4:"커피",5:"우유",6:"포카리",7:"보리차",8:"주스"}
price = {1:1000,2:1000,3:800,4:500,5:800,6:2000,7:1500,8:1500}

while True:
    try:
        select = int(input("구입할 음료수를 선택해주세요. (0:구입종료)>>> "))
    except:
        print("숫자로 입력해주세요!")
        continue
    else:
        result = select
    
    if result == 0: break
    
    while money < price[result]:
        print("잔액이 부족합니다!")
        coin = int(input("돈을 더 넣어주세요.(원단위) >>> "))
        money += coin
    
    money -= price[result]
    print("\n### %s 구입완료, %d원 남았습니다. ###\n"%(menu[result],money))
    
    if money == 0: break
    else:
        while True:
            yn = input("Y:계속구매, N:구매종료 >>> ")
            if yn == 'n' or yn == 'N' or yn == 'y' or yn =="Y":
                break
            else:
                print("지정된 문자만 입력해주세요.")
                continue
        if yn == 'Y' or yn == 'y': continue
        elif yn == 'N' or yn == 'n': 
            print("%d원을 반환합니다."%(money))
            break
            

