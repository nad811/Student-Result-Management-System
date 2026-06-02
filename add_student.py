from file_handler import save_student
from validator import valid_mark


def add_student():

    name = input("Student Name: ")

    english = input("English Marks: ")
    maths = input("Maths Marks: ")
    science = input("Science Marks: ")

    if not (
        valid_mark(english)
        and valid_mark(maths)
        and valid_mark(science)
    ):

        print("Invalid Marks")

        return

    save_student(
        [
            name,
            english,
            maths,
            science
        ]
    )

    print("Student Added")
