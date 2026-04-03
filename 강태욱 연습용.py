from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

#도시이름 입력

city = "서울"
def get_weather(city):
    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?where=nv&sm=top_sug.pre&fbm=0&acr=1&acq=%EC%9D%BC%EA%B8%B0%EC%98%88%EB%B3%B4+%EC%84%9C&qdt=0&ie=utf8&query=%EC%9D%BC%EA%B8%B0%EC%98%88%EB%B3%B4+"+city
    target = request.urlopen(url)#접속정보 등록
    soup = BeautifulSoup(target, "html.parser")

    tag = "div.temperature_text"#온도
    mytemp = soup.select_one(tag).get_text().strip() #공백이 많음
    
    tag = "div.temperature_info"#습도, 날씨, 풍량
    #포함한 모든 글자 추출
    temp = soup.select_one(tag).get_text() #공백이 많음
    temp = temp.strip() #앞뒤공백 삭제
    temp = ' '.join(temp.split()) #모든공백을 1개공백으로 압축
    temp = temp.split()
    return {
        'temp':mytemp,
        'yestd':temp[1]+" "+temp[2],#어제보다
        'weather':temp[3],#날씨
        'humd':temp[7],#습도
        'windd':temp[8],#풍향
        'winds':temp[9],#풍속
    }

city = '수원'
ans = get_weather(city)
print(f'{city} 온도는 {ans}')