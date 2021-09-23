n = int(input())
arr = list(map(int, input().split()))

i = 0
m = n
while i != n-2:
  for j in range(1, m):
    arr[j-1] = (arr[j-1] + arr[j])%10
  i += 1 

res = str(arr[0]*10 + arr[1])
if len(res) <= 1:
  print("0"+res)
else:
  print(res)

