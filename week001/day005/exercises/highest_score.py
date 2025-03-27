from random import randint

from week001.day002.primitive_data_types import weight

number_of_student = 100

student_scores = []

for _ in range(100):
    student_scores.append(randint(0, 200))

for student in range(len(student_scores)):
    print(f'Student #{student + 1:0>3} scored: {student_scores[student]}')
total_score = sum(student_scores)
print(f'Total score {total_score}')