from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
city = input('원하시는 주식을 확인해보세요')
def stock(city):
    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%A3%BC%EA%B0%80+" + city
    target = request.urlopen(url) # 접속정보 등록
    soup = BeautifulSoup(target, "html.parser")
    tag = 'a._target' # 온도
    temp = soup.select_one(tag).get_text()
    temp = ' '.join(temp.split())
    
    temp = temp.split()
    result = [temp[1]]
#포함한 모든 글자 추출
    print('주가:', result)

stock(city)
print("end")




