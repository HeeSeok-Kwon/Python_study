# N = int(input("거스름돈:"))
# count = 0
# while N>0:
#   if N>=500 :
#     count += N//500
#     N = N%500
#   elif N>=100 :
#     count += N//100
#     N = N%100
#   elif N>=50:
#     count += N//50
#     N = N%50
#   else :
#     count += N//10
#     N = N%10

# print(count)


n = 1260
count = 0

coin_type = [500,100,50,10]

for coin in coin_type:
  count += n//coin
  n %= coin

print(count)