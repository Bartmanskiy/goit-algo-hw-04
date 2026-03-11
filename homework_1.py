from pathlib import Path

def total_salary(path):
    salaries = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
             content = [element.strip().split(",") for element in file.readlines()]
             for employer in content: 
                 salary = float(employer[1].strip())
                 salaries.append(salary)
        total = sum(salaries)
        average = total / len(salaries)
        return total, average
    except FileNotFoundError:
        print('Файл не знайдено')
        return 0, 0
    except Exception:
        print('Файл пошкоджено')
        return 0, 0

total, average = total_salary("D:\Projects\goit-algo-hw-04\salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
