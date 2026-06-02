import csv

FILE_PATH = "../data/students.csv"


def read_students():

    students = []

    try:

        with open(FILE_PATH, "r") as file:

            reader = csv.reader(file)

            for row in reader:

                students.append(row)

    except FileNotFoundError:

        pass

    return students


def save_student(student):

    with open(FILE_PATH, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(student)


def overwrite_students(students):

    with open(FILE_PATH, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(students)
