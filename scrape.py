# scrape.py
# Ethan Malenchek
# a program to gather information on the top NFL fantasy scorers

import requests
import pandas as pd
from bs4 import BeautifulSoup
website_url = requests.get('https://fantasy.nfl.com/research/scoringleaders?position=O&statCategory=stats&statSeason=2019&statType=seasonStats&statWeek=5').text

soup = BeautifulSoup(website_url, 'html.parser') # parses entire page

my_table = soup.find('table',{'class':'tableType-player'}) # finds table of players on page

name_links = my_table.findAll('a',{'class':'playerName'}) # finds all <a> for player names

player_names = [] # instantiate list of player names

for link in name_links:
    player_names.append(link.get_text()) # parse links for player names and store in list

df = pd.DataFrame() # Data Frames construction for output formatting
df['player_names'] = player_names

print(df)
