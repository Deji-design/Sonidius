from operator import index
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from Lessons.major_scales_question_banks import SECTION_QUESTIONS
import random
from GUI.major_scales_diagrams import insert_keyboard_diagram
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ASSETS_FOLDER = PROJECT_ROOT / "assets"

# Connecting image Placeholders to actual images in the assets folder

DIAGRAMS = {
    "|image:standard_keyboard|":
        "STANDARD KEYBOARD.png",

    "|image:showing_semitones|":
        "STANDARD KEYBOARD (Showing semitones).png",

    "|image:showing_exceptions_B-C_and_E-F|":
        "STANDARD KEYBOARD (Tone exception).png",

    "|image:showing_tones|":
        "STANDARD KEYBOARD (Showing tones).png",

    "|image:showing_C_to_D|":
        "STANDARD KEYBOARD (C major C-D).png",

   }


def insert_keyboard_diagram(text_widget, embedded_diagrams):
    for marker, filename in DIAGRAMS.items():

        marker_index = text_widget.search(marker, "1.0", tk.END)

        if not marker_index:
            continue

        image_path = ASSETS_FOLDER / filename

        if not image_path.exists():
            print(f"Image not found: {image_path}")
            continue

        try:
            with Image.open(image_path) as original:
                image = original.convert("RGB")
                image.thumbnail((600, 350))
                photo = ImageTk.PhotoImage(image)

            # Create a frame to hold the image
            diagram_frame = tk.Frame(
                text_widget,
                bg="#FFF8E7"
            )

            image_label = tk.Label(
                diagram_frame,
                image=photo,
                bg="#FFF8E7"
            )
            image_label.image = photo
            image_label.pack(padx=5, pady=5)

            # Remove the placeholder and insert the image
            text_widget.delete(
                marker_index,
                f"{marker_index}+{len(marker)}c"
            )

            text_widget.window_create(
                marker_index,
                window=diagram_frame,
                padx=5,
                pady=8
            )

            embedded_diagrams.append(diagram_frame)

            print(f"Inserted image: {filename}")

        except Exception as error:
            print(f"Could not load {filename}: {error}")

