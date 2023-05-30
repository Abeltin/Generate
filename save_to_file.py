import os
def save_to_file(platform, login, password):
    # Сохранение платформы, логина и пароля в файл

    # Определение пути к папке для хранения файлов
    folder_path = "База паролей"

    # Проверка существования папки, и если она не существует, то создание её
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # Формирование пути к файлу с учетом названия платформы
    file_path = os.path.join(folder_path, f"{platform}.txt")

    # Открытие файла в режиме дозаписи и запись логина, пароля и перевода строки
    with open(file_path, "a") as file:
        file.write(f"Логин: {login}\n")
        file.write(f"Пароль: {password}\n")
        file.write("\n")