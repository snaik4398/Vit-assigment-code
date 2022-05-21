"""Q.6 A palindromic number (also known as a numeral palindrome or a numeric palindrome) is a number (such as 16461)
that remains the same when its digits are reversed. Write an algorithm/pseudocode, draw a flow chart and write the
python code to check whether the given number is palindrome or not. Check boundary conditions and print 'Invalid
input' for wrong input. Boundary Condition: Number>0
"""

num = int(input("Enter any number: "))
if num <= 0:
    print("Enter a number greater than 0.")
else:
    temp = num
    sum = 0
    while num > 0:
        digit = num % 10
        sum = (sum*10) + digit
        num = num//10
    if temp == sum:
        print(f"{temp} is a Palindrome Number.")
    else:
        print(f"{temp} isn't a Palindrome Number.")
