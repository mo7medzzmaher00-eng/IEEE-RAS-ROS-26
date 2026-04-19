import random
 

def pick_winner(names):
     if not names :
        return "no names in list"
     winner = random.choice(names)
     return f"Congratulations {winner}"

players = ["maher","mohamed","mohamed maher <;","maher on fire"]
print(pick_winner(players))