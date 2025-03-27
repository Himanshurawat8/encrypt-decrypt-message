letters = 'qwertyuiopasdfghjklzxcvbnm'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if letter == ' ':  # Preserve spaces
            ciphertext += ' '
        else:
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter  # Keep non-alphabet characters unchanged
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters  # Wrap around
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if letter == ' ':
            plaintext += ' '
        else:
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters  # Wrap around
                plaintext += letters[new_index]
    return plaintext

print("\n*** Custom Cipher Program ***\n")

user_input = input("Do you want to encrypt or decrypt? (e/d): ").lower()
print()

if user_input == 'e':
    print("Encryption Mode\n")
    key = int(input("Enter the key (1 to 25): "))  # Max key should be 25, as 26 is a full cycle
    text = input("Enter the text to encrypt: ")
    ciphertext = encrypt(text, key)
    print(f'Ciphertext: {ciphertext}')

elif user_input == 'd':
    print("Decryption Mode\n")
    key = int(input("Enter the key (1 to 25): "))
    text = input("Enter the text to decrypt: ")
    plaintext = decrypt(text, key)
    print(f'Plaintext: {plaintext}')

else:
    print("Invalid choice! Please enter 'e' or 'd'.")
