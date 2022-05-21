"""
Q.2 Given a size of square matrix and number of elements, find if it is an identity matrix or not?
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

count_1 = 0
count_0 = 0
for i in range(n):
    for j in range(n):
        if i == j and mat[i][j] == 1:
            count_1 = 1
        if i != j and mat[i][j] == 0:
            count_0 = 1

if count_1 == 1 and count_0 == 1:
    print("Identity Matrix")
else:
    print("Not an Identity Matrix")


