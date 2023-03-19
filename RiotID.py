import tkinter as tk
import pyperclip

def ascii_to_japanese(text):
  japanese_text = ''
  conversions = {'A': 'Ａ', 'B': 'Ｂ', 'C': 'Ｃ', 'D': 'Ｄ', 'E': 'Ｅ', 'F': 'Ｆ', 'G': 'Ｇ', 'H': 'Ｈ', 'I': 'Ｉ', 'J': 'Ｊ',
  'K': 'Ｋ', 'L': 'Ｌ', 'M': 'Ｍ', 'N': 'Ｎ', 'O': 'Ｏ', 'P': 'Ｐ', 'Q': 'Ｑ', 'R': 'Ｒ', 'S': 'Ｓ', 'T': 'Ｔ',
  'U': 'Ｕ', 'V': 'Ｖ', 'W': 'Ｗ', 'X': 'Ｘ', 'Y': 'Ｙ', 'Z': 'Ｚ',
  'a': 'ａ', 'b': 'ｂ', 'c': 'ｃ', 'd': 'ｄ', 'e': 'ｅ', 'f': 'ｆ', 'g': 'ｇ', 'h': 'ｈ', 'i': 'ｉ', 'j': 'ｊ',
  'k': 'ｋ', 'l': 'ｌ', 'm': 'ｍ', 'n': 'ｎ', 'o': 'ｏ', 'p': 'ｐ', 'q': 'ｑ', 'r': 'ｒ', 's': 'ｓ', 't': 'ｔ',
  'u': 'ｕ', 'v': 'ｖ', 'w': 'ｗ', 'x': 'ｘ', 'y': 'ｙ', 'z': 'ｚ'}
  for char in text:
    japanese_text += conversions.get(char, char)
  return japanese_text

def convertir_texto(event=None):
  text = entry.get()
  converted_text = ascii_to_japanese(text)
  result_label.config(text=converted_text)
  pyperclip.copy(converted_text)
  result_label.config(text=converted_text + "\nResultado copiado al portapapeles.")

root = tk.Tk()
root.title("Conversor de texto Ghosty")
root.geometry("400x200")

label = tk.Label(root, text="Introduce el texto a convertir:")
label.pack()

entry = tk.Entry(root)
entry.pack()
entry.bind("<Return>", convertir_texto)

convert_button = tk.Button(root, text="Convertir", command=convertir_texto)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()