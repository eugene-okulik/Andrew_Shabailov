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
values_1 = ('Andrew_2', 'Shabailov_2')
cursor.execute(query_1, values_1)
db.commit()

cursor.execute("SELECT * FROM students ORDER BY id DESC LIMIT 1")
student_id = cursor.fetchone()['id']

query_2 = "INSERT INTO `groups` (title, start_date, end_date ) VALUES (%s, %s, %s)"
group_values = ('lifebalance', '2 Mar', '29 Nov')
cursor.execute(query_2, group_values)
db.commit()

cursor.execute("SELECT * FROM `groups` ORDER BY id DESC LIMIT 1")
group_id = cursor.fetchone()['id']

query_3 = cursor.execute(f"UPDATE students SET group_id = '{group_id}' WHERE id = {student_id}")
db.commit()

query_4 = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
book_1 = 'history'
book_2 = 'mistery'
book_3 = 'luxury'
book_value_1 = (book_1, student_id)
book_value_2 = (book_2, student_id)
book_value_3 = (book_3, student_id)
cursor.execute(query_4, book_value_1)
cursor.execute(query_4, book_value_2)
cursor.execute(query_4, book_value_3)
db.commit()

query_5 = "INSERT INTO subjects (title) VALUES (%s)"
subject_1 = ('colors',)
subject_2 = ('flowers',)
subject_3 = ('sweets',)
cursor.execute(query_5, subject_1)
cursor.execute(query_5, subject_2)
cursor.execute(query_5, subject_3)
db.commit()

cursor.execute("SELECT * FROM subjects ORDER BY id DESC LIMIT 3")
data = cursor.fetchall()
subject_id_1, subject_id_2, subject_id_3 = [item['id'] for item in data]

query_6 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_value_1 = ('mat1', subject_id_1)
lesson_value_2 = ('mat2', subject_id_2)
lesson_value_3 = ('mat3', subject_id_3)
cursor.execute(query_6, lesson_value_1)
cursor.execute(query_6, lesson_value_2)
cursor.execute(query_6, lesson_value_3)
db.commit()

cursor.execute("SELECT * FROM lessons ORDER BY id DESC LIMIT 3")
data = cursor.fetchall()
lesson_id_1, lesson_id_2, lesson_id_3 = [item['id'] for item in data]

query_7 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
mark_value_1 = (9, lesson_id_1, student_id)
mark_value_2 = (8, lesson_id_2, student_id)
mark_value_3 = (7, lesson_id_3, student_id)
cursor.execute(query_7, mark_value_1)
cursor.execute(query_7, mark_value_2)
cursor.execute(query_7, mark_value_3)
db.commit()

db.close()
