import getter, generate_csv

# In this function we do all the work and return the list of player we failed to find the ratings for
def update_player_ratings():
    names = getter.get_all_players_name()
    first_player = name_spliter(names[0])
    generate_csv.write_first_row_csv(first_player[0], first_player[1])
    failed = []
    for name in names:
        # super inefficient because we had to open and close the file each time but safer 
        try:
            lst = name_spliter(name) 
            generate_csv.append_row_one_player(lst[0], lst[1])
        except:
            print(f"Having trouble finding {name}'s ratings")
            failed.append(name)
    return failed


# split the name into [last, first] and get rid of the symbols in names
def name_spliter(name_string: str):
    name = name_string.replace(".", "")
    name = name.replace("’", "")
    return name.split(" ")


if __name__ == "__main__":
    lst = update_player_ratings()
    with open("error.txt", "w") as myfile:
        for player in lst:
            myfile.write(f"{player}\n")
    
        