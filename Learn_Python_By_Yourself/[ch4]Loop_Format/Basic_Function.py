# enumerate
# 변수를 선언
example_list = ["요소A", "요소B", "요소C"]
# 그냥 출력
print("# 단순 출력")
print(example_list)
print()

# enumerate 적용
print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

# list 강제 변환
print("# list() 함수로 강제 변환해 출력")
print(list(enumerate(example_list)))
print()

print("# 반복문과 enumerate() 함수 조합해서 사용")
for i, value in enumerate(example_list):
  print("{}번째 요소는 {}입니다.".format(i, value)) 

# items
# 변수를 선언
example_dictionary = {
  "키A":"값A",
  "키B":"값B",
  "키C":"값C"
}

# 딕셔너리의 items() 함수 결과 출력
print("# 딕셔너리의 items() 함수")
print("items():", example_dictionary.items())
print()

print("# 딕셔너리의 items() 함수와 반복문 조합")
for key, value in example_dictionary.items():
  print("dictionary[{}] = {}".format(key, value))

# 리스트 안에 for문 사용
arr = [i*i for i in range(0,20,2)]
print(arr)

arr = ["사과","자두","초콜릿","바나나","체리"]
output = [fruits for fruits in arr if fruits != "초콜릿"]
print(output)

# 4-2
print("{:b}".format(10))
print(int("1010", 2))

print("{:o}".format(10))
print(int("12", 8))

print("{:x}".format(10))
print(int("10", 2))

string = "안녕안녕하세요"
print(string.count("안"))

output = [x for x in range(1,101) if "{:b}".format(x).count("0") == 1]
for i in output:
  print("{} : {}".format(i, "{:b}".format(i)))
print("합계:",sum(output))
