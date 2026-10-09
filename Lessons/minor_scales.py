import random

from Lessons.major_scales import ask_question
from Lessons.minor_scale_question_banks import SECTION_QUESTIONS


def minor_scales():
    print("""




    ==========================================
        SONIDIUS - MINOR SCALES
    ==========================================


   INTRODUCTION

If you are joining this lesson from the previous one, welcome back!!!!!!!!!
However, if you are here for your first lesson, get ready to advance your musical knowledge.

Minor scales can seem complicated at first, but a solid foundation in major scales makes them much easier to understand.
Because minor scales are closely related to major scales, many of the ideas you've already learned will help you throughout this lesson.
However, if you don’t have a solid understanding of major scales, you can review the previous lesson on major scales, which explains everything in detail.


INTRODUCTION TO MINOR SCALES

As usual, we’ll be going through this lesson with the help of our keyboard image.
If you have a physical keyboard instrument (keyboard, piano, or organ), you can use that too.

With a quick revision of major scales, we know that:

    All major scales follow the major scale formula (Tone - Tone - Semitone - Tone - Tone - Tone - Semitone)

    There are three main accidentals: sharp, flat, and natural

    Some notes can have different letters but sound the same pitch (enharmonic equivalents)

    Key signatures make writing music easy, preventing repetition of accidentals

    Major scales can have sharps or flats but not both at the same time

    All major scales can be summarized or derived with the aid of the Circle of fifths.

As said earlier, minor scales and major scales are closely related. 
Imagine them as family members; the major scale is the older sibling, while the minor scale is the younger sibling. 
Every minor scale has one relative major, and every major scale has one relative minor. 
Each pair shares the same notes and key signature but starts on a different note.


If we have a minor scale and we are looking for a major similar to it, we are looking for its relative major. 
Similarly, if we have a major scale and we are looking for the minor scale similar to it, we are looking for the relative minor.


    A major related to a minor = relative major
    

""")


    print("""

==========================================
    SECTION 1 - RELATIVE MINOR CONNECTION
==========================================

Every minor scale shares the same notes and key signature as its relative major scale.
But how do we know a minor scale’s relative major?

It is surprisingly easier than you think.
Choose a minor scale and count three semitones forward from its tonic

Starting with the simplest minor scale, one without accidentals, we’ll make an example.
The minor scale without any accidentals is the A minor scale.

Without counting, what major scale do you think would be its relative major?

By counting, we’ll find its relative major.

        A → A♯ → B → C

We moved three semitones forward, so the relative major of A minor is C major.

If you prefer a diagram, look below:

|insert picture in GUI|

Now you see how to find the relative major of a minor scale. Not hard at all.

Remember what was previously stated: minor scales share the same notes and key signatures as their relative majors.

How? You might ask.

We know C is the relative major of A minor.

We also know that the notes in C major are:

        C - D - E - F - G - A - B

So, what about A minor? We can construct it using a unique pattern.
Just as the major scales have a unique pattern, minor scales have theirs too.

The natural minor scale formula has five tones and two semitones (like the major scale formula).
The difference is that the arrangement is different.

Major scale formula:

    Tone - Tone - Semitone - Tone - Tone - Tone - Semitone

Natural minor scale formula:

    Tone - Semitone - Tone - Tone - Semitone - Tone - Tone

Five Tones, two semitones, but in different arrangements.

It is called the natural minor scale formula because there are other types of minor scales.
For now, we are only focusing on natural minor scales.

Using the natural minor scale formula, we will construct the A minor scale.

Can you try it out first?

        A - _ - _ - _ - _ - _ - A

The A minor scale has the notes.

        A - B - C - D - E - F - G - A

Look at how the scale was made from the formula

From:

A - B = 1 Tone
B - C = 1 Semitone
C - D = 1 Tone
D - E = 1 Tone
E - F = 1 Semitone
F - G = 1 Tone
G - A = 1 Tone 


Do you see how they relate? If you don’t understand, we talked about tones and semitones in the major scales lesson.

If you compare the C major scale to the A minor scale, what do you see?

They have completely different notes.
They have the same notes but in a different starting order.
They have the same notes and the same order.

They have the same seven notes, but they start on different notes and follow different interval patterns.
C major: C – D – E – F – G – A – B – C
A natural minor: A – B – C – D – E – F – G – A
This is why C major and A minor are called relative scales.

Just as C major has no accidentals in its key signature, A minor has no accidentals in its key signature.

Because A minor has no accidentals in its key signature, you might not immediately notice the connection between it and its relative major. 

""")

    questions = SECTION_QUESTIONS[1]

    while True:
        choice = input("\nType 'yes' to take the Section 1 quiz or 'no' to return to the main menu: ").strip().lower()
        if choice == "yes":
            break
        if choice == "no":
            return
        print("Kindly input 'yes' or 'no'.")

    while True:
        print("\n======================================")
        print("   SECTION 1 QUIZ: RELATIVE MINOR")
        print("======================================")

        score = 0
        selected_questions = random.sample(questions, 15)

        for question_number, question in enumerate(selected_questions, 1):
            if ask_question(question, question_number):
                score += 1

        print(f"\nYou scored {score}/15")

        if score >= 11:
            print("Congratulations! You have completed Section 1 of Minor Scales.")
            return

        print("You need at least 11/15 to complete this section.")
        while True:
            retry = input("\nType 'yes' to try Section 1 again or 'no' to return to the main menu: ").strip().lower()
            if retry == "yes":
                break
            if retry == "no":
                return
            print("Kindly input 'yes' or 'no'.")

    
