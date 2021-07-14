# 함수 만들기 
# 5-1

# def f(x):
#   return 2*x + 1
# print(f(10))

def f(x):
  return x**2+2*x + 1
print(f(10))

# 5-2
def mul(*values):
  value_sum = 1
  for value in values:
    value_sum *= value
  return value_sum
print(mul(5, 7 , 9, 10))

# 5-3
# error code
def function(*values, valueA, valueB):
  pass
function(1,2,3,4,5)

# works well
# def function(*values, valueA=10, valueB=20):
#   pass
# function(1,2,3,4,5)

# works well
# def function(valueA, valueB, *values):
#   pass
# function(1,2,3,4,5)

# works well
# def function(valueA=10, valueB=20, *values):
#   pass
# function(1,2,3,4,5)

