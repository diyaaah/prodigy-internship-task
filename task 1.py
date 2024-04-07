def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_message += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_message += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_message += char
    return encrypted_message

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (an integer between 0 and 25): "))
    
    # Encryption
    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted_message)
    
    # Decryption
    decrypted_message = caesar_cipher(encrypted_message, -shift)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
