"""
Q.4 Write a python code to perform matrix multiplication.
"""
import numpy as np

mat1 = list()
mat2 = list()
product_mat = list()

r1 = int(input("Enter the number of rows of first matrix: "))
c1 = int(input("Enter the number of columns of first matrix: "))
r2 = int(input("Enter the number of rows of second matrix: "))
c2 = int(input("Enter the number of columns of second matrix: "))

if r1 != c2:
    print("Matrix Multiplication isn't possible.")
else:
    print("Enter the elements of the 1st matrix row wise:")
    for i in range(r1):
        row_list = list()
        for j in range(c1):
            x = int(input("Enter the value: "))
            row_list.append(x)
        mat1.append(row_list)

    print("First Matrix")
    for i in range(r1):
        print(mat1[i])
        print()

    print("Enter the elements of the 2nd matrix row wise:")
    for i in range(r2):
        row_list = list()
        for j in range(c2):
            x = int(input("Enter the value: "))
            row_list.append(x)
        mat2.append(row_list)

    print("Second Matrix")
    for i in range(r2):
        print(mat2[i])
        print()

    product_mat = np.dot(mat1, mat2)

    print("Product Matrix")
    for i in range(r1):
        print(product_mat[i])
        print()
