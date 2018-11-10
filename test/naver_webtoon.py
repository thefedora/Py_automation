#! python3

import bs4, requests

res = requests.get('https://comic.naver.com/webtoon/detail.nhn?titleId=557672&no=248&weekday=thu')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
print(soup)
play_file = open('soup_file.txt', 'wb')
play_file.write(str(soup))
play_file.close()