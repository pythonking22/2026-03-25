import tkinter as tk
import requests
from bs4 import BeautifulSoup
import urllib.parse

def get_naver_weather(city):
    try:
        query = urllib.parse.quote(city + " 날씨")
        url = f"https://search.naver.com/search.naver?query={query}"
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
        }
        
        res = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        # 현재 온도
        temp = soup.select_one(".temperature_text strong")
        temp_text = temp.get_text(strip=True).replace("현재 온도", "") if temp else "정보 없음"

        # 날씨 상태 (맑음, 흐림 등)
        status = soup.select_one(".weather_main")
        status_text = status.get_text(strip=True) if status else "정보 없음"

        # 최저/최고 기온
        temp_range = soup.select(".temperature_inner .text")
        if len(temp_range) >= 2:
            low = temp_range[0].get_text(strip=True)
            high = temp_range[1].get_text(strip=True)
        else:
            low = high = "정보 없음"

        # 습도
        humidity = soup.select_one(".humidity_text")
        humidity_text = humidity.get_text(strip=True) if humidity else "정보 없음"

        # 풍속
        wind = soup.select_one(".wind_text")
        wind_text = wind.get_text(strip=True) if wind else "정보 없음"

        # 미세먼지
        dust = soup.select_one(".dustInfo .num")
        dust_text = dust.get_text(strip=True) if dust else "정보 없음"

        result = f"""
╔══════════════════════════════════════╗
  📍 {city} 날씨 (네이버 기준)
╚══════════════════════════════════════╝
  🌤  날씨 상태  : {status_text}
  🌡  현재 온도  : {temp_text}
  🔽  최저 온도  : {low}
  🔼  최고 온도  : {high}
  💧  습도      : {humidity_text}
  💨  풍속      : {wind_text}
  🌫  미세먼지   : {dust_text}
══════════════════════════════════════
"""
        return result

    except Exception as e:
        return f"\n  ❌ 오류 발생: {e}\n  인터넷 연결 또는 도시명을 확인해주세요.\n"


class WeatherCMD:
    def __init__(self, root):
        root.title("🌤 네이버 날씨 CMD")
        root.configure(bg="black")
        root.geometry("700x500")
        root.resizable(False, False)

        self.output = tk.Text(
            root, bg="black", fg="#00ff00",
            font=("Courier New", 12),
            state="disabled", bd=0, padx=10, pady=10
        )
        self.output.pack(fill="both", expand=True)

        frame = tk.Frame(root, bg="black")
        frame.pack(fill="x", padx=10, pady=(0, 10))

        tk.Label(frame, text=">>", bg="black", fg="#00ff00",
                 font=("Courier New", 13)).pack(side="left")

        self.entry = tk.Entry(
            frame, bg="black", fg="#00ff00",
            font=("Courier New", 13), insertbackground="#00ff00",
            bd=0, highlightthickness=1, highlightcolor="#00ff00"
        )
        self.entry.pack(side="left", fill="x", expand=True, padx=(5, 0))
        self.entry.bind("<Return>", self.handle_input)
        self.entry.focus()

        # 시작 메시지
        self.print_output("╔══════════════════════════════════════╗")
        self.print_output("  🌤  네이버 날씨 조회 프로그램 v1.0")
        self.print_output("╚══════════════════════════════════════╝")
        self.print_output("")
        self.print_output("  무슨 날씨가 궁금할까요?")
        self.print_output("  도시/지역명을 한글로 입력하세요")
        self.print_output("  예) 서울, 부산, 제주도, 뉴욕, 도쿄")
        self.print_output("")

    def print_output(self, text):
        self.output.config(state="normal")
        self.output.insert("end", text + "\n")
        self.output.see("end")
        self.output.config(state="disabled")

    def handle_input(self, event=None):
        city = self.entry.get().strip()
        if not city:
            return

        self.print_output(f">> {city}")
        self.entry.delete(0, "end")

        self.print_output("  🔍 네이버에서 검색 중...")
        result = get_naver_weather(city)
        self.print_output(result)
        self.print_output("  다른 지역도 검색해보세요!")
        self.print_output("")


root = tk.Tk()
WeatherCMD(root)
root.mainloop()