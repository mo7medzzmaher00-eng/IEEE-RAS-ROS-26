def safe_divide():
    while True:
        try:
            num1= float(input("enter frist number: "))
            num2= float(input("enter second number:"))

            result= num1 / num2
            print(f"ther result of divide is{result}")
            break
        except ZeroDivisionError:
            print("Cannot divide by zero, try again")

        except ValueError:
            print("Invalid input, enter numbers only")

safe_divide()