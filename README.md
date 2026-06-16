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
- Fixing Primary Key Issue
    - Set primary key to match id and puuid because puuid is the primary key and cannot be unique with different matches in the database.
- Add proper error handling
- Add Web interface.
- Add search to username and tag.  (because username and tag are fixed ATM)
- Add version control (example: v1.0.0)

### Updates Expected
- Add missing tables and relations to display missing data 
    - items
    - match metadata
    - champions
    - duration of match
    - ward score
    - total gold accumulated by team
    - total gold for each player
- Iterate through more than 1 match being seen. (expecting to see a history of 10 matches per page)
