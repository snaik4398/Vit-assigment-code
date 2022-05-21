initial = int(input("Enter the initial amount: "))
year = int(input("Enter the years: "))
expAmo = int(input("Enter the expected amount: "))
ROI = ((expAmo - initial) / (initial * year)) * 100
print("The Rate of interest will be: ", ROI)
