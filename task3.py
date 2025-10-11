import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізуємо colorama для роботи кольорів у Windows
init(autoreset=True)

def print_directory_structure(path: Path, indent: str = ""):
    """Рекурсивно виводить структуру директорії з кольоровим форматуванням."""
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/") # Директорії – сині
                # Рекурсивний виклик для вкладених директорій
                print_directory_structure(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}") # Файли – зелені
    except PermissionError:
        print(f"{indent}{Fore.RED}[Доступ заборонено до: {path}]")

def main():
    # Перевірка наявності аргументу командного рядка
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python hw03.py <шлях_до_директорії>")
        sys.exit(1)

    # Отримуємо шлях з аргументів
    directory_path = Path(sys.argv[1])

    # Перевіряємо, чи існує шлях і чи це директорія
    if not directory_path.exists():
        print(f"{Fore.RED} Помилка: вказаний шлях не існує.")
        sys.exit(1)
    if not directory_path.is_dir():
        print(f"{Fore.RED} Помилка: шлях не веде до директорії.")
        sys.exit(1)

    # Виводимо заголовок
    print(f"{Fore.CYAN}{Style.BRIGHT}Структура директорії: {directory_path.resolve()}\n")

     # Викликаємо функцію рекурсивного обходу
    print_directory_structure(directory_path)
    
if __name__ == "__main__":
    main()
