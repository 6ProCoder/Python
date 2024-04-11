import Tkinter as tk
import random
while __name__!="solo" and __name__!="duo":
    __name__= raw_input("solo or duo: ")
def Take_input():
    print "Start Game"
    y=0
    i=-1
    x = inputtxt.get("1.0", "end-1c")
    while x !=y:
        i = i+1
        y = raw_input("Guess what: ")
        if x==y:
            print
            print "Well done"
            print "Tries", i
            print
        elif i==5:
            print "5 Tries"
        elif i==10:
            print "10 Tries"



if __name__ == "duo":
    root = tk.Tk()

    root.title("Mini Game")
    l = tk.Label(root, text = "Give him something to guess")
    Q = tk.Label(root, text = " ")
    W = tk.Label(root, text = " ")
    E = tk.Label(root, text = " ")

    l.config(font =("Courier", 15))
    Q.config(font =("Courier", 15))
    W.config(font =("Courier", 5))
    E.config(font =("Courier", 5))

    inputtxt = tk.Text(root, height = 10,
                width = 25,
                bg = "light gray")

    Display = tk.Button(root, height = 2,
                 width = 20, 
                 text ="Submit",
                 command = lambda:Take_input())

    W.pack()
    l.pack()
    E.pack()
    inputtxt.pack()
    Q.pack()
    Display.pack()
    root.geometry("333x333")
    root.mainloop()
class NumberGuessGame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Set window title
        self.title("Number Guessing Game")

        # Create a label for displaying the game state
        self.label = tk.Label(self, text="Welcome to the number guessing game!")
        self.label.pack()

        # Create a label for displaying the current number
        self.number_label = tk.Label(self, text="")
        self.number_label.pack()

        # Create a text entry field for inputting the guess
        self.guess_entry = tk.Entry(self)
        self.guess_entry.pack()

        # Create a button for submitting the guess
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_guess)
        self.submit_button.pack()

        # Initialize the game variables
        self.secret_number = random.randint(1, 10)
        self.guess_count = 0
        self.guess_limit = 3

    def submit_guess(self):
        # Get the user's guess from the text entry field
        guess = int(self.guess_entry.get())

        # Increment the guess count
        self.guess_count += 1

        # Check if the guess is correct
        if guess == self.secret_number:
            self.label.config(text="Congratulations! You guessed the number!")
            self.number_label.config(text="")
            self.guess_entry.config(state="disabled")
            self.submit_button.config(state="disabled")
        elif self.guess_count < self.guess_limit:
            # Check if the guess is too high or too low
            if guess > self.secret_number:
                self.label.config(text="Too high! Try again.")
            else:
                self.label.config(text="Too low! Try again.")
            self.number_label.config(text="")
        else:
            # Game over
            self.label.config(text="Game over! The number was" + str( {self.secret_number}) )
            self.number_label.config(text="")
            self.guess_entry.config(state="disabled")
            self.submit_button.config(state="disabled")

if __name__ == "solo":
    app = NumberGuessGame()
    app.geometry("333x111")
    app.mainloop()
