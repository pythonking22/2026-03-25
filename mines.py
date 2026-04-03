#지뢰찾기(빨리 터트리기)
#10x10 영역에 3개의 지뢰를 매설
# 최소의 시도로 모두 터트리기
#실력대로 해보기
# (5x5-2), 중급(7x7-4) 고급(10x10-7)
#레벨을 선택하세요
#1 - 초급 (5x5) 지뢰 2개
#2 - 중급 (7x7) 지뢰 4개
#1 - 고급 (10x10) 지뢰 7개
# 선택 레벨>>
level = input("레벨 선택 (1:초급, 2:중급, 3:고급) >> ")
if level == '1':
    mines = []
    nums = []
    size = 5
    mine_target = 2
elif level == '2':
    mines = []
    nums = []
    size = 7
    mine_target = 4
elif level == '3':
    mines = []
    nums = []
    size = 10
    mine_target = 7
else:
    print("잘못된 입력! 기본값(고급)으로 설정")
    mines = []
    nums = []
    size = 10
    mine_target = 7
    for i in range(size):
        mines.append(['+'] * size)
    for i in range(size):
        nums.append([0] * size)
#임의의 지점에 지뢰 저장 (3개)
mine_count=0
while mine_count < mine_target:
    import random   
    row = random.randint(0, size-1)
    col = random.randint(0, size-1)
    #폭탄이 같은자리인경우 배치취소
    if nums[row][col]>= 9: continue
    mine_count += 1 #배치폭탄 갯수 1 증가
    nums[row][col] = 9
# 이웃한 8개 방의 숫자를 1증가
    if row !=0 and col !=0 : nums[row-1][col-1] += 1
    if row !=0 : nums[row-1][col] += 1
    if row !=0 and col !=size-1 : nums[row-1][col+1] += 1
    if col !=0 : nums[row][col-1] += 1
    if col !=size-1 : nums[row][col+1] += 1
    if row !=size-1 and col !=0 : nums[row+1][col-1] += 1
    if row !=size-1 : nums[row+1][col] += 1
    if row !=size-1 and col !=size-1 : nums[row+1][col+1] += 1
# 확인 
#for i in nums:
#   print(i)
remain_mine = mine_count #남은 폭탄갯수
attempt = 0
attempt += 1
while remain_mine !=0:
    msg='지뢰의 좌표를 입력하세요(0~size-1,0~size-1) x,y>>'
    attempt
    try:
        ans = input(msg)
        u_row, u_col = ans.split(',')
        u_row, u_col = int(u_row), int(u_col)
    except ValueError:
        print("입력 오류! 예: 3,4")
        continue
    if nums[u_row][u_col] >= 9: #지뢰 찾으면
        mines[u_row][u_col]="$"
        remain_mine -= 1 #남은 폭탄수 1감소
    else:
        mines[u_row][u_col]=str(nums[u_row][u_col])
        #mines 리스트 출력
    for m in mines:
        print(" ".join(m))
    print(f"남은 지뢰: {remain_mine}")
    print(f"총 시도 횟수: {attempt}")




