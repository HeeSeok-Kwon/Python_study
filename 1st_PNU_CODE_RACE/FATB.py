a, b = map(int, input().split())
res = 0

for i in range(a, b+1):
  res += i

print(res)
