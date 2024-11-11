# Krysta Dennis
# UWYO COSC 1010
# Submission Date:07NOV2024
# Lab 08
# Lab Section:12
# Sources, people worked with, help given to: Help from lily Trandhal, Used google for help with the formula,
#used google to help find reason for error
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def number_con(num):
    isNeg = False
    if "-" in num:
        isNeg = True
        num = num.replace("-","")
    if "." in num:
        if num.count(".") ==1:
            num_list = num.split(".")
            if len(num_list) == 2 and num_list[0].isdigit() and num_list[1].isdigit():            
                return -1 * float(num) if isNeg else float(num)
        
    elif num.isdigit():
        if isNeg:
            return -1 * int(num)
        else:
            return int(num)
    else:
        return False
    if answer is None:
        print("The equation has no real solutions.")
    else:
        print(f"The solutions to the equation are: {answer}")
       
print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def point_slope(m, b, low_x, up_x):
    points = []
    for x in range(low_x, up_x + 1):  
        y = m * x + b
        points.append((x, y))
    return points
while True:
    m = input("Enter a number for m or 'exit' to quit: ")
    if m.lower() == "exit":
        break
    m = number_con(m)
    if m == False:
        print("Invalid input for m, try again.")
        continue

    b = input("Enter a number for b or 'exit' to quit: ")
    if b.lower() == "exit":
        break
    b = number_con(b)
    if b == False:
        print("Invalid input for b, try again.")
        continue

    low_x = input("Enter a lower bound for x or 'exit' to quit: ")
    if low_x.lower() == "exit":
        break
    low_x = number_con(low_x)
    if low_x == False or not isinstance(low_x, int):
        print("Invalid input for lower bound, try again.")
        continue

    up_x = input("Enter an upper bound for x or 'exit' to quit: ")
    if up_x.lower() == "exit":
        break
    up_x = number_con(up_x)
    if up_x == False or not isinstance(up_x, int):
        print("Invalid input for upper bound, try again.")
        continue

    if low_x > up_x:
        print("Lower bound cannot be greater than upper bound. Try again.")
        continue

    points = point_slope(m, b, low_x, up_x)
    print("Generated points:", points)
    break


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null


import math

def quad_solve(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root_1, root_2
    elif discriminant == 0:
        z_root = -b / (2 * a)
        return z_root, z_root
    else:
        return None  
a = float(input("Enter a number for a: "))
b = float(input("Enter a number for b: "))
c = float(input("Enter a number for c: "))
answer = quad_solve(a, b, c)

if answer is None:
    print("The equation has no real solutions.")
else:
    print(f"The solutions to the equation are: {answer}")



