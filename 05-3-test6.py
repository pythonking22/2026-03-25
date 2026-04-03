with open("info.txt",'r',encoding='utf8') as file:
    for line in file: # 한줄씩 읽어줌
        name,w,h =line.strip().split(',')
        bmi =int(w)/((int(h)/100)**2)
        result=""
        if 25<= bmi:
            result='과체중'
        elif 18.5 <= bmi:
            result= "정상체중"
        else:
            result="저체충"
        print(f'이름:{name} 몸무게:{w} 키:{h}')
        print(f'Bmi:{round(bmi)} 결과:{result}')      
