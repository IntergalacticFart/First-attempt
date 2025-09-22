def grade_letter(grade):
    average = (grade[0] + grade[1] + grade[2] + grade[3] + grade[4]) / 5
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    return average, letter

name = input("enter student name: ")
grade = []
grade.append(int(input("enter the first grade: ")))
grade.append(int(input("enter the second grade: ")))
grade.append(int(input("enter the third grade: ")))
grade.append(int(input("enter the fourth grade: ")))
grade.append(int(input("enter the fifth grade: ")))
average, letter = grade_letter(grade)
print("the average is: ", average)
print("the letter is: ",letter)

#jeremiah grades: 47, 59, 93, 70, 89
#torrance grades: 94, 72, 91, 67, 100
#mary grades: 92, 44, 94, 83, 79
#beth grades: 77, 32, 27, 100, 92
#john grades: 100, 100, 100, 99, 82
#larry grades: 44, 89, 77, 66, 100
#megan grades: 50, 85, 75, 95, 95