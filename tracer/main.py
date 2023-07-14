# Usage_Tracer
# A simple computer statistics tracer.

import os
import sys
import time
import psutil
import json

def move_last_data_to_new_file():
    """
    Move the last data to a new file with the date and time as name.
    """
    with open("data/latest.json") as f:
        data = json.load(f)
    
    with open(f"data/{data['start'].replace(':', '-').replace(' ', '_')}.json", "w") as f:
        json.dump(data, f, indent=4)
    
    os.remove("data/latest.json")

def create_new_last_data_file():
    """
    Create a new last data file.
    """
    if not os.path.isdir("data"):
        os.mkdir("data")

    with open("data/latest.json", "w") as f:
        json.dump({
            "start": time.strftime("%Y-%m-%d %H:%M:%S"),
            "cpu": []
        }, f, indent=4)


def main():
    """
    The main function.
    """
    print("Moving latest.json to new file")
    try:
        move_last_data_to_new_file()
    except FileNotFoundError:
        print("Skipping latest.json move due to file not existing")
    print("Moved latest.json to new file")
    print("Creating new latest.json")
    create_new_last_data_file()
    print("Starting loop")
    print("Sampling every second")
    while True:
        with open("data/latest.json") as f:
            data = json.load(f)
        data["cpu"].append([psutil.cpu_percent(), time.strftime("%Y-%m-%d %H:%M:%S")])
        with open("data/latest.json", "w") as f:
            json.dump(data, f, indent=4)
        time.sleep(1)
    
if __name__ == "__main__":
    main()