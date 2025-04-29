# weekday.py
# Week 5 Task -  output whether today is a weekday

# Reference Material
# https://www.w3schools.com/python/python_datetime.asp
# Lecture notes

# Author: Lorraine Morrissey

import datetime
x = datetime.datetime.now()

today = x.strftime("%A")

print("Today is {}".format(today))

weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday',]

if today in weekdays:
    print("Yes, unfortunately today is a weekday.")
else:
    print(" It is the weekend, yay!")
