#file = open("basic.txt","a")
#file.write("\n")
#file.write("헬로 파이썬 프로그래밍 4")
#input("엔터키 누르세요")
#file.close()
#print('end')

with open("basic.txt", "a") as file:
    file.write("\n")
    file.write("Basic1\nBasic2\nBasic3")
    file.writelines()
print('end')

with open("basic.txt", 'r') as file:
    contents = file.read()
print(contents)