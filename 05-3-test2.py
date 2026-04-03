#숫자맞추기 게임 (UP DOWN)
#1=100사이 임의의숫자를 컴퓨터가 정한것을 스무고개형식으로 맞추는 게임
#출력예시) 
# 1~100사이 숫자 입력>>70 
# 낮춰주세요
#1 2 3 4 5 6 ........ 68, 69
# 1~100사이 숫자 입력>>60
#높여주세요
#61 62 63 64 ......... 68 69
# 1~100사이 숫자 입력>>65
#낮춰주세요
#61 62 63 64
############
print("### 숫자맞추기게임 v0.1 ###")
#1~100사이 임의의정수를 저장
import random
com=random.randint(1,100)
low= 1
high = 100
count=0
for count in range(0, 6):
    count +=1
    user=input(f"{count}번째 시도, 1~100사이 숫자>>")
    user=int(user)
    #판정
    if com == user:
        print(f"정답입니다. 당신은 {count}번 만에 맞췄습니다.")
        break #반복문 종료
    elif user < com:
        low = user + 1
        print(f"높습니다. 정답은 {low}~{high} 사이에 있습니다.")

    elif user > com:
        high = user - 1
        print(f"낮습니다. 정답은 {low}~{high} 사이에 있습니다.")

    if count >5:
        print(f"정답은 {com} 당신은 바보입니까?")
         
