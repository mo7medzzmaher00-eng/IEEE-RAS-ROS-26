import json

def save_inventory(data):
    with open("inventory.json", "w") as file:
        json.dump(data, file)
def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
inventory = 

save_inventory(inventory)

data = load_inventory()
print(data)    