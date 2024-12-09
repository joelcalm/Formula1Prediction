import requests
import pandas as pd

# Define file paths
results_file = "data/results.csv"
qualifying_file = "data/qualifying.csv"
driver_standings_file = "data/driver_standings.csv"
constructor_standings_file = "data/constructor_standings.csv"

# Load existing datasets
results_df = pd.read_csv(results_file)
qualifying_df = pd.read_csv(qualifying_file)
driver_standings_df = pd.read_csv(driver_standings_file)
constructor_standings_df = pd.read_csv(constructor_standings_file)

# Determine starting IDs for new entries
next_result_id = results_df["resultId"].max() + 1
next_qualify_id = qualifying_df["qualifyId"].max() + 1
next_driver_standings_id = driver_standings_df["driverStandingsId"].max() + 1
next_constructor_standings_id = constructor_standings_df["constructorStandingsId"].max() + 1

# Round to raceId mapping
RACE_ID_MAPPING = {
    24: 1144
}

# Define the Ergast API base URL
BASE_URL = "https://ergast.com/api/f1/2024/{round}/{endpoint}.json"

# Helper function to fetch data from the Ergast API
def fetch_data(round_number, endpoint):
    url = BASE_URL.format(round=round_number, endpoint=endpoint)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for round {round_number}, endpoint {endpoint}")
        return None

# Helper function to map status text to a numeric ID
def map_status_to_id(status_text):
    if status_text == "Finished":
        return 1
    elif status_text == "Retired":
        return 2
    elif "Disqualified" in status_text:
        return 3
    else:
        return 4  # For other cases
    
def update_results(round_number, data):
    global results_df, next_result_id

    race_id = RACE_ID_MAPPING.get(round_number)
    if not race_id:
        print(f"Round {round_number} does not have a mapped raceId. Skipping...")
        return

    if not data["MRData"]["RaceTable"]["Races"]:
        print(f"No race data found for round {round_number}. Skipping...")
        return

    race_results = data["MRData"]["RaceTable"]["Races"][0]["Results"]

    for i, result in enumerate(race_results):
        status_text = result["status"]
        status_id = map_status_to_id(status_text)

        new_entry = {
            "resultId": next_result_id,
            "raceId": race_id,
            "driverId": result["Driver"]["driverId"],
            "constructorId": result["Constructor"]["constructorId"],
            "number": result["number"],
            "grid": int(result["grid"]),
            "position": result.get("position", "\\N"),
            "positionText": result["positionText"],
            "positionOrder": i + 1,
            "points": float(result["points"]),
            "laps": int(result["laps"]),
            "time": result.get("Time", {}).get("time", "\\N"),
            "milliseconds": result.get("Time", {}).get("millis", "\\N"),
            "fastestLap": result.get("FastestLap", {}).get("lap", "\\N"),
            "rank": result.get("FastestLap", {}).get("rank", "\\N"),
            "fastestLapTime": result.get("FastestLap", {}).get("Time", "\\N"),
            "fastestLapSpeed": result.get("FastestLap", {}).get("AverageSpeed", {}).get("speed", "\\N"),
            "statusId": status_id
        }
        results_df = pd.concat([results_df, pd.DataFrame([new_entry])], ignore_index=True)
        next_result_id += 1
def update_qualifying(round_number, data):
    global qualifying_df, next_qualify_id

    race_id = RACE_ID_MAPPING.get(round_number)
    if not race_id:
        print(f"Round {round_number} does not have a mapped raceId. Skipping...")
        return

    if not data["MRData"]["RaceTable"]["Races"]:
        print(f"No qualifying data found for round {round_number}. Skipping...")
        return

    qualifying_results = data["MRData"]["RaceTable"]["Races"][0]["QualifyingResults"]

    for qualifying in qualifying_results:
        new_entry = {
            "qualifyId": next_qualify_id,
            "raceId": race_id,
            "driverId": qualifying["Driver"]["driverId"],
            "constructorId": qualifying["Constructor"]["constructorId"],
            "number": qualifying["number"],
            "position": int(qualifying["position"]),
            "q1": qualifying.get("Q1", "\\N"),
            "q2": qualifying.get("Q2", "\\N"),
            "q3": qualifying.get("Q3", "\\N")
        }
        qualifying_df = pd.concat([qualifying_df, pd.DataFrame([new_entry])], ignore_index=True)
        next_qualify_id += 1

def update_driver_standings(round_number, data):
    global driver_standings_df, next_driver_standings_id

    race_id = RACE_ID_MAPPING.get(round_number)
    if not race_id:
        print(f"Round {round_number} does not have a mapped raceId. Skipping...")
        return

    if not data["MRData"]["StandingsTable"]["StandingsLists"]:
        print(f"No driver standings data found for round {round_number}. Skipping...")
        return

    driver_standings = data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

    for driver in driver_standings:
        new_entry = {
            "driverStandingsId": next_driver_standings_id,
            "raceId": race_id,
            "driverId": driver["Driver"]["driverId"],
            "points": float(driver["points"]),
            "position": int(driver["position"]),
            "positionText": driver["positionText"],
            "wins": int(driver["wins"])
        }
        driver_standings_df = pd.concat([driver_standings_df, pd.DataFrame([new_entry])], ignore_index=True)
        next_driver_standings_id += 1
def update_constructor_standings(round_number, data):
    global constructor_standings_df, next_constructor_standings_id

    race_id = RACE_ID_MAPPING.get(round_number)
    if not race_id:
        print(f"Round {round_number} does not have a mapped raceId. Skipping...")
        return

    if not data["MRData"]["StandingsTable"]["StandingsLists"]:
        print(f"No constructor standings data found for round {round_number}. Skipping...")
        return

    constructor_standings = data["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"]

    for constructor in constructor_standings:
        new_entry = {
            "constructorStandingsId": next_constructor_standings_id,
            "raceId": race_id,
            "constructorId": constructor["Constructor"]["constructorId"],
            "points": float(constructor["points"]),
            "position": int(constructor["position"]),
            "positionText": constructor["positionText"],
            "wins": int(constructor["wins"])
        }
        constructor_standings_df = pd.concat([constructor_standings_df, pd.DataFrame([new_entry])], ignore_index=True)
        next_constructor_standings_id += 1


# Function to process and update results, qualifying, driver standings, and constructor standings
def process_and_update_data(round_number):
    race_id = RACE_ID_MAPPING.get(round_number)
    if not race_id:
        print(f"Round {round_number} does not have a mapped raceId. Skipping...")
        return

    # Results
    results_data = fetch_data(round_number, "results")
    if results_data:
        update_results(round_number, results_data)

    # Qualifying
    qualifying_data = fetch_data(round_number, "qualifying")
    if qualifying_data:
        update_qualifying(round_number, qualifying_data)

    # Driver Standings
    driver_standings_data = fetch_data(round_number, "driverStandings")
    if driver_standings_data:
        update_driver_standings(round_number, driver_standings_data)

    # Constructor Standings
    constructor_standings_data = fetch_data(round_number, "constructorStandings")
    if constructor_standings_data:
        update_constructor_standings(round_number, constructor_standings_data)

# Call the function for round 24
process_and_update_data(24)

# Save updated files
results_df.to_csv(results_file, index=False)
qualifying_df.to_csv(qualifying_file, index=False)
driver_standings_df.to_csv(driver_standings_file, index=False)
constructor_standings_df.to_csv(constructor_standings_file, index=False)

print("Files updated successfully for round 24!")
