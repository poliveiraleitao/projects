#ex => create a random student score from 1 to 100 for each name
student_dict = {
    "student": ['Paulo', 'Larissa', 'Ben', 'Thor', 'Kiwi', 'Alex'],
    "score": [56, 78, 50, 23, 33, 44]
}

import pandas

students_data_frame = pandas.DataFrame(student_dict)
print(students_data_frame)

#loop trough rows in a data frame
for (index, row) in students_data_frame.iterrows():
    print(row.student)

    if row.student == 'Paulo':
        print(row)