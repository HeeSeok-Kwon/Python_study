# 2021.07.24 파이썬 스터디 mini project 02
# 1. 숫자 하나 입력받고 1단부터 9단까지 출력
num = int(input())
print("for문 -- 구구단")
for i in range(9):
    res = "{}*{}={}".format(num,(i+1),num*(i+1))
    print(res)

print("while문 -- 구구단")
j = 1
while j < 10:
    res = "{}*{}={}".format(num,j,num*j)
    print(res)
    j += 1
