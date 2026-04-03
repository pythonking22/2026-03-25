print( 10==100 ) #==는 같냐는 의미
print( 10 != 100 ) # True
print( 10 <= 100) # True
print( 10 >= 100) # false
a= "가방"
b="하마"
print( a == b) # False
print( a < b) # 글자의 순서. True
print( a > b ) # False
c = 35 
print( 10 < c < 30) #True
print ( 10 < c < 20)# 

if not c < 30:
    print("c는 30보다 크다")
    print("c는 30보다 크다")

else:
    print("c는 30보다 작다")
    print("c는 30보다 작다")    
print("END")   
#########################
score = 88
grade = ""
if score> 90 :
    grade = "A"
elif score>= 80 :
    grade = "B"
elif score>= 70 :
    grade = "C"
else:
    grade = "F"
print(f"{score}의 학점은 {grade}")
##################################
score = 88
grade ="" 
if score <= 100 and score >=90:
    grade = "A" 
elif score <90 and score >=80:
    grade = "B" 
elif score <80 and score >=70:
    grade = "C" 
else:
    grade = "F"
print(f"{score}의 학점은 {grade}")
