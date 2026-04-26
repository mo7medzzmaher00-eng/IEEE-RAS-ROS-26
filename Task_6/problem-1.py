class dog:

    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def bark(self):
        print(f"woof my name is {self.name} my breed is {self.breed}" )    

frist_dog= dog("reko","boxer")
frist_dog.bark() 