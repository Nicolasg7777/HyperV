# HyperV Project.
---
Platform to visualize League of Legends player data and provide more insight in their match history.

## About

We want the data to be available and visual for users to see. That is what this
Application will solve.

## Features

- Display Game information.
    - Game History.
        - match summary (win or lose: 'win': True or False)
        - Match Ranks (get ranks of each puuid)
        - K/D/A (get each kda for each puuid: 'kda')
        - K/D percentage. (k/d (* 100))
        - participants (puuid)
            - ally team (team_id)
            - opposing team (team_id_)
    - Rank (maybe laTer.)

## Getting Started
TODO: ?

### Prerequisites
TODO: ?
### Installation
TODO: ?

### Missing Features
- Add proper error handling
- Add Web interface.
- Add search to username and tag.  (because username and tag are fixed ATM)

### Updates Expected
- Add missing tables and relations to display missing data 2/3 done.
    - match metadata
        - game mode - in Progress.
        - queue id - in Progress.
        - duration - in Progress.
        - game start - in Progress.
        - patch ?
        - champions - in Progress.
        - ward score - in Progress.
        - total gold accumulated by team - in Progress.
        - total gold for each player - in Progress.
- Iterate through more than 1 match being seen. (expecting to see a history of 10 matches per page)

  ## Known Issues (not yet fixed)                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                    
  ### High priority                                                                                                                                                                                                                                                 
  - [ ] `item` table has no primary key / unique constraint, so `INSERT OR IGNORE`                                                                                                                                                                                  
        never dedupes — every run of `main.py` adds 10 duplicate item rows.                                                                                                                                                                                         
  - [ ] `item` table isn't linked to `league` (foreign key was removed to clear a                                                                                                                                                                                   
        syntax error). `puuid` is just a loose column with no enforced relationship.                                                                                                                                                                                
  - [ ] API key is hardcoded in `extract.py` — move it to an environment variable /                                                                                                                                                                                 
        `.env` BEFORE committing or pushing (git history is permanent).                                                                                                                                                                                             
                                                                                                                                                                                                                                                                    
  ### Medium priority                                                                                                                                                                                                                                               
  - [ ] `insert_match_information` (models.py) is broken: 9 columns vs 10 `?`                                                                                                                                                                                       
        placeholders, and uses empty `row2[""]` keys.                                                                                                                                                                                                               
  - [ ] `get_matches_id_by_puuid` and `get_match_info_by_id` (extract.py) don't check                                                                                                                                                                               
        `response.status_code` like `account_by_riot` does — a failed call crashes.                                                                                                                                                                                 
  - [ ] Only the newest match is fetched (`data[0]`); the other 19 match IDs are ignored.                                                                                                                                                                           
  - [ ] Riot ID is hardcoded to `('LEGEND', 'NnE')` — can't query other accounts.                                                                                                                                                                                   
                                                                                                                                                                                                                                                                    
  ### Low priority / cleanup                                                                                                                                                                                                                                        
  - [ ] No `.gitignore` — `.venv/`, `.idea/`, `__pycache__/`, `*.db`, `data.json` get tracked.                                                                                                                                                                      
  - [ ] `win` column is `REAL`; should be `INTEGER` (0/1) since it's a boolean.                                                                                                                                                                                     
  - [ ] Connections from `get_connection()` are never closed.                                                                                                                                                                                                       
  - [ ] `championName` is stored in both `league` and `item` (duplicated data).                                                                                                                                                                                     
                                                                                                                                                                                                                                                                    
  ## Roadmap (implement next)                                                                                                                                                                                                                                       
  - [ ] Add a primary key + composite foreign key to `item` so it links to                                                                                                                                                                                          
        `league(puuid, match_Id)` — re-add the FK correctly (no `NOT NULL` inside the clause).                                                                                                                                                                      
  - [ ] Finish the `match` table (game_mode, queue_id, duration, game_start, patch,                                                                                                                                                                                 
        totalGold, wardScore) and wire up `insert_match_information`.                                                                                                                                                                                               
  - [ ] Add a `champion` lookup table (champion_Id, name, icon_url).                                                                                                                                                                                                
  - [ ] Add an `item` lookup table (item_Id, icon_url) for item names/icons.                                                                                                                                                                                        
  - [ ] Loop over all 20 match IDs instead of just the newest one.                                                                                                                                                                                                  
  - [ ] Move the API key to `.env` and load it with `os.environ` / python-dotenv.



### Version 1.0.1

##### Added features
  ## [1.0.1] - 2026-06-16                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                    
  ### Added                                                                                                                                                                                                                                                         
  - Item tracking per participant (item0–item6)                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                    
  ### Fixed                                                                                                                                                                                                                                                         
  - League primary key changed from `puuid` alone to the composite                                                                                                                                                                                                  
    `(puuid, match_Id)`. A player's puuid repeats across matches, so puuid                                                                                                                                                                                          
    alone isn't unique; the pair is — one row per player per match.