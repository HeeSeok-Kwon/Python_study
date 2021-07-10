# 변수와 입력
# 2-4
str_input = input("숫자 입력>")
num_input = int(str_input)
print()
print(num_input, "inch")
print(num_input*2.54, "cm")

# 2-5
str_input = input("숫자 입력>")
num_input = int(str_input)
print()
print("반지름:", num_input)
print("둘레:", 2*3.14*num_input)
print("넓이:", 3.14*num_input**2)

# 2-6
str_input1 = input()
str_input2 = input()
print(str_input1+" "+str_input2)
print(str_input2+" "+str_input1)

# swap
print(str_input1+" "+str_input2)
str_input1, str_input2 = str_input2, str_input1
print(str_input1+" "+str_input2)
