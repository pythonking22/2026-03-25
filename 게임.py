import curses
import random

# 화면 초기화
s = curses.initscr()
curses.curs_set(0)              # 커서 숨기기
sh, sw = s.getmaxyx()           # 화면 높이와 너비
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)                     # 키보드 입력 활성화
w.timeout(100)                   # 화면 갱신 시간(ms)

# 초기 스네이크 위치
snk_x = sw//4
snk_y = sh//2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# 먹이 초기 위치
food = [sh//2, sw//2]
w.addch(food[0], food[1], curses.ACS_PI)

# 초기 방향
key = curses.KEY_RIGHT

score = 0

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # 몸 길이 증가 위해 새로운 머리 위치 계산
    y = snake[0][0]
    x = snake[0][1]

    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    new_head = [y, x]

    # 벽 또는 자기 몸과 부딪히면 종료
    if y in [0, sh] or x in [0, sw] or new_head in snake:
        curses.endwin()
        print(f"게임 종료! 점수: {score}")
        quit()

    snake.insert(0, new_head)

    # 먹이를 먹으면 점수 증가, 새로운 먹이 생성
    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        # 꼬리 제거
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # 스네이크 머리 그리기
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)