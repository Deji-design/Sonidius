import tkinter as tk
from tkinter import messagebox

# Creating the main window
window = tk.Tk()
window.title("Sonidius")
window.geometry("900x650")
window.configure(bg="#FFF8E7")



# Main content area

main_frame = tk.Frame(window, bg="#FFF8E7")
main_frame.pack(fill="both", expand=True, padx=30, pady=25)



# App Title
title = tk.Label(
    main_frame,
    text="Sonidius",
    font=("Arial", 30, "bold"),
    fg="#6C4AD6",
    bg="#FFF8E7"
)

title.pack(pady=(5,5))

# Welcome Message
welcome = tk.Label(
    main_frame,
    text="Welcome to Sonidius! Your musical adventure starts here!",
    font=("Arial", 15),
    fg="#44405A",
    bg="#FFF8E7"
)
welcome.pack(pady=(0,25))

# Temporary action for lesson buttons
def open_lesson(lesson_name):
    messagebox.showinfo(
        "Coming Soon!",
        f"{lesson_name} will be connected to your lesson code next."
    )


# Lesson information
lessons = [
    ("Major Scales", "Discover the patterns behind major scales.", "#D9EAFD"),
    ("Minor Scales", "Explore the sounds of minor scales.", "#F9DDF0"),
    ("Note Intervals", "Learn the distances between musical notes.", "#DDF4D5"),
    ("Musical Terminologies", "Get to know the language of music.", "#FFE7B8")
]

# Area that holds the lesson cards
lesson_frame = tk.Frame(main_frame, bg="#FFF8E7")
lesson_frame.pack(fill="both", expand=True)

# Create the four lesson cards
for index, lesson in enumerate(lessons):
    lesson_name, description, card_color = lesson

    card = tk.Frame(
        lesson_frame,
        bg=card_color,
        padx=15,
        pady=15
    )

    card.grid(
        row=index // 2,
        column=index % 2,
        padx=12,
        pady=12,
        sticky="nsew"
    )

    lesson_title = tk.Label(
        card,
        text=lesson_name,
        font=("Arial", 16, "bold"),
        bg=card_color,
        fg="#302747",
        wraplength=300
    )
    lesson_title.pack(pady=(8, 6))

    lesson_description = tk.Label(
        card,
        text=description,
        font=("Arial", 11),
        bg=card_color,
        fg="#44405A",
        wraplength=300
    )
    lesson_description.pack(pady=5)

    lesson_button = tk.Button(
        card,
        text="Let's learn!",
        font=("Arial", 11, "bold"),
        bg="#6C4AB6",
        fg="white",
        activebackground="#54358F",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=15,
        pady=7,
        command=lambda name=lesson_name: open_lesson(name)
    )
    lesson_button.pack(pady=(12, 5))


# Give both card columns equal space
lesson_frame.columnconfigure(0, weight=1)
lesson_frame.columnconfigure(1, weight=1)
lesson_frame.rowconfigure(0, weight=1)
lesson_frame.rowconfigure(1, weight=1)


# Start the application
window.mainloop()