def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def main():
    try:
        a = int(input("Enter the first number (a): "))
        b = int(input("Enter the second number (b): "))
        gcd, x, y = extended_gcd(a, b)
        print(f"GCD: {gcd}")
        print(f"Coefficients: x = {x}, y = {y}")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()