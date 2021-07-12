# while
# 4-2
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}
for i in range(4):
  character[key_list[i]] = value_list[i]
print(character)

# 4-3
limit = 10000
i = 1
sum_value = 0
while sum_value <= limit:
  sum_value += i # 10011
  i += 1 # i가 추가로 더해짐
print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1,limit,sum_value))

# 4-4
max_value = 0
a = 0
b = 0
for i in range(1, 100):
  j = 100 - i

  if max_value <= i*j:
    max_value = i*j
    a = i
    b = j

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))
  
