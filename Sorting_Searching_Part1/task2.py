def main():
    student_name = input('Enter student\'s name: ')
    grades = []
    for i in range(10):
        grade = int(input('Enter grade: '))
        grades.append(grade)

    print(grades)
    grade_to_change = int(input('Enter the grade from the exam to retake: '))
    new_grade = int(input('New grade from the retake: '))

    grades[grades.index(grade_to_change)] = new_grade

    av_grade = sum(grades) / len(grades)
    print(av_grade)
    if av_grade >= 10.7:
        print('The student is granted a scholarship.')
    else:
        print('Sorry, mate no scholarship for you.')

    print(f'The grades of the student {student_name} are: ')
    grades.sort()
    for grade in grades:
        print(grade, end=' ')


if __name__ == '__main__':
    main()
