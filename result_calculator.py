from file_handler import read_students


def show_results():

    students = read_students()

    if len(students) == 0:

        print("No records found")

        return

    for student in students:

        total = (
            float(student[1]) +
            float(student[2]) +
            float(student[3])
        )

        percentage = total / 3

        print("\nName:", student[0])

        print("Total:", total)

        print(
            "Percentage:",
            round(percentage, 2)
        )
