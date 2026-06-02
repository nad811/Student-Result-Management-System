from file_handler import read_students


def view_students():

    students = read_students()

    if len(students) == 0:

        print("No records found")

        return

    for index, student in enumerate(students):

        print(
            f"{index + 1}. "
            f"{student[0]}"
        )
