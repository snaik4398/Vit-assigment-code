h = int(input("Enter hour: "))
m = int(input("Enter minutes:"))
if h <= 7:
    amount = (h // 5) * 200 + (h % 5) * 50 + m * 1
    print(amount)
else:
    print("Invalid Request")
