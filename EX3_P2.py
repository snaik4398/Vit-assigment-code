num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum1 = 0
sum2 = 0

for i in range(1, num1):
    if num1 % i == 0:
        sum1 += i

for i in range(1, num2):
    if num2 % i == 0:
        sum2 += i

if sum1 == num2 and sum2 == num1:
    print(f"({num1, num2}) are amicable pair.")
else:
    print(f"{num1, num2} are not amicable pair.")
