from tkinter import Tk, Button

# import modules
from help import how_to
from level_one import play_game


# -------------------- GRAPHICAL USER INTERFACE -----------------------------------

window = Tk()
window.title("Atarist Game")



# level selection
level_one_btn = Button(window, text="START GAME", font=("Stencil", 15), padx=20, pady=20, bg="Orange", fg="Maroon",
                command=lambda : [play_game()], width=10)
level_one_btn.grid(row=2, column=2)

# help button
help_btn = Button(window, text="HELP", font=("Stencil", 15), padx=20, pady=20, bg="Orange", fg="Maroon",
              command=how_to, width=10)
help_btn.grid(row=3, column=2)

quit_btn = Button(window, text="QUIT", font=("Stencil", 15), padx=20, pady=20, bg="Orange", fg="Maroon",
              command=window.quit,  width=10)
quit_btn.grid(row=4, column=2)


window.mainloop()