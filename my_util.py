from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
#도시이름 입력

def get_weather(city='서울'):
    
    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%9D%BC%EA%B8%B0%EC%98%88%EB%B3%B4+"+city
    target = request.urlopen(url) # 접속정보 등록
    soup = BeautifulSoup(target, "html.parser")


    tag = 'div.temperature_text' # 온도
    mytemp = soup.select_one(tag).get_text().strip() #공백이 많음
    
    tag = 'div.temperature_info' # 습도,날씨 , 풍량
    #포함한 모든 글자 추출 
    temp = soup.select_one(tag).get_text() #공백이 많음
    temp = temp.strip() #앞뒤공백 삭제
    temp = ' '.join(temp.split()) #모든공백을 1개 공백으로 압축
    temp = temp.split()
    print(temp)
    return {
        'temp' : mytemp,
        'yestd':temp[1]+" "+temp[2], #어제보다
        'weather':temp[3], #날씨
        'humd':temp[7], #습도
        'wd':temp[8], #풍향
        'winds':temp[9], #풍속
    }

def get_dust(city="서울"):
    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+"+city
    target = request.urlopen(url)#접속정보 등록
    soup = BeautifulSoup(target, "html.parser")

    tag = "div.detail_info.lv3 > dl"#미세먼지 오전
#포함한 모든 글자 추출
    temp = soup.select_one(tag).get_text()
    temp = ' '.join(temp.split())
    temp = temp.split()
    result = {temp[0] : temp[1]}#{'오전':'나쁨'}

    tag = "div.detail_info.lv2 > dl"#미세먼지 오후
#포함한 모든 글자 추출
    temp = soup.select_one(tag).get_text()
    temp = ' '.join(temp.split())
    temp = temp.split()
    result[temp[0]] = temp[1] #{'오전':'나쁨'}
    print('result:', result)
    return result

if __name__ == "__main__":
    city= '서울'
    ans= get_weather(city)
    print(f'{city} 온도는 {ans['temp']} 입니다.')
    ans = get_dust(city)
    print(f'{city} 미세먼지는 {ans['오전']}')
#print( "__name__", __name__)