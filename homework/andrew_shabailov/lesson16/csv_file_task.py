import csv
from pathlib import Path
from secrets import get_cursor

file_path = Path(
    r'D:\projects\homework\homework\eugene_okulik\Lesson_16\hw_data\data.csv'
)

def print_missing(cursor, table, field, value):
    cursor.execute(
        f"SELECT 1 FROM `{table}` WHERE `{field}` = %s LIMIT 1",
        (value,)
    )
    if cursor.fetchone() is None:
        print(f'Нет в базе: {table}.{field} = {value}')

db, cursor = get_cursor()

with open(file_path, newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        name = row['name']
        group_title = row['group_title']
        book_title = row['book_title']
        subject_title = row['subject_title']
        lesson_title = row['lesson_title']
        mark_value = row['mark_value']

        print_missing(cursor, 'students', 'name', name)
        print_missing(cursor, 'groups', 'title', group_title)
        print_missing(cursor, 'books', 'title', book_title)
        print_missing(cursor, 'subjects', 'title', subject_title)
        print_missing(cursor, 'lessons', 'title', lesson_title)
        print_missing(cursor, 'marks', 'value', mark_value)

cursor.close()
db.close()
