def fibo(x):
  if x == 1 or x == 2:
    return 1
  return fibo(x-1) + fibo(x-2)

x = int(input()) # 항의 번호 입력
print(fibo(x))
