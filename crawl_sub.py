import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# header는 이게 python에서 요청하는게 아니라, 유저가 요청하는것처럼해서
# html파일을 잘받아오도록함.

data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190715', headers=headers)
#get의 결과는 html이므로, data에 html 소스코드가 들어감

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

tr_result = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.albumtitle.ellipsis
rank = 1
for music in tr_result:
    singer = music.select_one('td.info > a.artist.ellipsis')
    title = music.select_one('td.info > a.title.ellipsis')
    print(rank, singer.text,title.text.strip())
    rank+=1