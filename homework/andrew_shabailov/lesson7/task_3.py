def string_rework(inp):
    index = inp.index(':') + 1
    res = inp[index::].lstrip()
    num = int(res) + 10
    print(num)

string_rework('результат операции: 42')
string_rework('результат операции: 54')
string_rework('результат работы программы: 209')
