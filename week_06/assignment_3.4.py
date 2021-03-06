# 4.6 Write a program to prompt the user for hours and rate per hour using input 
# to compute gross pay. Pay should be the normal rate for hours up 
# to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
# Put the logic to do the computation of pay in a function called computepay() and use 
# the function to do the computation. The function should return a value. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input unless you want to - 
# you can assume the user types numbers properly. 
# Do not name your variable sum or use the sum() function.

def computepay(h, r):
    h_dn_40 = 0
    h_up_40 = 0

    if (h > 40):
        h_dn_40 = 40
        h_up_40 = h - 40
    else:
        h_dn_40 = h

    return (h_dn_40 * rt) + (h_up_40 * rt * 1.5)

hrs = input("Enter hours: ")
rt = input("Enter rate: ")

try:
    hrs = float(hrs)     
    rt = float(rt)
except:
    print("Check values!")
    quit()

p = computepay(hrs, rt)
print("Pay", p)