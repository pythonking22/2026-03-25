from urllib import request
from bs4 import BeautifulSoup

url = "https://news.naver.com/section/105"
target = request.urlopen(url) # 접속정보 등록
soup = BeautifulSoup(target, "html.parser")
tag = 'li.rl_item .rl_txt' # 온도
temp = soup.select(tag)
for t in temp:
    tittle = t.get_text()
    print("기사제목:", tittle)