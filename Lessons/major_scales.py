import random


# ==========================================
# FUNCTION FOR ASKING QUESTIONS
# ==========================================

def ask_question(q, question_number):

    print(f"\nQuestion {question_number}: {q['question']}")

    # ==========================================
    # MULTIPLE CHOICE
    # ==========================================

    if q["type"] == "multiple_choice":

        # Convert the options dictionary into a list
        # so that the options can be shuffled
        options = list(q["options"].items())

        # Shuffle the options
        random.shuffle(options)

        # Letters that will be displayed
        letters = ["A", "B", "C", "D"]

        # This will store the new correct answer
        new_correct_answer = ""

        # Display the shuffled options
        for i in range(len(options)):

            old_letter = options[i][0]
            option_text = options[i][1]

            print(f"{letters[i]}. {option_text}")

            # Check whether this option was originally
            # the correct answer
            if old_letter == q["answer"]:
                new_correct_answer = letters[i]

        # Keep asking until the user enters A, B, C, or D
        while True:

            user_answer = input("\nYour answer: ").strip().upper()

            if user_answer in ["A", "B", "C", "D"]:

                if user_answer == new_correct_answer:
                    print("Correct!")
                    return True

                else:
                    print(f"Incorrect. The correct answer is {new_correct_answer}.")
                    return False

            else:

                print("Invalid answer. Kindly input A, B, C, or D.")


    # ==========================================
    # TRUE OR FALSE
    # ==========================================

    elif q["type"] == "true_false":

        print("A. True")
        print("B. False")

        while True:

            user_answer = input("\nYour answer: ").strip().upper()

            if user_answer in ["A", "B", "TRUE", "T"]:
                
                if q["answer"] == "TRUE":
                    print("Correct!")
                    return True

                else:
                    print("Incorrect. The correct answer is False.")
                    return False

            elif user_answer in ["B", "FALSE", "F"]:

                if q["answer"] == "FALSE":
                    print("Correct!")
                    return True

                else:
                    print("Incorrect. The correct answer is True.")
                    return False

            else:

                print("Invalid answer. Kindly input A/B or True/False.")


    # ==========================================
    # FILL IN THE BLANK
    # ==========================================

    elif q["type"] == "fill_blank":

        while True:

            user_answer = input("\nYour answer: ").strip().lower()

            if user_answer == "":
                print("Please enter an answer.")
                continue

            # Remove spaces and common punctuation
            cleaned_answer = (
                user_answer
                .replace(" ", "")
                .replace(",", "")
                .replace("-", "")
                .replace("–", "")
            )

            correct_answer = (
                q["answer"]
                .lower()
                .replace(" ", "")
                .replace(",", "")
                .replace("-", "")
                .replace("–", "")
            )

            if cleaned_answer == correct_answer:

                print("Correct!")
                return True

            else:

                print(f"Incorrect. The correct answer is {q['answer']}.")
                return False


    # ==========================================
    # KEYBOARD INTERACTION
    # ==========================================

    elif q["type"] == "keyboard":

        print("""
Keyboard:

C   C#   D   D#   E   F   F#   G   G#   A   A#   B
""")

        while True:

            user_answer = input("\nYour answer: ").strip().upper()

            if user_answer == "":

                print("Please enter an answer.")

            elif user_answer == q["answer"].upper():

                print("Correct!")
                return True

            else:

                print(f"Incorrect. The correct answer is {q['answer']}.")
                return False


    # ==========================================
    # SCALE BUILDING
    # ==========================================

    elif q["type"] == "scale_building":

        while True:

            user_answer = input("\nYour answer: ").strip().upper()

            if user_answer == "":

                print("Please enter an answer.")

            else:

                cleaned_answer = (
                    user_answer
                    .replace(" ", "")
                    .replace("-", "")
                    .replace("–", "")
                )

                correct_answer = (
                    q["answer"]
                    .upper()
                    .replace(" ", "")
                    .replace("-", "")
                    .replace("–", "")
                )

                if cleaned_answer == correct_answer:

                    print("Correct!")
                    return True

                else:

                    print(f"Incorrect. The correct answer is {q['answer']}.")
                    return False


    # ==========================================
    # IDENTIFY THE ERROR
    # ==========================================

    elif q["type"] == "identify_error":

        options = list(q["options"].items())

        random.shuffle(options)

        letters = ["A", "B", "C", "D"]

        new_correct_answer = ""

        for i in range(len(options)):

            old_letter = options[i][0]
            option_text = options[i][1]

            print(f"{letters[i]}. {option_text}")

            if old_letter == q["answer"]:

                new_correct_answer = letters[i]

        while True:

            user_answer = input("\nYour answer: ").strip().upper()

            if user_answer in ["A", "B", "C", "D"]:

                if user_answer == new_correct_answer:

                    print("Correct!")
                    return True

                else:

                    print(f"Incorrect. The correct answer is {new_correct_answer}.")
                    return False

            else:

                print("Invalid answer. Kindly input A, B, C, or D.")


    # ==========================================
    # CHALLENGE / APPLICATION
    # ==========================================

    elif q["type"] == "challenge":

        options = list(q["options"].items())

        random.shuffle(options)

        letters = ["A", "B", "C", "D"]

        new_correct_answer = ""

        for i in range(len(options)):

            old_letter = options[i][0]
            option_text = options[i][1]

            print(f"{letters[i]}. {option_text}")

            if old_letter == q["answer"]:

                new_correct_answer = letters[i]

        while True:

            user_answer = input("\nYour answer: ").strip().upper()

            if user_answer in ["A", "B", "C", "D"]:

                if user_answer == new_correct_answer:

                    print("Correct!")
                    return True

                else:

                    print(f"Incorrect. The correct answer is {new_correct_answer}.")
                    return False

            else:

                print("Invalid answer. Kindly input A, B, C, or D.")


# ==========================================
# MAJOR SCALES LESSON
# ==========================================

