# give me a example of data transfer objects in python from json to python object , displaying deserialization

from database import get_connection
from models import insert_information

row = []
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
            "kda": round(i["challenges"]["kda"], 3)
        }
        insert_information(con, var)







# find each participants - done
# win or loss - done
# kda - done
# kd percentage - done
# participants team - done
# keeping it simple.


# STEP 1: def function
# Step 2: for each Participant, we want to pick out kills, championName, and puuid.