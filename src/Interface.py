from PIL import Image, ImageTk
from Mechanics import set_item_texture
from Mechanics import read_config
from Board import *
import random

main_color = '#BFA173'
red_player_color = "#e6605e"
blue_player_color = "#8687eb"
green_player_color = "#316127"

# inintialising main window
window = tk.Tk()
window.title("Cave Conquerors")
window.geometry("1800x950+10+20")
window.configure(bg=main_color)


lbl = tk.Label(window, text="Cave Conquerors", fg='black', font=("Helvetica", 18), anchor="ne", bg=main_color)
lbl.pack()
version = tk.Label(window, text="v2.0", fg='black', font=("Helvetica", 9), anchor="e", bg=main_color)
version.pack()

dice_pic = Image.open("Resources/dice.png")
dice_pic = dice_pic.resize((70, 70))
dice_pic = ImageTk.PhotoImage(dice_pic)

backgroundimg = set_item_texture("background.jpg", (1795, 900))
bcg = tk.Label(window, image=backgroundimg)
bcg.place(x=0, y=60)

# creating players interface

turn_player1 = tk.Label(window, text="Player 1\r↓", fg='black', font=("Helvetica", 24), bg=main_color, borderwidth=3, relief="groove")
turn_player2 = tk.Label(window, text="Player 2\r↓", fg='black', font=("Helvetica", 24), bg=main_color, borderwidth=3, relief="groove")
turn_player3 = tk.Label(window, text="Player 3\r→", fg='black', font=("Helvetica", 24), bg=main_color, borderwidth=3, relief="groove")
turn_counter = tk.Label(window, text="Turn 1", fg='black', font=("Helvetica", 18), bg=main_color, borderwidth=3, relief="groove")

player_red = Player(window=window, coords=[125, 220], color=red_player_color, forces=40, type="dwarf", name="Player 1")
player_red.place_player()
player_blue = Player(window=window, coords=[695, 220], color=blue_player_color, forces=40, type="dwarf", name="Player 2")
player_blue.place_player()
player_green = Player(window=window, coords=[408, 655], color=green_player_color, forces=100, type="goblin", name="Player 3")
player_green.place_player()


# creating combat interface

canvas_combat = tk.Canvas(window, width=300, height=300, relief=tk.GROOVE, borderwidth=5, bg=main_color, highlightbackground="black")
canvas_combat.pack_propagate(False)
canvas_combat.place(x=910, y=400)


def battle_reset():
    dice_roll.configure(text="  ")
    dice_roll_2.configure(text="  ")
    attacker_picker.configure(background=main_color, activebackground=main_color)
    defender_picker.configure(background=main_color, activebackground=main_color)
    attacker_picker.menu.update()
    defender_picker.menu.update()


btn_combat = tk.Button(canvas_combat, text="Battle", fg='black', font=("Helvetica", 12),
                       command=battle_reset, anchor="n", bg=main_color, borderwidth=2, relief="groove")

attacker_picker = tk.Menubutton(canvas_combat, text="Attacker", relief="raised", background=main_color,
                                activebackground=main_color, justify="center", border=0, font=("Helvetica", 12))
attacker_picker.menu = tk.Menu(attacker_picker, tearoff=0, background=main_color)
attacker_picker["menu"] = attacker_picker.menu

defender_picker = tk.Menubutton(canvas_combat, text="Defender", relief="raised", background=main_color,
                                activebackground=main_color, justify="center", border=0, font=("Helvetica", 12))
defender_picker.menu = tk.Menu(defender_picker, tearoff=0, background=main_color)
defender_picker["menu"] = defender_picker.menu
# players_colors = [red_player_color, blue_player_color, "green"]
# for entry in players_colors:
#     attacker_picker.menu.add_command(label=Player.get_name(Player.instances[players_colors.index(entry)]),
#                                      command=lambda: attacker_picker.configure(background=entry, activebackground=entry),
#                                      background=entry)
#     defender_picker.menu.add_command(label=Player.get_name(Player.instances[players_colors.index(entry)]),
#                                      command=lambda: defender_picker.configure(background=entry, activebackground=entry),
#                                      background=entry)
# TODO: Figure out why loop isn't working properly here
attacker_picker.menu.add_command(label=Player.get_name(Player.instances[0]),
                                 command=lambda: attacker_picker.configure(background=red_player_color, activebackground=red_player_color), background=red_player_color)
attacker_picker.menu.add_command(label=Player.get_name(Player.instances[1]),
                                 command=lambda: attacker_picker.configure(background=blue_player_color, activebackground=blue_player_color), background=blue_player_color)
attacker_picker.menu.add_command(label=Player.get_name(Player.instances[2]),
                                 command=lambda: attacker_picker.configure(background=green_player_color, activebackground=green_player_color), background=green_player_color)
defender_picker.menu.add_command(label=Player.get_name(Player.instances[0]),
                                 command=lambda: defender_picker.configure(background=red_player_color, activebackground=red_player_color), background=red_player_color)
