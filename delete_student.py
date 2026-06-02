from file_handler import read_students
from file_handler import overwrite_students


def delete_student():

    students = read_students()

    if len(students) == 0:

        print("No students found")

        return

    for index, student in enumerate(students):

        print(
            f"{index + 1}. "
            f"{student[0]}"
        )

    choice = int(
        input("Choose Student: ")
    )

    if choice < 1 or choice > len(students):

        print("Invalid Choice")

        return

    students.pop(choice - 1)

    overwrite_students(students)

    print("Student Deleted")
