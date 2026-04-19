def move_player(pos,direction):
    x,y = pos
    if direction == "up":
        y+=1
    elif direction == "down":
        y-=1
    elif direction == "right":
        x+=1
    elif direction == "left":
        x-=1
    else:
        return "are you 3abeettt? invalid direction"   
    return (x,y)             

strat = (0,0)

print(move_player(strat,"up"))
print(move_player(strat,"down"))
print(move_player(strat,"right"))
print(move_player(strat,"left"))
print(move_player(strat,"usds"))