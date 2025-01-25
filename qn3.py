# Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

mark=int(input('Enter the score of the student: '))

if mark>100:
    print('Invalid score')
    exit()
    
if mark>=90:
    grade = 'A'
if mark>=80:
    grade = 'B'
if mark>=70:
    grade = 'C'
if mark>=60:
    grade = 'D'
if mark<60:
    grade = 'F'

print(f'{grade}')