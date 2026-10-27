import xml.etree.ElementTree as ET

filename = "currency.xml"

# Создаем пустые списки по условию Варианта 9
num_code_list = []
char_code_list = []

# Открываем и парсим XML-файл с правильной кодировкой windows-1251
tree = ET.parse(filename)
root = tree.getroot()

# Перебираем каждый тег <Valute> внутри файла
for valute in root.findall("Valute"):
    # Извлекаем текст из внутренних тегов
    num_code_raw = valute.find("NumCode").text
    char_code_raw = valute.find("CharCode").text
    nominal_raw = valute.find("Nominal").text
    value_raw = valute.find("Value").text

    # --- ПРИВЕДЕНИЕ ТИПОВ ---
    
    # 1. Цифровой код (NumCode) приводим к целому числу (int)
    num_code = int(num_code_raw)
    
    # 2. Буквенный код (CharCode) оставляем строкой (str)
    char_code = str(char_code_raw)
    
    # 3. Номинал приводим к целому числу (int)
    nominal = int(nominal_raw)
    
    # 4. Курс валюты (Value) переводим в дробное число (float), заменяя запятую на точку
    value = float(value_raw.replace(",", "."))

    # Добавляем полученные коды в наши два отдельных списка
    num_code_list.append(num_code)
    char_code_list.append(char_code)

# --- ВЫВОД РЕЗУЛЬТАТОВ НА ЭКРАН ---

print("Задание 4 успешно выполнено!")
print("-" * 50)
print(f"Список NumCode (тип элементов: int):\n{num_code_list}\n")
print(f"Список CharCode (тип элементов: str):\n{char_code_list}")
