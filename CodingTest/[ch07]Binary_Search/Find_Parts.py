# 부품 찾기 - my answer
def find_part(parts, target, start, end):
  if start > end:
    return "no"
  mid = (start+end)//2
  if parts[mid] == target:
    return "yes"
  elif parts[mid] >= target:
    return find_part(parts, target, start, mid-1)
  else: 
    return find_part(parts, target, mid+1, end)

n = int(input())
parts = list(map(int, input().split()))
parts.sort()

m = int(input())
demand = list(map(int, input().split()))

for i in range(m):
  result = find_part(parts, demand[i], 0, n-1)
  print(result, end=" ")
