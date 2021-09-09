# 순차 탐색
def sequential_search(n, target, array):
  for i in range(n):
    if array[i] == target:
      return i+1 # 타깃의 인덱스 반환 

print("생성할 원소의 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split() # 리스트로 대입 
# print(input_data)
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

result = sequential_search(n, target, array)
print(result)
