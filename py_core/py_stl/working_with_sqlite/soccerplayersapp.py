import json, sqlite3
from pathlib import Path


def get_data(filepath="./myjsonfile.json"):
    with open(filepath, "r") as file:
        data = json.load(file)
        return data


def db_insert(data: list):
    with sqlite3.connect("db.sqlite3") as connector:
        directive = "CREATE TABLE IF NOT EXISTS SoccerPlayers(id integer PRIMARY KEY ASC, jersey_num, name, country, nickname)"
        appCursor = connector.cursor()
        appCursor.execute(directive)
        if data:
            new_data = [[None, *row.values()] for row in data[1:]]
            appCursor.executemany(
                "INSERT INTO SoccerPlayers VALUES(?,?,?,?,?)", new_data
            )
            connector.commit()
        else:
            print("Cannot complete this task at the moment!")


# Reading from DB:
# 1. connect or open the sqlite file.
# 2. create a cursor object
# 3. write sql statement
# 4. execute sql statement using cursor.execute options
# 5. use the data in the cursor to read whatever the db returned back to us.
# 6. if db connection is still open, close it.
# 7. Rember databases cursor are exhaustive, they are iterators and once used, you will need to generate a new one.


def get_data_from_db():
    with sqlite3.connect("db.sqlite3") as connector:
        select_directive = "SELECT * FROM SoccerPlayers"
        appCursor = connector.cursor()
        appCursor.execute(select_directive)  # returns an cursor/iterator
        data = appCursor.fetchmany(20)  # converts data from iterator into a list
        with open("./dboutput.json", "w") as file:
            file.write(json.dumps({"players": data}))


# data = get_data()

# if data:
#     db_insert(data)

get_data_from_db()
