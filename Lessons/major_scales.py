import random


# ==========================================
# FUNCTION FOR ASKING QUESTIONS
# ==========================================

def ask_question(q, question_number):

    print(f"\nQuestion {question_number}: {q['question']}")

    # ==========================================
    # MULTIPLE CHOICE QUESTIONS
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
    # TRUE / FALSE QUESTIONS
    # ==========================================

    elif q["type"] == "true_false":

        print("A. True")
        print("B. False")

        while True:

            user_answer = input("\nYour answer: ").strip().upper()

            # TRUE
            if user_answer in ["A", "TRUE", "T"]:

                if q["answer"] == "TRUE":
                    print("Correct!")
                    return True

                else:
                    print("Incorrect. The correct answer is False.")
                    return False

            # FALSE
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
    # FILL IN THE BLANK QUESTIONS
    # ==========================================

    elif q["type"] == "fill_blank":

        while True:

            user_answer = input("\nYour answer: ").strip().upper()

            if user_answer == "":
                print("Please enter an answer.")
                continue

            # Remove spaces, commas and hyphens
            # so answers such as T, T, S and T-T-S
            # can be accepted
            normalized_user = (
                user_answer
                .replace(" ", "")
                .replace(",", "")
                .replace("-", "")
            )

            normalized_correct = (
                q["answer"]
                .upper()
                .replace(" ", "")
                .replace(",", "")
                .replace("-", "")
            )

            if normalized_user == normalized_correct:

                print("Correct!")
                return True

            else:

                print(f"Incorrect. The correct answer is {q['answer']}.")
                return False


    # ==========================================
    # KEYBOARD QUESTIONS
    # ==========================================

    elif q["type"] == "keyboard":

        print("""
Keyboard:

C  C#  D  D#  E  F  F#  G  G#  A  A#  B
""")

        while True:

            user_answer = input("\nYour answer: ").strip().upper()

            if user_answer == "":
                print("Please enter an answer.")
                continue

            # Allow both # and ♯
            user_answer = user_answer.replace("♯", "#")

            correct_answer = q["answer"].upper().replace("♯", "#")

            if user_answer == correct_answer:

                print("Correct!")
                return True

            else:

                print(f"Incorrect. The correct answer is {q['answer']}.")
                return False


    # ==========================================
    # SCALE-BUILDING QUESTIONS
    # ==========================================

    elif q["type"] == "scale_building":

        while True:

            user_answer = input("\nYour answer: ").strip().upper()

            if user_answer == "":
                print("Please enter an answer.")
                continue

            normalized_user = (
                user_answer
                .replace(" ", "")
                .replace(",", "")
                .replace("-", "")
            )

            normalized_correct = (
                q["answer"]
                .upper()
                .replace(" ", "")
                .replace(",", "")
                .replace("-", "")
            )

            if normalized_user == normalized_correct:

                print("Correct!")
                return True

            else:

                print(f"Incorrect. The correct answer is {q['answer']}.")
                return False


    # ==========================================
    # IDENTIFY THE ERROR QUESTIONS
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

                    print(
                        f"Incorrect. The correct answer is "
                        f"{new_correct_answer}."
                    )
                    return False

            else:

                print("Invalid answer. Kindly input A, B, C, or D.")


    # ==========================================
    # CHALLENGE QUESTIONS
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

                    print(
                        f"Incorrect. The correct answer is "
                        f"{new_correct_answer}."
                    )
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
        # MULTIPLE CHOICE - 30
        # ==========================================

        {
            "type": "multiple_choice",
            "question": "What is a semitone?",
            "options": {
                "A": "Two adjacent tones",
                "B": "The smallest interval between adjacent keys",
                "C": "Three semitones",
                "D": "A complete octave"
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
                "A": "C and D",
                "B": "D and E",
                "C": "E and F",
                "D": "F and G"
            },
            "answer": "C"
        },

        {
            "type": "multiple_choice",
            "question": "Which other natural pair is a semitone apart?",
            "options": {
                "A": "A and B",
                "B": "B and C",
                "C": "C and D",
                "D": "D and E"
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
            "question": "Two white keys with one black key between them are usually separated by a:",
            "options": {
                "A": "Semitone",
                "B": "Tone",
                "C": "Third",
                "D": "Fourth"
            },
            "answer": "B"
        },

        {
            "type": "multiple_choice",
            "question": "What is the interval pattern from C to F?",
            "options": {
                "A": "S-T-T",
                "B": "T-S-T",
                "C": "T-T-S",
                "D": "S-S-T"
            },
            "answer": "C"
        },

        {
            "type": "multiple_choice",
            "question": "Which pair is a tone apart?",
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
            "question": "3 tones are equal to how many semitones?",
            "options": {
                "A": "3",
                "B": "5",
                "C": "6",
                "D": "8"
            },
            "answer": "C"
        },

        {
            "type": "multiple_choice",
            "question": "2 tones are equal to how many semitones?",
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
            "question": "Which note comes immediately after E in the natural note sequence?",
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
            "question": "What note is a tone above C?",
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
            "question": "What note is a semitone above E?",
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
            "question": "What note is a semitone above B?",
            "options": {
                "A": "B#",
                "B": "A#",
                "C": "C",
                "D": "C#"
            },
            "answer": "C"
        },

        {
            "type": "multiple_choice",
            "question": "Which natural pair is NOT a semitone apart?",
            "options": {
                "A": "B-C",
                "B": "E-F",
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
                "A": "A tone is one semitone",
                "B": "A tone is two semitones",
                "C": "A tone is three semitones",
                "D": "A tone is four semitones"
            },
            "answer": "B"
        },

        {
            "type": "multiple_choice",
            "question": "Which pair of natural notes is separated by a tone?",
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
            "question": "What is the interval pattern from C to F?",
            "options": {
                "A": "T-T-S",
                "B": "T-S-T",
                "C": "S-T-T",
                "D": "S-S-T"
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
            "question": "Moving one key to the next key on a keyboard gives a:",
            "options": {
                "A": "Semitone",
                "B": "Tone",
                "C": "Third",
                "D": "Fourth"
            },
            "answer": "A"
        },

        {
            "type": "multiple_choice",
            "question": "Moving two semitones gives a:",
            "options": {
                "A": "Semitone",
                "B": "Tone",
                "C": "Third",
                "D": "Fourth"
            },
            "answer": "B"
        },

        {
            "type": "multiple_choice",
            "question": "What is the correct major-scale interval pattern?",
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
            "question": "What are the first four notes of the C major scale?",
            "options": {
                "A": "C-D-E-F",
                "B": "C-D-F-G",
                "C": "C-E-F-G",
                "D": "C-E-G-B"
            },
            "answer": "A"
        },


        # ==========================================
        # TRUE / FALSE - 5
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
        # FILL IN THE BLANK - 10
        # ==========================================

        {
            "type": "fill_blank",
            "question": "A tone is equal to ___ semitones.",
            "answer": "2"
        },

        {
            "type": "fill_blank",
            "question": "A semitone is the smallest interval between ___ keys.",
            "answer": "adjacent"
        },

        {
            "type": "fill_blank",
            "question": "C-D is ___ semitones.",
            "answer": "2"
        },

        {
            "type": "fill_blank",
            "question": "E-F is ___ semitone.",
            "answer": "1"
        },

        {
            "type": "fill_blank",
            "question": "B-C is ___ semitone.",
            "answer": "1"
        },

        {
            "type": "fill_blank",
            "question": "F-G is ___ semitones.",
            "answer": "2"
        },

        {
            "type": "fill_blank",
            "question": "A-B is ___ semitones.",
            "answer": "2"
        },

        {
            "type": "fill_blank",
            "question": "The first three intervals of C major are ___.",
            "answer": "TTS"
        },

        {
            "type": "fill_blank",
            "question": "The major scale begins with ___ tones.",
            "answer": "2"
        },

        {
            "type": "fill_blank",
            "question": "T-T-S-T-T-T-___ is the complete major-scale pattern.",
            "answer": "S"
        },


        # ==========================================
        # KEYBOARD - 8
        # ==========================================

        {
            "type": "keyboard",
            "question": "Starting from C, move up 1 semitone. What note do you reach?",
            "answer": "C#"
        },

        {
            "type": "keyboard",
            "question": "Starting from C, move up 2 semitones. What note do you reach?",
            "answer": "D"
        },

        {
            "type": "keyboard",
            "question": "Starting from D, move up 1 semitone. What note do you reach?",
            "answer": "D#"
        },

        {
            "type": "keyboard",
            "question": "Starting from E, move up 1 semitone. What note do you reach?",
            "answer": "F"
        },

        {
            "type": "keyboard",
            "question": "Starting from F, move up 2 semitones. What note do you reach?",
            "answer": "G"
        },

        {
            "type": "keyboard",
            "question": "Starting from G, move up 1 semitone. What note do you reach?",
            "answer": "G#"
        },

        {
            "type": "keyboard",
            "question": "Starting from A, move up 2 semitones. What note do you reach?",
            "answer": "B"
        },

        {
            "type": "keyboard",
            "question": "Starting from B, move up 1 semitone. What note do you reach?",
            "answer": "C"
        },


        # ==========================================
        # SCALE BUILDING - 8
        # ==========================================

        {
            "type": "scale_building",
            "question": "C-D-E-___ using the T-T-S pattern.",
            "answer": "F"
        },

        {
            "type": "scale_building",
            "question": "C-D-E-F-G-___",
            "answer": "A"
        },

        {
            "type": "scale_building",
            "question": "C-D-E-F-G-A-___",
            "answer": "B"
        },

        {
            "type": "scale_building",
            "question": "C-D-E-F-G-A-B-___",
            "answer": "C"
        },

        {
            "type": "scale_building",
            "question": "What is the interval pattern in C-D-E-F?",
            "answer": "TTS"
        },

        {
            "type": "scale_building",
            "question": "What is the interval pattern in F-G-A-B?",
            "answer": "TTT"
        },

        {
            "type": "scale_building",
            "question": "What is the interval after B in the C major scale?",
            "answer": "S"
        },

        {
            "type": "scale_building",
            "question": "What is the interval after E in the C major scale?",
            "answer": "S"
        },


        # ==========================================
        # IDENTIFY THE ERROR - 4
        # ==========================================

        {
            "type": "identify_error",
            "question": "Alex says: 'F-G is 1 semitone.' What is wrong?",
            "options": {
                "A": "Nothing is wrong",
                "B": "F-G is 2 semitones",
                "C": "F-G is 3 semitones",
                "D": "F-G is 4 semitones"
            },
            "answer": "B"
        },

        {
            "type": "identify_error",
            "question": "A student says: 'E-F is a tone.' What is wrong?",
            "options": {
                "A": "E-F is 2 tones",
                "B": "E-F is 3 semitones",
                "C": "E-F is a semitone",
                "D": "Nothing is wrong"
            },
            "answer": "C"
        },

        {
            "type": "identify_error",
            "question": "A student says: 'D-E is 2 semitones.' Is there an error?",
            "options": {
                "A": "D-E is 1 semitone",
                "B": "There is no error",
                "C": "D-E is 3 semitones",
                "D": "D-E is 4 semitones"
            },
            "answer": "B"
        },

        {
            "type": "identify_error",
            "question": "A student writes the major-scale pattern as T-T-S-T-T-T-T. What is the error?",
            "options": {
                "A": "The first T should be S",
                "B": "The final T should be S",
                "C": "The third S should be T",
                "D": "There is no error"
            },
            "answer": "B"
        },


        # ==========================================
        # CHALLENGE / APPLICATION - 5
        # ==========================================

        {
            "type": "challenge",
            "question": "Starting from C, move up 4 semitones. What note do you reach?",
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
            "question": "Starting from E, move up 3 semitones. What note do you reach?",
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
            "question": "The first three notes of a major scale starting on C follow T-T. Which notes are they?",
            "options": {
                "A": "C-D-E",
                "B": "C-D-F",
                "C": "C-E-F",
                "D": "C-E-G"
            },
            "answer": "A"
        },

        {
            "type": "challenge",
            "question": "Starting from C, move T-T-S. What note do you reach?",
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
            "question": "Which type of scale follows the pattern T-T-S-T-T-T-S?",
            "options": {
                "A": "Major scale",
                "B": "Minor scale",
                "C": "Chromatic scale",
                "D": "Pentatonic scale"
            },
            "answer": "A"
        }

    ]


    # ==========================================
    # CHECK QUESTION BANK
    # ==========================================

    multiple_choice_questions = []
    true_false_questions = []
    fill_blank_questions = []
    keyboard_questions = []
    scale_building_questions = []
    identify_error_questions = []
    challenge_questions = []

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
    # TEST LOOP
    # ==========================================
    #
    # The student can retry the test without
    # repeating the teaching notes.
    #

    while True:

        # ==========================================
        # CREATE A NEW RANDOM TEST
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

        # 2 Fill in the Blank
        selected_questions.extend(
            random.sample(fill_blank_questions, 2)
        )

        # 2 Keyboard
        selected_questions.extend(
            random.sample(keyboard_questions, 2)
        )

        # 2 Scale Building
        selected_questions.extend(
            random.sample(scale_building_questions, 2)
        )

        # 1 Identify the Error
        selected_questions.extend(
            random.sample(identify_error_questions, 1)
        )

        # 2 Challenge
        selected_questions.extend(
            random.sample(challenge_questions, 2)
        )

        # Shuffle the final 15 questions
        random.shuffle(selected_questions)


        # ==========================================
        # RUN THE TEST
        # ==========================================

        score = 0

        print("""
==========================================
          SECTION 1 TEST
==========================================

You will receive 15 questions.

Your questions will be randomly selected
from the question bank.

You need at least 11/15 to pass.

Good luck!
""")


        for i, question in enumerate(selected_questions, 1):

            if ask_question(question, i):

                score += 1


        # ==========================================
        # DISPLAY RESULTS
        # ==========================================

        print("""
==========================================
             TEST COMPLETE
==========================================
""")

        print(f"You scored {score}/15.")

        percentage = (score / 15) * 100

        print(f"Percentage: {percentage:.1f}%")


        # ==========================================
        # PASS
        # ==========================================

        if score >= 11:

            print("""
Congratulations!

You passed Section 1: Tones & Semitones.

You are ready to continue to the next section.
""")

            input("Press Enter to continue...")


            while True:

                next_section = input("""
Would you like to continue to Section 2?

A. Yes, continue
B. No, return to the main menu

Your choice: """).strip().upper()


                if next_section == "A":

                    # Section 2 will go here later
                    print("\nSection 2 coming soon!")

                    return


                elif next_section == "B":

                    return


                else:

                    print("Invalid choice. Kindly input A or B.")


        # ==========================================
        # FAIL
        # ==========================================

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

                    # Continue the test loop.
                    # This creates a completely new
                    # random set of 15 questions.
                    break


                elif retry == "no":

                    return


                else:

                    print("Kindly input 'yes' or 'no'.")

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

We have successfully cleared the C major scale. But you have probably heard of a sharp or a flat.
Maybe you have even seen these weird symbols : ♯, ♭, ♮ . Moving forward, we will explore what they mean.

If we want to move a note a semitone up or a semitone down, what do we do? This is when the magic of accidentals comes into play. 


WHAT ARE ACCIDENTALS?
Accidentals are symbols that change a note’s pitch.
Seems strange, right? Why do we need to change the pitch of notes? Don’t worry, we will find out later.


There are three main accidentals:


♯ SHARPS       - raise a note by one semitone 
♭ FLATS           - lower a note by one semitone 
♮ NATURALS  - cancel a previous sharp or flat


SHARPS ♯
Sharps raise a note by a semitone.
Think of them as always wanting more. They are not satisfied with what they have, and they want more- a semitone more.


For example,


D♯ is one semitone higher than D.


On the keyboard, D♯ would be the black key immediately to the right of the white key D 

|insert picture in GUI|

They also change the distance between notes.
Look at this:


The distance between C and D    = 1 tone
The distance between C and D♯  = 1 tone and 1 semitone


We'll explore this idea in much more detail when we learn about intervals. 


FLATS ♭
Flats lower a note by a semitone.
Similar to their sharp brothers, flats also change by a semitone. The difference between them is that a flat is more generous - it gives away a semitone, lowering the note by one semitone.


For example, 
	
E♭ is one semitone lower than E.


On the keyboard, E♭ is the black key immediately to the left of the white key E.

|insert picture in GUI|


Did you notice that the D♯ and the E♭ are on the same black key? 
Let’s look at why.


D♯ and E♭ are written differently and have different names, but on a standard piano, they produce the same pitch. 
This means you hear the same sound. These are called enharmonic equivalents. 


 In an accurately written seven-note major scale, all the seven letters of music (A-B-C-D-E-F-G) must be used exactly once.


For example,
In an F major scale 
F–G–A–B♭–C–D–E
The fourth note must be called B-flat. “Why?” you may ask. There must be a B-flat. This is because the scale needs to have all seven letters (F-G-A-B-C-D-E) in that order.


Why not use A♯?
Both A♯ and B♭ have the same pitch, so why can’t we use either one?


If we use A♯, there would be two A’s. Not only would that make the scale harder to read, but it would also look kinda weird.  
So we use B♭, not A♯ 




What if we run into a problem and we have to cancel the effect of an accidental? What do we do?
We enter the Natural!


NATURAL ♮
Naturals cancel the effect of a sharp or flat affecting a note, returning the note to its natural pitch.
They are the guys that keep things in moderation. They cancel the effect of sharps and flats, bringing notes back to their natural pitch. 


For example,


F♯ → F♮
F♯ was raised by a semitone, but we want the original F back. All we have to do is add a natural accidental.
Similarly:
B♭ → B♮
B♭ was lowered by a semitone. To return it to the original B, we add the natural accidental.


We have reached another milestone!! Now we understand accidentals.
Moving forward, we are going to discuss another exciting section.


Remember the major scale formula? 
T - T - S - T - T - T - S


This gives the major scales their unique sound - the sound we often sing.
Do - Re - Mi - Fa - Sol - La - Ti - Do.
This “song” is a different way to name notes.
But how do we know which notes belong in a particular key?
And how do we know when a note needs a sharp or flat, as we saw in F major?

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


But how do we know which notes belong in a particular key?
And how do we know when a note needs a sharp or flat, as we saw in F major?
    
This leads us into our next section:
  
==========================================
         SECTION 4: KEY SIGNATURES
==========================================

KEY SIGNATURES
Remember F major?
F - G - A - B♭ - C - D - E - F
We found out that a B♭ is needed to make the major-scale formula work.
T – T – S – T – T – T – S 
Imagine you were writing a musical piece in F major. Would you want to put a flat after every B you need? That would be very stressful. You might even give up on the piece.


Thankfully, we do not need to go through that stress.
Why so? Key signatures!


A key signature is a collection of sharps or flats written at the beginning of a piece of music. It helps identify the key and tells us which notes are consistently sharpened or flattened. Each major key has its own key signature, much like a signature helps identify a person.


Look below

|insert picture in GUI|

You may have seen this before: the numbers and the funny-looking G.

The funny-looking symbol is called the treble clef, and the five horizontal lines together are called a staff.

he topmost line on the treble staff is called F.

The sharp sign (♯) in the key signature tells us that every F in this piece is normally played as F♯.
This is much easier than writing a sharp sign every time an F appears.


If we wrote F♯  every time, it would look something like this:

|insert picture in GUI|

Quite frustrating.


A standard major-key key signature contains either sharps or flats, not a mixture of both. 


Back to F major,

F - G - A - B♭ - C - D - E - F

Previously, we have seen how the major-scale formula is applied.
Let’s jog our memory with another example! 
Look at the distance between each note:
	F - G = 1 Tone
	G - A = 1 Tone:
	A - B♭ = 1 Semitone
You might ask yourself how? Let’s go back to the keyboard.

|insert picture in GUI|

Do you see that B♭ comes right after A? This shows that they are a semitone apart.


	A - B♭ = 1 Semitone
Another one that might be confusing
Again, to the keyboard.

|insert picture in GUI|

We can see that B♭ - B is a semitone. We can also remember that B - C is a semitone.
Therefore, B♭ - C contains two semitones
B♭ - B - C 
1 semitone + 1 semitone = 1 Tone
Now you can see why B♭ - C is a tone 	


C - D = 1 Tone
	D - E = 1 Tone
Remember the exception:
	E - F = 1 Semitone


We can finally see how the major-scale formula is applied.


F - G - A - B♭ - C - D - E - F     =     T – T – S – T – T – T – S 


Now you know how to form the F major scale!!


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

We have discovered how to build the F major scale. 
We also figured out that key signatures tell us which note to sharpen or flatten.
But F major has a flat; what if we need a sharp?


Let’s put your brains to the test!


Our next major scale is G major; it has one sharp.
Can you find out what note needs to be sharpened and which note completes the scale?
Remember to use the major-scale formula
T - T - S - T - T -T - S
Using this, you can find your way. Start with G

G - ? - ? - ? - ? - ? - ? - G

This is your task:
Build the G major scale!




You did well; let’s see if you understand the why.


 From 
	G - A = 1 Tone
	A - B = 1 Tone
	B - C = 1 Semitone (The exception)



|insert picture in GUI|

    C - D = 1 Tone
    D - E = 1 Tone
    E - F♯ = 1 Tone
Why?

|insert picture in GUI|

But the major-scale formula requires a tone between E and the next note.
So F needs to be raised by one semitone.
A sharp raises a note by one semitone, so F becomes F♯.

Now:
E - F♯ = 2 Semitones = 1 Tone


    F♯ - G = 1 Semitone
Why?

|insert picture in GUI|

F - G is a tone.
But F♯ is one semitone higher than F.
Therefore, the distance from F♯ to G is only one semitone.
So:
F♯ - G = 1 Semitone

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

These orders help us identify key signatures.

You are slowly (or maybe already have) learning how accidentals are used in forming major scales.




We will move on to a major scale with two flats.


The name of the major scale is B♭ major.


The cool thing about major scales is that the accidentals are added in a specific order as we move to new major scales. 


For example, F major has one flat, while B♭ major has two. 
The flat in F major is on B. When we move to B♭ major, that flat stays, and the note E is flattened. 


F major   - flat on B
B♭ major - flats on B and E
 


The same theory works on major scales with sharps. The sharp in G major is on F. When we move to D major, that sharp stays, and another sharp is added to C. 


G major - sharp on F
D major - sharp on F and C



It's better to commit to memory which notes have accidentals, since you can’t always calculate them conveniently. 


Flats
F major  -  B♭
B♭ major - B♭, E♭
E♭ major - B♭, E♭, A♭
A♭ major - B♭, E♭, A♭, D♭
D♭ major - B♭, E♭, A♭, D♭, G♭
G♭ major - B♭, E♭, A♭, D♭, G♭, C♭
C♭ major - B♭, E♭, A♭, D♭, G♭, C♭, F♭


It might look overwhelming at first glance, but take a deep breath and calm down.
Use what you have learnt to write the major scales and compare them to the one above. You will find out they are similar. If not, go back and revise the lesson.


Another tip: for major keys with flats, the key is named after the second-to-last flat. 
For example, the second-to-last flat of B♭ is B♭.
The second-to-last flat of A♭ is A♭.
The second-to-last flat of G♭ is G♭ , and so on.
The only exception is F major, as it only has one flat and therefore no second-to-last.
This only works for major scales with flats, though.



Sharps
G major    - F♯ 
D major    - F♯ , C♯ 
A major    - F♯ , C♯ , G♯ 
E major    - F♯ , C♯ , G♯ , D♯ 
B major   - F♯ , C♯ , G♯ , D♯ , A♯ 
F♯ major - F♯ , C♯ , G♯ , D♯ , A♯ , E♯ 
C♯ major -F♯ , C♯ , G♯ , D♯ , A♯ , E♯ , B♯ 




Here is another surprising fact. The order of major scales with flats is in the reverse order of the notes that have sharps.


Notes that have flats:    B, E, A, D, G, C, F
Notes that have sharps: F, C, G, D, A, E, B


B → E → A → D → G → C → F
　　　　　　　　　　　　　　
F → C → G → D → A → E → B 

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

Finally, we are led to the last section of this lesson.


We have successfully learnt how to build a major scale, use accidentals, and recognize key signatures.
But there are 12 major scales. Do we have to learn every one of them separately, with their accidentals?


Luckily for us, that is not necessary. There is a clever way to organize them. 


 The Circle of Fifths
The Circle of Fifths is a diagram that shows the relationships between different musical keys. 


Like a circle, all the major scales follow each other in a certain pattern.


The secret about the circle of fifths is that it works a bit like a clock. It has a clockwise side and an anticlockwise side.

|insert picture in GUI|

The clockwise side takes us through major scales with sharps, while the anticlockwise side takes us through major scales with flats.
For the clockwise side, we move five notes up each time. For the anticlockwise side, we move five notes back, or four notes up.
Because C major has no sharps or flats, it starts the pattern for both sides.

|insert picture in GUI|

For example,
All major scales with a sharp are five notes apart.


We start with C and count up five notes.


C - D - E - F - G
We land on G major.
Another five notes:


G - A - B - C - D


We land on D major.

Can you try the next one?


D - ? - ? - ? - ?


It’s:


D - E - F - G - A

We land on A major.
Do you see the pattern?


C - G - D - A
As you continue adding five notes, you will eventually come to  this:


C → G → D → A → E → B → F♯ → C♯


What is something you notice about the key signature (number of sharps) as we move?

Another thing to notice is that as you go up, the number of sharps increases.


C major - 0 sharps
G major - 1 sharp
D major - 2 sharps
A major - 3 sharps
E major - 4 sharps 
…




There is also a way to predict notes that would have sharps!


Remember that the first scale with a sharp is G major, and it has a sharp on F.


To get the next sharp, also count five notes up.


F - G - A - B - C 


So the next sharp is on C.
To go a bit further,
C - D - E - F - G


The next sharp would be on G.
The notes that receive sharps follow the same five-notes-up pattern. 


To make it easier, let's use a diagram.

|insert picture in GUI|


So you see how easy it is to remember, and how to remember if you forget.


Moving on.
We go to the flats.


The pattern for flats, as stated earlier, is four notes up. Four notes up can also be thought of as five notes backward, whichever works best for you.


Once again, we start from C.
Counting four notes upward:


C - D - E - F


Counting five notes backwards,


C - B - A - G - F

So you see we get the same answer.

Further:


Counting four notes upward,


F - G - A - B


Counting five notes backwards:
F - E - D - C - B


Once again, we get the same answer.
Not as hard as it seemed, right?

But we have a problem: we just found out the next note is B, but from what we know, the name of the scale is B♭.

Why is that?


Let's bring back our knowledge of the major scale formula.
 T - T - S - T - T - T - S 


Since we are dealing with four notes upward, what part of the major scale formula would we use?


_  -  _  - _  


We will use T - T - S. 
Let’s work it out.
From F to G  is a tone.
From G to A is a tone.
But from A to B is a tone.
We need a semitone!


To reduce the distance between A and B from a tone to a semitone, we need to lower B by a semitone.


What can we use to lower B by a semitone?


A flat lowers a note by a semitone.
Therefore,


B → B♭ 


Now the distance from A to B♭  is a semitone, giving us the T - T - S we need.


This is why some major scale names have accidentals. To ensure they follow the major scale formula.

Like the scales with sharps, as we move forward, the number of flats increases.


C major - 0 flats
F major - 1 flat
B♭ major - 2 flats
E♭ major - 3 flats
A♭ major - 4 flats
…


Let’s finalize this section with an updated diagram of the Circle of Fifths.

|insert picture in GUI|

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
            

print(""""
"Congratulations, you have covered all the basics to understand major scales!!!
You should be proud of yourself for making it this far. Well done!!


Once in a while, go through this lesson and practice diligently. Everything you have learnt will stick like glue.


""")