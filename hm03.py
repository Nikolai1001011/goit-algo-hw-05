def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Invalid command. Enter a valid command."
        except ValueError:
            return "Invalid command. Give me name and phone please."
        except IndexError:
            return "Invalid command. Enter a valid command."

    return inner

# Функція додавання контакту
@input_error
def add_contact(args, contacts):
    name, phone = args
    # Перевірка чи ім'я контакту вже існує
    if name in contacts:
        return "Invalid command. Contact already exists."
    else:
        contacts[name] = phone
        return "Contact added."

# Функція зміни номера телефону
@input_error
def change_contact(args, contacts):
    name, phone = args
    # Перевірка чи ім'я контакту вже існує
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Invalid command. Contact does not exist."

# Функція виведення номера телефону
@input_error
def phone_contact(args, contacts):
    name = args[0]
    # Перевірка чи ім'я контакту існує
    if name in contacts:
        return contacts[name]
    else:
        return "Invalid command. Contact does not exist."

# Функція виведення всіх контактів
@input_error
def all_contacts(args, contacts):
    # Перевірка чи список контактів не порожній
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "Contact list is empty."

# Функція завершення роботи
def exit_program():
    return "Good bye!"

# Головна функція
def main():
    # Словник для зберігання контактів
    contacts = {}
    # Список доступних команд
    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": phone_contact,
        "all": all_contacts,
        "exit": exit_program
    }

    # Початок безкінечного циклу
    while True:
        # Зчитування команди з консолі
        command = input("Enter a command: ").strip().lower()
        # Розбивка команди на частини
        parts = command.split()
        # Перевірка чи команда відповідає доступним
        if parts[0] in commands:
            # Виклик відповідної функції для обробки команди
            result = commands[parts[0]](parts[1:], contacts)
            # Виведення результату роботи функції
            print(result)
            # Перевірка чи команда завершує програму
            if parts[0] == "exit":
                break
        else:
            # Виведення повідомлення про недійсну команду
            print("Invalid command. Enter a valid command.")

# Виклик головної функції
if __name__ == "__main__":
    main()