from Interface import *

import tkinter as tk


turn = 1
player = 1
# TODO  : Give player more control over the game. Add more interactions between territories, better traits for deeper territories
territories = {
    (290, 250): 5, (425, 250): 15, (560, 250): 5,  # first line
    (155, 385): 5, (290, 385): 10, (425, 385): 15, (560, 385): 10, (695, 385): 5,  # second line
    (155, 520): 10, (290, 520): 10, (425, 520): 5, (560, 520): 10, (695, 520): 10  # third line
}


def start():
    btn_turn = tk.Button(window, text="End Turn", bg=main_color, command=advance_turn, height=2, width=10, font=("Helvetica", 10))
    btn_turn.pack(pady=12)
    turn_counter.pack()
    btn_restart = tk.Button(window, text="Restart", bg=main_color, command=restart, height=2, width=10, font=("Helvetica", 10))
    btn_restart.place(x=30, y=70)
    turn_player1.place(x=140, y=130)
    btn_start.destroy()
    traits = create_trait_list()
    names = name_builder()
    for terr in territories:
        trait = str(random.choice(traits))
        traits.remove(trait)
        name = random.choice(names)
        names.remove(name)
        territory = Territory(window=window, coords=terr, name=name, value=territories.get(terr), trait=trait,
                              color=main_color)
        territory.t_place()


def restart():
    for instance in Territory.instances:
        del instance
    global player
    global turn
    turn = 1
    player = 1
    turn_counter.configure(text="Turn 1")
    turn_player1.place(x=140, y=130)
    turn_player2.place_forget()
    turn_player3.place_forget()
    traits = create_trait_list()
    names = name_builder()
    for terr in territories:
        trait = str(random.choice(traits))
        traits.remove(trait)
        name = random.choice(names)
        names.remove(name)
        territory = Territory(window=window, coords=terr, name=name, value=territories.get(terr), trait=trait,
                              color=main_color)
        territory.t_place()

def advance_turn():
    """This function adds a pointer to a currently acting player, and advances turn forward after both players acted.
    Also, it adds 5 to player forces at the beginning of each turn"""
    global player
    global turn
    if player == 1:
        player = 2
        turn_player2.place(x=710, y=130)
        turn_player1.place_forget()

    elif player == 2:
        player = 3
        turn_player3.place(x=270, y=680)
        turn_player2.place_forget()
    else:
        turn += 1
        player = 1
        turn_counter.configure(text="Turn " + str(turn))

        turn_player1.place(x=140, y=130)
        turn_player3.place_forget()
        # player_red.forces += 5
        # player_red.player_forces.configure(text=player_red.forces)
        # player_blue.forces += 5
        # player_blue.player_forces.configure(text=player_blue.forces)


btn_start = tk.Button(window, text="Start", bg=main_color, command=start, height=2, width=10, font=("Helvetica", 10))
btn_start.pack(pady=12)

canvas_description_list[0].place(x=1300, y=100)

window.mainloop()
