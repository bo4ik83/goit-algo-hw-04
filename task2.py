def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # Прибираємо зайві пробіли та символи переносу рядка
                line = line.strip()
                if not line: # Пропускаємо порожні рядки
                    continue

                # Пропускаємо порожні рядки
                parts = line.split(",")
                if len(parts) != 3:
                    print(f"Неправильний формат рядка: {line}")
                    continue

                cat_id, name, age = parts

                # Формуємо словник
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat_info)

        return cats
    
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return[]
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []
    
# Приклад використання:
cats_info = get_cats_info("cats.txt")
print(cats_info)
