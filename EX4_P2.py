l = []
even_count=0
odd_count=0
n = int(input("Enter the number of items in a list: "))
for i in range(n):
	l.append((int(input("Enter the value: "))))

for i in l:
	if i%2==0:
		even_count+=1
	else:
		odd_count+=1

print(f"Number of Even Numbers in the list: {even_count}")
print(f"Number of Odd Numbers in the list: {odd_count}")
