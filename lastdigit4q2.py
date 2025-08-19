number = int(input("Enter a number: "))
last_digit = abs(number) % 10  

if last_digit == 4:
    print(f"{number} ends with 4.")
else:
    print(f"{number} does not end with 4.")
