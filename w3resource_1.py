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

# # 7. Write a Python program to accept a filename from the user and print the extension of that.
#
# filename = input("Enter a filename:")
# x = filename.rsplit('.', 1)
# print('Sample Filename: ',filename)
# print('Output: ', x[1])

# # 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0])
# print(color_list[1])

# # 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# # exam_st_date = (11, 12, 2014)
# # Sample Output : The examination will start from : 11 / 12 / 2014
#
# exam_st_date = (11, 12, 2014)
# print(f"The examination will start from : {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")
# print("The examination will start from : %i / %i / %i " % exam_st_date)
# print("The examination will start from : {a} / {b} ".format(exam_st_date[0],
#                                                             exam_st_date[1]), exam_st_date[2]) # Not working

# # 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# # Sample value of n is 5
# # Expected Result : 615
#
# n = input('Enter n:')
# sum = int(n) + int (n+n) + int (n+n+n)
# print("Expected Result : ", sum)

# # 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# # Sample function : abs()
# # Expected Result :
# # abs(number) -> number
# # Return the absolute value of the argument.
# # TODO  : figure out a way to print this for any function.
# function = input("Sample function: ")
# name = function.replace('()',"")
# var = name + '.__doc__'
# print(abs.__doc__)


# # 12. Write a Python program to print the calendar of a given month and year.
# # Note : Use 'calendar' module.
#
# import calendar
# print(calendar.month(2019,9))

# # 13. Write a Python program to print the following here document. Go to the editor
# # Sample string :
# # a string that you "don't" have to escape
# # This
# # is a ....... multi-line
# # heredoc string --------> example
# print('''a string that you "don't" have to escape"
# This
# is a ....... multi-line
# heredoc string --------> example''')

# # 14. Write a Python program to calculate number of days between two dates.
# # Sample dates : (2014, 7, 2), (2014, 7, 11)
# # Expected output : 9 days
#
# from datetime import date
# date1 = datetime.date(2014,7,2)
# date2 = datetime.date(2014,7,11)
# print(date2-date1)

# 15. Write a Python program to get the volume of a sphere with radius 6.
# Click me to see the sample solution
import math
r = int(input('Radius : '))
print('Volume', 4/3*math.pi*pow(r, 3))