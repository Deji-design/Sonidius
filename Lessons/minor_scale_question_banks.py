"""Authored practice questions for the natural-minor lesson."""


def _multiple_choice(question, answer, distractors):
    options = [answer, *distractors]
    return {
        "type": "multiple_choice",
        "question": question,
        "options": {letter: option for letter, option in zip("ABCD", options)},
        "answer": "A",
    }


def _true_false(question, answer):
    return {"type": "true_false", "question": question, "answer": answer}


def _fill_blank(question, answer):
    return {"type": "fill_blank", "question": question, "answer": answer}


def _keyboard(question, answer):
    return {"type": "keyboard", "question": question, "answer": answer}


def _scale_building(question, answer):
    return {"type": "scale_building", "question": question, "answer": answer}


def _identify_error(question, options, answer):
    return {
        "type": "identify_error",
        "question": question,
        "options": options,
        "answer": answer,
    }


def _challenge(question, answer, distractors):
    item = _multiple_choice(question, answer, distractors)
    item["type"] = "challenge"
    return item


# Each group tests one fact from Section 1 with three differently worded prompts.
_multiple_choice_groups = [
    (
        [
            "What is the relative major of A minor?",
            "A minor is related to which major scale?",
            "Which major scale shares A minor's notes and key signature?",
        ],
        "C major",
        ["G major", "F major", "D major"],
    ),
    (
        [
            "How many semitones above A is the tonic of A minor's relative major?",
            "Count forward from A by three semitones. Which note do you reach?",
            "What is the distance from A to C on the keyboard?",
        ],
        "3 semitones",
        ["1 semitone", "2 semitones", "4 semitones"],
    ),
    (
        [
            "Which note sequence forms the A natural minor scale?",
            "Choose the notes of A minor in ascending order.",
            "Which set of notes belongs to A natural minor?",
        ],
        "A - B - C - D - E - F - G - A",
        [
            "A - B - C - D - E - F♯ - G - A",
            "A - B - C♯ - D - E - F - G - A",
            "A - B♭ - C - D - E - F - G - A",
        ],
    ),
    (
        [
            "Which pattern is the natural minor scale formula?",
            "Choose the tone-and-semitone order used by natural minor scales.",
            "What is the natural minor formula from tonic to octave?",
        ],
        "Tone - Semitone - Tone - Tone - Semitone - Tone - Tone",
        [
            "Tone - Tone - Semitone - Tone - Tone - Tone - Semitone",
            "Semitone - Tone - Tone - Tone - Semitone - Tone - Tone",
            "Tone - Tone - Tone - Semitone - Tone - Tone - Semitone",
        ],
    ),
    (
        [
            "How many tones and semitones are in a natural minor formula?",
            "A natural minor scale has five of which interval and two of which?",
            "Which interval count describes a natural minor scale?",
        ],
        "Five tones and two semitones",
        [
            "Four tones and three semitones",
            "Six tones and one semitone",
            "Three tones and four semitones",
        ],
    ),
    (
        [
            "What do a minor scale and its relative major share?",
            "Which statement about relative major and minor scales is correct?",
            "How are a relative major and minor connected?",
        ],
        "The same notes and key signature",
        [
            "The same tonic note only",
            "Different notes and the same tonic",
            "The same scale formula and starting note",
        ],
    ),
    (
        [
            "How does a relative minor differ from its relative major?",
            "What changes when you play a relative scale pair?",
            "Relative major and minor scales share notes, but what differs?",
        ],
        "They start on different notes",
        [
            "They use different key signatures",
            "They contain different notes",
            "They must have different numbers of notes",
        ],
    ),
    (
        [
            "What is the relative minor of C major?",
            "C major is paired with which relative minor?",
            "Which minor scale shares C major's notes and key signature?",
        ],
        "A minor",
        ["C minor", "D minor", "E minor"],
    ),
    (
        [
            "How is the natural minor formula arranged compared with the major formula?",
            "What is true about the major and natural minor scale patterns?",
            "Why does a natural minor scale sound different from a major scale?",
        ],
        "The tones and semitones are arranged differently",
        [
            "Natural minor has no semitones",
            "Natural minor has one extra note",
            "The two formulas have the same arrangement",
        ],
    ),
    (
        [
            "Why is this lesson focusing on natural minor scales?",
            "Which minor scale type is covered in this section?",
            "What kind of minor scale uses the formula taught here?",
        ],
        "Natural minor",
        ["Harmonic minor", "Melodic minor", "Chromatic minor"],
    ),
]

_multiple_choice_questions = [
    _multiple_choice(prompt, answer, distractors)
    for prompts, answer, distractors in _multiple_choice_groups
    for prompt in prompts
]

