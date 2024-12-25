import tkinter as tk
from tkinter import ttk

# Rotor dan reflektor sederhana
rotors = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Rotor I
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Rotor II
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Rotor III
]
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

# Fungsi Enkripsi/Deskripsi
def enigma_cipher(text, rotor_positions):
    rotor1, rotor2, rotor3 = [list(rotors[i]) for i in rotor_positions]
    result = ""

    for char in text.upper():
        if not char.isalpha():  # Abaikan karakter non-alfabet
            result += char
            continue

        # Forward pass
        idx = ord(char) - ord('A')
        idx = ord(rotor1[idx]) - ord('A')
        idx = ord(rotor2[idx]) - ord('A')
        idx = ord(rotor3[idx]) - ord('A')

        # Reflection
        reflected = reflector[idx]
        idx = ord(reflected) - ord('A')

        # Backward pass
        idx = rotor3.index(chr(idx + ord('A')))
        idx = rotor2.index(chr(idx + ord('A')))
        idx = rotor1.index(chr(idx + ord('A')))

        result += chr(idx + ord('A'))

        # Rotor Rotation
        rotor1 = rotor1[1:] + rotor1[:1]

    return result

# Fungsi untuk enkripsi
def encrypt_message():
    try:
        positions = [int(pos1.get()), int(pos2.get()), int(pos3.get())]
        plaintext = input_text.get("1.0", tk.END).strip()
        ciphertext = enigma_cipher(plaintext, positions)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, ciphertext)
    except ValueError:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Invalid rotor positions. Use numbers 0, 1, 2.")

# GUI Setup
root = tk.Tk()
root.title("Simple Enigma Machine")

# Input Text
tk.Label(root, text="Input Text:").pack(pady=5)
input_text = tk.Text(root, height=5, width=40)
input_text.pack(pady=5)

# Rotor Positions
tk.Label(root, text="Rotor Positions (0-2):").pack(pady=5)
rotor_frame = tk.Frame(root)
rotor_frame.pack()

pos1 = tk.Entry(rotor_frame, width=5)
pos1.pack(side=tk.LEFT, padx=5)
pos1.insert(0, "0")

pos2 = tk.Entry(rotor_frame, width=5)
pos2.pack(side=tk.LEFT, padx=5)
pos2.insert(0, "1")

pos3 = tk.Entry(rotor_frame, width=5)
pos3.pack(side=tk.LEFT, padx=5)
pos3.insert(0, "2")

# Encrypt Button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.pack(pady=10)

# Output Text
tk.Label(root, text="Output Text:").pack(pady=5)
output_text = tk.Text(root, height=5, width=40)
output_text.pack(pady=5)

# Run the Application
root.mainloop()
