import random

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_keys(prime):
    g = random.randint(2, prime - 2)
    private_key = random.randint(2, prime - 2)
    public_key = mod_exp(g, private_key, prime)
    return g, private_key, public_key

def encrypt(plaintext, public_key, g, prime):
    k = random.randint(2, prime - 2)
    while gcd(k, prime - 1) != 1:
        k = random.randint(2, prime - 2)
    c1 = mod_exp(g, k, prime)
    c2 = (plaintext * mod_exp(public_key, k, prime)) % prime
    return c1, c2

def decrypt(c1, c2, private_key, prime):
    s = mod_exp(c1, private_key, prime)
    s_inverse = pow(s, -1, prime)
    plaintext = (c2 * s_inverse) % prime
    return plaintext

def main():
    prime = int(input("Enter a large prime number: "))
    g, private_key, public_key = generate_keys(prime)
    print(f"Generated keys:\nGenerator (g): {g}\nPrivate Key: {private_key}\nPublic Key: {public_key}")
    plaintext = int(input("Enter the plaintext (as an integer): "))
    c1, c2 = encrypt(plaintext, public_key, g, prime)
    print(f"Ciphertext: (c1: {c1}, c2: {c2})")
    decrypted_plaintext = decrypt(c1, c2, private_key, prime)
    print(f"Decrypted Plaintext: {decrypted_plaintext}")

if __name__ == "__main__":
    main()
