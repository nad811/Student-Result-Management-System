from menu import display_menu

from add_student import add_student

from view_students import view_students

from result_calculator import show_results

from delete_student import delete_student


while True:

    display_menu()

    choice = input("Choose Option: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        show_results()

    elif choice == "4":

        delete_student()

    elif choice == "5":

        print("Goodbye")

        break

    else:

        print("Invalid Option")
