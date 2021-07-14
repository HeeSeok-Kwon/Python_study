# 함수 고급
# 5-1
numbers = [1,2,3,4,5,6]
print("::".join(str(i) for i in numbers))

# 5-2
numbers = list(range(1, 10+1))

print("# 홀수만 추출하기")
print(list(filter(lambda x: x%2 == 1,numbers)))
print()

print("# 3 이상, 7 미만 추출하기")
print(list(filter(lambda x: x >= 3 and x < 7,numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda x: x**2 < 50,numbers)))
print()