_true_false_facts = [
    ("A minor's relative major is C major.", "TRUE"),
    ("A minor's relative major is G major.", "FALSE"),
    ("Relative major and minor scales share the same notes.", "TRUE"),
    ("Relative major and minor scales start on the same note.", "FALSE"),
    ("A minor has no sharps or flats in its natural form.", "TRUE"),
    ("The A natural minor scale contains F-sharp.", "FALSE"),
    ("The natural minor formula is Tone-Semitone-Tone-Tone-Semitone-Tone-Tone.", "TRUE"),
    ("The natural minor formula arranges its intervals exactly like the major formula.", "FALSE"),
    ("A natural minor scale formula contains five tones and two semitones.", "TRUE"),
    ("A natural minor scale formula contains two tones and five semitones.", "FALSE"),
    ("Count three semitones forward from a minor tonic to find its relative major tonic.", "TRUE"),
    ("Count three semitones backward from a minor tonic to find its relative major tonic.", "FALSE"),
    ("The notes of A natural minor are A, B, C, D, E, F, and G.", "TRUE"),
    ("The notes of A natural minor are A, B, C-sharp, D, E, F, and G.", "FALSE"),
    ("C major and A minor share a key signature.", "TRUE"),
    ("C major and A minor have different notes.", "FALSE"),
    ("Natural minor is the only type of minor scale.", "FALSE"),
    ("The A minor scale starts and ends on A in the example shown.", "TRUE"),
    ("A tone is made up of two semitones.", "TRUE"),
    ("A semitone is larger than a tone.", "FALSE"),
]
_true_false_questions = [_true_false(question, answer) for question, answer in _true_false_facts]

_fill_blank_facts = [
    ("The relative major of A minor is ______ major.", "C"),
    ("To find a minor scale's relative major, count ______ semitones forward.", "3"),
    ("A minor and C major share the same notes and ______ signature.", "key"),
    ("A relative major and minor start on ______ notes.", "different"),
    ("The natural minor formula begins Tone - ______.", "Semitone"),
    ("Complete the natural minor formula: T - S - T - T - S - T - ______.", "T"),
    ("A natural minor formula has ______ tones and two semitones.", "5"),
    ("A natural minor formula has five tones and ______ semitones.", "2"),
    ("The relative minor of C major is ______ minor.", "A"),
    ("The tonic note of A minor is ______.", "A"),
    ("The natural A minor scale ends on ______ after its seventh note.", "A"),
    ("A minor's relative major begins on the note ______.", "C"),
    ("A minor uses the notes A - B - C - D - E - ______ - G.", "F"),
    ("A minor uses the notes A - B - C - D - E - F - ______.", "G"),
    ("A tone contains ______ semitones.", "2"),
]
_fill_blank_questions = [_fill_blank(question, answer) for question, answer in _fill_blank_facts]

_keyboard_facts = [
    ("On the keyboard, which note is three semitones above A?", "C"),
    ("Which key is the tonic of the A minor scale?", "A"),
    ("A minor's relative major starts on which keyboard note?", "C"),
    ("Which note begins the A natural minor scale?", "A"),
    ("Which note completes the A natural minor scale after G?", "A"),
    ("Move three semitones forward from A. Which key do you reach?", "C"),
    ("What is the first note in the A-B-C-D-E-F-G pattern?", "A"),
    ("What is the third note of A natural minor?", "C"),
    ("What is the sixth note of A natural minor?", "F"),
    ("What is the seventh note of A natural minor?", "G"),
]
_keyboard_questions = [_keyboard(question, answer) for question, answer in _keyboard_facts]

_a_minor_scale_prompts = [
    "Write the A natural minor scale from tonic to octave.",
    "Build A minor using the natural minor formula.",
    "Enter all notes of A natural minor in ascending order.",
    "Complete the scale that starts on A and follows T-S-T-T-S-T-T.",
    "What is the full note sequence for the natural minor scale beginning on A?",
    "Using the lesson's example, write A minor from its first A to its next A.",
    "List the seven notes and repeat the tonic to complete A natural minor.",
    "Fill the scale: A - ? - ? - ? - ? - ? - ? - A.",
    "Apply the natural minor pattern to A and enter the resulting scale.",
    "Write the A minor scale shown in Section 1.",
]
_scale_building_questions = [
    _scale_building(prompt, "A - B - C - D - E - F - G - A")
    for prompt in _a_minor_scale_prompts
]

