
for a in [1,3,5]:
    print(a)
print("END")
########### 로또번호
mylotto =[]
import random 
for a in [1,2,3,4,5,6,7,8,9,10]:
    r = random.randint(1,45)
    #생성된 난수가 로또에 없으면 저장
    if r not in mylotto:
        mylotto.append(r)
    if len(mylotto)==6:
        break #for문 탈출
mylotto.sort()
print('mylotto=', mylotto)