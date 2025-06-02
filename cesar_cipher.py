def welcome(): 
    '''function to print welcome message '''
    print("Welcome to the Caesar Cipher\n""This program encrypts and decrypts text with Caesar Cipher .")  

def enter_message():
    '''function to get user input for mode, message, and shift'''
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid input. Please enter 'e' or 'd'.")

    if mode == 'e':
        message = input("What message would you like to encrypt: ")
    else:
        message = input("What message would you like to decrypt: ")

    while True:
        shift = input("What is the shift number: ")
        if shift.isdigit():
            shift = int(shift)
            break
        else:
            print("Invalid shift. Please enter a valid shift number.")

    return mode, message, shift

def encrypt(message, shift):
    '''function to encrypt the message'''
    encrypted_message = ""
    for char in message.upper():
        if char.isalpha():
            encrypted_message += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    '''function to decrypt the message'''
    decrypted_message = ""
    for char in message.upper():
        if char.isalpha():
            decrypted_message += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted_message += char
    return decrypted_message

def process_file(filename, mode, shift):
    '''function to process the file'''
    try:
        with open(filename, 'r') as file:
            content = file.read().upper()

        if mode == 'e':
            result = encrypt(content, shift)
            print("Encrypted message:", result)
        elif mode == 'd':
            result = decrypt(content, shift)
            print("Decrypted message:", result)

    except FileNotFoundError:
        print("File not found:", filename)

def is_file(filename):
    '''function to check if file exists'''
    return os.path.isfile(filename)

def write_message(messages):
    '''function to write the message to a file'''
    with open("result.txt", 'w') as f:
        for message in messages:
            f.write(message + '\n')
    print("Output written to result.txt")
def message_or_file():
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid input. Please enter 'e' or 'd'.")
    while True:
        choice= input("would you like to read the file(f) or the console(c)?")
        if choice=='f':
            filename=input("enter a filename:")
            if is_file(filename):
                return mode,None,filename
            print("invalid filename")
            
        elif choice=='c':
            message=input("what message would you like to{}:".format("encrypt" if mode=='e' else "decrypt")).lower()
            return mode,message,None
        else:
            print ("invalid choice")


def main():
    welcome()
    mode, message, shift = message_or_file()
    if message is not None:
        while True:
            shift = input("What is the shift number: ")
            if shift.isdigit():
                shift = int(shift)
                break
            else:
                print("Invalid shift. Please enter a valid shift number.")


    if mode == 'e':
        encrypted_text = encrypt(message, shift)
        print("The encrypted message:", encrypted_text)
    elif mode == 'd':
        decrypted_text = decrypt(message, shift)
        print("The decrypted message:", decrypted_text)
    while True:

        another_msg = input("Would you like to continue (yes/no): ").lower()
        if another_msg == 'no':
            print("Thank you for using the program. Goodbye!")
            return
        elif another_msg == 'yes':
            main()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()