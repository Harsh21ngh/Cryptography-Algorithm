import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    gcd, x, _ = extended_euclidean(a, m)
    if gcd != 1:
        raise ValueError("Inverse doesn't exist.")
    return x % m

def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = mod_inverse(e, phi)
    return e, d, n

def letter_to_num(letter):
    return ord(letter.upper()) - ord('A')

def num_to_letter(num):
    return chr(num + ord('A'))

def rsa_encrypt(plaintext, e, n):
    return [pow(letter_to_num(char), e, n) for char in plaintext]

def rsa_decrypt(ciphertext, d, n):
    return ''.join([num_to_letter(pow(char, d, n)) for char in ciphertext])

if __name__ == "__main__":
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    e, d, n = generate_keys(p, q)
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")
    plaintext = input("Enter plaintext to encrypt (only uppercase letters): ")
    ciphertext = rsa_encrypt(plaintext, e, n)
    print(f"Ciphertext: {ciphertext}")
    decrypted = rsa_decrypt(ciphertext, d, n)
    print(f"Decrypted: {decrypted}")
