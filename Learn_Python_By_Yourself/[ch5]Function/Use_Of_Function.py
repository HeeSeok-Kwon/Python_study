# 함수 활용
# 5-1
# 내 방식
# buf = []
# def flatten(data):
#   print(data)
#   for i in data:
#     if type(i) == list:
#       flatten(i)
#     else:
#       buf.append(i)
#   return buf

# 정답 코드

def flatten(data):
  output = []
  for i in data:
    if type(i) == list:
      output += flatten(i) # list + list code
      # print("output:",output)
    else:
      output.append(i)
  return output

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본:",example)
print("원본:",flatten(example))

# 5-2
min_n = 2
max_n = 10
total_n = 100
memo={}

def sol(rest, sit):
  key = str([rest,sit])
  # print(key)
  if key in memo:
    return memo[key]
  if rest < 0:
    return 0
  if rest == 0:
    return 1
  cnt = 0
  for i in range(sit, max_n+1): # 2 ~ 10 까지
    cnt += sol(rest-i, i)
  memo[key] = cnt
  return cnt

print(sol(total_n, min_n))
