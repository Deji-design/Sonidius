# All predefined functions 

def major_scales ():

# Lesson begins
    print("""Welcome
Major scales are the basics of musical knowledge. 

How many major key signatures do you think exist in Western music
A. 12
B. 13
C. 14
D. 15
    """)
    answer = input ("Write your choice option here: ")
    if answer == "A" :
        print ("Impressive try, but there are 15 major scales")
    elif answer == "B" :
        print ("Close, but the answer is 15")
    elif answer == "C" :
        print ("ALmost there, But the answer is 15")
    elif answer == "D" :
        print ("Congratulations, you are correct. There are 15 major scales")
    else :
        print ("Kindly input a letter")

print (major_scales)




def minor_scales () :
    print (" Lesson coming soon")





def note_intervals () :
    print ("Lesson coming soon")  






def musical_terminologies () :
    print ("Lesson coming soon")






def main() :
# Introduction for user
    print("Welcome")

# Entry of user's information
    name = input("What is your full name? ").title().strip()
    nickname = input("What would you prefer to be referred to as? ").title().strip()
    age = int(input("What is your age? "))
    print()
    print(f"Welcome to the Interactive Music Tutor {nickname}!")


<<<<<<< Updated upstream
# Menu selection
=======
        print()
        print("Please select a number from the list below:")
        print()
        print("1. Learn major scales")
        print("2. Learn minor scales")
        print("3. Learn note intervals")
        print("4. Learn musical terminologies")
        print("5. Exit Sonidius")
        print()
>>>>>>> Stashed changes

    print ()
    print ("Please select a number from the list below:")
    print ("1. Learn major scales")
    print ("2. Learn minor scales")
    print ("3. Learn note intervals")
    print ("4. Learn musical terminologies")
    print ()
# Validates the user's choice
    try :
        choice = int(input("State choice here: "))

        if choice == 1 :
            print ("You have selected to learn major scales")
            print ()
            print ("Welcome to the major scales lesson")
            print ()
            major_scales ()
            
        elif choice == 2 :   
            print ("You have selected to learn minor scales")
            minor_scales()
        elif choice == 3 :
            print ("You have selected to learn note intervals")
            note_intervals ()
        elif choice == 4 :
            print ("You have selected to learn musical terminologies")
            musical_terminologies ()
        else :
            print(" Kindly pick a number from 1 to 4")
    except ValueError :
            print ("Please choose a number from the list above")
    

main ()




