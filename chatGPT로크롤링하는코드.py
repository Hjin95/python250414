import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 1. 뉴스 크롤링
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('.news_tit')

# 2. 엑셀 파일 생성 및 저장
wb = Workbook()
ws = wb.active
ws.title = "뉴스 제목"

# 제목 줄 추가
ws.append(["번호", "기사 제목", "기사 링크"])

# 뉴스 제목과 링크 저장
for i, title in enumerate(titles, 1):
    ws.append([i, title.text, title['href']])

# 엑셀 파일 저장
wb.save("results.xlsx")
print("results.xlsx 파일로 저장 완료!")
