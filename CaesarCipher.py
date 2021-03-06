
def caesar_encrypt(plaintext_message, shift):
    """
        Encrypts a string using a Caesar Cipher with a user-provided shift.
        Returns the encrypted message.
    """
    plaintext_message = plaintext_message.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_message = ""

    for char in plaintext_message:
        
        # Skip encryption if char is non-alphabetical
        if char not in alphabet:
            encrypted_message += char
            continue

        char_alphabet_index = alphabet.index(char)
        encrypted_message += alphabet[(char_alphabet_index + shift) % 26]

    return encrypted_message

if __name__ == "__main__":
    while True:
        message = input("Enter a message you would like encrypted: ")
        encrypted_message = caesar_encrypt(message, 17)
        print(f"Encrypted message: {encrypted_message}")