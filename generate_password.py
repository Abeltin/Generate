import random
import string
# определяем функцию, которая генерирует пароль с заданными параметрами
def generate_password(length, uppercase, lowercase, digits, symbols):
    # Генерация пароля с заданными параметрами
    # строка, содержащая все необходимые символы для генерации пароля
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    # генерируем пароль длиной length из заданных символов
    password = "".join(random.choice(characters) for _ in range(length))
    return password