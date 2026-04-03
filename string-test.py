s1 = "abc"
s2= 'abc'
s3="""abc""" #긴 문장을 쓸때 3겹 따옴표를 씀
s4= '''
강나루 건너서
밀밭길을
구름에 달 가듯이
가는 나그네
'''
print(s4)
# s2 = 'TOM's Bear'
s2 = "TOM's Bear"
print(s2)
s2 = 'TOM\'S Bear'
print(s2)
s5= "홍길동"
s6= "안녕하세요"
print( s5+s6)
print( s5+" "+ s6) #질문 print( s5, s6) 차이점 
print( s5, s6)
# print(s5 + 5) #오류. 이후코드 동작 안함
print("홍길동"*3)
print( "홍길동"[0]) #홍
print( "홍길동"[1]) #길
print( "홍길동"[2]) #동
print( s5[0]) #홍
print( s5[1]) #길
print( s5[2]) #동
print( s5[-1] ) #동 #마지막에서 첫번째
print( s5[-2] ) #길 #마지막에서 두번째
print( s5[-3] ) #동 #마지막에서 세번째