sections = [
    {"title": "Major Scales", 
    "content": """
Welcome!

Major scales are one of the foundations of music theory. In this lesson, you will learn how major scales are built, how tones and semitones work, how key signatures work, and how the Circle of Fifths connects everything together.

There are 15 major scales in classical music.
Let us begin!"""},

    {"title": "What is a Major Scale?",
     "content": """
A major scale is a sequence of seven different notes arranged according to a specific pattern. 
     
This specific pattern is called the major scale formula. 
The Major scale formula is based on the standard pattern of tones and semitones.
The pattern is clear and quite song-like:

 tone-tone-semitone-tone-tone-tone-semitone (T-T-S-T-T-T-S)

 But wait! What are these strange words?"""},

    {"title": "SECTION 1: TONES & SEMITONES",
     "content": """
These terms may seem confusing at first. What do they actually mean?
Everyone knows that tones have to do with music, and semitones?
They sound kinda like they came from tones. Or did semitones come before tones? 
It’s all so confusing!


So let’s make it simple.
For better understanding, let us think up a piano, keyboard, or organ - whichever one you wish to imagine.
Suppose you have a physical one around- even better! Go to it.
You could also use the image of the keyboard shown below.

|image:standard_keyboard|


Observe how there are both white and black keys. You might think they are there for the classic effect, but they're important.


The invisible space between any adjacent keys (either black and white or white and black) is a semitone.
More specifically, a semitone is the smallest interval (distance) between two adjacent (that means beside one another) keys on a standard piano or keyboard. 

|image:showing_semitones|


You will encounter semitones in many areas of music theory, so it's important to understand this idea. 


Another trick to remember: most neighboring natural notes (the white keys) are a tone apart. 
The exceptions are B–C and E–F, which are a semitone apart.


|image:showing_exceptions_B-C_and_E-F|

After talking about a part of the pair, we move to the other- the tone. A tone is made up of two semitones.
Think of it like a math equation:

1 Semitone + 1 Semitone = 1 Tone


Back to the keyboard, you can often see a tone between two white keys with a black key between them. For example, C to D is a tone. 
Remember our exception, though: B-C and E-F have a semitone each between them. 
You can remember this because they do not have a black key between them.
A tone can also be found between two black keys with a white key between them.


|image:showing_tones|

Now you can celebrate!!!! You have learnt the basics of tones and semitones!      

"""
    },

    {"title": "SECTION 2: C MAJOR & SCALE FORMULA",
     "content": """
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

|image:showing_C_to_D|

We will use our math equation to help us understand.

Remember:
1 Semitone + 1 Semitone = 1 Tone


From white key C to the next black key = 1 Semitone


We also know that from an adjacent black key to a white key is also a semitone.


From the black key to the white key D = 1 Semitone


1 Semitone + 1 Semitone = 1 Tone


Therefore, from white key C to white key D is a tone.


|image:showing_D_to_E|

From the keyboard, we can see that from D to E there is a black key. 
What do you think will be the interval between them?

Because of the little black key, the distance between D and E is once again:


1 Semitone + 1 Semitone = 1 Tone


|image:showing_E_to_F|

E - F


This one is rather easy. Try it out yourself.

|insert image in GUI|

It follows the exception we learnt. From E to F is a semitone.

Can you see a pattern already?

So far we have T - T - S.

F - G

|image:showing_F_to_G|


When we see a black key between two white keys, we know there are two semitones.
And two semitones make a tone.

G - A

|image:showing_G_to_A|

Can you come up with what is next?

From G to A is a tone.

A - B 

|image:showing_A_to_B|

A black key is between the two white keys, once again marking a tone.



B - C 


|image:showing_B_to_C|

Finally, we see the other half of our exception. From B to C is a semitone.

Together, we have matched the  C major scale to the major scale formula.




It’s not hard once you understand the basics!!!
     
"""
    },

    {"title": "SECTION 3: ACCIDENTALS",
     "content": """
     
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

|image:showing_D_to_Dsharp|

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

|image:showing_E_to_Eflat|


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
"""
        },

    {"title": "SECTION 4: KEY SIGNATURES",
     "content": """
But how do we know which notes belong in a particular key?
And how do we know when a note needs a sharp or flat, as we saw in F major?
    
This leads us into our next section:

 SECTION 4: KEY SIGNATURES

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

|image:showing_key_signature|

You may have seen this before: the numbers and the funny-looking G.

The funny-looking symbol is called the treble clef, and the five horizontal lines together are called a staff.

he topmost line on the treble staff is called F.

The sharp sign (♯) in the key signature tells us that every F in this piece is normally played as F♯.
This is much easier than writing a sharp sign every time an F appears.


If we wrote F♯  every time, it would look something like this:

|image:showing_Fsharp|

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

|image:showing_A_to_Bflat|

Do you see that B♭ comes right after A? This shows that they are a semitone apart.


	A - B♭ = 1 Semitone
Another one that might be confusing
Again, to the keyboard.

|image:showing_Bflat_to_C|

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

"""
    },
    
    {"title": "SECTION 5: BUILDING MAJOR SCALES",
     "content": """

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


    |image:showing_B_to_C|

    C - D = 1 Tone
    D - E = 1 Tone
    E - F♯ = 1 Tone
Why?

|image:showing_E_to_Fsharp|

But the major-scale formula requires a tone between E and the next note.
So F needs to be raised by one semitone.
A sharp raises a note by one semitone, so F becomes F♯.

Now:
E - F♯ = 2 Semitones = 1 Tone


    F♯ - G = 1 Semitone
Why?

|image:showing_Fsharp_to_G|

F - G is a tone.
But F♯ is one semitone higher than F.
Therefore, the distance from F♯ to G is only one semitone.
So:
F♯ - G = 1 Semitone 
    """
    },
    {"title": "SECTION 6: SHARP & FLAT ORDERS",
     "content": """

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
B major    - F♯ , C♯ , G♯ , D♯ , A♯ 
F♯ major   - F♯ , C♯ , G♯ , D♯ , A♯ , E♯ 
C♯ major   -F♯ , C♯ , G♯ , D♯ , A♯ , E♯ , B♯ 




Here is another surprising fact. The order of major scales with flats is in the reverse order of the notes that have sharps.


Notes that have flats:    B, E, A, D, G, C, F
Notes that have sharps: F, C, G, D, A, E, B


B → E → A → D → G → C → F
　　　　　　　　　　　　　　
F → C → G → D → A → E → B 
"""
    },

    {"title": "SECTION 7: CIRCLE OF FIFTHS",
     "content": """
    
Finally, we are led to the last section of this lesson.


We have successfully learnt how to build a major scale, use accidentals, and recognize key signatures.
But there are 12 major scales. Do we have to learn every one of them separately, with their accidentals?


Luckily for us, that is not necessary. There is a clever way to organize them. 


 The Circle of Fifths

 The Circle of Fifths is a diagram that shows the relationships between different musical keys. 


Like a circle, all the major scales follow each other in a certain pattern.


The secret about the circle of fifths is that it works a bit like a clock. It has a clockwise side and an anticlockwise side.

|image:showing_circle_of_fifths_with clockwise_and_anticlockwise_sides|

The clockwise side takes us through major scales with sharps, while the anticlockwise side takes us through major scales with flats.
For the clockwise side, we move five notes up each time. For the anticlockwise side, we move five notes back, or four notes up.
Because C major has no sharps or flats, it starts the pattern for both sides.

|image:showing_circle_of_fifths_with_C_at_the_start|

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

|image:showing_circle_of_fifths_with_the_sharp_side|


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

|image:showing_circle_of_fifths_with_the_flat_side|

"""
    }

]

