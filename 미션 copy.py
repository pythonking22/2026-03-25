from urllib import request
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+%EC%84%9C%EC%9A%B8"
target = request.urlopen(url) # 접속정보 등록
soup = BeautifulSoup(target, "html.parser")


tag = 'div.detail_info.lv3 > dl' # 온도
#포함한 모든 글자 추출
temp = soup.select_one(tag).get_text()
temp = ' '.join(temp.split())
print('temp:', temp)

tag ='div.detail_info.lv2 > dl'
temp = soup.select_one(tag).get_text()
temp = ' '.join(temp.split())
print('temp:', temp)