from getter import get_player_html, get_attributes, get_attributes_name, filter_attributes, get_archetype
import csv

#first row (titles) of the csv file
def write_first_row_csv(last, first):
    html = get_player_html(last, first)
    
    with open("players_ratings.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        top_row = get_attributes_name(html)
        writer.writerow(["Player Name", "Archetype"]+ top_row)
        
# get ratings of each player
def append_row_one_player(last, first):
    html = get_player_html(last, first)
    with open("players_ratings.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        attributes = get_attributes(html)
        filtered = filter_attributes(attributes)
        writer.writerow([f"{last} {first}", get_archetype(html)] + filtered)
