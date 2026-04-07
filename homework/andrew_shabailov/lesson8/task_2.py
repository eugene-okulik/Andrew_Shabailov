def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


num = {5, 200, 1000, 100000}
max_num = max(num)
count = 0


for value in fibonacci():
    count += 1
    if count in num:
        print(value)
    if count == max_num:
        break
