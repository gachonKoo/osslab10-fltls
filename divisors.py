import sys

number = int(sys.argv[1])

for i in range(1, number + 1):
    if number % i == 0:  # Check if 'i' is a divisor of 'number'
        print(i, end=" ")

print()  # Print a newline after all divisors are printed
