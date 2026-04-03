'''
금광찾기게임 (GoldMinder)
가로 세로 10x10공간안에 컴퓨터가 임의의 좌표에 금을 숨김
사용자가 임의의 x,y좌표를 입력하면 
금광의 직선거리를 정수로 반환.
정확한 좌표입력시 "금을 찾았읍니다" 출력
### 금광찾기게임 v0.1 ###
금의 좌표를 입력하세요(10x10이내 x,y) 5,7
금과의 직선거리 5 
...
...
금의 좌표를 입력하세요(10x10이내 x,y) 3,4
**정답입니다**
'''
print('### 금광찾기게임 v0.1 ###')
import random
com_x=random.randint(1,10)
com_y=random.randint(1,10)
while True:
    ans=input('금의 좌표를 입력하세요(10x10이내 x,y)')
    user_x, user_y = ans.split(",")
    user_x, user_y = int(user_x), int(user_y) #글자를 숫자로 
    diff_x = abs(com_x - user_x) #X좌표 절대값
    diff_y = abs(com_y - user_y) #Y좌표 절대값
    print(diff_x, diff_y)
    diff_z = (((diff_x**2)+(diff_y**2))**(0.5)) #지도상 직선거리
    diff_z = round(diff_z) # 반올림
    if diff_z == 0:
        print(f'금과의 직선거리 : {diff_z}')
        break # 정답
    else:
        print('틀렸습니다.')
    print(f'금과의 직선거리 : {diff_z}')
print('정답입니다')

