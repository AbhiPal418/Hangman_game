import tkinter as tk
import random


WORDS = ["SMARTPHONE", "PYHTON", "JAVA", "JAVASCRIPT", "LAPTOP", "COMPUTER",
         "HOUSE", "CYCLE", "CIRCLE", "APPLE", "BANANA", "EVENING", "MORNING",
         "KOLKATA", "DELHI", "MUMBAI", "NEWYORK", "INDIA", "AMERICA",
         "JAPAN", "RUSSIA", "AUSTRALIA"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f7") 

        self.data = random.choice(WORDS)
        self.guess_word = ["_"] * len(self.data)
        self.remaining_chances = 7

        self.label_title = tk.Label(root, text="🎯 Hangman Word Guess Game 🎯",
                                    font=("Helvetica", 20, "bold"),
                                    bg="#f0f4f7", fg="#333")
        self.label_title.pack(pady=15)

        self.box_frame = tk.Frame(root, bg="#f0f4f7")
        self.box_frame.pack(pady=20)

        self.letter_labels = []
        for _ in self.data:
            label = tk.Label(self.box_frame, text="_", font=("Helvetica", 22, "bold"),
                             width=2, height=1, bg="white", fg="black", relief="ridge", bd=2)
            label.pack(side=tk.LEFT, padx=5)
            self.letter_labels.append(label)

        self.info_label = tk.Label(root, text=f"Letters: {len(self.data)}   |   Chances left: {self.remaining_chances}",
                                   font=("Helvetica", 12, "italic"),
                                   bg="#f0f4f7", fg="#555")
        self.info_label.pack(pady=5)

        self.entry = tk.Entry(root, font=("Helvetica", 16), justify='center', bd=3, relief="groove", width=5)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.make_guess)

        self.guess_button = tk.Button(root, text="Guess", font=("Helvetica", 12, "bold"),
                                      bg="#5cb85c", fg="white", relief="raised", command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), fg="#d9534f", bg="#f0f4f7")
        self.result_label.pack(pady=20)

        self.restart_button = tk.Button(root, text="Restart Game", font=("Helvetica", 12),
                                        bg="#0275d8", fg="white", relief="raised", command=self.restart_game)
        self.restart_button.pack(pady=10)

    def make_guess(self, event=None):
        guess = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if not guess or len(guess) != 1 or not guess.isalpha():
            self.result_label.config(text="❗ Enter a single letter.", fg="#d9534f")
            return

        match_found = False
        for i, letter in enumerate(self.data):
            if letter == guess and self.guess_word[i] == "_":
                self.guess_word[i] = guess
                self.letter_labels[i].config(text=guess, bg="#5cb85c", fg="white")
                match_found = True

        if match_found:
            self.result_label.config(text="✅ Correct guess!", fg="#5cb85c")
        else:
            self.remaining_chances -= 1
            self.result_label.config(text="❌ Incorrect guess.", fg="#d9534f")

        self.info_label.config(
            text=f"Letters: {len(self.data)}   |   Chances left: {self.remaining_chances}")

        if "_" not in self.guess_word:
            self.result_label.config(
                text=f"🎉 You guessed it right! The word was '{self.data}'.", fg="#f0ad4e")
            self.disable_game()
        elif self.remaining_chances == 0:
            self.result_label.config(
                text=f"😢 You lost! The word was '{self.data}'.", fg="red")
            self.disable_game()

    def disable_game(self):
        self.entry.config(state='disabled')
        self.guess_button.config(state='disabled')

    def restart_game(self):
        self.data = random.choice(WORDS)
        self.guess_word = ["_"] * len(self.data)
        self.remaining_chances = 7

        for label in self.letter_labels:
            label.destroy()
        self.letter_labels = []

        for _ in self.data:
            label = tk.Label(self.box_frame, text="_", font=("Helvetica", 22, "bold"),
                             width=2, height=1, bg="white", fg="black", relief="ridge", bd=2)
            label.pack(side=tk.LEFT, padx=5)
            self.letter_labels.append(label)

        self.entry.config(state='normal')
        self.guess_button.config(state='normal')
        self.result_label.config(text="", fg="#d9534f")
        self.info_label.config(
            text=f"Letters: {len(self.data)}   |   Chances left: {self.remaining_chances}")


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
