n = int(input("Enter a number: "))
last_digit = n - (10 * int(n / 10))
if n % 3 == 0 and last_digit == 4:
    print("Yes")
else:
    print("No")
