binary = input("Enter binary number: ")

# Binary to Decimal
decimal = 0
power = 0

for digit in binary[::-1]:
    decimal += int(digit) * (2 ** power)
    power += 1

print("Decimal:", decimal)

# Decimal to Octal
octal = ""
temp = decimal

while temp > 0:
    octal = str(temp % 8) + octal
    temp = temp // 8

print("Octal:", octal)
