print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

#if-elif-else statement conditions
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill += 5
        print(f"your ticket is ${bill}")
    elif age > 18:
        bill += 12
        print(f"your ticket is ${bill}")
    else:
        bill += 7
        print(f"your ticket is {bill}")
    want_photo = input("Do you want to have a photo take? Type y for Yes and n for No: ")
    if want_photo == 'y':
        #Add $3 to their bill
        bill += 3
    print(f"your ticket is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
