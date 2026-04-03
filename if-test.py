import datetime

now = datetime.datetime.now()
print(now)
print(f"{now.year}년")
print(f"{now.month}월")
print(f"{now.day}일")
print(f"{now.hour}시")
print(f"{now.min}분")
print(f"{now.second}초")
print(f"{now.weekday()}요일") #0=월 1화 2수 3목 4금 5토 6일
##############
month = input("월을 입력하세요(1~12)")
month = int(month)
if 3 <= month <=5:
    print(f"이번 달은{month}월로 봄입니다!")
elif 6 <= month <=8:
    print(f"이번 달은{month}월로 여름입니다!")
elif 9 <= month <=11:
    print(f"이번 달은{month}월로 가을입니다!")
else:
    print(f"이번 달은{month}월로 겨울입니다!")

#################
number = input("정수 입력> ")
last_character = number[-1]

if last_character in "24680":
    print("짝수입니다")
else:
    print("홀수입니다")

####################
ans = input("나이를 입력하세요>>")
print(f"/{ans}/")
if ans: #공백이면 False
    print(f"입력값은 {ans}")
else:
    print(f"입력값은 {ans}")