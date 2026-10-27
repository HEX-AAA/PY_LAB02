'''Используя приложенный файл books.csv ИЛИ books-en.csv, выполнить следующее:

    1)Вывести количество записей, у которых в поле Название 
    строка длиннее 30 символов.
    2)Реализовать поиск книги по автору, использовать ограничение
    на выдачу в зависимости от варианта. 
    Реализовать генератор библиографических ссылок вида <автор>.
    <название> - <год> для 20 записей. Записи выбрать произвольно.
    Список сохраняется как отдельный файл текстового формата с нумерацией строк.

'''

import csv

filename = "books.csv"

long_titles_count = 0
#r - read
with open(filename, mode="r", encoding="cp1251") as bookfile:
    reader = csv.reader(bookfile, razdelitel=";")
    next(reader) #SKIP THE FIRST SENTENCE

    for row in reader:
        if len(row) >= 2:
            title = row[1] 
            if len(title) > 30:
                long_titles_count += 1



print(
    # 1)
    f"Количество записей с названием длиннее 30 символов: {long_titles_count}"
    #2)

)
