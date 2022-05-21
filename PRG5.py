"""A company wants its employees to work for 'X' hours on average per day in a week (Monday to Friday).  Given the
number of hours worked by an employee on each day of a week, design a flowchart and write a Python code to compute
the average number of hours worked by the employee. Number of hours worked can be floating point values. For example,
7 hours 30 minutes is entered as 7.5 hours """

work_hour_day1 = float(input("Enter number of hours worked on monday: "))
work_hour_day2 = float(input("Enter number of hours worked on tuesday: "))
work_hour_day3 = float(input("Enter number of hours worked on wednesday: "))
work_hour_day4 = float(input("Enter number of hours worked on thursday: "))
work_hour_day5 = float(input("Enter number of hours worked on friday: "))

avg_work_hour = (work_hour_day5+work_hour_day4+work_hour_day3+work_hour_day2+work_hour_day1)/5
print(f"Average hours worked in a week: {avg_work_hour}")
