# list
# 4-1
list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.extend(list_a)
print(list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.append(10)
print(list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.insert(3,0)
print(list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.remove(3)
print(list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.pop(3)
print(list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.clear()
print(list_a)

# 4-2
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
  if number >= 100:
    print("- 100 이상의 수:", number)


# 4-3
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
  if number%2 == 1:
    print(number, "는 홀수입니다.")
  else:
    print(number, "는 짝수입니다.")

for number in numbers:
  if number//100 > 0:
    print(number, "는 3 자릿수입니다.")
  elif number//10 > 0:
    print(number, "는 2 자릿수입니다.")
  else:
    print(number,"는 1 자릿수입니다.")

# 4-4
list_of_list = [
  [1,2,3],
  [4,5,6,7],
  [8,9]
]
for i in list_of_list:
  for j in i:
    print(j)

# 4-5
numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
  output[(number-1)%3].append(number)

print(output)
