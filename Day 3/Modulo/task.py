#Modulo operator
#Even numbers 12 % 2 == 00
print(12 % 4)
#Odds numbers
print(10 % 3)

number_to_check = (int(input("What is the number you want to check? ")))
if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")