alphabet = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


command = input("Type 'encode' to encrypt type decode to 'decrypt':\n")
text = input("Enter Your Message:\n")
shift = int(input("Enter The Shift Number\n"))

def checker():
        if text == "dev:manual" and shift == 5:
            import dev_manual
            print(dev_manual.manual)
        if text == "/manual" and shift == 2:
            with open('user_manual','r') as f:
                contents = f.read()
                print(contents)
def main():
    checker()
    print("Thanks For Using Dev Tools")

def decorator(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        print("Thanks For using this function")
        return result
    return wrapper


@decorator
def encrypt(text2,shift2):
    cipher_text = ""
    for letter in text2:
        position = alphabet.index(letter)
        new_position = position + shift2
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)

def decrypt(cipher_text,shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position-shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(plain_text)



if command == "checker":
    main()
if command == "encode":
    encrypt(text,shift)
if command == "decode":
    decrypt(text,shift)
else:
    print("Invalid Command")







