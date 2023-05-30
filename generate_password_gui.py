import tkinter as tk
from generate_password import generate_password  # Импорт функции генерации пароля
from save_to_file import save_to_file  # Импорт функции сохранения в файл

def generate_password_gui():
    # Создание графического интерфейса приложения для генерации паролей
    root = tk.Tk()
    root.title("Генератор паролей")

    width = 300
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # Создание метки и поля для ввода длины пароля
    length_label = tk.Label(root, text="Длина пароля:")
    length_label.pack()
    length_entry = tk.Entry(root)
    length_entry.pack()

    # Создание метки и поля для ввода платформы
    platform_label = tk.Label(root, text="Платформа:")
    platform_label.pack()
    platform_entry = tk.Entry(root)
    platform_entry.pack()

    # Создание метки и поля для ввода логина
    login_label = tk.Label(root, text="Логин:")
    login_label.pack()
    login_entry = tk.Entry(root)
    login_entry.pack()

    # Создание флажков для выбора опций генерации пароля
    uppercase_var = tk.BooleanVar()
    uppercase_checkbutton = tk.Checkbutton(root, text="Верхний регистр", variable=uppercase_var)
    uppercase_checkbutton.pack()

    lowercase_var = tk.BooleanVar()
    lowercase_checkbutton = tk.Checkbutton(root, text="Нижний регистр", variable=lowercase_var)
    lowercase_checkbutton.pack()

    digits_var = tk.BooleanVar()
    digits_checkbutton = tk.Checkbutton(root, text="Цифры", variable=digits_var)
    digits_checkbutton.pack()

    symbols_var = tk.BooleanVar()
    symbols_checkbutton = tk.Checkbutton(root, text="Символы", variable=symbols_var)
    symbols_checkbutton.pack()

    # Создание метки для отображения сгенерированного пароля
    password_label = tk.Label(root, text="")
    password_label.pack()

    def generate_button_clicked():
        # Обработчик события нажатия на кнопку "Сгенерировать"
        length = int(length_entry.get())  # Получение длины пароля из поля ввода
        uppercase = uppercase_var.get()  # Получение значения флажка верхнего регистра
        lowercase = lowercase_var.get()  # Получение значения флажка нижнего регистра
        digits = digits_var.get()  # Получение значения флажка цифр
        symbols = symbols_var.get()  # Получение значения флажка символов
        password = generate_password(length, uppercase, lowercase, digits, symbols)  # Генерация пароля
        password_label.config(text=password)  # Отображение сгенерированного пароля в метке

    # Создание кнопки "Сгенерировать" и привязка обработчика события
    generate_button = tk.Button(root, text="Сгенерировать", command=generate_button_clicked)
    generate_button.pack()

    def save_button_clicked():
        # Обработчик события нажатия на кнопку "Сохранить"
        platform = platform_entry.get()  # Получение названия платформы из поля ввода
        login = login_entry.get()  # Получение логина из поля ввода
        password = password_label.cget("text")  # Получение сгенерированного пароля из метки
        save_to_file(platform, login, password)  # Сохранение платформы, логина и пароля в файл

    # Создание кнопки "Сохранить" и привязка обработчика события
    save_button = tk.Button(root, text="Сохранить", command=save_button_clicked)
    save_button.pack()

    root.mainloop()


