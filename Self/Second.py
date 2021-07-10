# 2021.07.10 파이썬 스터디 mini project 01
# 초를 입력받고 시, 분, 초를 출력하는 프로그램

# 입력
sec = int(input("몇 초를 입력하시겠습니까? "))
if sec < 0:
    print("올바른 입력이 아닙니다! 다시 시도해주세요.")
else:
    # 시간
    hour = sec//3600
    sec -= (hour*3600) # sec = sec - (hour*3600) 
    # 분
    minute = sec//60
    sec -= (minute*60)
    print("{}시간 {}분 {}초 경과".format(hour, minute, sec))
