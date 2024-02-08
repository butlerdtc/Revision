while True:
    number1 = int(input("Enter your first number please: "))
    if number1 == 0:
        break
    else:
        number2 = int(input("Enter your second number please: "))

    if number1 == number2:
        print(f"Both numbers were {number1} and are equal")
    elif number1 > number2:
        print(f"{number1} is greater than {number2}")
    else:
        print(f"{number2} is greater than {number1}")


print("Goodbye")
