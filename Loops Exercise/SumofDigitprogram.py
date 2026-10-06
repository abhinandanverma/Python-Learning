num = input("Enter a number: ")

total = 0

for digit in num:
    total = total + int(digit)

print("Sum =", total)