import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl',
)

cursor = db.cursor(dictionary=True)

query_1 = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
values_1 = ('Andrew_5', 'Shabailov_5')
cursor.execute(query_1, values_1)
student_id = cursor.lastrowid
print(f'student_id: {student_id}')
db.commit()

query_2 = "INSERT INTO `groups` (title, start_date, end_date ) VALUES (%s, %s, %s)"
group_values = ('bright sun', '2 Mar', '29 Nov')
cursor.execute(query_2, group_values)
group_id = cursor.lastrowid
print(f'group_id: {group_id}')
db.commit()

query_3 = cursor.execute(f"UPDATE students SET group_id = '{group_id}' WHERE id = {student_id}")
db.commit()

query_4 = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(query_4, [
    ('fantasy', student_id),
    ('love', student_id),
    ('money', student_id)
])

db.commit()

subject_query = "INSERT INTO subjects (title) VALUES (%s)"
subjects = ['fantasy', 'history', 'oop']
subject_ids = {}

for title in subjects:
    cursor.execute(subject_query, (title,))
    subject_ids[title] = cursor.lastrowid

db.commit()
print(f'subject id: {', '.join(f"{k} - {v}" for k, v in subject_ids.items())}')

lesson_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"

data = [
    ('mat1', subject_ids['fantasy']),
    ('mat2', subject_ids['history']),
    ('mat3', subject_ids['oop']),
]

lesson_ids = {}

for title, subject_id in data:
    cursor.execute(lesson_query, (title, subject_id))
    lesson_ids[title] = cursor.lastrowid

db.commit()
print(f'lesson id: {', '.join(f"{k} - {v}" for k, v in lesson_ids.items())}')

query_11 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(query_11, [
    ('8', lesson_ids['mat1'], student_id),
    ('3', lesson_ids['mat2'], student_id),
    ('5', lesson_ids['mat3'], student_id),
])

db.commit()

query_12 = f"SELECT * FROM marks where student_id = {student_id}"
cursor.execute(query_12)
all_students_marks = cursor.fetchall()
marks = [mark['value'] for mark in all_students_marks]
print(f"Student marks: {', '.join(marks)}")

query_13 = f"SELECT * FROM books where taken_by_student_id = {student_id}"
cursor.execute(query_13)
all_students_books = cursor.fetchall()
titles = [book['title'] for book in all_students_books]
print(f"Student books: {', '.join(titles)}")

query_14 = """
SELECT
    s.id AS Id,
    s.name AS Name,
    s.second_name AS 'Last Name',
    g.title AS 'Group',
    GROUP_CONCAT(DISTINCT b.title) AS Books,
    GROUP_CONCAT(DISTINCT m.value) AS Marks

FROM students s

LEFT JOIN `groups` g
    ON g.id = s.group_id

LEFT JOIN books b
    ON b.taken_by_student_id = s.id

LEFT JOIN marks m
    ON m.student_id = s.id

WHERE s.id = %s

GROUP BY s.id, s.name, s.second_name, g.title
"""
cursor.execute(query_14, (student_id,))
result = cursor.fetchone()

print(f"""
Student: {result['Name']} {result['Last Name']}
Group: {result['Group']}
Books: {result['Books']}
Marks: {result['Marks']}
""")

db.close()
