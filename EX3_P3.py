m = int(input("Enter the value of M: "))
n = int(input("Enter the value of N: "))

if n < m:
    print("You don't get any point")
else:
    free_cells = n * n - m * m
    print(f"You've gained: {free_cells} points.")
