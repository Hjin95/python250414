#web1.py
#웹 크롤링을 위한 선언
from bs4 import BeautifulSoup

# 웹 페이지를 로딩
page = open('chap09_test.html', 'rt', encoding='utf-8').read()
# BeautifulSoup 객체 생성
soup = BeautifulSoup(page, 'html.parser')
#전체페이지를 출력
#print(soup.prettify())
#<p>를 몽땅검색
# print(soup.find_all('p'))
#<p>하나만검색
# print(soup.find_('p'))
# 조건검색 : <p class="outer-text">
#print(soup.find_all('p', class_='outer-text'))
#최근에는 attrs 속성 검색
#print(soup.find_all("p", attrs={'class':'outer-text'}))
#id속성 검색
#print(soup.find_all("p", id='first'))

# <p>의 text 속성 검색:태그 내부의 컨텐츠만 가져오기
for tag in soup.find_all("p"):
    title = tag.text
    title = title.replace("\n", "") # 줄바꿈 제거
    print(title)


