import csv
import json
import os

def players_csv_to_json(csv_filename, json_filename):
    # Get the current directory of the Python script
    current_directory = os.path.dirname(os.path.realpath(__file__))
    
    # Join the current directory with the filenames
    csv_filepath = os.path.join(current_directory, csv_filename)
    json_filepath = os.path.join(current_directory, json_filename)
    
    data = []
    
    with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            row["maties_id"] = int(row["maties_id"])  # Convert ID to int
            row["rating"] = int(row["rating"])  # Convert rating to int
            row["birth_year"] = int(row["birth_year"])  # Convert birth year to int
            data.append(row)
    
    with open(json_filepath, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"Converted {csv_filename} to {json_filename}")

def matches_csv_to_json(csv_filename, json_filename):
    # Get the current directory of the Python script
    current_directory = os.path.dirname(os.path.realpath(__file__))
    
    # Join the current directory with the filenames
    csv_filepath = os.path.join(current_directory, csv_filename)
    json_filepath = os.path.join(current_directory, json_filename)
    
    matches = []
    
    with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            match = {
                "match_id": row["match_id"],
                "match_date": row["match_date"],
                "event_name": row["event_name"],
                "event_type": row["event_type"],
                "province": row["province"],
                "stage": row["stage"],
                "winner": row["p1_name"] if int(row["p1_score"]) > int(row["p2_score"]) else row["p2_name"],
                "loser": row["p2_name"] if int(row["p1_score"]) > int(row["p2_score"]) else row["p1_name"],
                "score": f"{max(int(row['p1_score']), int(row['p2_score']))}-{min(int(row['p1_score']), int(row['p2_score']))}"
            }
            matches.append(match)
    
    with open(json_filepath, mode='w', encoding='utf-8') as json_file:
        json.dump(matches, json_file, indent=4)
    
    print(f"Converted {csv_filename} to {json_filename}")

matches_csv_to_json("matchresults.csv", "matches.json")
players_csv_to_json("playerdata.csv", "players.json")


