num  = float(input("Enter the CGPA: "))
if 9 <= num <= 10:
    print("outstanding")
elif 8 <= num <= 8.99:
    print("Excellent")
elif 7 <= num <= 7.99:
    print("good")
elif 6 <= num <= 6.99:
    print("Average")
elif 5 <= num <= 5.99:
    print("better")
elif 0 <= num <= 4.99:
    print("Poor")
print(num)
