txt1 = 'результат операции: 42'
txt2 = 'результат операции: 514'
txt3 = 'результат работы программы: 9'

index_1 = txt1.index(':') + 1
index_2 = txt2.index(':') + 1
index_3 = txt3.index(':') + 1

res_1 = txt1[index_1::].lstrip()
res_2 = txt2[index_2::].lstrip()
res_3 = txt3[index_3::].lstrip()

num1 = int(res_1) + 10
num2 = int(res_2) + 10
num3 = int(res_3) + 10

print(num1)
print(num2)
print(num3)
