age = 3

def p(): #함수의 안에 있는 age는 local 밖에 있는 age는 global이라고 불림
    global age #,함수 밖에 있는 age 즉 여기서도 age =3
    age =  5
    print('age', age)
p()
print('age', age)