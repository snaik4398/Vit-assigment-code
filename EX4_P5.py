test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = int(input("Enter the value of 'k': "))
op_list = list()
for i in test_list:
    if test_list.count(i) >= k:
        op_list.append(i)
print(f"{list(set(op_list))}")
