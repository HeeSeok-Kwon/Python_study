# Dictionary
# 4-1
dict_a = {}
dict_a['name'] = '구름'
print(dict_a)
del dict_a['name']
print(dict_a)

# 4-2
pets = [
  {"name":"구름", "age":5},
  {"name":"초코", "age":3},
  {"name":"아지", "age":1},
  {"name":"호랑이", "age":1}
]
print("# 우리 동네 애완 동물들")
for x in pets:
  print(x["name"], "{}살".format(x["age"]))

# 4-3
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}
for number in numbers:
#   counter[number] = 0
# for number in numbers:
#   counter[number] += 1
  if number in counter:
    counter[number] += 1
  else:
    counter[number] = 1
print(counter)

# 4-4
character = {
  "name":"기사",
  "level":12,
  "items": {
    "sword": "불꽃의 검",
    "armor": "풀플레이트"
  },
  "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
  if type(character[key]) == dict:
    for inner in character[key]:
      print(inner,":",character[key][inner])
  elif type(character[key]) == list:
    for inner in character[key]:
      print(key,":",inner)
  else:
    print(key,":",character[key])
