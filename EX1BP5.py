n = int(input("number of labourers engaged in work: "))
t = int(input("total number of toys to be made : "))
d = int(input("total number of days allotted for completion : "))
d1 = int(input("the number of days work had been done: "))
t1 = int(input("number of toys made in d1 days: "))
x = (((n * d1) * (t - t1)) / ((d - d1) * t1)) - n
print("Number of men required for completing the job: ", x)
