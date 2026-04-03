from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def get_dust(city):
    city_enc = quote_plus(city)
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+" + city_enc
    target = request.urlopen(url)
    soup = BeautifulSoup(target, "html.parser")

    # 태그 시도 목록 (네이버가 바뀌면 여기 수정)
    tags = ['dd.lvl', 'span.lvl', 'div.lvl', 'p.lvl']

    for tag in tags:
        result = soup.select_one(tag)
        if result:
            return result.get_text()

    # 태그를 못찾으면 후보 출력
    print("태그를 찾지 못했어요. 아래에서 직접 확인하세요:")
    print(soup.prettify()[:3000])
    return None

if __name__ == "__main__":
    city = input("어떤 도시의 미세먼지가 궁금하십니까? ")
    result = get_dust(city)
    if result:
        print(f'{city} 미세먼지: {result}')