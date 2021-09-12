n, m = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
start = h[0]
end = h[n-1]
res = 0
# 연산 횟수가 많음
while start < end:
  buf = 0
  for i in h:
    if i > start:
      buf += (i - start)
  if buf >= m:
    res = start
  start += 1

print(res)
