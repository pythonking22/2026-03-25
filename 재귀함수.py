#def fac(n):
#    if n==0:
#        return 1
#    else:
 #       return n*fac(n-1)
#ans = fac(3)
#print('fac(3)=',ans)
##########
t1= (1,3,5)
print(t1)
print(t1[1])#3
#t1[1] = 4 #오류. 튜플은 변경불가능
t2= [3]
print(type(t2))# class 'list'
t2= (3,)
print(type(t2))# class 'tuple'
# 학생들의 점수를 입력받아 총점과 평균계산
def calc_total_avg(*values):
    total =0
    avg= 0
    total= sum(values)
    avg=total/len(values)
    return total, avg

t, a=calc_total_avg(10,30,50)
print('total', t)# total
print('avg',a)# 평균

a,b= 10, 20
print(a,b)
a,b =b,a 
print(a,b)

print(calc_total_avg)


def print_func(fn):
    fn(); fn(); fn()
def hello():
    print("Hello")
print_func(hello)