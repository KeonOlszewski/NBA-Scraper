#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

fullName = input ("Enter player name (ex: Lebron James): ")
seasonYear = input ("Enter season (ex: 2019-2020): ")

#formating strings for the url
listName = fullName.lower().split(" ")

letterUrl = listName[1][0] #need initial of last name

firstUrl = listName[0][:2] #2 first letters of first name

lastUrl = listName[1][:5] #5 first letters of first name

yearUrl = (seasonYear.split("-"))[1] #only need 2020 part of 2019-2020 for example

url = "https://www.basketball-reference.com/players/"+letterUrl+"/"+lastUrl+firstUrl+"01/gamelog/"+yearUrl


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


print(fullName+" ppg: ",pointsAvg," in "+seasonYear)
print(fullName+" ppg in wins: ",pointsAvgInWin," in ", numWins," wins")
print(fullName+" ppg in losses: ",pointsAvgInLoss," in ", numLosses, "losses")

print("=================================================")         




  
    
plt.figure()
plt.bar(games, points)
plt.title(fullName+" Scoring "+seasonYear)
plt.axis([0, 82, 0, 50])
plt.ylabel('points')
plt.xlabel('game')
plt.show()

sys.exit()
