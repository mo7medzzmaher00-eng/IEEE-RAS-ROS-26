import random

def get_unique_lottery():
    numbers = set()

    while len(numbers)<6:
        num = random.randint(1,50)
        numbers.add(num)
    return numbers

print(get_unique_lottery())