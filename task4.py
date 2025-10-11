def parse_input(user_input):
    """Парсить введений рядок на команду та аргументи."""
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args

def add_contact(args, contacts):
    """Додає контакт: add [name] [phone]"""
    if len(args) < 2:
        return "Неправильний формат. Використання: add [ім'я] [номер]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """Змінює номер телефону для існуючого контакту."""
    if len(args) < 2:
        return "Неправильний формат. Використання: change [ім'я] [новий номер]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    """Показує номер телефону за іменем."""
    if len(args) < 1:
        return "Неправильний формат. Використання: phone [ім'я]"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."


def show_all(contacts):
    """Виводить усі збережені контакти."""
    if not contacts:
        return "No contacts saved."
    result = ["All contacts:"]
    for name, phone in contacts.items():
        result.append(f"  {name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


