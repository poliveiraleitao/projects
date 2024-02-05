#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key, value) in dict.items() if test}

#ex => create a random student score from 1 to 100 for each name
students = ['Paulo', 'Larissa', 'Ben', 'Thor', 'Kiwi', 'Alex']

import random
random_score = {name:random.randint(1,100) for name in students}
print(random_score)

passed_students = {name: score for name, score in random_score.items() if score > 60}
print(passed_students)

name_lengh = {name: len(name) for name in students}
print(name_lengh)

#get each word and write the lengh
sentence = 'what are you doing here?'
words = sentence.split()
print(words)
word_lengh = {word: len(word) for word in words}
print(word_lengh)


