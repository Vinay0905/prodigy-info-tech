def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift  
    
    for char in text:
        if char.isalpha():  
            shift_base = ord('A') if char.isupper() else ord('a')
            
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            
            result += char
    
    return result


print("Caesar Cipher Program")
while True:
    mode = input("Enter 'encrypt' to encrypt, 'decrypt' to decrypt, or 'exit' to quit: ").strip().lower()
    if mode == "exit":
        print("Exiting the program. Goodbye!")
        break
    elif mode not in ["encrypt", "decrypt"]:
        print("Invalid option. Please enter 'encrypt', 'decrypt', or 'exit'.")
        continue

    message = input("Enter your message: ").strip()
    try:
        shift_value = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        continue

    result = caesar_cipher(message, shift_value, mode)
    print(f"Result ({mode}ed): {result}")
