class passenger:
    def __init__(self,name):
        self.name= name
         
class flight:
    def __init__(self):
        self.passengers=[]         
    def add_passenger(self,passenger_obj):
        self.passengers.append(passenger_obj)
    

p1= passenger("mo")
p2= passenger("maher")

f= flight()
f.add_passenger(p1)
f.add_passenger(p2)
for p in f.passengers:
    print(p.name)