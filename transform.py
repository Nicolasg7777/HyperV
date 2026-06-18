# give me a example of data transfer objects in python from json to python object , displaying deserialization

from database import get_connection
from models import insert_information, insert_item_information

row = []
row1 = []
def parse_data(data):
    #for i in data["metadata"]["participants"]:
    #    print(i)

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


#def match_data(MatchData):
#    con = get_connection()
#    for i in MatchData()["info"]["participantFrames"]:
#        var3 = {
#            "totalGold": i[9]["totalGold"],
#
#        }
#        print(var3)

# find each participants - done
# win or loss - done
# kda - done
# kd percentage - done
# participants team - done
# keeping it simple.


# STEP 1: def function
# Step 2: for each Participant, we want to pick out kills, championName, and puuid.