
import sqlite3

def get_connection(db_path = 'league.db'):
    conn = sqlite3.connect(db_path)
    conn.execute('''PRAGMA foreign_keys = ON''')
    return conn

def create_table(conn):
    print("creating table")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS league (
        puuid TEXT NOT NULL,
        match_Id TEXT NOT NULL,
        championName TEXT NOT NULL,
        kills INT NOT NULL,
        deaths INT NOT NULL,
        team_id INT NOT NULL,
        team_position TEXT NOT NULL,
        assists INT NOT NULL,
        win REAL NOT NULL,
        kda FLOAT NOT NULL,
        PRIMARY KEY (puuid, match_Id)
        )
    """)

    conn.commit()

    print("table created successfully")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS item(
        item0 INT NOT NULL,
        item1 INT NOT NULL,
        item2 INT NOT NULL,
        item3 INT NOT NULL,
        item4 INT NOT NULL,
        item5 INT NOT NULL,
        item6 INT NOT NULL,
        puuid TEXT NOT NULL,
        championName TEXT NOT NULL
        )
    """)
    conn.commit()

    print("table2 created successfully")

# This is where i am working on the features in progress.
    conn.execute('''CREATE TABLE IF NOT EXISTS match (
        match_Id TEXT NOT NULL,
        championName TEXT NOT NULL,
        totalGold INT NOT NULL,
        wardScore INT NOT NULL,
        puuid TEXT NOT NULL,
        game_mode TEXT NOT NULL,
        queue_id INT NOT NULL,
        duration INT NOT NULL,
        game_start INT NOT NULL,
        patch TEXT NOT NULL,
        PRIMARY KEY (puuid, match_Id)
        )
    ''')

#    conn.execute('''CREATE TABLE IF NOT EXISTS champion (
#        champion_Id INT PRIMARY KEY,
#        name TEXT NOT NULL,
#        icon_url TEXT NOT NULL
#        )
#    ''')

