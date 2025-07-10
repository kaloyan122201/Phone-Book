def add_contact(phonebook):
    while True:
        info = input("Add new contact (or type 'exit' to stop): ")
        if info.lower() == "exit":
            break
        if "-" not in info:
            print("Invalid format. Use Name-Number.")
            continue
        name, phone = info.split("-")
        if name in phonebook:
            print(f"{name} updated.")
        else:
            print(f"{name} added.")
        phonebook[name] = phone

def remove_contact(phonebook):
    while True:
        name = input("Remove which contact? (or type 'exit'): ")
        if name.lower() == "exit":
            break
        if name in phonebook:
            del phonebook[name]
            print(f"{name} removed.")
        else:
            print(f"Contact {name} is not in the phonebook.")

def search_contact(phonebook):
    while True:
        name = input("Search for: ")
        if name.lower() == "exit":
            break
        if name in phonebook:
            print(f"{name} -> {phonebook[name]}")
        else:
            print(f"Contact {name} does not exist.")

def main():
    phonebook = {}
    print("Welcome to Phonebook!")
    while True:
        option = input("Choose: add / remove / search / exit: ").lower()
        if option == "add":
            add_contact(phonebook)
        elif option == "remove":
            remove_contact(phonebook)
        elif option == "search":
            search_contact(phonebook)
        elif option == "exit":
            break
        else:
            print("Invalid option.")

    print("\nYour phonebook:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")

if __name__ == "__main__":
    main()