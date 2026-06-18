# HyperV

Platform to visualize League of Legends player game data and provide insight into their match history.

## About

HyperV pulls a player's match data from the Riot Games API and stores it in a local SQLite database, so the information is available and easy to visualize.

## Preview

<img width="781" height="329" alt="image" src="https://github.com/user-attachments/assets/d1197a4f-378b-49d9-b304-93469439fa87" />

## Tech Stack

- **Python 3**
- **SQLite** for local storage
- **Riot Games API** (Account-V1 and Match-V5)
- **requests** and **python-dotenv**

## Getting Started

### Prerequisites

- Python 3.10 or newer (developed on 3.14)
- A Riot Games API key — get one at https://developer.riotgames.com

### Installation

1. Clone the repository.
2. (Optional) Create and activate a virtual environment.
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root with your API key:
   ```
   API_KEY=your-riot-api-key-here
   ```

### Usage

Run the app:

```bash
python main.py
```

This fetches the most recent match for the configured Riot ID, parses each participant, and stores the data in `league.db`.

## Features

- Match summary (win or loss)
- Champion played per participant
- K/D/A per player
- Team and team position per participant
- Items per participant (item0–item6)

## Roadmap

- [ ] Add search by username and tag (currently fixed).
- [ ] Loop over all 20 match IDs instead of only the newest one.
- [ ] Finish the `match` table (game mode, queue id, duration, game start, patch, total gold, ward score) and wire up `insert_match_information`.
- [ ] Add a `champion` lookup table (champion_Id, name, icon_url).
- [ ] Add an `item` lookup table (item_Id, icon_url) for item names and icons.
- [ ] Give `item` a primary key and a composite foreign key to `league(puuid, match_Id)`.
- [ ] Add proper error handling.
- [ ] Add a web interface.

## Changelog

### [1.0.1] – 2026-06-16

**Added**
- Item tracking per participant (item0–item6).

**Fixed**
- `league` primary key changed from `puuid` alone to the composite `(puuid, match_Id)`. A player's puuid repeats across matches, so puuid alone isn't unique — the pair is (one row per player per match).

## License

This project does not currently have a license.
