# scrape.py
# Ethan Malenchek
# a program to gather information on the top NFL fantasy scorers

import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
website_url = requests.get('https://fantasy.nfl.com/research/scoringleaders').text
path = './top_25.csv'

soup = BeautifulSoup(website_url, 'html.parser') # parses entire page

my_table = soup.find('table',{'class':'tableType-player'}) # finds table of players on page

name_links = my_table.findAll('a',{'class':'playerName'}) # finds all <a> for player names
points = my_table.findAll('span',{'class':'playerSeasonTotal'}) # stores player points
positions = my_table.findAll('em')

player_names = [] # instantiate list of player names
player_points = [] # instantiate list of player points
player_positions = [] # instantiate list of player positions

count = 0

for link in name_links:
    player_names.append(link.get_text()) # parse links for player names and store in list

for point in points:
    player_points.append(point.get_text()) # parse spans for player points and store in list

for position in positions:
    count = count + 1
    if count > 7: # skips heading <em> elements
        player_positions.append(position.get_text()) # parse <em> for position/team and store in list

dataf = pd.DataFrame( # construct data frame
    {'Player Names':player_names,
     'Total Points':player_points,
     'Position & Team':player_positions,
    })

dataf['Player Names'] = player_names
dataf['Total Points'] = player_points
dataf['Position & Team'] = player_positions

print(dataf)

dataf.to_csv(path, index = False) # export data frame to csv
