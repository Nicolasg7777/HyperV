# All API Requests will go here.

import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

account_v1 = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"
match_v5 = f"https://americas.api.riotgames.com/lol/match/v5/matches/"

def account_by_riot(gamename, tagline):
    response = requests.get(f'{account_v1}{gamename}/{tagline}', headers={"X-Riot-Token": api_key})
    if response.status_code != 200:
        print(f"Error Code:{response.status_code}")
        return None
    else:
        data = response.json()
        return data["puuid"]

def get_matches_id_by_puuid(puuid):
    response = requests.get(f'{match_v5}by-puuid/{puuid}/ids?start=0&count=20', headers={"X-Riot-Token": api_key})
    data = response.json()
    # print(data)
    return data[1]

def get_match_info_by_id(match_id):
    response = requests.get(f'{match_v5}{match_id}', headers={"X-Riot-Token": api_key})
    print(response.url)
    data = response.json()
    #print(data)
    return data

# parse_data(get_match_info_by_id(get_matches_id_by_puuid(account_by_riot('LEGEND','NnE'))))



#get_match_info_by_id(get_matches_id_by_puuid(account_by_riot('LEGEND','NnE')))
# data returned: ['NA1_5581877957', 'NA1_5581845019', 'NA1_5581827465', 'NA1_5580397431', 'NA1_5580268818', 'NA1_5579776718', 'NA1_5578973639', 'NA1_5578957394', 'NA1_5578943835', 'NA1_5578418590', 'NA1_5578413110', 'NA1_5577794873', 'NA1_5577769634', 'NA1_5577722873', 'NA1_5577701390', 'NA1_5577676603', 'NA1_5577653572', 'NA1_5577592255', 'NA1_5577590882', 'NA1_5577563464']
# get_matches_id_by_puuid(account_by_riot('LEGEND','NnE'))
#puuid = account_by_riot('LEGEND','NnE')
#print(puuid)
#test = get_match_id_by_puuid(account_by_riot('LEGEND','NnE'))
#print(test)
# Create a class for these functions Later on. maybe?