defender_picker.menu.add_command(label=Player.get_name(Player.instances[1]),
                                 command=lambda: defender_picker.configure(background=blue_player_color, activebackground=blue_player_color), background=blue_player_color)
defender_picker.menu.add_command(label=Player.get_name(Player.instances[2]),
                                 command=lambda: defender_picker.configure(background=green_player_color, activebackground=green_player_color), background=green_player_color)

btn_dice = tk.Button(canvas_combat, image=dice_pic, bg=main_color, command=lambda: dice_roll.configure(text=random.choice(range(1, 7))), height=50, width=50, font=("Helvetica", 10))
btn_dice_2 = tk.Button(canvas_combat, image=dice_pic, bg=main_color, command=lambda: dice_roll_2.configure(text=random.choice(range(1, 7))), height=50, width=50, font=("Helvetica", 10))
dice_roll = tk.Label(canvas_combat, text="  ", fg='black', font=("Helvetica", 18), anchor="ne", bg=main_color, borderwidth=2, relief="groove")
dice_roll_2 = tk.Label(canvas_combat, text="  ", fg='black', font=("Helvetica", 18), anchor="ne", bg=main_color, borderwidth=2, relief="groove")

player1_forces = tk.Entry(canvas_combat, bd=4, width=6, bg=main_color, font=("Helvetica", 10), justify="center")
player2_forces = tk.Entry(canvas_combat, bd=4, width=6, bg=main_color, font=("Helvetica", 10), justify="center")

# lbl_rally = tk.Label(canvas_combat, text="Rally", fg='black', font=("Helvetica", 12), anchor="n", bg=main_color, borderwidth=0, relief="groove")
cbx_rally_left = tk.Checkbutton(canvas_combat, text="Rally", bg=main_color, activebackground=main_color, font=("Helvetica", 12))
cbx_rally_right = tk.Checkbutton(canvas_combat, text="Rally", bg=main_color, activebackground=main_color, font=("Helvetica", 12))
cbx_rally_left.select()
cbx_rally_right.select()

cbx_diversion_left = tk.Checkbutton(canvas_combat, text="Diversion", bg=main_color, activebackground=main_color, font=("Helvetica", 12))
cbx_diversion_right = tk.Checkbutton(canvas_combat, text="Diversion", bg=main_color, activebackground=main_color, font=("Helvetica", 12))
cbx_diversion_left.select()
cbx_diversion_right.select()

cbx_buckleup_left = tk.Checkbutton(canvas_combat, text="Buckle Up", bg=main_color, activebackground=main_color, font=("Helvetica", 12))
cbx_buckleup_right = tk.Checkbutton(canvas_combat, text="Buckle Up", bg=main_color, activebackground=main_color, font=("Helvetica", 12))
cbx_buckleup_left.select()
cbx_buckleup_right.select()


btn_combat.place(x=130, y=10)
attacker_picker.place(x=40, y=10)
defender_picker.place(x=200, y=10)

player1_forces.place(x=50, y=60)
btn_dice.place(x=50, y=100)
dice_roll.place(x=116, y=110)

player2_forces.place(x=210, y=60)
btn_dice_2.place(x=210, y=100)
dice_roll_2.place(x=180, y=110)

cbx_rally_left.place(x=30, y=160)
cbx_rally_right.place(x=190, y=160)

cbx_diversion_left.place(x=30, y=190)
cbx_diversion_right.place(x=190, y=190)

cbx_buckleup_left.place(x=30, y=220)
cbx_buckleup_right.place(x=190, y=220)

# creating descriptions interface

trait_descriptions = read_config("trait_descriptions")
rules_descriptions = read_config("rules_descriptions")
canvas_description_list = []
icons = []


def switch_page():
    if canvas_description_list[0]:
        canvas_description_list[0].place_forget()
        canvas_description_list[1].place(x=1300, y=100)
        canvas_description_list[0], canvas_description_list[1] = canvas_description_list[1], canvas_description_list[0]


def create_canvas_description(canvas_title, item_description_list):
    canvas_description = tk.Canvas(window, width=400, height=700, relief=tk.GROOVE, borderwidth=5, bg=main_color, highlightbackground="black")
    canvas_description.pack_propagate(False)

    item_description_label = tk.Label(canvas_description, text=canvas_title, fg='black', font=("Helvetica", 18), anchor="w", bg=main_color)
    item_description_label.pack(pady=8)
    position = 0
    for item in item_description_list:
        if item[0] != 0:
            icon = set_item_texture(item[0], (50, 50))
            icons.append(icon)
            canvas_description.create_image(30, 68 + position, image=icon)
        canvas_description.create_text(55, 68 + position, text=item[1], font=("Helvetica", 10), width=350, anchor="w",
                                       activefill="#313d52")
        position += 49
    button_next = tk.Button(canvas_description, text="►", bg=main_color, command=switch_page, height=1, width=2,
                            font=("Helvetica", 10))
    canvas_description.create_window(385, 30, window=button_next)
    canvas_description_list.append(canvas_description)

create_canvas_description("Rules:", rules_descriptions)
create_canvas_description("Traits:", trait_descriptions)

active_canvas_description = canvas_description_list[0]

