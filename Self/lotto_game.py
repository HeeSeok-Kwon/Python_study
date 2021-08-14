# lotto 번호 6개 추출하는 프로그램

from random import sample

def lotto_extract() :
    lotto_numbers = sorted(sample(range(1, 10), k=6))
    for j in range(0, 2):
        cnt = 0
        for r in range(j,j+4):
            if lotto_numbers[r] + 1 == lotto_numbers[r+1]: cnt += 1  
        if cnt > 4: 
            return "consecutive numbers!!!"
    return lotto_numbers


play_times = input("게임 횟수를 입력해주세요> ")

for i in range(0, int(play_times)):
    result = lotto_extract()
    print(result)
