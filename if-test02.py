ans = input("나이를 입력하세요>>")
print(f"/{ans}/")
ans = ans.strip() # 공백삭제 strip은 공백을 지움
if ans: #공백이면 False
   # print(f"입력값은 {ans}")
   pass
else:
    print("입력안함")   