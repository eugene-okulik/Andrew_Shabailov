import os
import datetime


base_dir = os.path.dirname(__file__)
home_dir = os.path.dirname(os.path.dirname(base_dir))
eugene_dir = os.path.join(home_dir, 'eugene_okulik', 'hw_13', 'data.txt')


with open(eugene_dir, 'r', encoding='utf-8') as eugene_file:
    new_data = [line.strip() for line in eugene_file]


date_str1 = new_data[0].split()[2]
date_str2 = new_data[1].split()[2]
date_str3 = new_data[2].split()[2]

date_now = datetime.datetime.now()

d1 = datetime.datetime.strptime(date_str1, "%H:%M:%S.%f")
d2 = datetime.datetime.strptime(date_str2, "%H:%M:%S.%f")
d3 = datetime.datetime.strptime(date_str3, "%H:%M:%S.%f")

result1 = d1 - datetime.timedelta(days=7)
result2 = d2.strftime('%A')
result3 = date_now - d3

print(result1.time())
print(result2)
print(result3)
