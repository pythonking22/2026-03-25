names = [] # 빈 리스트
scores = [] #빈 리스트
names.append('홍')
scores.append(80)
names.append('김')
scores.append(90)
print(names)
print(scores)
#del names[1] #김 삭제
#names.pop(1) #김 삭제
names.remove('김')
print(names)
scores.clear()
print('scores=',scores)
##################
arr=[30, 50, 70, 60]
arr.sort(reverse=True) #오름차순(ascending)
print(arr)
