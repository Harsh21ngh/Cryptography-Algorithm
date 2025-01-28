def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and 26 are not coprime, choose a different 'a' value.")
    return ''.join([chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A')) if char.isalpha() else char for char in text.upper()])

def affine_decrypt(cipher, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Modular inverse does not exist, choose a different 'a' value.")
    return ''.join([chr(((a_inv * (ord(char) - ord('A') - b)) % 26) + ord('A')) if char.isalpha() else char for char in cipher.upper()])

def main():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice!")
        return

    text = input("Enter the text: ").strip()
    a = int(input("Enter the value of 'a' (must be coprime with 26): ").strip())
    b = int(input("Enter the value of 'b': ").strip())

    if choice == 'encrypt':
        encrypted_text = affine_encrypt(text, a, b)
        print(f"Encrypted text: {encrypted_text}")
    elif choice == 'decrypt':
        decrypted_text = affine_decrypt(text, a, b)
        print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()