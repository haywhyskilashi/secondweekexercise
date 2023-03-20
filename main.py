print("Welcome to BOA bank")
pin = int(input("Enter your atm pin: "))

while pin != 1234:
    pin = int(input("Incorrect PIN: Enter the correct PIN: "))

if pin == 1234:
    print("Pin accepted")

# exercise 2

guess = 0
tries = 0

while guess != 6 and tries < 5:
    guess = int(input("Guess the number: "))
    tries = tries + 1

if guess != 6:
    print('You ran out of tries')
else:
    print("You got it")

# exercise 3

for x in range(101):
    print('I will not throw airplanes in class')

# exercise 4

r = 1.1
area = 3.801327

areaOfCircle = r * area
print("Area of the circle is: ", areaOfCircle)



# exercise 5 Write a Python program that accepts the user's first and last name and prints
# them in reverse order with a space between them

firstName = input("Enter Your first name: ")
lastName = input("Enter Your last name: ")

fullName = firstName + " " + lastName
reversedName = fullName[::-1]
lastNameFirst = lastName + " " + firstName
print(fullName)
print(reversedName)
print("Last name first: ", lastNameFirst)


# Exercise 6 Write a Python program that accepts a sequence of comma-separated
# numbers from the user and
# generates a list and a tuple of those numbers.

sampleData = (input("Enter series of numbers followed by comma: "))
listData = sampleData.split()
tupleData = tuple(listData)

print(listData)
print(tupleData)




# Exercise 8. Write a Python program to display
# the first and last colors from the following list.



colorlist = ['Red', "Green", "White", "Black"]

print((colorlist[0]),(colorlist[3]))


# Exercise 10. Write a Python program that accepts
# an integer (n) and computes the value of n+nn+nnn

userInput = int(input("Enter a number: "))
n1= int("%s" % userInput)
n2= int("%s%s" % (userInput, userInput))
n3= int("%s%s%s" % (userInput, userInput, userInput))

print(n1+n2+n3)


