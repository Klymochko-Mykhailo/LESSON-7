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
