def print_n_times(n, *values): #n번 반복합니다. 
    for i in range(n):#values는 리스트처럼 활용합니다.
        for value in values:
            print(value)#단순한 줄바꿈
print_n_times(3, "안녕하세요" ,"즐거운" ,"파이썬 프로그래밍")


##############
def print_n_times(*values, n):
    for i in range(n):
        for v in values:
            print(v)
        print(v)
print_n_times("안녕", "즐거운" ,"파이썬 프로그래밍", n=3) 
#############
def print_n_times(*values, n=1):
    for i in range(n):
        for v in values:
            print(v)
        print()
    return #함수는 무조건 return을 함 return은 함수의 진행을 막음
ans= print_n_times("안녕", "즐거운" ,"파이썬 프로그래밍", n=3)
print('ans', ans)
############
#value=input(">")
#print(value)

#def return_test():
#    return 
#value=return_test()
#print(value)

#greeting(이름) -> 출력; 안녕하세요 이름님 
def greeting(name):
    return "안녕하세요"+" " +name+ "님"
ans=greeting("강태욱") # -> 안녕하세요 홍길동님
print(ans)

#입력받는 숫자들의 평균을 반환하는 함수 
def calc_avg(*values):
    tot= 0 
    for i in values:
        tot += i 
        return tot/ len(values)
ans =calc_avg(10, 20, 30, 40, 50)
print(ans)
ans = calc_avg(10,20)
print(ans)


#def get_grade(values):
    #if 90<= values:
        #return 'A'
    #if 80<=values:
        #return 'B'
   # if 70<=values:
       # return 'C'
    #return 'F'
#values = int(input("점수를 입력하세요 (0~100): "))
#grade = get_grade(values)
#print(f"점수: {values}-> 학점:{grade}")

#가위, 바위, 보 중 하나는 임의로 반환하는 함수
#이름; get_gbb()
## 사용예시
def get_gbb():
    import random
    #choices = ['가위', '바위', '보']
    arr= ('가위','바위','보')
    r = random.randint(1, 3)         
    return arr[r]                   
ans = get_gbb()
print(ans)