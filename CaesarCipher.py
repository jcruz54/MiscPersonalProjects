
class CaesarCipher():

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    @staticmethod
    def brute_force_decrypt(encrypted_message):
        """
        """
        pass

    @staticmethod
    def decrypt(encrypted_message, shift):
        """
        """
        pass

    @staticmethod
    def encrypt(plaintext_message, shift):
        """
            Encrypts a string using a Caesar Cipher with a user-provided shift.
            Returns the encrypted message.
        """
        plaintext_message = plaintext_message.lower()
        encrypted_message = ""

        for char in plaintext_message:
            
            # Skip encryption if char is non-alphabetical
            if char not in CaesarCipher.alphabet:
                encrypted_message += char
                continue

            char_alphabet_index = CaesarCipher.alphabet.index(char)
            encrypted_message += CaesarCipher.alphabet[(char_alphabet_index + shift) % 26]

        return encrypted_message

if __name__ == "__main__":
    while True:
        message = input("Enter a message you would like encrypted: ")
        encrypted_message = CaesarCipher.encrypt(message, 1)
        print(f"Encrypted message: {encrypted_message}")
