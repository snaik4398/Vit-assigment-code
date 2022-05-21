"""Q.1 Currency converter

X, a currency conversion agent, serves his customers in exchanging currencies from Indian rupee to US Dollar. Deign
an algorithm and write a Python program to automate the process of finding the equivalent amount in US Dollar. """

rupees = float(input("Enter the amount in Indian Rupees: "))
print(f"{rupees} Indian Rupees = {'%.2f'%(rupees/74.87)} US Dollars.")
