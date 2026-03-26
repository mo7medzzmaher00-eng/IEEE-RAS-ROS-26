import math 

numbers=[]

while  True:
    num=int(input ("inter numbers (-1 will break):"))

    if num is -1 :
        break

    numbers.append(num)
print(f"max number is: {max(numbers)}")
print(f"min number is: {min(numbers)}")
