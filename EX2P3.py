print("enter the marks of five subjects: ")
marks = []
for i in range(5):
    sub = int(input())
    marks.append(sub)

for j in range(5):
    if marks[j] >= 90:
        print(str(marks[j]) + "-->the grade is 'S'")
    elif 80 <= marks[j] < 90:
        print(str(marks[j]) + "-->the grade is 'A'")
    elif 70 <= marks[j] < 80:
        print(str(marks[j]) + "-->the grade is 'B'")
    elif 60 <= marks[j] < 70:
        print(str(marks[j]) + "-->the grade is 'C'")
    elif 50 <= marks[j] < 60:
        print(str(marks[j]) + "-->the grade is 'D'")
    elif 40 <= marks[j] < 50:
        print(str(marks[j]) + "-->the grade is 'E'")
    else:
        print(str(marks[j]) + "-->the grade is 'F'")