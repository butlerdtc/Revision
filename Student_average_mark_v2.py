names = []
total_marks = 0
best_mark = 0
best_student = []
while True:
    student_name = input("Student name: ").lower()
    if student_name == "x":
        break
    else:
        mark = int(input(f"{student_name}'s mark: "))
        while not 0 <= mark <= 100:
            print("Please enter correct mark")
            mark = int(input(f"{student_name}'s mark: "))
        else:
            total_marks += mark
            names.append([student_name, mark])
total_student = len(names)

for student_name in names:
    if student_name[1] > best_mark:
        best_mark = student_name[1]
        best_student = [student_name]
    elif student_name[1] == best_mark:
        best_student.append(student_name)

average_mark = round(total_marks/total_student, 2)
print(f"The average mark was {average_mark}: ")
if len(best_student) > 1:
    print(f"The best students are: ")
    for names in best_student:
        print(f"\t{names[0]}")
    print(f"\twith {best_student[0][1]} marks")
else:
    print(f"{best_student[0][0]} was the best with a mark of {best_mark}")

for student_name in names:
    if 100 >= student_name[1] >= 90:
        print(f"{student_name[0]} scored an A+ with a mark of "
              f"{student_name[1]}")
    elif 90 > student_name[1] >= 85:
        print(f"{student_name[0]} scored an A with a mark of "
              f"{student_name[1]}")
    elif 85 > student_name[1] >= 80:
        print(f"{student_name[0]} scored an A- with a mark of "
              f"{student_name[1]}")
    elif 80 > student_name[1] >= 75:
        print(f"{student_name[0]} scored a B+ with a mark of "
              f"{student_name[1]}")
    elif 75 > student_name[1] >= 70:
        print(f"{student_name[0]} scored a B with a mark of "
              f"{student_name[1]}")
    elif 70 > student_name[1] >= 65:
        print(f"{student_name[0]} scored a B- with a mark of "
              f"{student_name[1]}")
    elif 65 > student_name[1] >= 60:
        print(f"{student_name[0]} scored a C+ with a mark of "
              f"{student_name[1]}")
    elif 60 > student_name[1] >= 55:
        print(f"{student_name[0]} scored a C with a mark of "
              f"{student_name[1]}")
    elif 55 > student_name[1] >= 50:
        print(f"{student_name[0]} scored a C- with a mark of "
              f"{student_name[1]}")
    elif 50 > student_name[1] >= 40:
        print(f"{student_name[0]} scored a D with a mark of "
              f"{student_name[1]}")
    else:
        print(f"{student_name[0]} scored an E with a mark of "
              f"{student_name[1]}")
