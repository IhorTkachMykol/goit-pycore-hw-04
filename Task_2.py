def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # пропуск порожніх рядків
                if not line:
                    continue

                try:
                    cat_id, name, age = line.split(",")
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    # якщо формат рядка неправильний
                    print(f"Пропущено некоректний рядок: {line}")
                    continue

        return cats

    except FileNotFoundError:
        print("Файл не знайдено!")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None
cats_info = get_cats_info("cats.txt")
print(cats_info)
