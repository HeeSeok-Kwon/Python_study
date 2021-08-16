try:
    n = int(input())
except Exception as error:
    print(error)
else:
    total_count = 0
    money_types = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
    for money in money_types:
        count = (n//money)
        print(money, count)
        total_count += count
        n %= money
    print("Total number of currency needed:",total_count) 
finally:
    print("Program is ended anyway")
