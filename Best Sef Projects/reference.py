import base64
import sys

documents = [
    [1, "Name", None],
    [2, "Aadhar", 12],
    [3, "Pan card", 10],
    [4, "Passport", 8],
    [5, "Voter Id", 10],
    [6, "Driving License", 11]
]

def caesar_cipher(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # Leave digits and base64 symbols unchanged
            result += char
    return result

def caesar_decipher(text, shift=3):
    return caesar_cipher(text, -shift)

def create_encrypted_code():
    password = input("Set Password:\n")
    encoded_password = base64.b64encode(password.encode()).decode()

    print("\nAvailable Documents:")
    for doc in documents:
        limit_text = f" (Limit {doc[2]} chars)" if doc[2] else ""
        print(f"{doc[0]}. {doc[1]}{limit_text}")

    try:
        num_docs = int(input("\nEnter number of documents you want to input:\n"))
    except ValueError:
        print("Invalid number.")
        sys.exit()

    combined_data = ""

    for i in range(num_docs):
        try:
            index = int(input(f"Enter index of document #{i + 1}:\n"))
            if not (1 <= index <= len(documents)):
                print("Invalid index.")
                sys.exit()
        except ValueError:
            print("Invalid input.")
            sys.exit()

        doc = documents[index - 1]
        doc_name = doc[1]
        char_limit = doc[2]

        detail = input(f"Enter details for '{doc_name}':\n")
        if char_limit is not None and len(detail) > char_limit:
            print(f"Details exceed limit of {char_limit} characters.")
            sys.exit()

        combined_data += f"{doc_name}:{detail};"

    # Encode combined data with base64
    base64_data = base64.b64encode(combined_data.encode()).decode()

    # Combine password and data with delimiter
    combined_str = encoded_password + "::" + base64_data

    # Apply Caesar cipher to combined string
    final_code = caesar_cipher(combined_str, shift=3)

    print("\n🔐 Your unique encrypted code (keep it safe):\n")
    print(final_code)
    print("\nUse this code and your password to unlock later.")

def unlock_code():
    input_code = input("Enter your encrypted code:\n")
    # First decode Caesar cipher
    decoded_caesar = caesar_decipher(input_code, shift=3)

    try:
        encoded_password, encoded_data = decoded_caesar.split("::")
    except ValueError:
        print("Invalid code format.")
        return

    entered_password = input("Enter your password:\n")
    entered_encoded = base64.b64encode(entered_password.encode()).decode()

    if entered_encoded != encoded_password:
        print("❌ Incorrect password. Access denied.")
        return

    # Decode base64 data
    try:
        decoded_data = base64.b64decode(encoded_data.encode()).decode()
    except Exception:
        print("Error decoding data. Possibly corrupted.")
        return

    print("\n🔓 Password verified. Document Details:\n")
    entries = decoded_data.strip(';').split(';')
    for idx, entry in enumerate(entries, 1):
        name, detail = entry.split(':', 1)
        print(f"{idx}. {name}: {detail}")

def main():
    print("Choose an option:")
    print("1. Create encrypted code")
    print("2. Unlock code with password")

    choice = input("Enter 1 or 2:\n")
    if choice == '1':
        create_encrypted_code()
    elif choice == '2':
        unlock_code()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
