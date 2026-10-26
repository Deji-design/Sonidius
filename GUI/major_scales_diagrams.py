import tkinter as tk 


# Keep track of diagrams embedded in the lesson notes
embedded_diagrams = []


def insert_keyboard_diagram(text_widget):
    marker = "|insert image in GUI|"

    # Find the place where the diagram belongs
    marker_index = text_widget.search(
        marker, "1.0", tk.END
    )

    if not marker_index:
        return

    # Remove the placeholder text
    text_widget.delete(
        marker_index,
        f"{marker_index}+{len(marker)}c"
    )

    # Create a space for the diagram
    text_widget.insert(marker_index, "\n")
    diagram_index = f"{marker_index}+1c"

    diagram_frame = tk.Frame(
        text_widget,
        bg="#FFF8E7"
    )

    canvas = tk.Canvas(
        diagram_frame,
        width=510,
        height=155,
        bg="#FFF8E7",
        highlightthickness=0
    )
    canvas.pack()

    # Diagram heading
    canvas.create_text(
        255, 15,
        text="The Piano Keyboard",
        font=("Arial", 15, "bold"),
        fill="#6C4AD6"
    )

    # Draw the seven white keys
    start_x = 25
    key_width = 65
    top_y = 32
    bottom_y = 135

    white_notes = ["C", "D", "E", "F", "G", "A", "B"]

    for i, note in enumerate(white_notes):
        x = start_x + i * key_width

        canvas.create_rectangle(
            x, top_y,
            x + key_width, bottom_y,
            fill="white",
            outline="#33215F",
            width=2
        )

        canvas.create_text(
            x + key_width / 2,
            117,
            text=note,
            font=("Arial", 12, "bold"),
            fill="#33215F"
        )

    # Draw the five black keys
    black_keys = [
        (0, "C#"),
        (1, "D#"),
        (3, "F#"),
        (4, "G#"),
        (5, "A#")
    ]

    for position, note in black_keys:
        x = start_x + (position + 1) * key_width - 18

        canvas.create_rectangle(
            x, top_y,
            x + 36, 95,
            fill="#33215F",
            outline="#33215F"
        )

        canvas.create_text(
            x + 18, 78,
            text=note,
            font=("Arial", 8, "bold"),
            fill="white"
        )

    # Embed the diagram inside the lesson notes
    text_widget.window_create(
        diagram_index,
        window=diagram_frame,
        padx=5,
        pady=8
    )

    text_widget.insert(
        f"{diagram_index}+1c", "\n"
    )

    embedded_diagrams.append(diagram_frame)
