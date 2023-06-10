#!/usr/bin/env python3

# Script Name:                  Python
# Author:                       Raphael Chookagian
# Date of latest revision:      06/08/2023
# Purpose:                      Create a Python script that:

# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

import os

# Declaration of variables
a = 5
b = 10

# Main

if a == b:
    print("a is equal to b")

if a != b:
    print("a is not equal to b")

if a < b:
    print("a is less than b")

if a <= b:
    print("a is less than or equal to b")

if a > b:
    print("a is greater than b")

if a >= b:
    print("a is greater than or equal to b")


# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

age = 16

if age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 18 and age < 65:
    print("You are an adult.")
elif age == 16:
    print("You can drive!")
elif age >= 17 and age < 21:
    print("You are underage.")
elif age >= 21:
    print("You can legally drink!")
else:
    print("You are a senior citizen.")


# Create an if statement that includes both elif and else to execute when both if and elif are not met.

temperature = 77

if temperature < 32:
    print("It's freezing outside.")
elif temperature >= 32 and temperature < 68:
    print("It's chilly outside.")
elif temperature >= 68 and temperature < 86:
    print("It's a pleasant day.")
else:
    print("It's hot outside.")


# Stretch Goals:

# Create an if statement with two conditions by using and between conditions.
num = 15

if num >= 10 and num <= 20:
    print("The number is between 10 and 20.")

# Create an if statement with two conditions by using or between conditions.
num = 5

if num < 0 or num > 10:
    print("The number is either negative or greater than 10.")

# Create a nested if statement.
age = 18
height = 63

if age >= 18:
    print("You are eligible for this ride.")
    if height >= 63:
        print("You meet the height requirement for this ride.")
    else:
        print("You do not meet the height requirement for this ride.")
else:
    print("You do not meet the requirements for this ride.")


# Create an if statement that includes pass to avoid errors.
age = 25

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    pass
