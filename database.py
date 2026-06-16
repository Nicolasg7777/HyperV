
import sqlite3

def get_connection(db_path = 'league.db'):
    return sqlite3.connect(db_path)

def create_table(conn):
    print("creating table")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS league (
        puuid TEXT NOT NULL PRIMARY KEY,
        match_Id TEXT NOT NULL,
        championName TEXT NOT NULL,
        kills INT NOT NULL,
        deaths INT NOT NULL,
        team_id INT NOT NULL,
        team_position TEXT NOT NULL,
        assists INT NOT NULL,
        win REAL NOT NULL,
        kda FLOAT NOT NULL
        )
    """)

    conn.commit()

    print("table created successfully")

#    conn.execute('''CREATE TABLE IF NOT EXISTS match (
#        match_Id TEXT NOT NULL PRIMARY KEY,
#        game_mode TEXT NOT NULL,
#        queue_id INT NOT NULL,
#        duration INT NOT NULL,
#        game_start INT NOT NULL,
#        patch TEXT NOT NULL
#        )
#    ''')

#    conn.execute('''CREATE TABLE IF NOT EXISTS champion (
#        champion_Id INT PRIMARY KEY,
#        name TEXT NOT NULL,
#        icon_url TEXT NOT NULL
#        )
#    ''')

#    conn.execute('''CREATE TABLE IF NOT EXISTS item (
#        item_Id INT NOT NULL PRIMARY KEY,
#        icon_url TEXT NOT NULL
#        )
#    ''')