print("""

MINORS WITH ACCIDENTALS

To see how minor scales with accidentals relate to their relative majors, let’s use a minor scale with one sharp in its key signature.

Before we name the minor scale, which major scale do you think would be its relative major? (Hint: think of a major scale that has one sharp.)



It is G major!

Since we know the relative major, we can find the minor.
What do you think it will be?




It is E minor  

How?

Remember, if we are looking for a relative minor, we count three semitones backwards from the major scale’s tonic. If we are looking for a relative major, we count three semitones forward from the minor scale’s tonic.

Looking for a relative minor
Count three semitones backwards
<============================


Looking for a relative major
Count three semitones forward
=============================>

Since we are looking for the relative minor of G major, we are going to count three semitones back.

G → F♯ → F → E

And that's how we can find the relative minor of any major scale: count three semitones backwards from its tonic. 

So G is the relative major of E minor.

Notice that both scales have a sharp in their key signature.

E minor: E - F♯  - G - A - B - C - D - E 
G major: G - A - B - C - D - E - F♯  - G 

They contain the same seven notes. 



Before you think to yourself, “ This is a lot of work! Do I have to learn all the natural minors and their relative majors?” – wait.

Just as you did not need to memorize all the major scales, you don’t need to memorize every minor scale and its relative major. 

We can use what helped us in the major scales lesson: The Circle of Fifths!

CIRCLE OF FIFTHS (MINOR SCALES EDITION)

Imagine you are a baker who is really good at making pancakes. You can make any pancake from scratch. However, because you are very busy, you like to use pancake mix. It is a quicker way to make pancakes, and the pancakes still taste yummy!

The Circle of Fifths is the pancake mix. 

It helps us find minors and their relative majors easily. However, we are still bakers! That means we still need to learn how to find a minor’s relative major from scratch.

Once we know how to do it from scratch, the Circle of Fifths gives us a much quicker way to get the same answer.

Let’s look at a picture of the Circle of Fifths.









You see how all the major scales are shown on the circle.


If you don’t know or have forgotten the pattern for the Circle of Fifths, here it is.

To find the next major scale with sharps in its key signature, count five note names forward from the previous major scale tonic.

Let’s see an example,  

We’ll start with C major because it has no sharps or flats in its key signature.

To find the next major scale with a sharp, we will count five note names forward from C.

C → D → E → F → G
1 →  2 →  3 →  4 →  5


As we can see, G major is the next major with sharps, and it has one sharp.


Let’s try another one!

What will be the next major scale with sharps, and how many sharps will it have?

Major scale →
Number of sharps →

It’s the D major scale, and it has 2 sharps.

The pattern for major scales with sharps is moving five note names forward around the Circle of Fifths. Each time we move to the next major scale, we add one sharp.



How about major scales with flats?

Simple! Count five note names backwards. If you prefer to move forward, however, you can count four note names forward.

Again, we’ll start with C major.


Five note names backwards.

C → B → A → G → F 
1  →  2 →  3 →  4 →  5

Or, four note names forward.

C → D → E → F 
1  →  2 →  3 →  4


Either way, we still arrive at F major, which has one flat.

Earlier in the lesson, we found out that we could find relative minor scales from major scales. Since the Circle of Fifths contains all the major scales, we can fit all the minor scales as well.

For starters, we already know the relative minor scales of some major scales.

C major → A minor
G major → E minor

What comes next on the Circle? D major!
What do you think the relative minor of D major is? 
(Hint: count three semitones backward)



It’s B minor!

Again, we go to the Circle; we now have three minor scales in place.

(add picture)





Now it’s your turn!

Try to find the relative minors for all the remaining major scales with sharps.
You can use the Circle of Fifths as a guide.





A major  →
E major →
B major  →
F♯ major →


Now that you know how to find relative minors of major scales with sharps in their key signature, you can do the same for major scales with flats.


The first major scale with a flat is F major. It has one flat. Let’s find the relative minor of F major.

Move three semitones backwards.

(put a picture of the movement of three semitones using a keyboard)






F → E → D♯ → D


Notice that D♯ appears as one of the steps because we are counting in semitones and not just counting note names.

Therefore, the relative minor of F major is D minor.

Try finding the relative minor of the other major scales with flats in their key signature.

B♭ major →
E♭ major →
A♭ major →
D♭ major →
G♭ major →
C♭ major →



In this exercise, did some of your answers have sharps? Don’t be discouraged!
You aren’t technically wrong. However, since we are dealing with major scales that have flats in their key signature, there is a more accurate way to write the relative minor scales.
What do I mean?

For example, the relative minor of D♭ major is B♭ minor. Why not A♯ minor, though?

Both A♯ and B♭ have the same pitch and make the same sound, so they can be compared to a person with different names. This means A♯ and B♭ are enharmonic equivalents. 
(If you don’t understand this term, go back to the major scales lesson)

Just as people can have different names depending on the situation, the names of notes also depend on musical context (or “musical situations”).

Remember how we said that minor scales must follow the key signatures of their relative majors?

The notes in D♭ major are:
D♭ – E♭ – F – G♭ – A♭ – B♭ – C – D♭ 

Therefore, its relative minor must use these same seven notes, but in a different order:
B♭ – C – D♭ – E♭ – F – G♭ – A♭ – B♭
Notice that there is no A♯ in D♭ major. If we called the relative minor A♯ minor, we would be using a note that isn't part of the D♭ major collection.
That is why B♭ is the correct spelling of the relative minor of D♭  major.

Same pitch, different spelling — the musical context tells us which name to use.

Here is the updated picture of our Circle of fifths (Minor Scales Edition)








We are finally done with everything you need to know about the basics of natural minor scales.
Congratulations!!!!

Before we have our final celebration, we need to understand the two remaining types of minor scales.

Do not worry! You will only be learning a few things about them.


HARMONIC MINOR SCALE


The good thing about the remaining minor scales is that they are only slightly different from the natural minor scales we have learnt.

What is the difference between a natural minor scale and a harmonic minor scale?

It’s just one semitone.

Surprising right?

The harmonic minor scale is a natural minor scale that has its seventh note raised by a semitone.

Let’s use A minor as an example.
The notes in A minor are:

A - B - C - D - E - F - G - A


This is the natural A minor scale.

If we want to turn it into a harmonic scale, all we have to do is raise the seventh note by a semitone.

What is the seventh note? 


The seventh note is G. Therefore, we will raise G by a semitone.
Raising G by a semitone would give G♯.

So the A minor harmonic scale would have these notes:

A - B - C - D - E - F - G♯ - A


Does it seem like you understand? We’ll take another.

E natural minor has the following notes:

E - F♯ - G - A - B - C - D - E
 
What is the seventh note?


We will raise the seventh note by a semitone. So, we will raise D by a semitone to give D♯.

The E minor harmonic scale would have the following notes:

E - F♯ - G - A - B - C - D♯ - E  

That’s how harmonic minor scales work.



Try yourself!

Write out the notes in the B harmonic minor scale. 

B - _ - _ - _ - _ - _ - _ - B



We will take one more example to make sure we fully understand.
This example would be a minor scale with flats in its key signature, B♭ minor.
The notes in B♭ natural minor are: 

B♭ - C - D♭ - E♭ - F - G♭ - A♭ - B♭

The seventh note is A♭.

We will raise the seventh note by a semitone.
Therefore, we will raise A♭ by a semitone.

What do you think A♭ would become after raising it by a semitone?



We will have A.

In summary, a harmonic minor scale is created when the seventh note of a natural minor is raised by a semitone.
Harmonic minor scales follow all other rules of the natural minor scales.


How about the last type of minor scale?
Hold on, we are about to dive into it.


MELODIC MINOR SCALE

This type of minor scale can be confusing. It involves two phases. Ascending (going up) and descending (going down).

Let’s break the phases into parts.

Ascending

Ascending means counting from the scale’s tonic (first note) to its octave (last note).

We have been using ascending format since the beginning of this lesson.
For example,

A minor:
A - B - C - D - E - F - G - A

What happens in a melodic minor scale while ascending?

The sixth and seventh notes are raised by a semitone.

We will use A minor as a case study.

What is the sixth note in the A minor scale?


The sixth note is F. So if the sixth note is raised by a semitone, it becomes F♯.
As we saw earlier, the seventh note is G, and when raised, it becomes G♯.

A melodic minor scale (ascending) can be written as:

A - B - C - D - E - F♯ - G♯ - A

Now you try for E minor.

E - _ -  _ - _ - _ - _ - _ -  E

Not so hard, is it?

To make sure we are really good at ascending, let’s try B♭ minor.

What is the sixth note in B♭ minor?

While ascending, what should be the notes in the B♭ melodic minor scale?

B♭ - _ - _ - _ - _ - _ - _ -  B♭

 We are done with the ascending phase. Good job!!


Descending

Descending looks a bit different from what we are used to. Descending in a scale starts from the octave (last letter) to the tonic (first letter).

A minor scale descending would look like this:

A - G - F - E - D - C - B - A


Can you see the difference?

Ascending
A - B - C - D - E - F - G - A
======================>
(Read from left to right)

Descending
A - B - C - D - E - F - G - A
<======================
(Read from right to left)

For a melodic minor scale, when descending, the sixth and seventh notes that were raised while ascending return to their original notes.

In short, when descending, the melodic minor scale becomes the same as a natural minor scale.

Using the A minor scale, look at the notes:


A - B - C - D - E - F - G - A
<======================
(Read it from right to left)

Both G♯ and F♯ are restored to G and F.


Try writing the notes for the descending B♭ minor.

B♭ - C - _ - _ - _ - _ - _ - B♭
(Read from right to left)

You now know how to write the melodic minor scale in both phases, while ascending and descending.


Bravo!!!!

You have completed the Minor Scales Lesson.
Congratulations! You can now take on a challenge in the minor scale.






""")
