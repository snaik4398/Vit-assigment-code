test_list = [6, 3, 7, 2, 6, 8, 4, 3, 9, 2, 1, 3]

print("The original list is : " + str(test_list))

n = int(input("Enter the value of 'n': "))
m = int(input("Enter the value of 'n': "))

k = 0
res = []
if n * m != len(test_list):
    res = "Matrix Not Possible"
else:
    for i in range(0, n):
        sub = []
        for j in range(0, m):
            sub.append(test_list[k])
            k += 1
        res.append(sub)

print("Constructed Matrix : " + str(res))
