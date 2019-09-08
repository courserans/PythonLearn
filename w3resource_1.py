# Python Basic (Part -I) - Exercises, Practice, Solution
# https://www.w3resource.com/python-exercises/python-basic-exercises.php

# # 1. Print in the correct format

# string = 'Twinkle, twinkle, little star,' \
#          '\n\tHow I wonder what you are! ' \
#          '\n\t\tUp above the world so high,' \
#          '\n\tLike a diamond in the sky.' \
#          '\nTwinkle, twinkle, little star,' \
#          '\n\tHow I wonder what you are'
# print(string)


# # 2. Write a Python program to display the current date and time

# import sys
# print(sys.version)
# print(sys.version_info)

# # 3. Write a Python program to display the current date and time

# import datetime
# print(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%d-%d %H:%m:%S"))

# # 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
# import math
# radius = float(input("Input the radius of the circle: "))
# area = math.pi*math.pow(radius,2)
# print("Areas - %.2f" %area)
# print("Areas - {0:.2f}".format(area))


# # 5. Write a Python program which accepts the user's first and last name and
# # print them in reverse order with a space between them.
#
# name = input("Enter your name <first name> <last name> : ")
# print(name)
# x = name.split()
# print(f"{x[1]} {x[0]}")
# print(x[1] + " " + x[0])


# # 6. Write a Python program which accepts a sequence of comma-separated numbers from user and
# # generate a list and a tuple with those numbers.
#
# number = input("Enter a sequence of comma separated numbers : ")
# mylist = list(number.split(','))
# mytuple = tuple(mylist)
# print("List :", mylist)
# print("Tuple :", mytuple)
# print("List : {0}".format(mylist))
# print("List : {0}".format(mytuple))




