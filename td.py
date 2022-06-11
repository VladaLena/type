# Последовательность - это итерируемый объект, к которому можно обратиться по целочисленному индексу,
# а также узнать длину последовательности при помощи функции len()

# Итерируемый объект - это объект, к котрому можо обратиться по магическому методу __iter__,
# который возврвщает итератор. В свою очередь, к итератору можно обратиться по магическому методу
# __next__, который возвращает элементы итерируемого объекта по порядкуб а по окончании выдает
# исключение StopIteration
 
# Последовательности: str, list, tuple
# Отображение: dict
# Множество: set (уникальные элементы)

# Итерируемые:
# l = [1, 2, 3, 4, 'list']
# st = 'python'
# t = (1, 1.3, 'tuple')
# d = {1: 'o', 2: 't', 3: 't'}
# se = (5, 3.9, 'set')

# iterator = l.__iter__()
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

# for i in l:
#     print(i)


# Упорядоченные
# s = 'string'
# print(s[2])
# l = [0, 1, 2, 3]
# print(l[0])
# d = {1: 'o', 2: 't', 4: 'f'}   # начиная с версии 3.6
# print(d[1])
# t = (1, 2, 'tuple')
# print(t[1])

# Неупорядоченные
# se = {'r', 'o', 100, 'set'}
# print(se)
# d = {1: 'o', 2: 't', 4: 'f'}   # до версии 3.6
# print(d)


# Изменяемые:
# l = [0, 1, 2, 3]
# l[0] = 100
# print(l)
# d = {1: 'o', 2: 't', 4: 'f'}
# d[1] = 'five'
# print(d)
# se = {'r', 'o', 100, 'set'}
# se.add('open')
# print(se)

# Неизменяемые
# s = 'string'
# s[0] = 'l'
# TypeError: 'str' object does not support item assignment
# t = (1, 2, 'tuple')
# t[0] = '15'
# TypeError: 'tuple' object does not support item assignment

# Общие операции с последовательностями(на примере list):
# l = [0, 1, 2, 3, 4, 5, 8, 0, 0, 0]    
# print(1 in l)      
# l1 = l + [0, 3]     
# print(l1)
# print(l * 3)    
# print(l[2])
# print(l1[0:3:2])
# print(len(l1))
# print(min(l))
# print(max(l))
# print(l.index(3))
# print(l.count(0))   
# print(sum(l))










