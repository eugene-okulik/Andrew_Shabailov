import datetime as dt


current_date = "Jan 15, 2023 - 12:05:33"
p_date = dt.datetime.strptime(current_date, '%b %d, %Y - %H:%M:%S')

print(p_date.strftime('%B'))
print(p_date.strftime('%d.%m.%Y, %H:%M'))
