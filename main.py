print("ЛАСКАВО ПРОСИМО")



my_list = [1, 2, 3, 4, 5, 7, 6, 7, 8, 9, 3, 6, 7, 8 ]
my_count = my_list.count(7)
print(my_count)
my_list.sort(reverse =True)
print(my_list)

chars = ["яблуко", "апельсин", "банан"]
new_chars = chars.reverse()
print(chars)

my_dict = {'age': 25, 'name': 'Vlados', 'city': 'Lublin'}
my_dict["emeil"] = "vladosik@gmail.com"

del my_dict["age"]

print(my_dict)

print("name" in my_dict)
print("age" in my_dict)

my_dict.update({'age': 26, 'name': 'Vlados', 'city': 'Lublin', "emeil": "vladosik@gmail.com"})

new_dict = my_dict.copy()
del new_dict["age"]

print(my_dict)
print(new_dict)

lst = [1, 2, 3, 4, 5, 6, 2, 2, 4, 3, 4, 6, 5, 5]
d_lst = set(lst)
lst = list(d_lst)

print(d_lst)
print(lst)

nambers = {1, 2, 3, 4, 5}
nambers.add(7)
print(nambers)

nambers = {1, 2, 3, 4, 5}
nambers.remove(5)
print(nambers)

nambers = {1, 2, 3, 4, 5}
nambers.discard(4)
print(nambers)

a = {1, 2, 3}
b= {4, 5, 3}
print(a.intersection(b))
print(a & b)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.difference(b))
print(a - b)

print(a.symmetric_difference(b))
print(a ^ b)

print(a.union(b))
print(a | b)

s = "Pryvit"
print(s.upper())

name = 'Vlados'
print('Hello, {}!'.format(name))

age = 25
print('Hello, {}! you are {} yesr old'.format(name, age))

print('Hello, {name}! you are {age} yesr old'.format(name = 'Vladik', age = 17))

print('Hello, {1}! you are {0} yesr old'.format(age, name))

s = 'Hello, World!'
first_file = s[6:13]
print(first_file)

nambers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_nambers = nambers[0:10:2]
print(odd_nambers)

nambers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nambers = nambers[1:10:2]
print(even_nambers)

nambers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_nambers = nambers[::-1]
print(reversed_nambers)

nambers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_nambers = nambers[:]
print(copy_nambers)