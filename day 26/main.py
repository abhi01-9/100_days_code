import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# Loop through a list
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

# Loop through a dictionary
passed_students = {student: student_score for (student, student_score) in students_scores.items() if
                   student_score >= 60}
print(passed_students)

# Iterate through dictionaries
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

# Iterate over pandas dataframe
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)


# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
