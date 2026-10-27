import csv

filename = "books.csv"
search_author = "Петрановская"  # Сюда можно вписать любого автора
price_limit = 200.0

print(f"Результаты поиска автора '{search_author}' стоимостью от {price_limit} руб.:")


with open(filename, mode="r", encoding="cp1251") as file:
    reader = csv.reader(file, delimiter=";")
    next(reader) 

    for row in reader:
        if len(row) >= 8:
            title = row[1]       
            author_fio = row[4]  
            price_raw = row[7]  

            try:
                price = float(price_raw.replace(",", "."))
            except ValueError:
                price = 0.0

            if search_author.lower() in author_fio.lower() and price >= price_limit:
                print(f"x {title} (Цена: {price} руб.)")
