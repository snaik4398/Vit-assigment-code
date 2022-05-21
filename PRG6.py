"""Little Bob loves chocolate, and he goes to a store with Rs. N in his pocket. The price of each chocolate is Rs. C.
The store offers a discount: for every M wrappers he gives to the store, he gets one chocolate for free. This offer
is available only once. How many chocolates does Bob get to eat? """

n = int(input("Enter the value of N: "))  # Bob's budget
c = int(input("Enter the value of C: "))  # Price of a chocolate
m = int(input("Enter the value of M: "))  # discount for number of wrappers

num_of_chocolates = n / c
returning_wrapper = num_of_chocolates / m
Chocolates_received = num_of_chocolates + returning_wrapper

print(f"Bob get {Chocolates_received} to eat.")
