# Даны такие списки:

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students = ', '.join(students)
subjects = ', '.join(subjects)

print(students)
print(subjects)
print(f'Students {students} study these {subjects}')