def note_intervals():
    print("""Welcome to Note Intervals
Before you start, here's the big idea:
An interval is the distance between two notes.
For example:
C → E
There are two things you need to figure out:

1. The interval number — How many letter names apart are the notes?

   * C → D = 2nd

   * C → E = 3rd

   * C → F = 4th

2. The interval quality — How many semitones are between them?

   * C → E = 4 semitones → Major 3rd

   * C → Eb = 3 semitones → Minor 3rd

Your Core Strategy
Every time you see two notes, ask yourself:
"What number is it?" → "What quality is it?"
Step 1: Count the letter names.
Step 2: Count the semitones.
Step 3: Combine them.
What You'll Learn
You'll progress through 6 levels, starting with simple intervals and gradually working toward accidentals, diminished and augmented intervals, ascending/descending intervals, and challenging enharmonic spellings.
You don't need to memorize everything at once. The tutor will explain your mistakes and help you recognize the patterns.
Quick Warm-Up
C → D
What interval do you think this is?
A) Major 2nd
B) Minor 2nd
C) Major 3rd
D) Perfect 4th
Hint: First count the letter names: C → D = ?
Let's begin.""")

    answer = input ("Write your choice option here: ")
    if answer == "A" :
        print ("Correct, C → D is a Major 2nd")
    elif answer == "B" :
        print ("Close, but the answer is Major 2nd")
    elif answer == "C" :
        print ("ALmost there, But the answer is Major 2nd")
    elif answer == "D" :
        print ("Not quite, the answer is Major 2nd")
    else :
        print ("Kindly input a letter")


