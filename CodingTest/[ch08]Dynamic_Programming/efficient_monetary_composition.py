n, m = map(int, input().split())

money = []
for i in range(n):
    money.append(int(input()))
    
d = [10001]*(m+1)
d[0] = 0

for i in money:
    for j in range(1, m+1): # for j in range(i, m+1): --> loop 횟수 줄일 수 있다.
        if j-i >= 0:        # Index error만 처리 --> (i-k)원 만드는 방법이 존재하는 경우를 고려한 조건문 필요
            d[j] = min(d[j], d[j-i]+1)
    
if d[m] == 10001: 
    print(-1)
else:
    print(d[m])
