from Lessons.major_scales import major_scales
from Lessons.musical_terminologies import musical_terminologies
from Lessons.minor_scales import minor_scales
from Lessons.note_intervals import note_intervals


def main():

    print("Welcome")

    # Entry of user's information
    name = input("What is your full name? ").title().strip()
    nickname = input("What would you prefer to be referred to as? ").title().strip()
    age = int(input("What is your age? "))

    print()
    print(f"Welcome to the Interactive Music Tutor {nickname}!")

    # MAIN MENU
    while True:

        print()
        print("======================================")
        print("          SONIDIUS MAIN MENU")
        print("======================================")
        print()
        print("Please select a number from the list below:")
        print()
        print("1. Learn major scales")
        print("2. Learn minor scales")
        print("3. Learn note intervals")
        print("4. Learn musical terminologies")
        print("5. Exit Sonidius")
        print()

        try:

            choice = int(input("State choice here: "))

            if choice == 1:

                print("You have selected to learn major scales")
                print()

                major_scales()

            elif choice == 2:

                print("You have selected to learn minor scales")
                print()

                minor_scales()

            elif choice == 3:

                print("You have selected to learn note intervals")
                print()

                note_intervals()

            elif choice == 4:

                print("You have selected to learn musical terminologies")
                print()

                musical_terminologies()

            elif choice == 5:

                print()
                print(f"Goodbye {nickname}! Thanks for using Sonidius.")
                break

            else:

                print("Kindly pick a number from 1 to 5.")

        except ValueError:

            print("Please choose a number from the list above.")


main()