n, m = map(int, input().split())

money = []
for i in range(n):
    money.append(int(input()))
    
d = [10001]*(m+1)
d[0] = 0

for i in money:
    for j in range(1, m+1):
        if j-i >= 0:
            d[j] = min(d[j], d[j-i]+1)
    
if d[m] == 10001: 
    print(-1)
else:
    print(d[m])
