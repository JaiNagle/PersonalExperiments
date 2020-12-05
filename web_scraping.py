# TOP RATED TV SHOWS LIST

import requests
import time
import pandas as pd
from bs4 import BeautifulSoup


page = requests.get(f"https://www.imdb.com/chart/toptv/")
soup = BeautifulSoup(page.text, 'html.parser')


tv_title = []
for title in soup.find_all("td", class_="titleColumn"):
    time.sleep(1.0)
    tv_title.append(title.a.contents[0])
print('done titles')

tv_year = []
for year in soup.find_all("td", class_="titleColumn"):
    time.sleep(1.0)
    tv_year.append(year.span.contents[0][1:-1])
print('done years')

tv_rate = []
for rate in soup.find_all('td', class_="ratingColumn imdbRating"):
    time.sleep(1.0)
    tv_rate.append(rate.strong.contents[0])
print('done ratings')


dic = {'TV Show': tv_title, 'TV Year': tv_year, 'Rating': tv_rate}
df = pd.DataFrame(dic)
df.to_excel('test1.xlsx')


# DEBUG
# print(tv_title)
# print(tv_year)
# print(tv_rate)
