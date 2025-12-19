def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                new_char = chr((ord(char) - start + shift) % 26 + start)
            elif mode == "decrypt":
                new_char = chr((ord(char) - start - shift) % 26 + start)

            result += new_char
        else:
            result += char

    return result

message = input("Enter the message: ")
shift = int(input("Enter shift value: "))
choice = input("Type 'encrypt' or 'decrypt': ").lower()
output = caesar_cipher(message, shift, choice)
print("Result:", output)