PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


new_list1 = list(map(lambda x: x.strip(), PRICE_LIST.split()))

key = new_list1[0::2]
values = [int(x.rstrip('р')) for x in new_list1[1::2]]

new_dict = dict(zip(key, values))
print(new_dict)
