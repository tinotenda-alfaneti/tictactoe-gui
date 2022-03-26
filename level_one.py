from tkinter import *  # importing everything from tkinter
from tkinter import messagebox  # for popup messages for winning or error
from level_two import level_2

def play_game():

    # initializing game window
    game_window = Tk()
    game_window.title("TICTACTOE-LEVEL 1")
    global click_count, clicked
    click_count = 0
    clicked = False

    # function to disable all buttons after a person wins or all buttons clicked
    def disable_all_buttons():
        for btn in buttons:
            btn.config(state=DISABLED)
        

    # Function to check for a winner and changing the colour of the boxes
    def checkifwon(text):
        global winner, click_count
        winner = False

        # checking for winning conditions for Player 1 i.e Xs and popup message if there is winner also changing box colour
        if b1["text"] == text and b2["text"] == text and b3["text"] == text:
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner = True

        elif b4["text"] == text and b5["text"] == text and b6["text"] == text:
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner = True

        elif b7["text"] == text and b8["text"] == text and b9["text"] == text:
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner = True

        elif b1["text"] == text and b4["text"] == text and b7["text"] == text:
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner = True

        elif b2["text"] == text and b5["text"] == text and b8["text"] == text:
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner = True

        elif b3["text"] == text and b6["text"] == text and b9["text"] == text:
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner = True

        elif b1["text"] == text and b5["text"] == text and b9["text"] == text:
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner = True

        elif b3["text"] == text and b5["text"] == text and b7["text"] == text:
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner = True

        if winner:
            value = messagebox.askokcancel("TICTACTOE", f"Congratulations\nPlayer {text} Wins.\nGo to LEVEL 2?")
            disable_all_buttons()
            if value:
                game_window.destroy()
                level_2()
            elif value == False:
                reset()

        # checking if there is no winner and giving message if there no winner
        if click_count == 9 and winner == False:
            messagebox.showinfo("TicTacToe", "There is no winner\n\nRestart Game")
            disable_all_buttons()

    # Function to insert the text in the buttons. The clicked value alternates between False and True thereby changing the input in the boxes
    # when the user tries to click a box that is occupied the game pops up an error message
    def b_click(b):
        global clicked
        global click_count
        

        if b["text"] == "" and clicked == True:
            b["text"] = "X"
            clicked = False
            click_count += 1
            checkifwon("X")
        elif b["text"] == "" and clicked == False:
            b["text"] = "O"
            clicked = True
            click_count += 1
            checkifwon("O")
        else:
            messagebox.showerror("TICTACTOE", "Oops! That box has already been selected\nPick another box ")

    # Function that restarts the game after a person wins or draw or just restarting to start again
    def reset():
        
        global b1, b2, b3, b4, b5, b6, b7, b8, b9  # to make the buttons accessible outside this function
        global buttons, click_count
        buttons = list()
        click_count = 0

        # building the buttons for our game and making them have the command of the function b_click()
        b1 = Button(game_window, text="", font=("Helvetica", 20), height=3, width=6, fg="white", bg="Blue",
                    command=lambda: b_click(b1))
        buttons.append(b1)
        b2 = Button(game_window, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="Green",
                    command=lambda: b_click(b2))
        buttons.append(b2)
        b3 = Button(game_window, text="", font=("Helvetica", 20), height=3, width=6, fg="white", bg="Blue",
                    command=lambda: b_click(b3))
        buttons.append(b3)
        b4 = Button(game_window, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="Green",
                    command=lambda: b_click(b4))
        buttons.append(b4)
        b5 = Button(game_window, text="", font=("Helvetica", 20), height=3, width=6, fg="Purple", bg="White",
                    command=lambda: b_click(b5))
        buttons.append(b5)
        b6 = Button(game_window, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="Green",
                    command=lambda: b_click(b6))
        buttons.append(b6)
        b7 = Button(game_window, text="", font=("Helvetica", 20), height=3, width=6, fg="white", bg="Blue",
                    command=lambda: b_click(b7))
        buttons.append(b7)
        b8 = Button(game_window, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="Green",
                    command=lambda: b_click(b8))
        buttons.append(b8)
        b9 = Button(game_window, text="", font=("Helvetica", 20), height=3, width=6, fg="white", bg="Blue",
                    command=lambda: b_click(b9))
        buttons.append(b9)

        # after building the buttons we then grid the on out game_window window otherwise we won't see them
        n = len(buttons)
        for i in range(n):
            buttons[i].grid(row=int(i//(n**0.5)), column=int(i%(n**0.5)))
            

    # creating the menu to put options
    levelselection = Menu(game_window)
    game_window.config(menu=levelselection)

    # creating the options menu with level selection as label
    options_menu = Menu(levelselection, font=("Stencil", 9), fg="Red", bg="Yellow")
    levelselection.add_cascade(label="MENU", menu=options_menu)
    options_menu.add_command(label="EXIT", command=game_window.destroy)

    # information to players
    player1 = Label(game_window, text="Player O", padx=15, pady=6, fg="Black")
    player1.grid(row=5, column=0)
    player2 = Label(game_window, text="Player X", padx=15, pady=6, fg="Black")
    player2.grid(row=6, column=0)

    # Game reset button with the function reset() as the command
    restart_game = Button(game_window, text="Restart Game", padx=6, pady=6, font=("Stencil", 9), bg="Yellow", fg="Red",
                            command=reset)
    restart_game.grid(row=7, column=2)

    reset()

    game_window.mainloop()
