
def insert_information(conn, row):
    conn.execute(
        "INSERT OR IGNORE INTO league (match_Id,puuid,championName,kills,deaths,team_Id,team_Position,assists,win,kda) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (row["matchId"], row["puuid"], row["championName"],row["kills"], row["deaths"], row["teamId"], row["teamPosition"],row["assists"],row["win"],row["kda"])
    )
    conn.commit()

def insert_item_information(conn, row1):
    conn.execute(
        "INSERT OR IGNORE INTO item (match_Id,puuid,item0,item1,item2,item3,item4,item5,item6,championName) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (row1["matchId"],row1["puuid"],row1["item0"],row1["item1"],row1["item2"],row1["item3"],row1["item4"],row1["item5"],row1["item6"],row1["championName"])
    )
    conn.commit()

def insert_match_information(conn, row2):
    conn.execute(
        "INSERT OR IGNORE INTO match(gameMode,puuid,championName,gameDuration,goldEarned,match_Id) VALUES(?,?,?,?,?,?)",
        (row2["gameMode"],row2["puuid"],row2["championName"],row2["gameDuration"],row2["goldEarned"],row2["match_Id"])
    )
    conn.commit()


