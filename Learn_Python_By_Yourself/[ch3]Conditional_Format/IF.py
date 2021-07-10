# 3-4
a = int(input("> 1번째 숫자:"))
b = int(input("> 2번째 숫자:"))
print()

if a > b:
    print("처음 입력했던 {:.1f}가 {:.1f}보다 더 큽니다.".format(a, b))
if b > a :
    print("두 번째로 입력했던 {:.1f}가 {:.1f}보다 더 큽니다.".format(b, a))
