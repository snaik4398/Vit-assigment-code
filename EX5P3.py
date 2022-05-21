"""
Q.3 Given the rows and columns of a two-dimensional matrix and number of elements, find the sum of
its diagonals and the absolute difference between the two diagonals.
"""

n = int(input("enter the number of rows and columns: "))
mat = list()

print("Enter the elements of the matrix row wise:")
for i in range(n):
    row_list = list()
    for j in range(n):
        x = int(input("Enter the value: "))
        row_list.append(x)
    mat.append(row_list)

print("The Matrix")
for i in range(n):
    print(mat[i])
    print()

d1_sum = 0
d2_sum = 0

for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            d2_sum += mat[i][j]
        if i == j:
            d1_sum += mat[i][j]

print(f"Sum of diagonal1: {d1_sum}.")
print(f"Sum of diagonal2: {d2_sum}.")
print(f"Absolute difference between the two diagonals: {abs(d1_sum - d2_sum)}.")
