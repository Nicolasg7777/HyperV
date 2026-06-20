# give me a example of data transfer objects in python from json to python object , displaying deserialization

from database import get_connection
from models import insert_information, insert_item_information, insert_match_information

row = []
row1 = []
row2 = []
def parse_data(data):
    con = get_connection()
    for i in data["info"]["participants"]:
        var = {
            "matchId": data["metadata"]["matchId"],
            "puuid": i["puuid"],
            "championName": i["championName"],
            "kills": i["kills"],
            "deaths": i["deaths"],
            "teamId": i["teamId"],
            "teamPosition": i["teamPosition"],
            "assists": i["assists"],
            "win": i["win"],
            "kda": round(i["challenges"]["kda"], 3),
        }
        insert_information(con, var)
    con = get_connection()
    for i in data["info"]["participants"]:
        var2 = {
            "matchId": data["metadata"]["matchId"],
            "championName": i["championName"],
            "puuid": i["puuid"],
            "item0": i["item0"],
            "item1": i["item1"],
            "item2": i["item2"],
            "item3": i["item3"],
            "item4": i["item4"],
            "item5": i["item5"],
            "item6": i["item6"],
        }
        insert_item_information(con, var2)
    for i in data["info"]["participants"]:
        var3 = {
            "gameMode": data["info"]["gameMode"],
            "puuid": i["puuid"],
            "championName": i["championName"],
            # divide the game duration by 60 to get minutes and display it minutes.
            "gameDuration": round(data["info"]["gameDuration"]/60, 2),
            "goldEarned": i["goldEarned"],
            "match_Id": data["metadata"]["matchId"],
        }
        insert_match_information(con, var3)

# STEP 1: def function
# Step 2: for each Participant, we want to pick out kills, championName, and puuid.