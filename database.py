
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

    print("league table created successfully")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS item(
        match_Id TEXT NOT NULL,
        item0 INT NOT NULL,
        item1 INT NOT NULL,
        item2 INT NOT NULL,
        item3 INT NOT NULL,
        item4 INT NOT NULL,
        item5 INT NOT NULL,
        item6 INT NOT NULL,
        puuid TEXT NOT NULL,
        championName TEXT NOT NULL,
        FOREIGN KEY(puuid, match_Id) REFERENCES league(puuid, match_Id)
        )
    """)
    conn.commit()

    print("item table created successfully")


    conn.execute('''CREATE TABLE IF NOT EXISTS match (
        match_Id TEXT NOT NULL,
        gameMode TEXT NOT NULL,
        puuid TEXT NOT NULL,
        championName TEXT NOT NULL,
        goldEarned INT NOT NULL,
        gameDuration INT NOT NULL,
        PRIMARY KEY (gameMode, puuid)
        FOREIGN KEY(puuid,match_Id) REFERENCES league(puuid, match_Id)
        )
    ''')
    conn.commit()
    print("match table created successfully")


#    conn.execute('''CREATE TABLE IF NOT EXISTS champion (
#        champion_Id INT PRIMARY KEY,
#        name TEXT NOT NULL,
#        icon_url TEXT NOT NULL
#        )
#    ''')

