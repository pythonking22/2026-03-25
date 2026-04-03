from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

#city = input('어느 도시의 미세먼지가 궁금하십니까?')
def get_dust(city='서울'):
    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+" + city
    target = request.urlopen(url) # 접속정보 등록
    soup = BeautifulSoup(target, "html.parser")


    tag = 'div.detail_info.lv3 > dl' # 온도
    #포함한 모든 글자 추출
    temp = soup.select_one(tag).get_text()
    temp = ' '.join(temp.split())
    temp = temp.split()
    result = {temp[0] : temp[1]} #{'오전' : '나쁨'}

    tag ='div.detail_info.lv2 > dl'
    temp = soup.select_one(tag).get_text()
    temp = ' '.join(temp.split())
    temp = temp.split()
    result = [temp[0]] = temp[1]
    print('result', result)
    return result

get_dust()

