# Q.5 Write a python code to find the sum of the following series. Get N from the user.
#
# 1+2+3+4+5+………………………………+N
# 2+4+6+8+10+……………………………+ N

n = int(input("Enter the number of terms: "))
print(f"Sum of Series1: {n*(n+1)/2}")
print(f"Sum of Series2: {n*(n+1)}")