def major_scales():

    # ==========================================
    # INTRODUCTION
    # ==========================================

    print("""
==========================================
        SONIDIUS - MAJOR SCALES
==========================================

Welcome!

Major scales are one of the foundations of
music theory. In this lesson, you will learn
how major scales are built, how tones and
semitones work, how key signatures work,
and how the Circle of Fifths connects
everything together.

There are 15 major key signatures in
Western music.

Let us begin!
""")

    while True:

        answer = input("""
How many major key signatures do you think
exist in Western music?

A. 12
B. 13
C. 14
D. 15

Write your choice: """).strip().upper()

        if answer == "A":
            print("Impressive try, but there are 15 major key signatures.")
            break

        elif answer == "B":
            print("Close, but the answer is 15.")
            break

        elif answer == "C":
            print("Almost there, but the answer is 15.")
            break

        elif answer == "D":
            print("Congratulations! You are correct. There are 15 major key signatures.")
            break

        else:
            print("Invalid answer. Kindly input A, B, C, or D.")

    input("\nPress Enter to begin the lesson...")


    print("""  
   WHAT IS A MAJOR SCALE?


A major scale is a sequence of seven different notes arranged according to a specific pattern.


This specific pattern is called the major scale formula. 
The Major scale formula is based on the standard pattern of tones and semitones.
The pattern is clear and quite song-like:

 tone-tone-semitone-tone-tone-tone-semitone (T-T-S-T-T-T-S)

 But wait! What are these strange words?
 
    """)

    # ==========================================
    # SECTION 1: TONES AND SEMITONES
    # ==========================================

    print("""
==========================================
       SECTION 1: TONES & SEMITONES
==========================================

These terms may seem confusing at first. What do they actually mean?
Everyone knows that tones have to do with music, and semitones?
They sound kinda like they came from tones. Or did semitones come before tones? 
It’s all so confusing!


So let’s make it simple.
For better understanding, let us think up a piano, keyboard, or organ - whichever one you wish to imagine.
Suppose you have a physical one around- even better! Go to it.
You could also use the image of the keyboard shown below.

|insert image in GUI|


Observe how there are both white and black keys. You might think they are there for the classic effect, but they're important.


The invisible space between any adjacent keys (either black and white or white and black) is a semitone.
More specifically, a semitone is the smallest interval (distance) between two adjacent (that means beside one another) keys on a standard piano or keyboard. 

|insert image in GUI|


You will encounter semitones in many areas of music theory, so it's important to understand this idea. 


Another trick to remember: most neighboring natural notes (the white keys) are a tone apart. 
The exceptions are B–C and E–F, which are a semitone apart.


|insert image in GUI|

After talking about a part of the pair, we move to the other- the tone. A tone is made up of two semitones.
Think of it like a math equation:

1 Semitone + 1 Semitone = 1 Tone


Back to the keyboard, you can often see a tone between two white keys with a black key between them. For example, C to D is a tone. 
Remember our exception, though: B-C and E-F have a semitone each between them. 
You can remember this because they do not have a black key between them.
A tone can also be found between two black keys with a white key between them.


|insert image in GUI|

Now you can celebrate!!!! You have learnt the basics of tones and semitones! 


""")

    while True:

        x = input(
            "Are you ready to test your knowledge?\n"
            "Type 'yes' to start or 'no' to return to the main menu: "
        ).strip().lower()

        if x == "yes":
            break

        elif x == "no":
            return

        else:
            print("Kindly input 'yes' or 'no'.")


    # ==========================================
    # SECTION 1 QUESTION BANK
    # ==========================================

    questions = [

        # ==========================================
        # MULTIPLE CHOICE - 30 QUESTIONS
        # ==========================================

        {
            "type": "multiple_choice",
            "question": "What is a semitone?",
            "options": {
                "A": "The distance between two tones",
                "B": "The smallest interval between adjacent keys",
                "C": "Two whole tones",
                "D": "The distance between two scales"
            },
            "answer": "B"
        },

        {
            "type": "multiple_choice",
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
            "type": "multiple_choice",
            "question": "Is C to D a tone or semitone?",
            "options": {
                "A": "Tone",
                "B": "Semitone",
                "C": "Neither",
                "D": "Both"
            },
            "answer": "A"
        },

        {
            "type": "multiple_choice",
            "question": "Is E to F a tone or semitone?",
            "options": {
                "A": "Tone",
                "B": "Semitone",
                "C": "Neither",
                "D": "Both"
            },
            "answer": "B"
        },

        {
            "type": "multiple_choice",
            "question": "Which pair of natural notes is a semitone apart?",
            "options": {
                "A": "C-D",
                "B": "D-E",
                "C": "E-F",
                "D": "F-G"
            },
            "answer": "C"
        },

        {
            "type": "multiple_choice",
            "question": "Which other pair of natural notes is a semitone apart?",
            "options": {
                "A": "A-B",
                "B": "B-C",
                "C": "C-D",
                "D": "F-G"
            },
            "answer": "B"
        },

        {
            "type": "multiple_choice",
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
            "type": "multiple_choice",
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
            "type": "multiple_choice",
            "question": "Two white keys with one black key between them are usually separated by what?",
            "options": {
                "A": "Two tones",
                "B": "A tone",
                "C": "A semitone",
                "D": "Three semitones"
            },
            "answer": "B"
        },

        {
            "type": "multiple_choice",
            "question": "What is the interval pattern from C to F?",
            "options": {
                "A": "T-S-T",
                "B": "S-T-T",
                "C": "T-T-S",
                "D": "S-S-T"
            },
            "answer": "C"
        },

        {
            "type": "multiple_choice",
            "question": "Which pair of natural notes is a tone apart?",
            "options": {
                "A": "E-F",
                "B": "B-C",
                "C": "C-D",
                "D": "None"
            },
            "answer": "C"
        },

        {
            "type": "multiple_choice",
            "question": "Which pair is one semitone apart?",
            "options": {
                "A": "C-D",
                "B": "D-E",
                "C": "F-G",
                "D": "B-C"
            },
            "answer": "D"
        },

        {
            "type": "multiple_choice",
            "question": "Three tones are equal to how many semitones?",
            "options": {
                "A": "3",
                "B": "4",
                "C": "6",
                "D": "8"
            },
            "answer": "C"
        },

        {
            "type": "multiple_choice",
            "question": "Two tones are equal to how many semitones?",
            "options": {
                "A": "2",
                "B": "3",
                "C": "4",
                "D": "5"
            },
            "answer": "C"
        },

        {
            "type": "multiple_choice",
            "question": "Which natural note comes immediately after E?",
            "options": {
                "A": "F",
                "B": "F#",
                "C": "G",
                "D": "D"
            },
            "answer": "A"
        },

        {
            "type": "multiple_choice",
            "question": "What note is one tone above C?",
            "options": {
                "A": "C#",
                "B": "D",
                "C": "D#",
                "D": "E"
            },
            "answer": "B"
        },

        {
            "type": "multiple_choice",
            "question": "What note is one semitone above E?",
            "options": {
                "A": "F",
                "B": "F#",
                "C": "D#",
                "D": "G"
            },
            "answer": "A"
        },

        {
            "type": "multiple_choice",
            "question": "What note is one semitone above B?",
            "options": {
                "A": "B#",
                "B": "C#",
                "C": "C",
                "D": "A#"
            },
            "answer": "C"
        },

        {
            "type": "multiple_choice",
            "question": "Which natural-note pair is NOT a semitone apart?",
            "options": {
                "A": "E-F",
                "B": "B-C",
                "C": "C-D",
                "D": "None"
            },
            "answer": "C"
        },

        {
            "type": "multiple_choice",
            "question": "How many semitones are between F and G?",
            "options": {
                "A": "1",
                "B": "2",
                "C": "3",
                "D": "4"
            },
            "answer": "B"
        },

        {
            "type": "multiple_choice",
            "question": "How many semitones are between A and B?",
            "options": {
                "A": "1",
                "B": "2",
                "C": "3",
                "D": "4"
            },
            "answer": "B"
        },

        {
            "type": "multiple_choice",
            "question": "How many semitones are between B and C?",
            "options": {
                "A": "1",
                "B": "2",
                "C": "3",
                "D": "4"
            },
            "answer": "A"
        },

        {
            "type": "multiple_choice",
            "question": "Which statement is correct?",
            "options": {
                "A": "A tone equals one semitone",
                "B": "A tone equals two semitones",
                "C": "A semitone equals two tones",
                "D": "A tone has no semitones"
            },
            "answer": "B"
        },

        {
            "type": "multiple_choice",
            "question": "Which natural-note pair is separated by a tone?",
            "options": {
                "A": "E-F",
                "B": "B-C",
                "C": "D-E",
                "D": "None"
            },
            "answer": "C"
        },

        {
            "type": "multiple_choice",
            "question": "What is the interval pattern from C to G?",
            "options": {
                "A": "T-T-S-T",
                "B": "T-S-T-T",
                "C": "S-T-T-T",
                "D": "T-T-T-S"
            },
            "answer": "A"
        },

        {
            "type": "multiple_choice",
            "question": "What is the interval pattern from E to G?",
            "options": {
                "A": "T-T",
                "B": "S-T",
                "C": "T-S",
                "D": "S-S"
            },
            "answer": "B"
        },

        {
            "type": "multiple_choice",
            "question": "Moving one key to an adjacent key on a keyboard represents what?",
            "options": {
                "A": "A semitone",
                "B": "A tone",
                "C": "Two tones",
                "D": "A scale"
            },
            "answer": "A"
        },

        {
            "type": "multiple_choice",
            "question": "Moving two semitones represents what?",
            "options": {
                "A": "A semitone",
                "B": "A tone",
                "C": "Three tones",
                "D": "A scale"
            },
            "answer": "B"
        },

        {
            "type": "multiple_choice",
            "question": "Which is the correct major-scale interval pattern?",
            "options": {
                "A": "T-T-S-T-T-T-S",
                "B": "T-S-T-T-S-T-T",
                "C": "S-T-T-S-T-T-T",
                "D": "T-T-T-S-T-S-T"
            },
            "answer": "A"
        },

        {
            "type": "multiple_choice",
            "question": "Which sequence correctly shows the first four notes of the C major scale?",
            "options": {
                "A": "C-D-E-F",
                "B": "C-C#-D-E",
                "C": "C-D#-E-F#",
                "D": "C-E-F-G"
            },
            "answer": "A"
        },


        # ==========================================
        # TRUE / FALSE - 5 QUESTIONS
        # ==========================================

        {
            "type": "true_false",
            "question": "A tone is made up of two semitones.",
            "answer": "TRUE"
        },

        {
            "type": "true_false",
            "question": "C to D is a semitone.",
            "answer": "FALSE"
        },

        {
            "type": "true_false",
            "question": "E to F is a semitone.",
            "answer": "TRUE"
        },

        {
            "type": "true_false",
            "question": "B to C is a tone.",
            "answer": "FALSE"
        },

        {
            "type": "true_false",
            "question": "Every pair of adjacent natural notes is a tone apart.",
            "answer": "FALSE"
        },


        # ==========================================
        # FILL IN THE BLANK - 10 QUESTIONS
        # ==========================================

        {
            "type": "fill_blank",
            "question": "A tone is equal to _____ semitones.",
            "answer": "2"
        },

        {
            "type": "fill_blank",
            "question": "A semitone is the smallest interval between _____ keys.",
            "answer": "adjacent"
        },

        {
            "type": "fill_blank",
            "question": "C to D is _____ semitones.",
            "answer": "2"
        },

        {
            "type": "fill_blank",
            "question": "E to F is _____ semitone.",
            "answer": "1"
        },

        {
            "type": "fill_blank",
            "question": "B to C is _____ semitone.",
            "answer": "1"
        },

        {
            "type": "fill_blank",
            "question": "F to G is _____ semitones.",
            "answer": "2"
        },

        {
            "type": "fill_blank",
            "question": "A to B is _____ semitones.",
            "answer": "2"
        },

        {
            "type": "fill_blank",
            "question": "The first three intervals of the C major scale are _____, _____, _____.",
            "answer": "TTS"
        },

        {
            "type": "fill_blank",
            "question": "The major scale begins with two _____ .",
            "answer": "tones"
        },

        {
            "type": "fill_blank",
            "question": "The complete major scale pattern is T-T-S-T-T-T-_____.",
            "answer": "S"
        },


        # ==========================================
        # KEYBOARD INTERACTION - 8 QUESTIONS
        # ==========================================

        {
            "type": "keyboard",
            "question": "Starting from C, move up one semitone. What note do you reach?",
            "answer": "C#"
        },

        {
            "type": "keyboard",
            "question": "Starting from C, move up two semitones. What note do you reach?",
            "answer": "D"
        },

        {
            "type": "keyboard",
            "question": "Starting from D, move up one semitone. What note do you reach?",
            "answer": "D#"
        },

        {
            "type": "keyboard",
            "question": "Starting from E, move up one semitone. What note do you reach?",
            "answer": "F"
        },

        {
            "type": "keyboard",
            "question": "Starting from F, move up two semitones. What note do you reach?",
            "answer": "G"
        },

        {
            "type": "keyboard",
            "question": "Starting from G, move up one semitone. What note do you reach?",
            "answer": "G#"
        },

        {
            "type": "keyboard",
            "question": "Starting from A, move up two semitones. What note do you reach?",
            "answer": "B"
        },

        {
            "type": "keyboard",
            "question": "Starting from B, move up one semitone. What note do you reach?",
            "answer": "C"
        },


        # ==========================================
        # SCALE BUILDING - 8 QUESTIONS
        # ==========================================

        {
            "type": "scale_building",
            "question": "Using the major-scale pattern T-T-S, complete: C-D-E-_____",
            "answer": "F"
        },

        {
            "type": "scale_building",
            "question": "Complete the C major scale: C-D-E-F-G-_____",
            "answer": "A"
        },

        {
            "type": "scale_building",
            "question": "Complete the C major scale: C-D-E-F-G-A-_____",
            "answer": "B"
        },

        {
            "type": "scale_building",
            "question": "Complete the C major scale: C-D-E-F-G-A-B-_____",
            "answer": "C"
        },

        {
            "type": "scale_building",
            "question": "What is the interval pattern from C-D-E-F?",
            "answer": "TTS"
        },

        {
            "type": "scale_building",
            "question": "What is the interval pattern from F-G-A-B?",
            "answer": "TTT"
        },

        {
            "type": "scale_building",
            "question": "What interval comes after B in the C major scale?",
            "answer": "S"
        },

        {
            "type": "scale_building",
            "question": "What interval comes after E in the C major scale?",
            "answer": "S"
        },


        # ==========================================
        # IDENTIFY THE ERROR - 4 QUESTIONS
        # ==========================================

        {
            "type": "identify_error",
            "question": "Alex says: 'F to G is one semitone.' What is wrong?",
            "options": {
                "A": "Nothing is wrong.",
                "B": "F to G is two semitones.",
                "C": "F to G is three semitones.",
                "D": "F to G is four semitones."
            },
            "answer": "B"
        },

        {
            "type": "identify_error",
            "question": "A student says: 'E to F is a tone.' What is the error?",
            "options": {
                "A": "E to F is two tones.",
                "B": "E to F is three semitones.",
                "C": "E to F is a semitone.",
                "D": "There is no error."
            },
            "answer": "C"
        },

        {
            "type": "identify_error",
            "question": "A student calculates D to E as 2 semitones. What is the error?",
            "options": {
                "A": "D to E is one semitone.",
                "B": "D to E is two semitones.",
                "C": "D to E is three semitones.",
                "D": "D to E is four semitones."
            },
            "answer": "B"
        },

        {
            "type": "identify_error",
            "question": "Which part of this major-scale pattern is wrong? T-T-S-T-T-T-T",
            "options": {
                "A": "The first T",
                "B": "The final T should be S",
                "C": "The first S",
                "D": "Nothing is wrong"
            },
            "answer": "B"
        },


        # ==========================================
        # CHALLENGE / APPLICATION - 5 QUESTIONS
        # ==========================================

        {
            "type": "challenge",
            "question": "Starting from C, move up 4 semitones. Which note do you reach?",
            "options": {
                "A": "D",
                "B": "D#",
                "C": "E",
                "D": "F"
            },
            "answer": "C"
        },

        {
            "type": "challenge",
            "question": "Starting from E, move up 3 semitones. Which note do you reach?",
            "options": {
                "A": "F#",
                "B": "G",
                "C": "G#",
                "D": "A"
            },
            "answer": "B"
        },

        {
            "type": "challenge",
            "question": "The first three notes of a major scale follow T-T. Starting from C, which notes should they be?",
            "options": {
                "A": "C-D-E",
                "B": "C-C#-D",
                "C": "C-D-F",
                "D": "C-E-F"
            },
            "answer": "A"
        },

        {
            "type": "challenge",
            "question": "Starting from C, after following T-T-S, where do you land?",
            "options": {
                "A": "E",
                "B": "F",
                "C": "F#",
                "D": "G"
            },
            "answer": "B"
        },

        {
            "type": "challenge",
            "question": "Which of the following represents a major scale?",
            "options": {
                "A": "T-T-S-T-T-T-S",
                "B": "T-S-T-T-S-T-T",
                "C": "S-T-T-S-T-T-T",
                "D": "T-T-T-S-T-S-T"
            },
            "answer": "A"
        }

    ]


    # ==========================================
    # SELECT 15 QUESTIONS
    # ==========================================

    # We want every attempt to contain
    # different types of questions.

    multiple_choice_questions = []

    true_false_questions = []

    fill_blank_questions = []

    keyboard_questions = []

    scale_building_questions = []

    identify_error_questions = []

    challenge_questions = []


    # Separate the questions by type

    for question in questions:

        if question["type"] == "multiple_choice":
            multiple_choice_questions.append(question)

        elif question["type"] == "true_false":
            true_false_questions.append(question)

        elif question["type"] == "fill_blank":
            fill_blank_questions.append(question)

        elif question["type"] == "keyboard":
            keyboard_questions.append(question)

        elif question["type"] == "scale_building":
            scale_building_questions.append(question)

        elif question["type"] == "identify_error":
            identify_error_questions.append(question)

        elif question["type"] == "challenge":
            challenge_questions.append(question)


    # ==========================================
    # CREATE A BALANCED 15-QUESTION TEST
    # ==========================================

    selected_questions = []

    # 5 Multiple Choice
    selected_questions.extend(
        random.sample(multiple_choice_questions, 5)
    )

    # 1 True / False
    selected_questions.extend(
        random.sample(true_false_questions, 1)
    )

    # 2 Fill in the blank
    selected_questions.extend(
        random.sample(fill_blank_questions, 2)
    )

    # 2 Keyboard questions
    selected_questions.extend(
        random.sample(keyboard_questions, 2)
    )

    # 2 Scale-building questions
    selected_questions.extend(
        random.sample(scale_building_questions, 2)
    )

    # 1 Identify-the-error question
    selected_questions.extend(
        random.sample(identify_error_questions, 1)
    )

    # 2 Challenge questions
    selected_questions.extend(
        random.sample(challenge_questions, 2)
    )


    # Shuffle the final 15 questions
    random.shuffle(selected_questions)


    # ==========================================
    # START THE TEST
    # ==========================================

    print("""
==========================================
       SECTION 1 TEST
==========================================

You will receive 15 questions from a
70-question question bank.

The questions will be randomly selected.

You need at least 11 correct answers
to pass this section.

Good luck!
""")


    score = 0


    # Ask all 15 selected questions

    for i, question in enumerate(selected_questions, 1):

        if ask_question(question, i):

            score += 1


    # ==========================================
    # TEST RESULTS
    # ==========================================

    print("""
==========================================
             TEST COMPLETE
==========================================
""")

    print(f"You scored {score}/15.")

    percentage = (score / 15) * 100

    print(f"Percentage: {percentage:.1f}%")


    if score >= 11:

        print("""
Congratulations!

You passed Section 1: Tones & Semitones.

You are ready to continue to the next section.
""")

        input("Press Enter to continue...")

    else:

        print("""
You did not pass this attempt.

Don't worry. Review the notes and try again.
You will receive a new set of questions next time.
""")

        while True:

            retry = input(
                "Would you like to try the test again? "
                "(yes/no): "
            ).strip().lower()

            if retry == "yes":

                # Restart the lesson test
                return major_scales()

            elif retry == "no":

                return

            else:
                print("Kindly input 'yes' or 'no'.")
            
            next_section = input("""
Would you like to continue to Section 2?

A. Yes, continue
B. No, return to the main menu

Your choice: """).strip().upper()

            if next_section == "A":
                break

            elif next_section == "B":
                return

            else:
                print("Invalid choice. Returning to the main menu.")
                return

        else:

            print("""
You need at least 7/10 to complete this section.

Let's try again so you can master the topic.
""")

            retry = input("""
Would you like to try Section 1 again?

A. Yes, try again
B. Return to the main menu

Your choice: """).strip().upper()

            if retry == "A":
                continue

            else:
                return


    # ==========================================
    # SECTION 2: C MAJOR & MAJOR SCALE FORMULA
    # ==========================================

    print("""
==========================================
     SECTION 2: C MAJOR & SCALE FORMULA
==========================================

We know that from C to D is a tone. 
This makes it easier to understand our first major scale, C major.



C Major
C major is the foundation of major scales. If you want to learn the keyboard, you will first be taught C major.


C major is a major scale that has no accidentals (you will learn more about accidentals soon).
The C major scale contains seven different notes:
C - D - E - F - G - A - B 
Usually, when we write a major scale, we continue one more note after the seventh note, returning to the starting note at a higher pitch.
It is the same reason why we sing:

Do - Re -Mi - Fa - Sol - La - Ti - Do 

We start with Do and end with Do.

For example:
C – D – E – F – G – A – B – C
The distance from the first C to the second C is called an octave.
The second C has the same letter name as the first C, but it sounds higher. 

How does this group of letters follow the major scale formula?

We know that all major scales should follow
T - T - S - T - T -T - S
So let’s see how exactly.
We will break each interval with the help of our friend “the keyboard”.


	 C - D 

|insert picture in GUI|

We will use our math equation to help us understand.

Remember:
1 Semitone + 1 Semitone = 1 Tone


From white key C to the next black key = 1 Semitone


We also know that from an adjacent black key to a white key is also a semitone.


From the black key to the white key D = 1 Semitone


1 Semitone + 1 Semitone = 1 Tone


Therefore, from white key C to white key D is a tone.


|insert picture in GUI|

From the keyboard, we can see that from D to E there is a black key. 
What do you think will be the interval between them?

Because of the little black key, the distance between D and E is once again:


1 Semitone + 1 Semitone = 1 Tone

|insert picture in GUI|

E - F


This one is rather easy. Try it out yourself.

|insert image in GUI|

It follows the exception we learnt. From E to F is a semitone.

Can you see a pattern already?

So far we have T - T - S.

F - G

|insert picture in GUI|


When we see a black key between two white keys, we know there are two semitones.
And two semitones make a tone.

G - A

|insert picture in GUI|

Can you come up with what is next?

From G to A is a tone.

A - B 

|insert picture in GUI|

A black key is between the two white keys, once again marking a tone.



B - C 


|insert picture in GUI|

Finally, we see the other half of our exception. From B to C is a semitone.

Together, we have matched the  C major scale to the major scale formula.




It’s not hard once you understand the basics!!!


We have successfully cleared the C major scale. But you have probably heard of a sharp or a flat.
Maybe you have even seen these weird symbols : ♯, ♭, ♮ . Moving forward, we will explore what they mean.




""")

    questions = [
        {
            "question": "What is the formula for a major scale?",
            "options": {
                "A": "T-T-S-T-T-T-S",
                "B": "S-S-T-T-S-T-T",
                "C": "T-S-T-T-S-T-T",
                "D": "T-T-T-S-S-T-S"
            },
            "answer": "A"
        },

        {
            "question": "Which notes make up the C major scale?",
            "options": {
                "A": "C-D-E-F-G-A-B-C",
                "B": "C-D-E-F#-G-A-B-C",
                "C": "C-D-Eb-F-G-A-B-C",
                "D": "C#-D-E-F-G-A-B-C"
            },
            "answer": "A"
        },

        {
            "question": "How many accidentals are in the C major scale?",
            "options": {
                "A": "1",
                "B": "2",
                "C": "7",
                "D": "0"
            },
            "answer": "D"
        },

        {
            "question": "What is the first interval in the major scale formula?",
            "options": {
                "A": "Semitone",
                "B": "Tone",
                "C": "Octave",
                "D": "Third"
            },
            "answer": "B"
        },

        {
            "question": "What is the third interval in the major scale formula?",
            "options": {
                "A": "Tone",
                "B": "Semitone",
                "C": "Octave",
                "D": "Fourth"
            },
            "answer": "B"
        },

        {
            "question": "Which natural notes are a semitone apart?",
            "options": {
                "A": "C-D",
                "B": "D-E",
                "C": "E-F",
                "D": "F-G"
            },
            "answer": "C"
        },

        {
            "question": "Which other natural notes are a semitone apart?",
            "options": {
                "A": "A-B",
                "B": "B-C",
                "C": "C-D",
                "D": "F-G"
            },
            "answer": "B"
        },

        {
            "question": "What is an octave?",
            "options": {
                "A": "The smallest interval",
                "B": "Two semitones",
                "C": "The distance between a note and the next note with the same letter name",
                "D": "A type of accidental"
            },
            "answer": "C"
        },

        {
            "question": "How many different letter names are used in a major scale?",
            "options": {
                "A": "5",
                "B": "6",
                "C": "7",
                "D": "8"
            },
            "answer": "C"
        },

        {
            "question": "Which pattern correctly describes C-D-E-F?",
            "options": {
                "A": "T-S-T",
                "B": "T-T-S",
                "C": "S-T-T",
                "D": "S-S-T"
            },
            "answer": "B"
        }
    ]


    while True:

        print("\n======================================")
        print("    SECTION 2: C MAJOR & FORMULA")
        print("======================================")

        score = 0

        shuffled_questions = questions.copy()

        random.shuffle(shuffled_questions)

        for i, q in enumerate(shuffled_questions, 1):

            if ask_question(q, i):
                score += 1

        print(f"\nYou scored {score}/10")

        if score >= 7:

            print("Congratulations! You have completed Section 2.")

            next_section = input("""
Would you like to continue to Section 3?

A. Yes, continue
B. No, return to the main menu

Your choice: """).strip().upper()

            if next_section == "A":
                break

            elif next_section == "B":
                return

            else:
                print("Invalid choice. Returning to the main menu.")
                return

        else:

            print("You need at least 7/10 to complete this section.")

            retry = input("""
Would you like to try Section 2 again?

A. Yes, try again
B. Return to the main menu

Your choice: """).strip().upper()

            if retry == "A":
                continue

            else:
                return


    # ==========================================
    # SECTION 3: ACCIDENTALS
    # ==========================================

    print("""
==========================================
          SECTION 3: ACCIDENTALS
==========================================

Accidentals change the pitch of notes.

Sharp (♯) = raises a note by one semitone.

Flat (♭) = lowers a note by one semitone.

Natural (♮) = cancels a previous sharp or flat.

For example:

F → F♯
B → B♭

D♯ and E♭ are enharmonic equivalents.
They have the same pitch but different names.
""")

    questions = [
        {
            "question": "What does a sharp do?",
            "options": {
                "A": "Raises a note by one semitone",
                "B": "Lowers a note by one semitone",
                "C": "Raises a note by one tone",
                "D": "Cancels a note"
            },
            "answer": "A"
        },

        {
            "question": "What does a flat do?",
            "options": {
                "A": "Raises a note by one semitone",
                "B": "Lowers a note by one semitone",
                "C": "Raises a note by one tone",
                "D": "Doubles the pitch"
            },
            "answer": "B"
        },

        {
            "question": "What does a natural sign do?",
            "options": {
                "A": "Raises a note",
                "B": "Lowers a note",
                "C": "Cancels a previous sharp or flat",
                "D": "Creates an octave"
            },
            "answer": "C"
        },

        {
            "question": "What note do you get when F is raised by one semitone?",
            "options": {
                "A": "F♭",
                "B": "F♯",
                "C": "G♭♭",
                "D": "E♯"
            },
            "answer": "B"
        },

        {
            "question": "What note do you get when B is lowered by one semitone?",
            "options": {
                "A": "B♯",
                "B": "C",
                "C": "B♭",
                "D": "A"
            },
            "answer": "C"
        },

        {
            "question": "D♯ and E♭ are examples of what?",
            "options": {
                "A": "Octaves",
                "B": "Enharmonic equivalents",
                "C": "Tones",
                "D": "Key signatures"
            },
            "answer": "B"
        },

        {
            "question": "What does enharmonic mean?",
            "options": {
                "A": "Different pitches with the same letter",
                "B": "The same pitch represented by different note names",
                "C": "Two notes one octave apart",
                "D": "Two notes that are always a tone apart"
            },
            "answer": "B"
        },

        {
            "question": "How many different letter names should a major scale contain?",
            "options": {
                "A": "5",
                "B": "6",
                "C": "7",
                "D": "8"
            },
            "answer": "C"
        },

        {
            "question": "Which is the correct seven-letter spelling?",
            "options": {
                "A": "A-B-C-D-E-F-G",
                "B": "A-B-C-D-E-F-F",
                "C": "A-B-C-C-E-F-G",
                "D": "A-B-B-D-E-F-G"
            },
            "answer": "A"
        },

        {
            "question": "Which pair has the same pitch but different note names?",
            "options": {
                "A": "C-D",
                "B": "D-E",
                "C": "D♯-E♭",
                "D": "F-G"
            },
            "answer": "C"
        }
    ]


    while True:

        print("\n======================================")
        print("       SECTION 3: ACCIDENTALS")
        print("======================================")

        score = 0

        shuffled_questions = questions.copy()

        random.shuffle(shuffled_questions)

        for i, q in enumerate(shuffled_questions, 1):

            if ask_question(q, i):
                score += 1

        print(f"\nYou scored {score}/10")

        if score >= 7:

            print("Congratulations! You have completed Section 3.")

            next_section = input("""
Would you like to continue to Section 4?

A. Yes, continue
B. No, return to the main menu

Your choice: """).strip().upper()

            if next_section == "A":
                break

            elif next_section == "B":
                return

            else:
                print("Invalid choice. Returning to the main menu.")
                return

        else:

            print("You need at least 7/10 to complete this section.")

            retry = input("""
Would you like to try Section 3 again?

A. Yes, try again
B. Return to the main menu

Your choice: """).strip().upper()

            if retry == "A":
                continue

            else:
                return


    # ==========================================
    # SECTION 4: KEY SIGNATURES
    # ==========================================

    print("""
==========================================
         SECTION 4: KEY SIGNATURES
==========================================

A key signature is a collection of sharps
or flats written at the beginning of a
piece of music.

It tells us which notes are consistently
raised or lowered throughout the piece.

For example:

F major has one flat:

B♭

Therefore:

F - G - A - B♭ - C - D - E - F
""")

    questions = [
        {
            "question": "What is a key signature?",
            "options": {
                "A": "A type of musical instrument",
                "B": "A collection of sharps or flats that identifies a key",
                "C": "The final note of a scale",
                "D": "A type of rhythm"
            },
            "answer": "B"
        },

        {
            "question": "What does a key signature help identify?",
            "options": {
                "A": "The key of a piece of music",
                "B": "The tempo",
                "C": "The volume",
                "D": "The instrument"
            },
            "answer": "A"
        },

        {
            "question": "A major key signature can contain:",
            "options": {
                "A": "Only sharps and flats together",
                "B": "Sharps or flats",
                "C": "Only natural signs",
                "D": "Only one accidental"
            },
            "answer": "B"
        },

        {
            "question": "How many flats are in the key signature of F major?",
            "options": {
                "A": "0",
                "B": "1",
                "C": "2",
                "D": "3"
            },
            "answer": "B"
        },

        {
            "question": "Which note is flat in F major?",
            "options": {
                "A": "A♭",
                "B": "E♭",
                "C": "B♭",
                "D": "D♭"
            },
            "answer": "C"
        },

        {
            "question": "Which is the F major scale?",
            "options": {
                "A": "F-G-A-B-C-D-E-F",
                "B": "F-G-A-B♭-C-D-E-F",
                "C": "F-G-A-B♯-C-D-E-F",
                "D": "F-G-A-B-C♯-D-E-F"
            },
            "answer": "B"
        },

        {
            "question": "Why is B lowered to B♭ in F major?",
            "options": {
                "A": "To make A-B♭ a semitone",
                "B": "To make A-B♭ a tone",
                "C": "To create an octave",
                "D": "Because all F major notes are flat"
            },
            "answer": "B"
        },

        {
            "question": "What is the distance from A to B♭?",
            "options": {
                "A": "A tone",
                "B": "A semitone",
                "C": "An octave",
                "D": "A third"
            },
            "answer": "B"
        },

        {
            "question": "What is the distance from B♭ to C?",
            "options": {
                "A": "A semitone",
                "B": "A tone",
                "C": "An octave",
                "D": "A fourth"
            },
            "answer": "B"
        },

        {
            "question": "Which major key has no sharps or flats in its key signature?",
            "options": {
                "A": "G major",
                "B": "F major",
                "C": "C major",
                "D": "D major"
            },
            "answer": "C"
        }
    ]


    while True:

        print("\n======================================")
        print("       SECTION 4: KEY SIGNATURES")
        print("======================================")

        score = 0

        shuffled_questions = questions.copy()

        random.shuffle(shuffled_questions)

        for i, q in enumerate(shuffled_questions, 1):

            if ask_question(q, i):
                score += 1

        print(f"\nYou scored {score}/10")

        if score >= 7:

            print("Congratulations! You have completed Section 4.")

            next_section = input("""
Would you like to continue to Section 5?

A. Yes, continue
B. No, return to the main menu

Your choice: """).strip().upper()

            if next_section == "A":
                break

            elif next_section == "B":
                return

            else:
                print("Invalid choice. Returning to the main menu.")
                return

        else:

            print("You need at least 7/10 to complete this section.")

            retry = input("""
Would you like to try Section 4 again?

A. Yes, try again
B. Return to the main menu

Your choice: """).strip().upper()

            if retry == "A":
                continue

            else:
                return


    # ==========================================
    # SECTION 5: BUILDING MAJOR SCALES
    # ==========================================

    print("""
==========================================
       SECTION 5: BUILDING MAJOR SCALES
==========================================

To build a major scale, we start with the
tonic (the starting note) and apply the
major scale formula:

T - T - S - T - T - T - S

Let's look at G major.

G - A - B - C - D - E - F♯ - G

G major contains one sharp: F♯.

Why?

Because E to F is naturally a semitone,
but the major scale requires a tone at
that position.

Raising F to F♯ gives:

E → F♯ = Tone

Then:

F♯ → G = Semitone
""")

    questions = [
        {
            "question": "What should you choose first when building a major scale?",
            "options": {
                "A": "The tonic",
                "B": "The final accidental",
                "C": "The octave",
                "D": "The key signature"
            },
            "answer": "A"
        },

        {
            "question": "Which is the G major scale?",
            "options": {
                "A": "G-A-B-C-D-E-F-G",
                "B": "G-A-B-C-D-E-F♯-G",
                "C": "G-A-B♭-C-D-E-F-G",
                "D": "G-A♭-B-C-D-E-F-G"
            },
            "answer": "B"
        },

        {
            "question": "How many sharps are in G major?",
            "options": {
                "A": "0",
                "B": "1",
                "C": "2",
                "D": "3"
            },
            "answer": "B"
        },

        {
            "question": "Which note is sharp in G major?",
            "options": {
                "A": "C♯",
                "B": "D♯",
                "C": "F♯",
                "D": "G♯"
            },
            "answer": "C"
        },

        {
            "question": "Why is F raised to F♯ in G major?",
            "options": {
                "A": "To make E-F♯ a tone",
                "B": "To make E-F♯ a semitone",
                "C": "To make F♯-G a tone",
                "D": "To create an octave"
            },
            "answer": "A"
        },

        {
            "question": "What is the distance from E to F♯?",
            "options": {
                "A": "Semitone",
                "B": "Tone",
                "C": "Octave",
                "D": "Third"
            },
            "answer": "B"
        },

        {
            "question": "What is the distance from F♯ to G?",
            "options": {
                "A": "Tone",
                "B": "Semitone",
                "C": "Octave",
                "D": "Fourth"
            },
            "answer": "B"
        },

        {
            "question": "Which major key has exactly one sharp?",
            "options": {
                "A": "F major",
                "B": "C major",
                "C": "G major",
                "D": "D major"
            },
            "answer": "C"
        },

        {
            "question": "Which note is NOT part of G major?",
            "options": {
                "A": "G",
                "B": "B",
                "C": "F",
                "D": "F♯"
            },
            "answer": "C"
        },

        {
            "question": "What note completes the G major scale?",
            "options": {
                "A": "F",
                "B": "F♯",
                "C": "G♯",
                "D": "A"
            },
            "answer": "B"
        }
    ]


    while True:

        print("\n======================================")
        print("     SECTION 5: BUILDING SCALES")
        print("======================================")

        score = 0

        shuffled_questions = questions.copy()

        random.shuffle(shuffled_questions)

        for i, q in enumerate(shuffled_questions, 1):

            if ask_question(q, i):
                score += 1

        print(f"\nYou scored {score}/10")

        if score >= 7:

            print("Congratulations! You have completed Section 5.")

            next_section = input("""
Would you like to continue to Section 6?

A. Yes, continue
B. No, return to the main menu

Your choice: """).strip().upper()

            if next_section == "A":
                break

            elif next_section == "B":
                return

            else:
                print("Invalid choice. Returning to the main menu.")
                return

        else:

            print("You need at least 7/10 to complete this section.")

            retry = input("""
Would you like to try Section 5 again?

A. Yes, try again
B. Return to the main menu

Your choice: """).strip().upper()

            if retry == "A":
                continue

            else:
                return


    # ==========================================
    # SECTION 6: SHARP & FLAT ORDERS
    # ==========================================

    print("""
==========================================
      SECTION 6: SHARP & FLAT ORDERS
==========================================

The order of flats is:

B - E - A - D - G - C - F

The order of sharps is:

F - C - G - D - A - E - B

You can remember them as:

BEADGCF
FCGDAEB

These orders help us identify key signatures.
""")

    questions = [
        {
            "question": "What is the order of flats?",
            "options": {
                "A": "B-E-A-D-G-C-F",
                "B": "F-C-G-D-A-E-B",
                "C": "C-G-D-A-E-B-F",
                "D": "A-B-C-D-E-F-G"
            },
            "answer": "A"
        },

        {
            "question": "What is the order of sharps?",
            "options": {
                "A": "B-E-A-D-G-C-F",
                "B": "F-C-G-D-A-E-B",
                "C": "C-F-B-E-A-D-G",
                "D": "G-D-A-E-B-F-C"
            },
            "answer": "B"
        },

        {
            "question": "Which flat appears first in the order of flats?",
            "options": {
                "A": "E♭",
                "B": "A♭",
                "C": "B♭",
                "D": "D♭"
            },
            "answer": "C"
        },

        {
            "question": "Which sharp appears first in the order of sharps?",
            "options": {
                "A": "C♯",
                "B": "F♯",
                "C": "G♯",
                "D": "D♯"
            },
            "answer": "B"
        },

        {
            "question": "How many flats are in B♭ major?",
            "options": {
                "A": "1",
                "B": "2",
                "C": "3",
                "D": "4"
            },
            "answer": "B"
        },

        {
            "question": "How many sharps are in A major?",
            "options": {
                "A": "1",
                "B": "2",
                "C": "3",
                "D": "4"
            },
            "answer": "C"
        },

        {
            "question": "Which flats are in E♭ major?",
            "options": {
                "A": "B♭ and E♭",
                "B": "B♭, E♭ and A♭",
                "C": "B♭, E♭, A♭ and D♭",
                "D": "B♭ only"
            },
            "answer": "B"
        },

        {
            "question": "Which sharps are in E major?",
            "options": {
                "A": "F♯, C♯ and G♯",
                "B": "F♯ and C♯",
                "C": "F♯, C♯, G♯ and D♯",
                "D": "F♯ only"
            },
            "answer": "C"
        },

        {
            "question": "For major keys with flats, how can you identify the key?",
            "options": {
                "A": "Use the first flat",
                "B": "Use the last flat",
                "C": "Use the second-to-last flat",
                "D": "Use the first sharp"
            },
            "answer": "C"
        },

        {
            "question": "Which major key is the exception to the second-to-last-flat rule?",
            "options": {
                "A": "F major",
                "B": "B♭ major",
                "C": "E♭ major",
                "D": "A♭ major"
            },
            "answer": "A"
        }
    ]


    while True:

        print("\n======================================")
        print("    SECTION 6: SHARP & FLAT ORDERS")
        print("======================================")

        score = 0

        shuffled_questions = questions.copy()

        random.shuffle(shuffled_questions)

        for i, q in enumerate(shuffled_questions, 1):

            if ask_question(q, i):
                score += 1

        print(f"\nYou scored {score}/10")

        if score >= 7:

            print("Congratulations! You have completed Section 6.")

            next_section = input("""
Would you like to continue to Section 7?

A. Yes, continue
B. No, return to the main menu

Your choice: """).strip().upper()

            if next_section == "A":
                break

            elif next_section == "B":
                return

            else:
                print("Invalid choice. Returning to the main menu.")
                return

        else:

            print("You need at least 7/10 to complete this section.")

            retry = input("""
Would you like to try Section 6 again?

A. Yes, try again
B. Return to the main menu

Your choice: """).strip().upper()

            if retry == "A":
                continue

            else:
                return


    # ==========================================
    # SECTION 7: CIRCLE OF FIFTHS
    # ==========================================

    print("""
==========================================
        SECTION 7: CIRCLE OF FIFTHS
==========================================

The Circle of Fifths is a diagram that shows
the relationships between major keys.

C major is at the top and has no sharps
or flats.

Moving clockwise:

C → G → D → A → E → B → F♯ → C♯

Each step adds one sharp.

Moving anticlockwise:

C → F → B♭ → E♭ → A♭ ...

Each step adds one flat.

The Circle of Fifths helps us understand
key signatures and relationships between keys.
""")

    questions = [
        {
            "question": "Which major key is at the top of the Circle of Fifths?",
            "options": {
                "A": "G major",
                "B": "F major",
                "C": "C major",
                "D": "D major"
            },
            "answer": "C"
        },

        {
            "question": "How many sharps or flats does C major have?",
            "options": {
                "A": "0",
                "B": "1",
                "C": "2",
                "D": "7"
            },
            "answer": "A"
        },

        {
            "question": "Moving clockwise around the Circle of Fifths takes you toward:",
            "options": {
                "A": "Flat keys",
                "B": "Sharp keys",
                "C": "Minor keys only",
                "D": "Natural notes only"
            },
            "answer": "B"
        },

        {
            "question": "What happens to the number of sharps when moving clockwise?",
            "options": {
                "A": "It decreases",
                "B": "It stays the same",
                "C": "It increases by one",
                "D": "It becomes zero"
            },
            "answer": "C"
        },

        {
            "question": "Which key comes after C when moving clockwise?",
            "options": {
                "A": "F",
                "B": "G",
                "C": "D",
                "D": "B♭"
            },
            "answer": "B"
        },

        {
            "question": "Which key comes after G when moving clockwise?",
            "options": {
                "A": "F",
                "B": "A",
                "C": "D",
                "D": "E"
            },
            "answer": "C"
        },

        {
            "question": "Moving anticlockwise around the Circle of Fifths takes you toward:",
            "options": {
                "A": "Sharp keys",
                "B": "Flat keys",
                "C": "Only minor keys",
                "D": "No key signatures"
            },
            "answer": "B"
        },

        {
            "question": "Which key comes after C when moving anticlockwise?",
            "options": {
                "A": "G",
                "B": "D",
                "C": "F",
                "D": "A"
            },
            "answer": "C"
        },

        {
            "question": "How many flats does B♭ major have?",
            "options": {
                "A": "1",
                "B": "2",
                "C": "3",
                "D": "4"
            },
            "answer": "B"
        },

        {
            "question": "Why is B♭ used in B♭ major?",
            "options": {
                "A": "To make A-B♭ a tone and follow the major scale formula",
                "B": "To make A-B♭ a semitone",
                "C": "To create an octave",
                "D": "Because every note in B♭ major is flat"
            },
            "answer": "A"
        }
    ]


    while True:

        print("\n======================================")
        print("       SECTION 7: CIRCLE OF FIFTHS")
        print("======================================")

        score = 0

        shuffled_questions = questions.copy()

        random.shuffle(shuffled_questions)

        for i, q in enumerate(shuffled_questions, 1):

            if ask_question(q, i):
                score += 1

        print("\n======================================")
        print("              RESULTS")
        print("======================================")

        print(f"You scored {score}/10")

        if score >= 7:

            print("""
==========================================
       MAJOR SCALES COMPLETED!
==========================================

Congratulations!

You have successfully completed all
7 sections of the Major Scales lesson.

You can now:

✓ Identify tones and semitones
✓ Understand the major scale formula
✓ Use accidentals
✓ Understand key signatures
✓ Build major scales
✓ Use sharp and flat orders
✓ Understand the Circle of Fifths

You will now return to the main menu.
""")

            input("Press Enter to return to the main menu...")
            return

        else:

            print("""
You need at least 7/10 to complete
the final section.
""")

            retry = input("""
Would you like to try Section 7 again?

A. Yes, try again
B. Return to the main menu

Your choice: """).strip().upper()

            if retry == "A":
                continue

            else:
                return