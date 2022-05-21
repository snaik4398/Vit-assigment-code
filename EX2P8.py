"""Develop an algorithm and write the Python code to print the following pattern. Check boundary conditions and print
'Invalid input' for wrong output.
*
***
*****
*******

Boundary Condition:
n > 0
"""

number_of_rows = int(input("Enter the number of rows: "))
if number_of_rows <= 0:
    print("Invalid Input")
else:
    for i in range(number_of_rows):
        for j in range(2 * i + 1):
            print("*", end="")
        print()
