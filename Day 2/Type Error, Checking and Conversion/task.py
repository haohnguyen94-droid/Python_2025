len("12345")

print(type("Hello"))
print(type(12345))
print(type(3.14))
print(type(True))

#convert data into different type using type()
#not all data type can be converting to another data type
print(int("123") + int("456"))

name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: " )) #str
print(type(name_of_the_user)) #int
print("Number of letters in your name: " + str(length_of_name))