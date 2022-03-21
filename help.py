from tkinter import Tk, Label, Button

def how_to():
    help_window = Tk()
    help_window.title("How to Play")

    # Label with the information on how to play the game and packing it on the screen
    how_to_play = Label(help_window,
                        text="How To Play?\n\nNB: This is a 2-player game and it is played offline\n\nThe goal of the game in Level 1 is to have 3 Xs or 3 Os to align\n"
                                "Either horizontally, vertically or diagonally\n\nThe goal of the game in Level 2 is to have 4 Xs or 4 Os to align\nEither horizontally, vertically or diagonally\n"
                                "\n\nRULES\nRule 1: Make sure to find ways to align\nRule 2: Make sure to block the opponent's alignments\n"
                                "Rule 3: Obey Rule 1 and Rule 2\n\nENJOY\n\n",
                        font=("Bradley", 9), bg="yellow", fg="black")
    how_to_play.pack()
    
    spacing = Label(help_window, text="").pack()  # this is a space just to make the game look good
    exitting = Button(help_window, text="Exit", bg="yellow", fg="red", font=("Stencil", 11), command=help_window.destroy).pack()

    help_window.mainloop()
