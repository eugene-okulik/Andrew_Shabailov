import csv
import os
from secrets import cursor


base_dir = os.path.dirname(__file__)
home_dir = os.path.dirname(os.path.dirname(base_dir))
eugene_dir = os.path.join(home_dir, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

sql = """
SELECT
    s.name,
    s.second_name,
    g.title      AS group_title,
    b.title      AS book_title,
    sub.title    AS subject_title,
    l.title      AS lesson_title,
    m.value      AS mark_value
FROM students s
JOIN `groups` g
    ON s.group_id = g.id
JOIN books b
    ON b.taken_by_student_id = s.id
JOIN marks m
    ON m.student_id = s.id
JOIN lessons l
    ON m.lesson_id = l.id
JOIN subjects sub
    ON l.subject_id = sub.id
WHERE
    s.name = %s
    AND s.second_name = %s
    AND g.title = %s
    AND b.title = %s
    AND sub.title = %s
    AND l.title = %s
    AND m.value = %s
"""


with open(eugene_dir, 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        cursor.execute(
            sql,
            (
                row['name'],
                row['second_name'],
                row['group_title'],
                row['book_title'],
                row['subject_title'],
                row['lesson_title'],
                row['mark_value'],
            )
        )

        if cursor.fetchone() is None:
            print(f'Нет в базе: {dict(row)}')

cursor.close()
