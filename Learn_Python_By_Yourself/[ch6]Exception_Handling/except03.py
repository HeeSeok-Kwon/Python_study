list_number = [52, 273, 32, 72, 100]

try:
  number_input = int(input("정수 입력>"))
  print("{}번째 요소: {}".format(number_input, list_number[number_input]))
  예외.발생해주세요() # 처리하지 않은 에러 발생
except ValueError as excpetion:
  print("정수를 입력해주세요!")
  print(type(excpetion), excpetion)
except IndexError as excpetion:
   print("리스트의 인덱스를 벗어났어요!")
  print(type(excpetion), excpetion)
