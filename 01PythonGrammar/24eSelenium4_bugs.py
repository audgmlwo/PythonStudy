import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

#웹드라이버 로드
driver = webdriver.Chrome()
#지니차트 200 페이지에 접속 후 정보 얻어오기
url = 'https://music.bugs.co.kr/chart'
driver.get(url)

#얻어온 HTML 소스를 파상하기위해 Soup 객체로 변환
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#파싱한 정보를 저장하기 위해 리스트 생성
song_data = []
rank = 1

songs = soup.select('table.byChart > tbody > tr') # 하면 차트만 셀렉트해서 예외처리나 if else 로 none값 처리를 할필요가없음.
#songs = soup.select('tbody>tr') 범위가 더 넓어서 예외처리 해야됨.
for song in songs:
    # 제목 추출
    titles = song.select('p.title > a')
    title = titles[0].text.strip() if titles else "정보 없음"

    # 가수 추출
    singers = song.select('p.artist > a')
    singer = singers[0].text.strip() if singers else "정보 없음"

    # 데이터 저장
    song_data.append(['Bugs', rank, title, singer])
    rank += 1
   
#크롤링이 완료되면 판다스를 이용해서 엑셀로 저장        
columns = ['서비스','순위','타이틀','가수']
#데이터프레임 생성 시 컬럼을 하나 추가
pd_data = pd.DataFrame(song_data, columns=columns)
#최상위 5개의 데이터 확인
print(pd_data.head())
pd_data.to_excel('./saveFiles/bugs_chart.xlsx', index =False)

