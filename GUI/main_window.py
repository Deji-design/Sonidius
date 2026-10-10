import tkinter as tk

window = tk.Tk()
window.title("Sonidius")
window.geometry("800x600")

label = tk.Label(window, text="Welcome to Sonidius!", font=("Helvetica", 24))
label.pack(pady=20)


window.mainloop()