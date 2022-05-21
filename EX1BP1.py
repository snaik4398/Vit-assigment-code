length = int(input("Enter the length in feet: "))
breadth = int(input("Enter the breadth in feet: "))
row = (length // 2) + 1
column = (breadth // 2) + 1
total = row * column
print("Number of rows: ", row)
print("Number of columns: ", column)
print("Number of plant required: ", total)
