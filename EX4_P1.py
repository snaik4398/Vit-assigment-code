n = int(input("Enter he number of total coins: "))
l = list()
for i in range(n):
	l.append(input("Enter the amount of coin: "))

print(f"Wallet: {l}")
print(f"Unique Coins: {set(l)}")
print(f"Number of unique coins: {len(set(l))}")

