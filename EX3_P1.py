number_of_farms = int(input("Enter the number of farms: "))
farms = list()
for i in range(number_of_farms):
    print(f"enter the amount of milk collected from farm{i+1}")
    l = int(input("Liter: :"))
    ml = int(input("Ml: "))
    farms.append(l*1000 +ml)

total = sum(farms)
print(f"Total milk collected: {total//1000}Ltr {total%1000}Ml")


                            
