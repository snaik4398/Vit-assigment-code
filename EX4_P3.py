test_list = [[5, 3, 2], [8, 6, 3], [3, 5, 2], [3, 6], [3, 7, 4], [2, 9]]
print(f"test_list: {test_list}")
k = int(input("Enter the value of 'k': "))
for i in range(len(test_list)):
	if i == k-1:
		test_list[i].reverse()
print(f"Output: {test_list}")

