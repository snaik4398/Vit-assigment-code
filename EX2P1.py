""" gradeing system """



n = int(input("number of S grade: "))
t = int(input("total attendance: "))
p = int(input("Participation in sports activity in a semester: "))
if n <= 0 or t <= 0 or p <= 0:
    print("Invalid Input")
elif n >= 3 and t >= 90 and p >= 2:
    print("EXCELLENT")
elif n >= 3 and t >= 90:
    print("VERY GOOD")
elif n >= 3 and p >= 2:
    print("GOOD")