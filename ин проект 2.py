import tkinter as tk
from tkinter import messagebox

MORSE_EN = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': '/', '!': '!'
}

MORSE_RU = {
    'А':'.-', 'Б':'-...', 'В':'.--', 'Г':'--.', 'Д':'-..', 'Е':'.',
    'Ж':'...-', 'З':'--..', 'И':'..', 'Й':'.---', 'К':'-.-',
    'Л':'.-..', 'М':'--', 'Н':'-.', 'О':'---', 'П':'.--.', 'Р':'.-.',
    'С':'...', 'Т':'-', 'У':'..-', 'Ф':'..-.', 'Х':'....', 'Ц':'-.-.',
    'Ч':'---.', 'Ш':'----', 'Щ':'--.-', 'Ъ':'--.--', 'Ы':'-.--',
    'Ь':'-..-', 'Э':'..-..', 'Ю':'..--', 'Я':'.-.-', ' ':'/', '!': '!'
}


class MorseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Программа шифрования текста с помощью азбуки Морзе")
        self.root.geometry("600x350")
        self.root.resizable(False, False)

        self.current_lang = "RU"

        tk.Label(root, text="Введите текст:").place(x=20, y=20)
        self.entry_text = tk.Entry(root, width=60)
        self.entry_text.place(x=120, y=20)

        self.btn_en = tk.Button(root, text="English", width=15, command=self.set_en, bg="lightgray")
        self.btn_en.place(x=30, y=70)
        self.btn_ru = tk.Button(root, text="Русский", width=15, command=self.set_ru)
        self.btn_ru.place(x=160, y=70)

        tk.Button(root, text="Зашифровать", width=15, command=self.encrypt).place(x=30, y=120)
        tk.Button(root, text="Расшифровать", width=15, command=self.decrypt).place(x=160, y=120)

        tk.Label(root, text="Азбука Морзе:").place(x=340, y=60)
        self.alphabet_display = tk.Text(root, width=28, height=12)
        self.alphabet_display.place(x=340, y=85)
      # Поле результата
        tk.Label(root, text="Результат:").place(x=20, y=280)
        self.result_text = tk.Entry(root, width=90)
        self.result_text.place(x=20, y=310)

        self.update_alphabet_view()

    def set_en(self):
        self.current_lang = "EN"
        self.btn_en.config(bg="lightgray")
        self.btn_ru.config(bg="white")
        self.update_alphabet_view()

    def set_ru(self):
        self.current_lang = "RU"
        self.btn_ru.config(bg="lightgray")
        self.btn_en.config(bg="white")
        self.update_alphabet_view()

    def update_alphabet_view(self):
        # Очищаем и выводим текущий словарь
        self.alphabet_display.delete('1.0', tk.END)
        data = MORSE_EN if self.current_lang == "EN" else MORSE_RU
        for char, code in sorted(data.items()):
            if char != ' ':
                self.alphabet_display.insert(tk.END, f"{char} : {code}")

    def encrypt(self):
        text = self.entry_text.get().upper()
        data = MORSE_EN if self.current_lang == "EN" else MORSE_RU
        res = []
        for char in text:
            if char in data:
                res.append(data[char])
            else:
                res.append("?")
        self.result_text.delete(0, tk.END)
        self.result_text.insert(0, " ".join(res))

    def decrypt(self):
        code_text = self.entry_text.get().strip().split()
        data = MORSE_EN if self.current_lang == "EN" else MORSE_RU
        # Переворачиваем словарь для поиска по коду
        reverse_data = {v: k for k, v in data.items()}
        res = []
        for code in code_text:
            if code in reverse_data:
                res.append(reverse_data[code])
            else:
                res.append("?")
        self.result_text.delete(0, tk.END)
        self.result_text.insert(0, "".join(res))


if __name__ == "__main__":
    root = tk.Tk()
    app = MorseApp(root)
    root.mainloop()