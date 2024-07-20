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

if age >= 26 :
    print('loL')
else:
    print('KEK')

a = input('Введіть число')
a = int(a)
if a > 0:
    print('Число додатне')
elif a < 0:
    print("Число від'ємне")
else:
    print('Це число - нуль')

first_name = "Vladyslav"
last_name = "Hakov"
full_name = first_name + " " + last_name
print(full_name)

name: str = "Vlad"
age: int = 25
height: float = 1.83
is_student: bool = True
has_high_degree: None = None

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

fruit = "apple"

print(f"Fruit: {fruit}")

massege = "Name: {}, Age: {}, Height: {}, Student: {}".format(name, age, height, is_student)
print(f"Massege: {massege}")

width = 10
height = 5

area = width * height
perimeter = 2 * (width + height)

print(f"Perimeter: {perimeter}")
print(f"Area: {area}")

height = int(25.0)

print(type(name), type(age), type(height), type(is_student))

value_one =5
value_two = 7

print("Equals", value_one == value_two)
print("Equals", value_one != value_two)
print("Equals", value_one >= value_two)
print("Equals", value_one <= value_two)
print("Equals", value_one < value_two)
print("Equals", value_one > value_two)

sentence_one = "Hello world"
sentence_two = "Hello " + "world"

print(sentence_one, sentence_two, sep='\n')

print(f"Are sentence equal? {sentence_one == sentence_two}")
print(f"Are sentence identical? {sentence_one is sentence_two}")

print(f"Path of sentence in memory {id(sentence_one)}")
print(f"Path of sentence in memory {id(sentence_two)}")

entertaiment = input("Enter entertainment: ")
print(f"Enter entertainment: {entertaiment}")

FLOORS = 5
APARTMENTS_PER_FLOOR = 4
apartament_number = int(input("Enter apartament number: "))
apartament_per_entrance = FLOORS * APARTMENTS_PER_FLOOR
antrance_number = (apartament_number - 1) // apartament_per_entrance + 1
floor_number = ((apartament_number - 1) % apartament_per_entrance) // APARTMENTS_PER_FLOOR + 1
print(f"Entrance number: {antrance_number}, floor number: {floor_number}")

my_liast = [1, True, 2345, "fruits", None, 1.83]
print(my_liast)
user = ["Vlad", "Hako"]
print(user[1], user[0], sep="\t")

my_liast = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -432, -30, 0]

my_liast.append(220)
print(my_liast)

print(my_liast[8])

my_liast.insert(3, -88)
print(my_liast)

my_liast.pop()
print(my_liast)

my_liast.remove(-88)
print(my_liast)

my_liast = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -432, -30, 0]

new_list = [ "loop", "start"]

print(my_liast, new_list, sep="\n")
my_liast.extend(new_list)
print(my_liast)

my_liast.append(new_list)
print(my_liast)

my_liast = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -432, -30, 0]

print(my_liast.index(8))

my_liast.insert(my_liast.index(8), 20)
print(my_liast)

my_liast[my_liast.index(7)] = None
print(my_liast)

my_liast[5] = "LOL"
print(my_liast)

old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -432, -30, 0]

new_list = old_list.copy()

print(old_list, new_list, sep="\n")

new_list.append(6)
print(old_list, new_list, sep="\n")

old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -432, -30, 0]

sorted_list = sorted(old_list.copy())
print(sorted_list)

old_list.sort()
print(old_list)

old_list.sort(reverse = True)
print(old_list)

old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -432, -30, 0]

print(sorted(old_list[::-1]))

old = [1, 2, 3, 4, 5, 6, 7, 8]
print(old == old[::-1])
new = [8, 7, 6, 5, 5, 6, 7, 8]
print(new == new[::-1])

print(old_list[::-1])
print(old_list[-1])
print(old_list[3:])
print(old_list[:6:])
print(old_list[2:10:])
print(old_list[:6:-1])
print(old_list[:19:2])
print(old_list[::])
print(old_list[::-1])

my_list = [[1,2,3,4,5,6,7,8,9], [23,35,57,789,56,68,45,234,123], [-1,-2,-3,-4,-5,-6,-7,-8,-9]]

print(my_list[1][1])
print(my_list[1][0:2])
print(my_list[2][::-1])
print(my_list[0][0:7])
print(len(my_list[1]))

person = {"name": "Vlad", "age": 22, "phone": "+4879138****", "student": True}

print(person)

new_data = {';ocation': 'Ukraine, Lviv', 'lang': 'ukr' }
person.update(new_data)

print(person)
print(person.get("name", "Noname"))
print(person.get("phone", None))
print(person.get("lang", None))
print(person.get("age", None))

person.pop("name")
print(person)

person["age"] = 25
print(person["age"])

person["test"] = True
print(person)

person.update({(1, ): False})
print(person)

dict_a = {'Alex':12, 'Olga':10}
dict_b = {'Boris':9, 'Kostya':10}
dict_c = {'Ira':11, 'Vova':6}

print(dict_a)
dict_a.update(dict_b)
print(dict_a)
dict_c.update(dict_a)
print(dict_c)
dict_a.update({"LOL":10})
print(dict_a)

person = {"name": "Vlad", "age": 22, "phone": "+4879138****", "student": True}

print(person)

person['test'] = person.pop('student')
print(person)

test = person.pop('test')
print(test)

my_set = {1,2,3,'test',5,'python',7,8,9}
print(my_set)

my_set.add('Test')
print(my_set)

my_set.remove(2)
print(my_set)

my_set.discard('Test')
print(my_set)

list_data_one = [1, 1, 2, 3, 4, 5, 8, 13, 21, 7, 5, 100, 122, 13]
list_data_two = [0, 2, 54, 3, 24, 5, 6, 7, 15, 9, 10, 110, 122, 13]

print(list(set(list_data_one) & set(list_data_two)))
print(list(set(list_data_one) | set(list_data_two)))
print(list(set(list_data_one) - set(list_data_two)))
print(list(set(list_data_one) ^ set(list_data_two)))

my_tuple = (1, )
print(my_tuple, type(my_tuple))

my_tuple = (1)
print(my_tuple, type(my_tuple))

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple, type(my_tuple))

circle = {
    (0, 0): "Center",
    (0, 1): "90",
    (1, 0): "0 or 360",
    (0, -1): "270",
    (-1, 0): "180",
}
print(circle.get((0, 1)))

