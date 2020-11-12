#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



#url = "https://www.basketball-reference.com/players/j/jamesle01/gamelog/2020" #Lebron James

#url = "https://www.basketball-reference.com/players/l/lowryky01/gamelog/2020" #Kyle Lowry

url = "https://www.basketball-reference.com/players/h/herroty01/gamelog/2020/" #Tyler Herro

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



pointsInWin = []
pointsInLoss = []
points = []
games = []
numWins = 0
numLosses = 0 
for row in table:
    if(len(row) >= 26):
        points.append(int(row[26]))
        games.append(int(row[0]))
        if("W" in row[6]):
            pointsInWin.append(int(row[26]))
            numWins += 1
        else:
            pointsInLoss.append(int(row[26]))
            numLosses += 1

pointsAvgInWin = np.average(pointsInWin)
pointsAvgInWin = round(pointsAvgInWin, 2)

pointsAvg = np.average(points)
pointsAvg = round(pointsAvg, 2)

pointsAvgInLoss = np.average(pointsInLoss)
pointsAvgInLoss = round(pointsAvgInLoss, 2)

print("=================================================")


print("Tyler Herro ppg: ",pointsAvg)
print("Tyler Herro ppg in wins: ",pointsAvgInWin," in ", numWins," wins")
print("Tyler Herro ppg in losses: ",pointsAvgInLoss," in ", numLosses, "losses")

print("=================================================")         




  
    
plt.figure()
plt.bar(games, points)
plt.title('Tyler Herro Scoring 2019-2020')
plt.axis([0, 67, 0, 50])
plt.ylabel('points')
plt.xlabel('game')
plt.show()
