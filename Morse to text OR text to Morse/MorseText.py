import tkinter as tk
from tkinter import messagebox
import pyperclip

CHAR_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', '(': '-.--.',
    ')': '-.--.-', ':': '---...', ',': '--..--', '=': '-...-',
    '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.',
    '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

MORSE_TO_CHAR = {m: c for c, m in CHAR_TO_MORSE.items()}

def text_to_morse(text):
    encoded_words = []
    for word in text.strip().split():
        encoded_letters = [CHAR_TO_MORSE.get(ch.upper(), '#') for ch in word]
        encoded_words.append(' '.join(encoded_letters))
    return ' / '.join(encoded_words)

def morse_to_text(morse):
    decoded_words = []
    for word in morse.strip().split('/'):
        letters = [MORSE_TO_CHAR.get(ch, '#') for ch in word.strip().split()]
        decoded_words.append(''.join(letters))
    return ' '.join(decoded_words)

def convert_to_morse():
    text = input_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter some text!")
        return
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, text_to_morse(text))

def convert_to_text():
    morse = input_box.get("1.0", tk.END).strip()
    if not morse:
        messagebox.showwarning("Warning", "Please enter Morse code!")
        return
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, morse_to_text(morse))

def copy_output():
    result = output_box.get("1.0", tk.END).strip()
    if result:
        pyperclip.copy(result)
        messagebox.showinfo("Copied", "Output copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No output to copy!")

def clear_all():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)

root = tk.Tk()
root.title("Morse Code Converter 🐍")
root.geometry("500x400")
root.resizable(False, False)

tk.Label(root, text="Enter Text or Morse Code:", font=("Arial", 12)).pack(pady=5)

input_box = tk.Text(root, height=4, width=50)
input_box.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Text → Morse", command=convert_to_morse, width=15, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Morse → Text", command=convert_to_text, width=15, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Clear", command=clear_all, width=15, bg="#FF9800", fg="white").grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Copy Output", command=copy_output, width=15, bg="#9C27B0", fg="white").grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Output:", font=("Arial", 12)).pack(pady=5)

output_box = tk.Text(root, height=4, width=50)
output_box.pack(pady=5)

root.mainloop()
