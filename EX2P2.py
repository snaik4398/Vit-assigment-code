hr = int(input("Enter Hour: "))
mn = int(input("Enter minute: "))
sec = int(input("Enter seconds: "))
if 0 < hr < 24 and 0 < mn < 59 and 0 < sec < 59:
    print(f"The time in 24 hour format {hr}:{mn}:{sec}")

if hr > 12:
    hr = hr - 12
    print(f"The time in 12 hour format {hr}:{mn}:{sec}")