
def insert_information(conn, row):
    conn.execute(
        "INSERT OR IGNORE INTO league (match_Id,puuid,championName,kills,deaths,team_Id,team_Position,assists,win,kda) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (row["matchId"], row["puuid"], row["championName"],row["kills"], row["deaths"], row["teamId"], row["teamPosition"],row["assists"],row["win"],row["kda"])
    )
    conn.commit()

def insert_item_information(conn, row1):
    conn.execute(
        "INSERT OR IGNORE INTO item (puuid,item0,item1,item2,item3,item4,item5,item6,championName) VALUES (?,?,?,?,?,?,?,?,?)",
        (row1["puuid"],row1["item0"],row1["item1"],row1["item2"],row1["item3"],row1["item4"],row1["item5"],row1["item6"],row1["championName"])
    )
    conn.commit()
# This is where i am working on the features in progress.
def insert_match_information(conn, row2):
    conn.execute(
        "INSERT OR IGNORE INTO match(match_Id,championName,totalGold,wardScore,puuid,game_mode,queue_id,duration,game_start) VALUES(?,?,?,?,?,?,?,?,?,?)",
        (row2["matchId"],row2[""],row2[""],row2[""],row2[""],row2[""],row2[""],row2[""],row2[""],row2[""])
    )

