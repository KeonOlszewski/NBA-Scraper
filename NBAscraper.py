#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt



#url = "https://www.basketball-reference.com/players/j/jamesle01/gamelog/2020"

url = "https://www.basketball-reference.com/players/l/lowryky01/gamelog/2020"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
htmltable = soup.find(id="all_pgl_basic")
table_rows = htmltable.find_all('tr')

table = []


for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    if len(row) > 0:
        table.append(row)


points = []
for row in table:
    if(len(row) >= 26):
         points.append(int(row[26]))

games = []
for row in table:
    if(len(row) >= 26):
         games.append(int(row[0]))


    
plt.figure()
plt.bar(games, points)
plt.title('Kyle Lowry Scoring 2019-2020')
plt.axis([0, 67, 0, 50])
plt.ylabel('points')
plt.xlabel('game')
plt.show()
