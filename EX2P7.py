"""Draw a flow chart and write a python pseudocode, program to print the following pattern. Get input as a number of
rows from the user. Display "Invalid input" if the boundary condition fails.
1 2 3 4 5
2 2 3 4 5
3 3 3 4 5
4 4 4 4 5
5 5 5 5 5
"""

number_of_rows = int(input("Enter the number of rows: "))

for i in range(1, number_of_rows+1):
    for j in range(i):
        print(i, end="")
    for k in range(i+1, number_of_rows+1):
        print(k, end="")
    print()

