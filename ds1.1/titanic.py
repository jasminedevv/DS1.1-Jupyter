import csv

data = open("titanic.csv", "r")

with open('titanic.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    # sets where to find if they died or not
    survived_index = 1
    # sets where to find passenger sex
    sex_index = 4
    lady_survivors = 0
    for row in data:
        if row[survived_index] == "1" and row[sex_index] == "female":
            lady_survivors += 1
    print(lady_survivors, "women survived the Titanic.")