def open_major_scales(parent):
    lesson_window = tk.Toplevel(parent)
    lesson_window.title("Sonidius - Major Scales")
    lesson_window.geometry("850x750")
    lesson_window.configure(bg="#FFF8E7")

# Current section
    current_section = 0
    embedded_diagrams = []


    # Sections the user has passed
    passed_sections = set()

# Lesson heading
    heading = tk.Label(
        lesson_window,
        text="Major Scales",
        font=("Arial", 26, "bold"),
        fg="#6C4AD6",
        bg="#FFF8E7"
    )
    
    heading.pack(pady=(20, 10))

# Section heading
    section_heading = tk.Label(
        lesson_window,
        text="",
        font=("Arial", 17, "bold"),
        fg="#6C4AD6",
        bg="#FFF8E7"
    )
    section_heading.pack(pady=5)

# Placeholder for the lesson notes
    notes = scrolledtext.ScrolledText(
        lesson_window,
        wrap=tk.WORD,
        font=("Arial", 13),
        width=75,
        height=18,
        bg="#FFF8E7",
        fg="#33215F",
        bd=0,
        relief="flat",
        highlightthickness=0,
        spacing1=2,
        spacing2=2,
        spacing3=2
    )

    notes.pack(padx=60, pady=10, fill="both", expand=True)


    def show_section(index):
           nonlocal current_section
   
           # Keep the section index within valid limits
           if index < 0 or index >= len(sections):
               return
   
           # Do not allow users to skip an unpassed section
           if index > current_section and current_section not in passed_sections:
               return
           
            # Remove diagrams from the previous section
           for diagram in embedded_diagrams:
               diagram.destroy()
   
           embedded_diagrams.clear()
   
           
           current_section = index
           section = sections[current_section]
   
           section_heading.config(text=section["title"])
   
           notes.configure(state="normal")
           notes.delete("1.0", tk.END)
           notes.insert(tk.END, section["content"])
       
   
           # Replace any image placeholders in this section
           insert_keyboard_diagram(notes, embedded_diagrams)
                   
           
           notes.configure(state="disabled")
   
           # Update button states
           previous_button.config(
               state="normal" if current_section > 0 else "disabled"
           )
           next_button.config(
               state="normal"
              if current_section in passed_sections
              and current_section < len(sections) - 1
              else "disabled"
           )
   
           # Upgrade progress
           progress_label.config(
               text=f"Section {current_section + 1} of {len(sections)}"
           )

   
    
    
    def start_quiz():
            print("Button clicked!")
            # Get questions for the current lesson section
            section_number = current_section + 1

            print("Section number:", section_number)

            print("Question bank type:", type(SECTION_QUESTIONS))
            print("Available section keys:", list(SECTION_QUESTIONS.keys()))
            
            all_questions = SECTION_QUESTIONS.get(section_number, [])

            # The GUI currently supports these question types
            supported_types = {"multiple_choice", "true_false"}

            # Keep only questions the GUI can display
            available_questions = [
                q for q in all_questions
                if q.get("type") in supported_types
            ]

            if len(available_questions) < 15:
                messagebox.showwarning(
                    "Not Enough Questions",
                    f"This section has only {len(available_questions)} "
                    "questions supported by the quiz GUI. "
                    "At least 15 are needed."
                )
                return

            # Group questions by type
            questions_by_type = {}

            for question in available_questions:
                question_type = question["type"]
                questions_by_type.setdefault(question_type, []).append(question)

            # Select at least one question from each available type
            selected_questions = []

            for question_group in questions_by_type.values():
                selected_questions.append(random.choice(question_group))

            # Fill the remaining places randomly, without repeating questions
            remaining_questions = [
                 q for q in available_questions
                 if q not in selected_questions
            ]

            selected_questions.extend(
                random.sample(remaining_questions, 15 - len(selected_questions))
)

            # Shuffle the final set so the types appear in random order
            random.shuffle(selected_questions)

            questions = selected_questions

            print("Selected question count:", len(questions))
            print("Selected types:", {q["type"] for q in questions})
            print("Questions found:", len(questions))
            
            if not questions:
                messagebox.showinfo(
                    "No Quiz Available",
                    f"There are no quiz questions for Section {section_number} yet."
                )
                return
    
            # Create the quiz window
            quiz_window = tk.Toplevel(lesson_window)
            quiz_window.title("Sonidius - Major Scales Quiz")
            quiz_window.geometry("650x500")
            quiz_window.configure(bg="#FFF8E7")
    
            question_index = 0
            score = 0
    
            quiz_heading = tk.Label(
                quiz_window,
                text="Major Scales Quiz",
                font=("Arial", 22, "bold"),
                fg="#6C4AD6",
                bg="#FFF8E7"
            )
            quiz_heading.pack(pady=15)
    
            progress = tk.Label(
                quiz_window,
                text="",
                font=("Arial", 11),
                bg="#FFF8E7",
                fg="#44405A"
            )
            progress.pack(pady=5)
    
            question_label = tk.Label(
                quiz_window,
                text="",
                font=("Arial", 15, "bold"),
                wraplength=560,
                bg="#FFF8E7",
                fg="#33215F"
            )
            question_label.pack(pady=20, padx=20)
    
            answers_frame = tk.Frame(
                quiz_window,
                bg="#FFF8E7"
            )
            answers_frame.pack(fill="x", padx=35, pady=10)

            # Feedback after an answer
            feedback_label = tk.Label(
                quiz_window,
                text="",
                font=("Arial", 12, "bold"),
                bg="#FFF8E7",
                wraplength=560
            )
            feedback_label.pack(pady=10)
    
            next_question_button = tk.Button(
                quiz_window,
                text="Next Question →",
                font=("Arial", 11),
                state="disabled"
            )
            next_question_button.pack(pady=10)

            def show_question():
                # Clear previous answer buttons
                for widget in answers_frame.winfo_children():
                    widget.destroy()

                feedback_label.config(text="")
                next_question_button.config(
                    text="Next Question →",
                    state="disabled"
                )

                # Check whether the quiz is complete
                if question_index >= len(questions):

                    if score >= 11:
                        # Record that this section has been passed
                        passed_sections.add(current_section)

                        question_label.config(
                             text=(
                                 f"Final Score: {score}/{len(questions)}\n\n"
                                 "Congratulations! You passed this section!"
                            )
                        )

                        if current_section < len(sections) - 1:
                            next_button.config(state="normal")

                            next_question_button.config(
                                text="Continue to Next Section",
                                state="normal",
                                command=lambda: (
                                    quiz_window.destroy(),
                                    show_section(current_section + 1)
                            )
                        )
                        else:
                             next_question_button.config(
                                text="Finish",
                                state="normal",
                                command=quiz_window.destroy
                        )

                    else:
                        question_label.config(
                            text=(
                                f"Final Score: {score}/{len(questions)}\n\n"
                                "You need at least 11 correct answers to pass. "
                                "Please try again!"
                         )
                        )

                        next_question_button.config(
                             text="Try Again",
                             state="normal",
                             command=lambda: (
                                quiz_window.destroy(),
                                start_quiz()
                            )
                        )

                    return

                # Display the current question
                q = questions[question_index]

                progress.config(
                    text=f"Question {question_index + 1} of {len(questions)}"
                )
                question_label.config(text=q["question"])

                def check_answer(selected_answer):
                    nonlocal score

                    # Prevent answering twice
                    for button in answers_frame.winfo_children():
                        button.config(state="disabled")

                    correct_answer = q["answer"]

                    if selected_answer == correct_answer:
                        score += 1
                        feedback_label.config(
                            text="Correct! Well done.",
                            fg="#218838"
                        )
                    else:
                        feedback_label.config(
                            text=f"Not quite. The correct answer is {correct_answer}.",
                            fg="#C0392B"
                        )

                    next_question_button.config(state="normal")

                if q["type"] == "multiple_choice":
                    for option_key, option_text in q["options"].items():
                        button = tk.Button(
                            answers_frame,
                            text=f"{option_key}. {option_text}",
                            font=("Arial", 11),
                            wraplength=520,
                            justify="left",
                            anchor="w",
                            command=lambda key=option_key: check_answer(key)
                        )
                        button.pack(fill="x", pady=4)

                elif q["type"] == "true_false":
                    for answer in ("TRUE", "FALSE"):
                        button = tk.Button(
                            answers_frame,
                            text=answer.title(),
                            font=("Arial", 12),
                            command=lambda value=answer: check_answer(value)
                        )
                        button.pack(fill="x", pady=5)

            
            def go_to_next_question():
                nonlocal question_index
                question_index += 1
                show_question()
            
            next_question_button.config(
            command=go_to_next_question
        )
            # Display the first section
            show_question()
                    
    
    navigation = tk.Frame(lesson_window, bg="#FFF8E7")
    navigation.pack(fill="x", padx=25, pady=12)
            
    previous_button = tk.Button(
        navigation,
        text="← Previous",
        command=lambda: show_section(current_section - 1),
        font=("Arial", 11),
        state="disabled"
                )
    previous_button.pack(side="left")
            
    progress_label = tk.Label(
        navigation,
        text="",
        font=("Arial", 10),
        bg="#FFF8E7",
        fg="#44405A"
    )
    progress_label.pack(side="left", expand=True)
            
    next_button = tk.Button(
        navigation,
        text="Next →",
        command=lambda: show_section(current_section + 1),
        font=("Arial", 11)
                )
    next_button.pack(side="right")
            
    quiz_button = tk.Button(
        lesson_window,
        text="Start Quiz",
        command=start_quiz,
        font=("Arial", 12, "bold"),
        bg="#6C4AD6",
        fg="white",
        activebackground="#5535B5",
        activeforeground="white",
        padx=20,
        pady=8
    )
    quiz_button.pack(pady=(0, 15))
    print("Start Quiz button has been created!")
     # 4. Display the first section
    show_section(0)


