import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        # GUI Layout
        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.result = tk.Label(master, text="")
        self.result.pack()

        self.submit = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.submit.pack()

        self.attempt_label = tk.Label(master, text="Attempts: 0")
        self.attempt_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.result.config(text="Too low. Try again.")
            elif guess > self.number_to_guess:
                self.result.config(text="Too high. Try again.")
            else:
                self.result.config(text="🎉 Correct! You guessed it in {} attempts.".format(self.attempts))
                self.submit.config(state="disabled")

            self.attempt_label.config(text="Attempts: {}".format(self.attempts))
        except ValueError:
            self.result.config(text="❌ Please enter a valid number.")

# Run the game
root = tk.Tk()
game = GuessingGame(root)
root.mainloop()