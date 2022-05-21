number_of_subjects = int(input("Enter the number of subjects: "))
marks = []

for i in range(number_of_subjects):
    x = int(input(f"Enter the marks for subject{i + 1}: "))
    marks.append(x)

s_count = 0
a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0

for x in marks:
    if x > 100 or x < 0:
        print("Invalid Input")
    elif 90 <= x <= 100:
        s_count += 1
    elif 80 <= x < 90:
        a_count += 1
    elif 70 <= x < 80:
        b_count += 1
    elif 60 <= x < 70:
        c_count += 1
    elif 50 <= x < 60:
        d_count += 1
    else:
        f_count += 1

if s_count >= 2 and a_count >= 2:
    print("Eligible for Scholarship.")
else:
    print("Not Eligible for Scholarship")
