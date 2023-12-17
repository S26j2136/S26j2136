def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Display
print("Choose an option:")
print("1. Find gcd")
print("2. Find lcm")

choice = input("Enter 1 or 2: ")

# Check 
if choice not in ['1', '2']:
    print("Invalid choice. Please enter 1 or 2.")
else:
    try:
        a = int(input("Enter the first integer (a): "))
        b = int(input("Enter the second integer (b): "))

        if choice == '1':
            result = gcd(a, b)
            print(f"The greatest common divisor (gcd) of {a} and {b} is: {result}")
        elif choice == '2':
            result = lcm(a, b)
            print(f"The least common multiple (lcm) of {a} and {b} is: {result}")

    except ValueError:
        print("Please enter valid integers.")