_identify_error_options = [
    {
        "A": "A - B - C - D - E - F - G - A",
        "B": "A - B - C - D - E - F♯ - G - A",
        "C": "A - B - C♯ - D - E - F - G - A",
        "D": "A - B♭ - C - D - E - F - G - A",
    },
    {
        "A": "A - B - C♯ - D - E - F - G - A",
        "B": "A - B - C - D - E - F - G - A",
        "C": "A - B - C - D - E - F♯ - G - A",
        "D": "A - B - C - D♯ - E - F - G - A",
    },
    {
        "A": "A - B - C - D - E - F - G - A",
        "B": "A - B - C - D - E - F - G♯ - A",
        "C": "A - B - C - D - E♭ - F - G - A",
        "D": "A - B♭ - C - D - E - F - G - A",
    },
    {
        "A": "A - B - C - D♯ - E - F - G - A",
        "B": "A - B - C - D - E - F - G - A",
        "C": "A - B - C - D - E - F♯ - G - A",
        "D": "A - B - C♯ - D - E - F - G - A",
    },
    {
        "A": "A - B - C - D - E - F - G - A",
        "B": "A - B - C - D - E - F♯ - G - A",
        "C": "A - B♭ - C - D - E - F - G - A",
        "D": "A - B - C - D - E♭ - F - G - A",
    },
    {
        "A": "A - B - C - D - E - F - G - A",
        "B": "A - B - C - D - E - F - G♯ - A",
        "C": "A - B - C♯ - D - E - F - G - A",
        "D": "A - B - C - D♯ - E - F - G - A",
    },
    {
        "A": "A - B - C - D - E - F♯ - G - A",
        "B": "A - B - C - D - E - F - G - A",
        "C": "A - B - C - D - E♭ - F - G - A",
        "D": "A - B♭ - C - D - E - F - G - A",
    },
    {
        "A": "A - B - C - D - E - F - G - A",
        "B": "A - B - C♯ - D - E - F - G - A",
        "C": "A - B - C - D - E - F♯ - G - A",
        "D": "A - B - C - D - E♭ - F - G - A",
    },
    {
        "A": "A - B - C - D - E - F - G - A",
        "B": "A - B♭ - C - D - E - F - G - A",
        "C": "A - B - C - D - E - F - G♯ - A",
        "D": "A - B - C - D♯ - E - F - G - A",
    },
    {
        "A": "A - B - C - D - E - F - G - A",
        "B": "A - B - C - D - E♭ - F - G - A",
        "C": "A - B - C♯ - D - E - F - G - A",
        "D": "A - B - C - D - E - F♯ - G - A",
    },
]
_identify_error_prompts = [
    "Which option correctly shows A natural minor?",
    "Select the correctly spelled A minor scale.",
    "Which sequence has no altered notes and follows the A minor example?",
    "Choose the correct ascending A natural minor scale.",
    "Which scale below matches the lesson's A minor notes?",
    "Identify the correctly formed natural minor scale starting on A.",
    "Which option uses the notes of A natural minor?",
    "Select the correct note order for A minor.",
    "Which sequence begins and ends on A and uses the lesson's notes?",
    "Find the correct A natural minor scale among these choices.",
]
_identify_error_questions = [
    _identify_error(prompt, options, "A" if options["A"] == "A - B - C - D - E - F - G - A" else "B")
    for prompt, options in zip(_identify_error_prompts, _identify_error_options)
]

_challenge_groups = [
    (
        "A minor and C major use the same notes. What makes them different scales?",
        "They begin on different notes",
        ["They have different key signatures", "They have different notes", "One has eight different notes"],
    ),
    (
        "Starting on A, which note is reached after three semitones?",
        "C",
        ["B", "D", "E"],
    ),
    (
        "Which formula creates the A-B-C-D-E-F-G-A pattern?",
        "T - S - T - T - S - T - T",
        ["T - T - S - T - T - T - S", "S - T - T - S - T - T - T", "T - T - T - S - T - T - S"],
    ),
    (
        "If C major is the relative major, which scale is its relative minor?",
        "A minor",
        ["C minor", "F minor", "G minor"],
    ),
    (
        "Which statement correctly combines the lesson's relative-scale rule?",
        "A relative major and minor share notes and a key signature but start on different notes",
        [
            "They share a tonic but use different notes",
            "They share neither notes nor key signatures",
            "They always start on the same note",
        ],
    ),
]
_challenge_questions = [
    _challenge(question, answer, distractors)
    for question, answer, distractors in _challenge_groups
]

SECTION_QUESTIONS = {
    1: [
        *_multiple_choice_questions,
        *_true_false_questions,
        *_fill_blank_questions,
        *_keyboard_questions,
        *_scale_building_questions,
        *_identify_error_questions,
        *_challenge_questions,
    ]
}

assert len(SECTION_QUESTIONS[1]) == 100
