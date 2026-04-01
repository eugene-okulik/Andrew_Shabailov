my_dict = {'tuple': 'tuple', 'list': 'list', 'dict': 'dict', 'set': 'set'}
print(my_dict)

my_dict['tuple'] = ('one', 2, 'three', 4, 'five',)
my_dict['list'] = ['first', 'second', 'third', 'fourth', '5']
my_dict['dict'] = {'car': 'blue', 'bus': 'orange', 'wi-fi': 'free', 'job': 'well-paid'}
my_dict['set'] = {1, 3.14, "hello", False, (1, 2, 3)}
print(my_dict)

last_tuple_item = my_dict['tuple'][-1]
print(last_tuple_item)

_list = my_dict['list']
_list.append('text')
print(_list)

popped = _list.pop(1)
print(popped)


list_dict = my_dict['dict']
list_dict[('i am a tuple',)] = 'fixed'
print(list_dict)

delete_item = list_dict.pop('bus')
print(delete_item)
print(list_dict)

set = my_dict['set']
set.add('line_22')
print(set)

deleted_set_item = set.pop()
print(deleted_set_item)
print(set)
