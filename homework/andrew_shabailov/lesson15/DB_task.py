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

query_5 = "INSERT INTO subjects (title) VALUES (%s)"
sub_title_1 = ('fantasy',)
cursor.execute(query_5, sub_title_1)
subject_id_1 = cursor.lastrowid
print(f'subject_id_1: {subject_id_1}')
db.commit()

query_6 = "INSERT INTO subjects (title) VALUES (%s)"
sub_title_2 = ('history',)
cursor.execute(query_6, sub_title_2)
subject_id_2 = cursor.lastrowid
print(f'subject_id_2: {subject_id_2}')
db.commit()

query_7 = "INSERT INTO subjects (title) VALUES (%s)"
sub_title_3 = ('oop',)
cursor.execute(query_7, sub_title_3)
subject_id_3 = cursor.lastrowid
print(f'subject_id_3: {subject_id_3}')
db.commit()

query_8 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_value_1 = ('mat1', subject_id_1)
cursor.execute(query_8, lesson_value_1)
lesson_id_1 = cursor.lastrowid
print(f'lesson_id_1: {lesson_id_1}')
db.commit()

query_9 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_value_2 = ('mat2', subject_id_2)
cursor.execute(query_9, lesson_value_2)
lesson_id_2 = cursor.lastrowid
print(f'lesson_id_2: {lesson_id_2}')
db.commit()

query_10 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_value_3 = ('mat3', subject_id_3)
cursor.execute(query_10, lesson_value_3)
lesson_id_3 = cursor.lastrowid
print(f'lesson_id_3: {lesson_id_3}')
db.commit()

query_11 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(query_11, [
    ('8', lesson_id_1, student_id),
    ('3', lesson_id_2, student_id),
    ('5', lesson_id_3, student_id),
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
