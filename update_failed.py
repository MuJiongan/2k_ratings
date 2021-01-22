import update, generate_csv

# this file is for appending players that has failed to append in update.py
# I have already change the names in error.txt and now we append these players 
if __name__ == "__main__":
    lst = []    
    # convert the file to a list
    with open('error.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            lst.append(line.strip())
    print(lst)
    # append players
    for player in lst:
        name_list = update.name_spliter(player)
        generate_csv.append_row_one_player(name_list[0], name_list[1])
            