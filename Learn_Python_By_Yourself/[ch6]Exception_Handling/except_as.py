list_number = [52, 273, 32, 72, 100]

try:
  number_input = int(input("정수 입력>"))
  print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as excpetion:
  print("excpetion:", excpetion)
except IndexError as excpetion:
  print("excpetion:", excpetion)
