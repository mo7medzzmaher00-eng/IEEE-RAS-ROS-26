class Calculator:
    def add(self,a,b):
        return a + b
    
    def subtract(self,a,b):
        return a - b
    
    def multiply(self,a,b):
        return a * b

clc = Calculator()

print(clc.add(5,3))
print(clc.subtract(5,3))
print(clc.multiply(5,3))
