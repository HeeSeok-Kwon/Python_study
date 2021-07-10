# format()

# format_basic
# format() 함수로 숫자를 문자열로 변환하기
string_a = "{}".format(10)
# 출력하기
print(string_a)
print(type(string_a))
print()

# format01
# format() 함수로 숫자를 문자열로 변환하기
format_a = "{}만원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)
# 출력하기
print(format_a)
print(format_b)
print(format_c)
print(format_d)
print()
# IndexError
# print("{} {}".format(1, 2, 3, 4, 5))
# print("{} {} {}".format(1, 2))

# format02
# 정수
output_a = "{:d}".format(52)
# 특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)
# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)
print()

# format03
# 기호와 함께 출력하기
output_f = "{:+d}".format(52)
output_g = "{:-d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)
print()

# format04
# 조합하기
output_h = "{:+5d}".format(52)
output_i = "{:+5d}".format(-52)
output_j = "{:=+5d}".format(52)
output_k = "{:=+5d}".format(-52)
output_l = "{:+05d}".format(52)
output_m = "{:+05d}".format(-52)

print("# 조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)
print()
# print("{:=+05d}".format(-52)) # "{:+05d}".format(-52) 과 같은 결과
# print("{:=0+5dd}".format(-52)) # Invalid format specifier


# format05
output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)
output_c = "{:+15f}".format(52.273)
output_d = "{:+015f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print()

# format06
# 소수점 아래 자릿수 지정
output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)
print()

# format07
# 의미 없는 소수점 제거
output_a = 52.0
output_b = "{:g}".format(output_a)
print(output_a)
print(output_b)

# 2-3
a = input("> 1번째 숫자: ")
b = input("> 2 번째 숫자: ")
print()

print("{} + {} = {}".format(a, b, int(a)+int(b)))

# 2-4
string = "hello"
string.upper()
print("A 지점:", string)
print("B 지점:", string.upper())
