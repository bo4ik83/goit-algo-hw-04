def total_salary(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        total = 0.0
        count = 0

        for line in lines:
            line = line.strip()
            if not line: # Пропускаємо порожні рядки
                continue

            try:
                name, salary = line.split(",")
                total += int(salary)
                count += 1
            except ValueError:
                print(f"Помилка у рядку: {line}")
                continue

        if count == 0:
            return (0.0, 0.0)
        
        average = total / count
        return (total, average)
    
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return (0.0, 0.0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0.0, 0.0)

# Приклад використання:
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}") 