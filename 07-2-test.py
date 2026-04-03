from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
city = "서울"
city = input("날씨를 알고싶은 도시이름입력>>")
city = quote_plus(city)
url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%9D%BC%EA%B8%B0%EC%98%88%EB%B3%B4+"+city
target = request.urlopen(url)
soup = BeautifulSoup(target, 'html.parser')

temp = soup.select_one("div.temperature_text").get_text()
print('temp=', temp)
summary = soup.select("dl.summary_list")

for dl in summary:
    dt_list = dl.find_all("dt")
    dd_list = dl.find_all("dd")
    
    for dt, dd in zip(dt_list, dd_list):
        if "습도" in dt.get_text():
            print("습도 =", dd.get_text(strip=True))
print('end')
