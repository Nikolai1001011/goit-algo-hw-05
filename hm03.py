from collections import UserDict

# Базовий клас для полів запису
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для зберігання імені контакту, наслідується від Field
class Name(Field):
    pass

# Клас для зберігання номера телефону з валідацією формату (10 цифр), наслідується від Field
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

# Клас для зберігання інформації про контакт
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # Додавання телефону до списку
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    # Видалення телефону зі списку
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    # Редагування телефону (замінює старий номер новим)
    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    # Перетворення об'єкта на рядок для зручного відображення
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# Клас для зберігання та управління записами, наслідується від UserDict
class AddressBook(UserDict):
    # Додавання запису до адресної книги
    def add_record(self, record):
        self.data[record.name.value] = record

    # Пошук запису за ім'ям
    def find(self, name):
        return self.data[name]

    # Видалення запису за ім'ям
    def delete(self, name):
        del self.data[name]

# Декоратор для обробки помилок введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return inner

# Функція для додавання контакту
@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name].add_phone(phone)
    else:
        record = Record(name)
        record.add_phone(phone)
        contacts.add_record(record)
    return "Contact added."

# Функція для пошуку контакту за ім'ям
@input_error
def find_contact(args, contacts):
    name = args[0]
    record = contacts.find(name)
    return str(record)

# Функція для видалення контакту за ім'ям
@input_error
def delete_contact(args, contacts):
    name = args[0]
    contacts.delete(name)
    return "Contact deleted."

# Функція для виведення всіх контактів
@input_error
def show_all(args, contacts):
    result = []
    for name, record in contacts.items():
        result.append(str(record))
    return '\n'.join(result)

# Основний цикл програми
def main():
    contacts = AddressBook()

    while True:
        command = input("Enter a command: ").lower()
        if command == "exit":
            break
        elif command == "add":
            args = input("Enter the argument for the command (name phone): ").split()
            print(add_contact(args, contacts))
        elif command == "phone":
            args = input("Enter the name for the command: ").split()
            print(find_contact(args, contacts))
        elif command == "delete":
            args = input("Enter the name for the command: ").split()
            print(delete_contact(args, contacts))
        elif command == "all":
            print(show_all([], contacts))
        else:
            print("Unknown command. Please use add, phone, delete, all or exit.")
if __name__ == "__main__":
    main()
