def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    # print(a, b) #Для вызова с разным количеством аргументов
    # print(a)
    # print()
    
values_list = [55 , 'abc', True]
values_dict = {'a': 22, 'b': 'cba', 'c': False}
values_list_2 = [54.32, 'Строка']

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
