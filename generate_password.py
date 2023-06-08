import random
import string

# Определяем функцию, которая генерирует пароль с заданными параметрами
def generate_password(length, uppercase, lowercase, digits, symbols):
    # Строка, содержащая все необходимые символы для генерации пароля
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    # Генерируем пароль длиной length из заданных символов
    password = "".join(random.choice(characters) for _ in range(length))
    return password
