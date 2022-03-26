from tkinter import Button, Label, messagebox, Menu, Tk, DISABLED
#from level_one import play_game

def level_2():
    level2 = Tk()
    level2.title("TICTACTOE-LEVEL 2")

    # variables clicked must be boolean and count must be integer and the must be global
    global clicked
    global count
    clicked = True
    count = 0

    # function to disable buttons when there is a winner or the buttons are all filled
    def disable_all_buttons():
        for btn in buttons:
            btn.config(state=DISABLED)
        

    # Function to look for a winner/draw and give a popup message and change the colour of the buttons that led to the win
    def check_if_won(text):
        global winner, count, clicked
        winner = False

        # checking for player 1(Xs)
        if btn1["text"] == text and btn2["text"] == text and btn3["text"] == text and btn4["text"] == text:
            btn1.config(bg="white")
            btn2.config(bg="white")
            btn3.config(bg="white")
            btn4.config(bg="white")
            winner = True

        elif btn5["text"] == text and btn6["text"] == text and btn7["text"] == text and btn8["text"] == text:
            btn5.config(bg="white")
            btn6.config(bg="white")
            btn7.config(bg="white")
            btn8.config(bg="white")
            winner = True

        elif btn9["text"] == text and btn10["text"] == text and btn11["text"] == text and btn12["text"] == text:
            btn9.config(bg="white")
            btn10.config(bg="white")
            btn11.config(bg="white")
            btn12.config(bg="white")
            winner = True

        elif btn13["text"] == text and btn14["text"] == text and btn15["text"] == text and btn16["text"] == text:
            btn13.config(bg="white")
            btn14.config(bg="white")
            btn15.config(bg="white")
            btn16.config(bg="white")
            winner = True

        elif btn1["text"] == text and btn5["text"] == text and btn9["text"] == text and btn13["text"] == text:
            btn1.config(bg="black")
            btn5.config(bg="black")
            btn9.config(bg="black")
            btn13.config(bg="black")
            winner = True

        elif btn2["text"] == text and btn6["text"] == text and btn10["text"] == text and btn14["text"] == text:
            btn2.config(bg="black")
            btn6.config(bg="black")
            btn10.config(bg="black")
            btn14.config(bg="black")
            winner = True

        elif btn3["text"] == text and btn7["text"] == text and btn11["text"] == text and btn15["text"] == text:
            btn3.config(bg="black")
            btn7.config(bg="black")
            btn11.config(bg="black")
            btn15.config(bg="black")
            winner = True

        elif btn4["text"] == text and btn8["text"] == text and btn12["text"] == text and btn16["text"] == text:
            btn4.config(bg="black")
            btn8.config(bg="black")
            btn12.config(bg="black")
            btn16.config(bg="black")
            winner = True

        elif btn1["text"] == text and btn6["text"] == text and btn11["text"] == text and btn16["text"] == text:
            btn1.config(bg="pink")
            btn6.config(bg="pink")
            btn11.config(bg="pink")
            btn16.config(bg="pink")
            winner = True

        elif btn4["text"] == text and btn7["text"] == text and btn10["text"] == text and btn13["text"] == text:
            btn4.config(bg="pink")
            btn7.config(bg="pink")
            btn10.config(bg="pink")
            btn13.config(bg="pink")
            winner = True
        
        if winner:
            messagebox.showinfo("TICTACTOE", f"Congratulations\nPlayer {text} Wins")
            disable_all_buttons()

        # checking if there is no winner and giving message if there no winner
        if count == 16 and winner == False:
            messagebox.showinfo("TicTacToe", "There is no winner\n\nRestart Game")
            disable_all_buttons()




    # Function to insert a text in the button when it is clicked and pops up a message when a player clicks a taken button. When it is first time it will be true and hence X is printed the clicked is set to false
    # When clicked the second time it will be false and hence O is inserted and clicked is set to True.
    def b_clicked(b):
        global clicked, count

        if b["text"] == "" and clicked == True:
            b["text"] = "X"
            clicked = False
            count = count + 1
            check_if_won("X")
        elif b["text"] == "" and clicked == False:
            b["text"] = "O"
            clicked = True
            count = count + 1
            check_if_won("O")
        else:
            messagebox.showerror("TicTacToe-Level2", "Oops! That box has already been selected\nPick another box ")

    def reset():
        global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16
        global clicked, count
        clicked = True
        count = 0
        global buttons
        buttons = list()

        # creating the buttons
        btn1 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="Blue",
                      command=lambda: b_clicked(btn1))
        btn2 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="Green",
                      command=lambda: b_clicked(btn2))
        btn3 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="Yellow",
                      command=lambda: b_clicked(btn3))
        btn4 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="red",
                      command=lambda: b_clicked(btn4))
        btn5 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="red",
                      command=lambda: b_clicked(btn5))
        btn6 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="yellow",
                      command=lambda: b_clicked(btn6))
        btn7 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="green",
                      command=lambda: b_clicked(btn7))
        btn8 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="blue",
                      command=lambda: b_clicked(btn8))
        btn9 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="blue",
                      command=lambda: b_clicked(btn9))
        btn10 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="Green",
                       command=lambda: b_clicked(btn10))
        btn11 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="yellow",
                       command=lambda: b_clicked(btn11))
        btn12 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="red",
                       command=lambda: b_clicked(btn12))
        btn13 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="red",
                       command=lambda: b_clicked(btn13))
        btn14 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="yellow",
                       command=lambda: b_clicked(btn14))
        btn15 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="green",
                       command=lambda: b_clicked(btn15))
        btn16 = Button(level2, text="", font=("Helvetica", 20), height=3, width=6, fg="Black", bg="blue",
                       command=lambda: b_clicked(btn16))
        
        buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16]

        # gridding the buttons in the playground
        n = len(buttons)
        for i in range(n):
            buttons[i].grid(row=int(i//(n**0.5)), column=int(i%(n**0.5)))

    # creating the menu to put options
    levelselection = Menu(level2)
    level2.config(menu=levelselection)

    # creating the options menu with level selection as label
    options_menu = Menu(levelselection)
    levelselection.add_cascade(label="MENU", menu=options_menu)
    options_menu.add_command(label="EXIT LEVEL 2", command=level2.destroy)
    options_menu.add_command(label="QUIT GAME", command=level2.destroy)
    reset()  # without this call to the reset function the game board will need the restart button to be played

    # information to players
    player1 = Label(level2, text="Player X", padx=15, pady=6, fg="Black")
    player1.grid(row=5, column=0)
    player2 = Label(level2, text="Player O", padx=15, pady=6, fg="Black")
    player2.grid(row=6, column=0)

    # Game reset button with the function reset() as the command
    gameRestart = Button(level2, text="Restart Game", padx=6, pady=6, font=("Stencil", 9), bg="Yellow", fg="Red",
                         command=reset)
    gameRestart.grid(row=7, column=3)

    level2.mainloop()


