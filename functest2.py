def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    return None


print_params()
print_params(2 + int('3'), 'str', False)
print_params(b=25)
print_params(c=[1,2,3])


values_list = [10, 'second', True]
unpacking_1 = print_params(*values_list)


values_dict = {'a': 3, 'b': 'something', 'c': False}
unpacking_2 = print_params(**values_dict)


values_list_2 = [25, 'hello']
print_params(*values_list_2, 42)







