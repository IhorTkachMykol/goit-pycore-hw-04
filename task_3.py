import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama (для Windows та інших систем)
init(autoreset=True)

def print_tree(path: Path, indent: str = ""):
    """Рекурсивне виведення файлової структури."""
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/")
                print_tree(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}[Access Denied]")


def main():
    # Перевірка аргументів
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: потрібно вказати шлях до директорії.")
        print("Приклад: python tree_view.py C:/Users/Igor/Documents")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    # Перевірка існування шляху
    if not directory_path.exists():
        print(Fore.RED + "Помилка: вказаний шлях не існує.")
        sys.exit(1)

    # Перевірка чи це директорія
    if not directory_path.is_dir():
        print(Fore.RED + "Помилка: вказаний шлях не є директорією.")
        sys.exit(1)

    print(Fore.CYAN + f"Структура директорії: {directory_path}\n")
    print_tree(directory_path)


if __name__ == "__main__":
    main()
