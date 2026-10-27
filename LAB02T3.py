import csv
import random

filename = "books.csv"
output_filename = "res.txt"

all_books = []


with open(filename, mode="r", encoding="cp1251") as file:
    reader = csv.reader(file, delimiter=";")
    next(reader) 

    for row in reader:
        if len(row) >= 7:
            title = row 
            author = row   
            date_field = row  


            if "." in date_field:
                year = date_field.split(".")[2].split()[0]
            else:
                year = "Неизвестно"

            all_books.append({
                "author": author,
                "title": title,
                "year": year
            })

sample_size = min(20, len(all_books))
random_books = random.sample(all_books, sample_size)

with open(output_filename, mode="w", encoding="cp1251") as out_file:
    # Использование enumerate(..., start=1) сразу дает нумерацию с единицы
    for index, book in enumerate(random_books, start=1):
        # Формируем строку по заданию: <автор>. <название> - <год>
        link = f"{index}. {book['author']}. {book['title']} - {book['year']}\n"
        out_file.write(link)

print(f"Задание 3 выполнено! Список из {sample_size} случайных ссылок сохранен в: {output_filename}")
