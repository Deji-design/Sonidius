import random

<<<<<<< HEAD
# Lesson begins
    print("""Welcome

WHAT IS A MAJOR SCALE?

It is a sequence of seven different notes arranged according to a specific pattern.

Majors scales are based on the Major scale formula. The Major scale formula is based on the pattern of tones and semitones. 
The pattern is tone-tone-semitone-tone-tone-tone-semitone.

WHAT ARE TONES AND SEMITONES?

A tone is a full step, while a semitone is a half step.
A piano is a visual representation of tones and semitones. 
A semitone is the distance between two adjacent keys on a piano.
And a tone consists of two semitones.


AN EXAMPLE?
The C major scale is a good example of a major scale. The C major scale consists of the following notes: C, D, E, F, G, A, B, C.





=======
>>>>>>> 6b644958f4c89a2cc0849acb9353a93154c616c2

# ==========================================
# FUNCTION FOR ASKING QUESTIONS
# ==========================================

def ask_question(q, question_number):

    print(f"\nQuestion {question_number}: {q['question']}")

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

Let's begin!
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


    # ==========================================
    # SECTION 1: TONES AND SEMITONES
    # ==========================================

    print("""
==========================================
       SECTION 1: TONES & SEMITONES
==========================================

Before we build major scales, we need to
understand tones and semitones.

A semitone is the smallest interval between
two adjacent keys on a standard piano.

Two semitones make one tone.

For example:
C → C# = semitone
C → D  = tone

Remember that E-F and B-C are natural
semitones.

The other adjacent natural notes are tones.

C-D = Tone
D-E = Tone
E-F = Semitone
F-G = Tone
G-A = Tone
A-B = Tone
B-C = Semitone

The major scale pattern is:

T - T - S - T - T - T - S
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


    while True:

        print("\n======================================")
        print("       SECTION 1: TONES & SEMITONES")
        print("======================================")

        score = 0

        # Copy the questions
        shuffled_questions = questions.copy()

        # Shuffle the questions
        random.shuffle(shuffled_questions)

        for i, q in enumerate(shuffled_questions, 1):

            if ask_question(q, i):
                score += 1

        print("\n======================================")
        print("              RESULTS")
        print("======================================")

        print(f"You scored {score}/{len(questions)}")

        if score >= 7:

            print("Congratulations! You have completed Section 1.")

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

The major scale follows a specific pattern:

T - T - S - T - T - T - S

C major is the easiest major scale to build
because it contains no sharps or flats.

C major:

C - D - E - F - G - A - B - C

The scale contains seven different note names
before returning to C.

The distance from one C to the next C is called
an octave.
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