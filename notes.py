def main():
    while True:
        show_menu()
        choice = int(input("Ваш выбор: "))
        if choice == 1:
            try:
                show_data()
            except FileNotFoundError:
                print("Файл не создан")
        elif choice == 2:
            data = input("Введите данные: ")
            save_data(data)
        elif choice == 3:
            data = input("Введите ключевое слово заметки: ")
            new_data = input("Введите новые данные: ")
            change_data(data, new_data)
        elif choice == 4:
            data = input("Введите ключевое слово заметки: ")
            delete_data(data)
            print("Данные удалены")
        else:
            break


def show_menu():
    print("Нажмите 1, чтобы посмотреть все данные")
    print("Нажмите 2, чтобы добавить данные")
    print("Нажмите 3, чтобы изменить данные")
    print("Нажмите 4, чтобы удалить данные")
    print("Нажмите 5, чтобы выйти из программы")


def show_data():
    print()
    with open("notes.txt", "r", encoding="utf-8") as file:
        print(file.read())
    print()


def save_data(stroka):
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(f"{stroka}\n")


def change_data(old, new):
    with open("notes.txt", "r", encoding="utf-8") as file:
        info = file.readlines()
    with open("notes.txt", "w", encoding="utf-8") as file:
        for line in info:
            if old.lower() not in line.lower():
                file.write(line)
            else:
                file.write(f"{new}\n")
                print("Данные изменены")


def delete_data(old):
    with open("notes.txt", "r", encoding="utf-8") as file:
        info = file.readlines()
    with open("notes.txt", "w", encoding="utf-8") as file:
        for line in info:
            if old.lower() not in line.lower():
                file.write(line)
            else:
                file.write("")


def find_data(data):
    result = []
    with open("notes.txt", "r", encoding="utf-8") as file:
        info = file.readlines()
        for line in info:
            if data.lower() in line.lower():
                result.append(line)
    return result


main()