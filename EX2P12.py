n = int(input("Enter the number of terms: "))
a = []
for i in range(n):
    a.append(int(input("Enter the value: ")))

flag = False
for x in a:
    if a.count(x) > 1:
        flag = True

if flag:
    print("Duplicate")
else:
    print("Unique")
