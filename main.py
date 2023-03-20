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


# Write a Python program that prints the
# calendar for a given month and year.
# Note : Use 'calendar' module.


from datetime import date

todays_date = date.today()

print("Current date: ", todays_date)

print("Current year: ", todays_date.year)
print("Current month: ", todays_date.month)
print("Current day: ", todays_date.day)


# Write a Python program to calculate the
# number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)


from datetime import date

date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)

numberOfDays = date2 - date1

print("The number of days between the given range of "
      "date is: ", numberOfDays)


# Write a Python program to get the volume of
# a sphere with radius six.

radius = 6.0
pi = 3.14

volume = (4.0/3.0) * pi * (radius**3)

print("The volume of sphere is: ", volume)





# Write a Python program to calculate the sum of three given numbers. If the
# values are equal, return three times their sum.

def my_function(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum
print(my_function(1,2,3))
print(my_function(3,3,3))





# Write a Python program that determines whether a given number (accepted from the user) is even or odd,
# and prints an appropriate message to the user.


givenNumber = int(input("Enter a number: "))

if givenNumber % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")





# Write a Python program to count
# the number 4 in a given list.


list2 = [1, 3, 4, 5, 2, 4, 5, 6, 8, 2, 4, 9, 0]
print(list2.count(4))








