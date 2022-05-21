"""Relay Race

In an ultra race, four runners are there and each of them cover equal distance. Given the total distance to be covered
by the runners, design an algorithm and write a Python code to determine the Km and meter of distance to be covered
by each runner? For example, if the total distance to be covered is 2 Km and 500 m then the distance to be covered by
each runner is 0Km and 625 m. """

total_dis_km = int(input("Enter the total distance covered KM: "))
total_dis_m = int(input("Enter the total distance covered M: "))
total_distance = (total_dis_km*1000) + total_dis_m
print(f"Distance covered by each runner: {total_distance%4}KM and {total_distance/4}M")

