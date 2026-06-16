
def insert_information(conn, row):
    conn.execute(
        "INSERT INTO league (match_Id,puuid,championName,kills,deaths,team_Id,team_Position,assists,win,kda) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (row["matchId"], row["puuid"], row["championName"],row["kills"], row["deaths"], row["teamId"], row["teamPosition"],row["assists"],row["win"],row["kda"])
    )
    conn.commit()