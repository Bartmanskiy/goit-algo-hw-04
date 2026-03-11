from pathlib import Path

def get_cats_info(path):
    list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            info = [element.strip().split(',') for element in file.readlines()]
            for element in info:
                dict = {}
                dict["id"] = element[0]
                dict["name"] = element[1]
                dict["age"] = element[2]
                
                list.append(dict)
        
        return list

    except FileNotFoundError:
        print('Файл не знайдено')
        return []
    except Exception:
        print('Файл пошкоджено')
        return []


cats_info = get_cats_info("D:\Projects\goit-algo-hw-04\information_of_cats.txt")
for cat in cats_info:
    print(cat)
