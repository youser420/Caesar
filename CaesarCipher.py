import fileinput
def encrypt(text,key):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + key-65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text,key):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - key-65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - key - 97) % 26 + 97)
        else:
            result += char
    return result


#check the above function
VALUE=1
while VALUE:
    print("1. Encryption")
    print("2. Decryption")
    print("3. Exit")
    print("Enter your option")
    option=int(input())
    if option == 1:

        key=int(input("Enter key number: "))
        fpath=r"C:\Users\Tarun\source\repos\CaesarCipher\pythonn.txt"
        data = open(fpath, 'r').read()
        file_path = r"C:\Users\Tarun\source\repos\CaesarCipher\encrypted.txt"
        with open(file_path, 'w') as file:
            file.write(encrypt(data,key))
    
        print("File created successfully!!")
       
    elif option == 2:

        key = int(input("Enter key number: "))
        fpath = r"C:\Users\Tarun\source\repos\CaesarCipher\encrypted.txt"
        data = open(fpath, 'r').read()
        file_path = r"C:\Users\Tarun\source\repos\CaesarCipher\decrypted1.txt"
        with open(file_path, 'w') as file:
            file.write(decrypt(data, key))

        print("File created successfully!!")


    elif option == 3:
        quit()

