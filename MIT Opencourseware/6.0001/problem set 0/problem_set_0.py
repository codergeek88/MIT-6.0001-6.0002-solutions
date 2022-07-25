## Write a program that does the following in order:
## 1. Asks the user to enter a number “x” 
## 2. Asks the user to enter a number “y”
## 3. Prints out number “x”, raised to the power “y”. 
## 4. Prints out the log (base 2) of “x”.

from math import log2
x=input("enter a number x")
y=input("enter a number y")
x_int=int(x)
y_int=int(y)
print(x_int**y_int)
print(log2(x_int))