n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
  total = 0
  mid = (start+end)//2
  # 잘랐을 때 떡의 양 계산
  for x in arr:
    if x > mid:
      total += x - mid
  
  if total < m:
    end = mid - 1
  else:
    result = mid # 최대한 덜 잘랐을 때가 정답
    start = mid + 1

print(result)
