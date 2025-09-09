import base64
import sys
from datetime import datetime, timezone, timedelta

file = "notes.txt"
password = "samarthp1234@"

with open(file,'a') as f:
    pass

def check_password():
    pwd = input("Enter The Password:\n")
    if pwd == password:
        return True
    else:
        print("Wrong Password")
        return False


def add_note():
    if not check_password():
        return
    
    note = input("Enter The Note:\n")
    IST = timezone(timedelta(hours=5,minutes=30))
    now = datetime.now(IST)
    now2 = now.strftime("%d-%m-%Y %I:%M:%S %p")
    final = f"{now2} - {note}"
    enc = base64.b64encode(final.encode()).decode()
    with open(file,'a') as f:
        f.write(enc+"\n")
    print("Note Saved Successfully")



def view_notes():
    if not check_password():
        return
    try:
        with open(file,'r') as f:
            lines = f.readlines()
            if not lines:
                print("No Notes Present 📪")
                return

            for l in lines:
                dec = base64.b64decode(l.strip().encode()).decode()
                print("-",dec)

    except FileNotFoundError:
        print("No Notes File Found")

def delete_note():
    view_notes()
    target = input("Enter the exact Time such as dd-mm-YYYY HH:MM:SS AM/PM: ").strip()
    kept_notes = []
    deleted = False

    try:
        datetime.strptime(target, "%d-%m-%Y %I:%M:%S %p")
    except ValueError:
        print(" Invalid timestamp format. Please enter the full date and time as shown.")
        return

    with open(file, "r") as f:
        notes = f.readlines()

    for note in notes:
        try:
            decoded = base64.b64decode(note.strip().encode()).decode()
            if decoded.startswith(target):
                deleted = True
                continue
            kept_notes.append(note)
        except Exception:
            kept_notes.append(note)

    with open(file, "w") as f:
        f.writelines(kept_notes)

    if deleted:
        print("✅ Note Successfully Deleted")
    else:
        print("⚠️ No matching note found with that timestamp.")

while True:
    print("1.Add Notes")
    print("2.View Notes")
    print("3.Delete Notes")
    print("4.Exit")

    choice = input("Enter the choice:\n")
    match choice:
        case "1":
            add_note()
            sys.exit()
        case "2":
            view_notes()
            sys.exit()
        case "3":
            delete_note()
            sys.exit()
        case "4":
            print("Thanks For Visiting Function")
            sys.exit()
        case _:
            print("Invalid Choice")
            sys.exit()

