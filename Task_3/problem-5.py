menu = {"apple": 0.5,
"banana": 0.3,
"orange":0.2,
"pizza":0.6,
"eggs":0.35}

items_bought = ["eggs","apple", "banana", "pizza","eggs"]

def calculate_bill(menu, items_bought):
    total = 0

    for item in items_bought:
        if item in menu:
            total += menu[item]

    return f"the total price is ${total}"

print(calculate_bill(menu, items_bought))