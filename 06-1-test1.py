try:
    list_1 =[10,20,30]
    n = list_1[3]
    print(n)
except Exception as ex:
    print("오류 발생!!")
    print('TYPE',type(ex))
    print('ex', ex)

print("end")

#list_input_a =["52", "273", "32", "스파이", "103"]
#list_number=[]
#for item in list_input_a:
 #   try:
 #       float(item)
 #       list_number.append(item)
 #   except:
 #       pass
#print(f" {{  }} 내부에 있는 숫자는{list_number}입니다.")
