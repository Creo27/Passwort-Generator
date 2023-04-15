import random
import pyperclip
import tkinter as tk
from tkinter import ttk

# GUI-Setup
root = tk.Tk()
root.title("Passwort-Generator")
root.geometry("300x260")
root.resizable(False, False)

# Passwort-Stärke-Auswahl
label_stärke = ttk.Label(root, text="Passwort-Stärke")
label_stärke.pack(pady=(20, 5))

frame_stärke = ttk.Frame(root)
frame_stärke.pack()

var_stärke = tk.IntVar()
radio_schwach = ttk.Radiobutton(frame_stärke, text="Schwach", variable=var_stärke, value=1)
radio_schwach.pack(side=tk.LEFT, padx=(0, 10))
radio_mittel = ttk.Radiobutton(frame_stärke, text="Mittel", variable=var_stärke, value=2)
radio_mittel.pack(side=tk.LEFT, padx=(0, 10))
radio_stark = ttk.Radiobutton(frame_stärke, text="Stark", variable=var_stärke, value=3)
radio_stark.pack(side=tk.LEFT, padx=(0, 10))

# Passwort-Länge-Auswahl
label_länge = ttk.Label(root, text="Passwort-Länge")
label_länge.pack(pady=(20, 5))

combo_länge = ttk.Combobox(root, state="readonly")
combo_länge.pack()

combo_länge['values'] = list(range(8, 33))
combo_länge.current(0)

# Passwort-Generierung
frame_buttons = ttk.Frame(root)
frame_buttons.pack(pady=(20, 0))

def generate_password():
    passwort = ""
    länge = int(combo_länge.get())
    stärke = var_stärke.get()

    if stärke == 1:
        zeichen = "abcdefghijklmnopqrstuvwxyz"
    elif stärke == 2:
        zeichen = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    else:
        zeichen = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+~`|}{[]:;?><,./-="

    for i in range(länge):
        passwort += random.choice(zeichen)

    pyperclip.copy(passwort)
    label_passwort.config(text=passwort)

button_generate = ttk.Button(frame_buttons, text="Generieren", command=generate_password)
button_generate.pack(side=tk.LEFT, padx=(0, 10))

button_copy = ttk.Button(frame_buttons, text="Kopieren", command=lambda: pyperclip.copy(label_passwort.cget("text")))
button_copy.pack(side=tk.LEFT)

# Passwort-Anzeige
label_passwort_text = ttk.Label(root, text="Passwort")
label_passwort_text.pack(pady=(30, 10))

label_passwort = ttk.Label(root, text="")
label_passwort.pack()

root.mainloop()
