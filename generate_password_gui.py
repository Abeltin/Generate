import tkinter as tk
from generate_password import generate_password
import pyodbc

# Настройка подключения к базе данных SQL Server
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=KOMPUTER;'
    'Database=generate;'
    'UID=sa;'
    'PWD=sa;'
)


# Определяем функцию, которая создает пользовательский интерфейс для генерации пароля
def generate_password_gui():
    root = tk.Tk()
    root.title("Генератор паролей")

    # Задаем фиксированный размер окна
    root.resizable(width=False, height=False)

    # Задаем размеры окна
    width = 300
    height = 300
    root.geometry('{}x{}'.format(width, height))

    # Центрируем окно на экране
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry('+{}+{}'.format(x, y))

    # Добавляем элементы пользовательского интерфейса
    platform_label = tk.Label(root, text="Платформа:")
    platform_label.pack()
    platform_entry = tk.Entry(root)
    platform_entry.pack()

    login_label = tk.Label(root, text="Логин:")
    login_label.pack()
    login_entry = tk.Entry(root)
    login_entry.pack()

    length_label = tk.Label(root, text="Длина пароля:")
    length_label.pack()
    length_entry = tk.Entry(root)
    length_entry.pack()

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

    password_label = tk.Label(root, text="")
    password_label.pack()

    # Определяем функцию, которая будет вызвана при нажатии на кнопку "Сгенерировать"
    def generate_button_clicked():
        platform = platform_entry.get()
        login = login_entry.get()
        length = int(length_entry.get())
        uppercase = uppercase_var.get()
        lowercase = lowercase_var.get()
        digits = digits_var.get()
        symbols = symbols_var.get()

        # Генерируем пароль с заданными параметрами и выводим его на экран
        password = generate_password(length, uppercase, lowercase, digits, symbols)
        password_label.config(text=password)

        # Сохраняем платформу, логин и пароль в базу данных
        save_to_database(platform, login, password)

    generate_button = tk.Button(root, text="Сгенерировать", command=generate_button_clicked)
    generate_button.pack()

    # Запускаем главный цикл обработки событий пользовательского интерфейса
    root.mainloop()


# Функция для сохранения данных в базу данных
def save_to_database(platform, login, password):
    # Создаем объект-курсор для выполнения SQL-запросов
    cursor = conn.cursor()

    # Формируем SQL-запрос для вставки данных в таблицу
    query = "INSERT INTO passwords (platform, login, password) VALUES (?, ?, ?)"

    # Выполняем SQL-запрос с передачей параметров
    cursor.execute(query, (platform, login, password))

    # Подтверждаем изменения в базе данных
    conn.commit()

    # Закрываем курсор
    cursor.close()
