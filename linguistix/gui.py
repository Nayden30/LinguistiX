import tkinter as tk
from tkinter import filedialog, messagebox

from .io.corpus import read_corpus
from .analysis.tokenization import tokenize
from .analysis.frequency import word_frequencies


class LinguistiXGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("LinguistiX GUI")

        open_button = tk.Button(root, text="Ouvrir des fichiers", command=self.open_files)
        open_button.pack(pady=10)

        self.result = tk.Text(root, width=40, height=20)
        self.result.pack(padx=10, pady=10)

    def open_files(self):
        paths = filedialog.askopenfilenames(title="Choisir des fichiers texte")
        if not paths:
            return
        try:
            text = read_corpus(paths)
            tokens = tokenize(text)
            freq = word_frequencies(tokens)
            self.display_frequencies(freq)
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def display_frequencies(self, freq, n=10):
        self.result.delete("1.0", tk.END)
        for word, count in freq.most_common(n):
            self.result.insert(tk.END, f"{word}\t{count}\n")


def main():
    root = tk.Tk()
    app = LinguistiXGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
