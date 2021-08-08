try:
    num = int(input())
except Exception as error:
    print(error)
else:
    print("for문 -- 구구단")
    for i in range(9):
        res = "{}*{}={}".format(num,(i+1),num*(i+1))
        print(res)

    print("while문 -- 구구단")
    j = 1
    while j < 10:
        res = "{}*{}={}".format(num,j,num*j)
        print(res)
        j += 1
finally:
    print("Program is ended anyway")
