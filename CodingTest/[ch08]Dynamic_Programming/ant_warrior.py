# 내 답안 -- 정답 코드가 아님, 오류가 있을 수 있음
n = int(input())
k = list(map(int, input().split()))

d = [0]*101

for i in range(n-1, -1, -1):
  d[i] = max(d[i+1], d[i+2] + k[i])

print(d[0])
