import logging
from datetime import datetime

# Завдання 1

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d"
)

logging.info("Програма запущена")

# Завдання 2

def error_example():
    try:
        x = 10 / 0
    except Exception as e:
        logging.error(f"Сталася помилка: {e}")

error_example()

# Завдання 3

def login(username, password):
    try:
        assert username == "kiril" and password == "1234", \
            "Невірне ім'я користувача або пароль"
        print("Вхід виконано успішно")
    except AssertionError as e:
        print(e)

login("kiril", "1234")
login("user", "0000")

# Завдання 4

def check_age(age):
    try:
        assert age >= 18, "Вам має бути 18 років або більше"
        print("Ви можете використовувати цей сервіс")
    except AssertionError as e:
        print(e)

check_age(20)
check_age(15)

# Завдання 5

def process_list(input_list):
    try:
        assert len(input_list) >= 3, \
            "Список повинен містити принаймні 3 елементи"
        print(f"Список містить {len(input_list)} елементів")
    except AssertionError as e:
        print(e)

process_list([1, 2, 3, 4])
process_list([1])
