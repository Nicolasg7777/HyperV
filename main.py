from database import create_table, get_connection
from extract import get_match_info_by_id, get_matches_id_by_puuid, account_by_riot
from transform import parse_data

def main():
    # conn = get_connection('league.db')
    create_table(get_connection())

    parse_data(get_match_info_by_id(get_matches_id_by_puuid(account_by_riot('LEGEND', 'NnE'))))

if __name__ == "__main__":
    main()
