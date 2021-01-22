from bs4 import BeautifulSoup
import requests, csv

# get a player's archetype
def get_archetype(html):
    soup = BeautifulSoup(html, 'html.parser')
    ps = soup.find("span", class_= "text-light")
    return ps.text

# get player's attributes
def get_attributes(html):
    soup = BeautifulSoup(html, 'html.parser')
    ps = soup.find_all("span", class_="attribute-box")
    attri_list = []
    for attribute in ps:
        attri_list.append(attribute.text)
    return attri_list[0: 45]

# get the names of each attribute, useful for generating the first row of the csv
def get_attributes_name(html):
    soup = BeautifulSoup(html, 'html.parser')
    ps = soup.find_all("span", class_="attribute-box")
    subsequent_ps = []
    for element in ps:
        subsequent_ps.append(element.next_sibling)
    attri_list = []
    for attribute in subsequent_ps:
        if (attribute != None):
            attri_list.append(attribute)
    return attri_list
    
# use request to get the html
def get_player_html(last, first):
    url = f"https://www.2kratings.com/{last}-{first}"
    html_text = requests.get(url).text
    return html_text

#filter the attributes to only the ones we want
def filter_attributes(attributes):
    outside_Scoring = attributes[1: 7]
    inside_Scoring = attributes[16: 24]
    defending = attributes[31: 39]
    athleticism = attributes[8: 15]
    playmaking = attributes[25: 30]
    rebounding = attributes[40: 42]
    return outside_Scoring + athleticism + inside_Scoring + playmaking + defending + rebounding

# Use this site to get all the players name
def get_all_players_name():
    url = "https://nba2kw.com/list/nba-2k21-all-player-ratings/"
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    ps = soup.find_all("span", class_="player-photo")
    subsequent_ps = []
    for element in ps:
        subsequent_ps.append(element.next_sibling)
    names = []
    for name in subsequent_ps:
        if (name != None):
            names.append(name)
    return names






