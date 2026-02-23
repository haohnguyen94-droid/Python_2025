print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

#if-else statement condition
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print(f"your ticket is $5")
    elif age > 18:
        print(f"your ticket is $12")
    else:
        print(f"your ticket is $7")
else:
    print("Sorry you have to grow taller before you can ride.")
