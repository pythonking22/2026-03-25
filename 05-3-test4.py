#######map() 함수############
def power(item):
    return item**2

list_1=[1,2,3]
r1=map(power, list_1)
list_2='10,20,30'.split(',')
print(list_2)
list_3 = [int(i) for i in list_2]
print(list_3)
print(type(r1))
print(list(r1)) #r1은 리스트 형태이기 때문에
a=2 , 4, 6
print(list(a))

def to_int(c):
    return int(c)
r2=map(to_int, list_2)
print(list(r2))
########짝수만 추출###########
list_4 = [ i for i in list_1 if i%2==0 ]
#원래의 경우
#for i in list1:
#    if i%2==0:
#        list4.append(i) 로 해야됨 
def only_even(i):
    return i%2==0


list_4 = filter(only_even, list_1)

print(type(list_4))
print(list(list_4))
#######################################
names = '홍길동,김길동,박길동'.split(',') #김씨만 추출해주는 필터 생성
def only_kim(i):
    return i[0]== '김'
kims = filter(only_kim, names)
print(list(kims))


power = lambda x: x*x 
print(power(3))
print(list(map(power, [1,3,5])))
a=map(power, [1,3,5])
print(list(a))
