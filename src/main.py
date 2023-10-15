from src.Board import *
from Mechanics import name_builder
import random

from PIL import Image, ImageTk
import tkinter as tk

main_color = '#BFA173'
turn = 1
player = 1
# TODO  : Give player more control over the game. Add more interactions between territories, better traits for deeper territories
territories = {
    (290, 320): 5, (460, 320): 10, (630, 320): 5,  # first line
    (120, 490): 5, (290, 490): 10, (460, 490): 10, (630, 490): 10, (800, 490): 5,  # second line
    (120, 660): 15, (290, 660): 15,(460, 660): 10, (630, 660): 15, (800, 660): 15  # third line
}

window = tk.Tk()
window.title("Cave Conquerors")
window.geometry("1100x900+10+20")
window.configure(bg=main_color)


lbl = tk.Label(window, text="Cave Conquerors", fg='black', font=("Helvetica", 18), anchor="ne", bg=main_color)
lbl.pack()
version = tk.Label(window, text="v1.0", fg='black', font=("Helvetica", 9), anchor="e", bg=main_color)
version.pack()

dice_pic = Image.open("Resources/dice.png")
dice_pic = dice_pic.resize((70, 70))
dice_pic = ImageTk.PhotoImage(dice_pic)

backgroundimg = tk.PhotoImage(file="Resources/wall_underground.png")
bcg = tk.Label(window, image=backgroundimg)
bcg.place(x=-5, y=60)


def start():
    btn_turn = tk.Button(window, text="End Turn", bg=main_color, command=advance_turn, height=2, width=10, font=("Helvetica", 10))
    btn_turn.pack(pady=12)
    turn_counter.pack()
    turn_player1.place(x=140, y=200)
    btn_start.destroy()


def advance_turn():
    """This function adds a pointer to a currently acting player, and advances turn forward after both players acted.
    Also, it adds 5 to player forces at the beginning of each turn"""
    global player
    global turn
    if player == 1:
        player = 2
        turn_player2.place(x=820, y=200)
        turn_player1.place_forget()
    else:
        turn += 1
        player = 1
        turn_counter.configure(text="Turn " + str(turn))
        player_red.forces += 5
        player_red.player_forces.configure(text=player_red.forces)
        turn_player1.place(x=140, y=200)
        turn_player2.place_forget()
        player_blue.forces += 5
        player_blue.player_forces.configure(text=player_blue.forces)


btn_dice = tk.Button(window, image=dice_pic, bg=main_color, command=lambda: dice_roll.configure(text=random.choice(range(1, 7))), height=50, width=50, font=("Helvetica", 10))
btn_dice.place(x=522, y=180)
dice_roll = tk.Label(window, text="  ", fg='black', font=("Helvetica", 18), anchor="ne", bg=main_color, borderwidth=2, relief="groove")
dice_roll.place(x=539, y=240)
btn_start = tk.Button(window, text="Start", bg=main_color, command=start, height=2, width=10, font=("Helvetica", 10))
btn_start.pack(pady=12)

player1_forces = tk.Entry(window, bd=4, width=5, bg=main_color, font=("Helvetica", 10), justify="center")
player2_forces = tk.Entry(window, bd=4, width=5, bg=main_color, font=("Helvetica", 10), justify="center")
player1_forces.place(x=452, y=200)
player2_forces.place(x=597, y=200)

turn_player1 = tk.Label(window, text="Player 1\r↓", fg='black', font=("Helvetica", 24), bg=main_color, borderwidth=3, relief="groove")
turn_player2 = tk.Label(window, text="Player 2\r↓", fg='black', font=("Helvetica", 24), bg=main_color, borderwidth=3, relief="groove")
turn_counter = tk.Label(window, text="Turn 1", fg='black', font=("Helvetica", 18), bg=main_color, borderwidth=3, relief="groove")

player_red = Player(window=window, coords=[120, 320], color="#e6605e", forces=75)
player_red.place_player()
player_blue = Player(window=window, coords=[800, 320], color="#8687eb", forces=75)
player_blue.place_player()


for terr in territories:
    territory = Territory(window=window, coords=terr, name=name_builder(), value=territories.get(terr), trait="No trait", color=main_color)
    territory.t_place()

window.mainloop()
