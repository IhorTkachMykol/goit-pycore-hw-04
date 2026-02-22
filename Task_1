def total_salary(path):
    try:
        total = 0
        count = 0

        # читаємо файл
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # пропускаємо порожні рядки
                if not line:
                    continue

                # розділяємо ім'я та зарплату
                try:
                    name, salary = line.split(",")
                    total += int(salary)
                    count += 1
                except ValueError:
                    # якщо рядок має неправильний формат
                    print(f"Пропущено некоректний рядок: {line}")
                    continue

        if count == 0:
            return 0, 0

        average = total / count
        return total, average

    except FileNotFoundError:
        print("Файл не знайдено!")
        return None, None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None, None
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
