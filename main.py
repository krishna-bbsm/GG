import tkinter as tk
from PIL import Image, ImageTk
from random import randint

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("GuessQuest")
        self.master.attributes('-fullscreen', True)
        self.background_image = Image.open("image.jpg")
        self.background_image = self.background_image.resize((self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.background_image = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.title = tk.Label(self.master, text="Guess Quest", font=("Helvetica", 32), bg='black', fg='white')
        self.title.pack()
        self.level_label = tk.Label(self.master, text="Level: 1", font=("Helvetica", 24), bg='black', fg='white')
        self.level_label.pack()
        self.score_tab = tk.Text(master, height=2, width=60, font=("Helvetica", 16), bg='light grey')
        self.score_tab.pack()
        self.score_tab.config(state='disabled')
        self.score_tab.tag_configure('center', justify='center')
        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.destroy, bg='light coral', fg='black', font=("Helvetica", 16), relief='groove', bd=5)
        self.exit_button.pack()
        self.start_game()

    def start_game(self):
        self.level = 1
        self.points = [100,75,50,25,10]
        self.points_scored = []
        self.new_game()

    def new_game(self):
        if self.level > 3:
            self.level_label.config(text="Final Score: {}".format(sum(self.points_scored)))
            self.play_again_button = tk.Button(self.master, text="Play Again", command=self.play_again, bg='light green', fg='black', font=("Helvetica", 16), relief='groove', bd=5)
            self.play_again_button.pack()
            return
        self.end_value = self.level * 10
        self.secret_number = randint(1, self.end_value)
        self.attempts = 5
        self.guess_number = tk.StringVar()
        self.label_text = tk.StringVar()
        self.label_text.set("Guess the secret number between 1 and {} ({} attempts left):".format(self.end_value, self.attempts))
        self.label = tk.Label(self.master, textvariable=self.label_text, bg='black', fg='white', font=("Helvetica", 16))
        self.label.pack()
        self.entry = tk.Entry(self.master, textvariable=self.guess_number, font=("Helvetica", 16))
        self.entry.pack()
        self.button = tk.Button(self.master, text="Guess", command=self.check_guess, bg='light blue', fg='black', font=("Helvetica", 16), relief='groove', bd=5)
        self.button.pack()

    def play_again(self):
        self.level = 1
        self.level_label.config(text="Level: {}".format(self.level))
        self.play_again_button.destroy()
        self.start_game()

    def check_guess(self):
        guess = int(self.guess_number.get())
        if guess == self.secret_number:
            self.score_tab.config(state='normal')
            self.score_tab.delete('1.0', tk.END)
            self.score_tab.insert(tk.END, "Your Guess is Correct, You Won the level {} with {} points\n".format(self.level, self.points[5-self.attempts]))
            self.score_tab.tag_add('center', '1.0', 'end')
            self.score_tab.config(state='disabled')
            self.points_scored.append(self.points[5-self.attempts])
            self.level += 1
            if self.level <= 3:
                self.level_label.config(text="Level: {}".format(self.level))
            self.label.destroy()
            self.entry.destroy()
            self.button.destroy()
            self.new_game()
        elif guess < self.secret_number:
            self.score_tab.config(state='normal')
            self.score_tab.delete('1.0', tk.END)
            self.score_tab.insert(tk.END, "Your Guess is lower than secret number\n")
            self.score_tab.tag_add('center', '1.0', 'end')
            self.score_tab.config(state='disabled')
        else:
            self.score_tab.config(state='normal')
            self.score_tab.delete('1.0', tk.END)
            self.score_tab.insert(tk.END, "Your Guess is higher than secret number\n")
            self.score_tab.tag_add('center', '1.0', 'end')
            self.score_tab.config(state='disabled')
        self.attempts -= 1
        self.label_text.set("Guess the secret number between 1 and {} ({} attempts left):".format(self.end_value, self.attempts))
        if self.attempts == 0:
            self.score_tab.config(state='normal')
            self.score_tab.delete('1.0', tk.END)
            self.score_tab.insert(tk.END, "Game Over, You Loose the Game, secret number is {}\n".format(self.secret_number))
            self.score_tab.tag_add('center', '1.0', 'end')
            self.score_tab.config(state='disabled')
            self.label.destroy()
            self.entry.destroy()
            self.button.destroy()
            if self.level < 3:
                self.play_again_button = tk.Button(self.master, text="Play Again", command=self.play_again, bg='light green', fg='black', font=("Helvetica", 16), relief='groove', bd=5)
                self.play_again_button.pack()

root = tk.Tk()
game = Game(root)
root.mainloop()
