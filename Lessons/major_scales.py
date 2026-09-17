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

    
# SECTION 1: TONES AND SEMITONES
    print("Now that you have learnt about tones and semitones, do you think you are ready to test your knowledge?")
    x=input("Type 'yes' to start the quiz or 'no' to exit: ").strip().lower()
    if x == "yes":
        print("Let's begin the quiz!")
        def quiz_1():
            questions = [
                {
                    "question": "What is a semitone?",
                    "options": {
                        "A": "The largest interval between two keys",
                        "B": "The smallest interval between two adjacent keys",
                        "C": "Two tones combined",
                        "D": "The distance between two octaves"
                    },
                    "answer": "B"
                },

                {
                    "question": "How many semitones make one tone?",
                    "options": {
                        "A": "1",
                        "B": "2",
                        "C": "3",
                        "D": "4"
                    },
                    "answer": "B"
                },

                {
                    "question": "Is C to D a tone or a semitone?",
                    "options": {
                        "A": "Tone",
                        "B": "Semitone",
                        "C": "Neither",
                        "D": "An octave"
                    },
                    "answer": "A"
                },

                {
                    "question": "Is E to F a tone or a semitone?",
                    "options": {
                        "A": "Tone",
                        "B": "Semitone",
                        "C": "Both",
                        "D": "Neither"
                    },
                    "answer": "B"
                },

                {
                    "question": "Which pair of natural notes is a semitone apart?",
                    "options": {
                        "A": "C and D",
                        "B": "D and E",
                        "C": "E and F",
                        "D": "F and G"
                    },
                    "answer": "C"
                },

                {
                    "question": "Which other pair of natural notes is a semitone apart?",
                    "options": {
                        "A": "A and B",
                        "B": "B and C",
                        "C": "C and D",
                        "D": "F and G"
                    },
                    "answer": "B"
                },

                {
                    "question": "How many semitones are between C and D?",
                    "options": {
                        "A": "1",
                        "B": "2",
                        "C": "3",
                        "D": "4"
                    },
                    "answer": "B"
                },

                {
                    "question": "How many semitones are between E and F?",
                    "options": {
                        "A": "1",
                        "B": "2",
                        "C": "3",
                        "D": "4"
                    },
                    "answer": "A"
                },

                {
                    "question": "If two white keys have one black key between them, what is the distance between them?",
                    "options": {
                        "A": "A semitone",
                        "B": "A tone",
                        "C": "An octave",
                        "D": "A third"
                    },
                    "answer": "B"
                },

                {
                    "question": "What is the interval pattern in C-D-E-F?",
                    "options": {
                        "A": "S-T-T",
                        "B": "T-S-T",
                        "C": "T-T-S",
                        "D": "S-S-T"
                    },
                    "answer": "C"
                }
            ]

            print("======================================")
            print("       SONIDIUS - MAJOR SCALES")
            print("       SECTION 1: TONES & SEMITONES")
            print("======================================")

            score = 0

            for i, q in enumerate(questions, 1):

                print(f"\nQuestion {i}: {q['question']}")

                for letter, option in q["options"].items():
                    print(f"{letter}. {option}")

                user_answer = input("\nYour answer: ").strip().upper()

                if user_answer == q["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is {q['answer']}.")

            print("\n======================================")
            print("              RESULTS")
            print("======================================")

            print(f"You scored {score}/{len(questions)}")

            if score == len(questions):
                print("Perfect score! You mastered this section.")
            elif score >= 7:
                print("Great job! You understand the basics.")
            elif score >= 5:
                print("Not bad! Keep practicing.")
            else:
                print("Keep practicing. You'll get there!")

        quiz_1()

    elif x == "no":
        print("Thank you for participating. Goodbye!")
    else:
        print("Kindly input 'yes' or 'no'.")