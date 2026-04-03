#구구단출력 - 3단
# 3 * 1 = 3 
# 3 * 2 = 6
dan = 3
print( "{} * {} = {}". format(dan,1,dan*1)) #dan=첫번째 대괄호 , 1=두번째 대괄호 , dan*1= 세번째 대괄호 
print( "{} * {:05d} = {}". format(dan,1,dan*1))
print("헬로 Python 프로그래밍".upper())
a="""
         헬로 파이썬 프로그래밍
"""         
print(a.strip()+"/")
print("안녕123".isalnum()) # True   is~()는 확인용도로 사용
print("abc abc programming".find("bc",))
a="안녕하세요"
print("안녕" in a)
print("방가" in a)

b= "홍,김,박,강".split(",")
print(b)
b= "100,200,300,400,500".split(",")
print(int(b[0]))
print(int(b[0])+int(b[1]))
#합과 평균
total = 0 
mean = 0
total= int(b[0])+int(b[1])+int(b[2])+int(b[3])
print("total={}".format(total))
print("Average={}".format(total/4))
print("total="+str(total))
print(f"total={total}")
print(f"평균={total/4}")

#구구단 3단
dan=3
print(f"{dan}*{1}={dan*1}")
print(f"{dan}*{2}={dan*2}")
print(f"{dan}*{3}={dan*3}")
print(f"{dan}*{4}={dan*4}")
print(f"{dan}*{5}={dan*5}")
print(f"{dan}*{6}={dan*6}")

#생년을 입력받아 나이를 계산해서 출력하기 생년=input("생년월일을 입력하세요")
#나이=2026-int(생년)+1
#print(f"당신의 나이는 {나이}살 입니다.")
print("{}{}".format(52,type(273)))
"{} {}".format(52,type(273))