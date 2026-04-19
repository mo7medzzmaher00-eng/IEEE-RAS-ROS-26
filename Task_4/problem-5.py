import json

try:
    with open("config.json", "r") as file:
        print("System Ready.")

except FileNotFoundError:
    default_data = {"setting": "default"}

    with open("config.json", "w") as file:
        json.dump(default_data, file)

    print("Config file created.")
    