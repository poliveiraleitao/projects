number = [1,2,3]
new_list = []
for n in number:
    add_1 = n + 1
    new_list.append((add_1))
print(new_list)

new_list_2 = [n + 1 for n in number]
print(new_list_2)

name = 'Paulo'
letter_list = [letter for letter in name]
print(letter_list)

n_range = range(1,5)
double_range = [n * 2 for n in n_range]
print(double_range)

names = ['Paulo', 'Larissa', 'Ben', 'Thor', 'Kiwi', 'Alex']
short_names = [name for name in names if len(name) < 5]
print(short_names)

names = ['Paulo', 'Larissa', 'Ben', 'Thor', 'Kiwi', 'Alex']
upper_short_names = [name.upper() for name in names if len(name) < 5]
print(upper_short_names)

numbers = [1, 1, 2, 3, 5, 8,13, 21, 34, 55]
#square numbers
square_numbers = [n**2 for n in numbers]
print(square_numbers)
#filter even numbers
even_numbers = [n for n in numbers if n % 2 != 0]
print(even_numbers)


list_a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
list_b = (1, 5, 10)
number_in_a_and_b = [n for n in list_a if n in list_b]
print(number_in_a_and_b)

