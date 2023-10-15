import tkinter as tk
from Mechanics import random_trait, name_builder

#  Field constructors


class Player:
    """This class used to create starting point on the field for each player.
     It also used as a holder of player data: amount of units and score."""
    def __init__(self, window, coords: list[int, int], forces: int, color: str):
        self.window = window
        self.coords = coords
        self.position = None
        self.name = None
        self.forces = forces
        self.color = color
        self.field_forces = None
        self.player_forces = None

    def place_player(self):
        self.position = tk.Canvas(self.window, width=150, height=150, relief=tk.GROOVE, borderwidth=5, bg=self.color,
                                  highlightbackground="black")
        self.position.place(x=self.coords[0], y=self.coords[1])
        self.player_forces = tk.Label(self.position, bd=4, width=6, text=self.forces, bg=self.color, font=("Helvetica", 14), )
        self.field_forces = tk.Entry(self.position, bd=4, width=4, bg=self.color, font=("Helvetica", 10),
                                     justify="center")

        player_name = tk.Entry(self.position, bd=4, width=10, bg=self.color, font=("Helvetica", 10), justify="center")
        player_forces_label = tk.Label(self.position, text="Units", bd=4, width=6, bg=self.color, font=("Helvetica", 14),
                                       justify="center")
        player_score_label = tk.Label(self.position, text="Score", bd=4, width=6, bg=self.color, font=("Helvetica", 14),
                                      justify="center")
        player_score = tk.Entry(self.position, bd=4, width=6, bg=self.color, font=("Helvetica", 10), justify="center")

        btn_add_forces = tk.Button(self.position, text="+", bg=self.color, command=self.add_units, height=1,
                                   width=2, font=("Helvetica", 10))
        btn_subtract_forces = tk.Button(self.position, text="-", bg=self.color, command=self.subtract_units, height=1,
                                        width=2, font=("Helvetica", 10))

        self.position.create_window(82, 20, window=player_name)
        self.position.create_window(50, 60, window=player_forces_label)
        self.position.create_window(112, 60, window=self.player_forces)
        self.position.create_window(50, 140, window=player_score_label)
        self.position.create_window(112, 140, window=player_score)
        self.position.create_window(80, 90, window=self.field_forces)
        self.position.create_window(120, 90, window=btn_add_forces)
        self.position.create_window(40, 90, window=btn_subtract_forces)

    def add_units(self):
        self.forces += int(self.field_forces.get())
        self.player_forces.configure(text=self.forces)

    def subtract_units(self):
        self.forces -= int(self.field_forces.get())
        self.player_forces.configure(text=self.forces)


class Territory:
    """This class is used for creation of 'caves', forming a game field from square territories.
    Each territory has a name, trait (initially hidden) and value, and can be claimed by player, which is reflected
     by changing color of the territory. It also can be reinforced by player, adding temporary forces"""
    def __init__(self, window, coords: tuple[int, int], name: str, value: int, trait: str, color: str):
        self.window = window
        self.frame_territory = None
        self.coords = coords
        self.name = name
        self.value = value
        self.trait = trait
        self.color = color
        self.is_reinforced = False
        self.is_used = False

    def __str__(self):
        return f"{self.coords}, {self.name}, {self.value}, {self.trait}, {self.color}, {self.is_reinforced}"

    def change_color_red(self):
        """This and next function assign a territory to a corresponding player. It also reveals the hidden trait"""
        self.frame_territory.configure(bg="#e6605e")
        self.frame_territory.itemconfig(tagOrId="trait", text=self.trait)
        self.frame_territory.update()

    def change_color_blue(self):
        self.frame_territory.configure(bg="#8687eb")
        self.frame_territory.itemconfig(tagOrId="trait", text=self.trait)
        self.frame_territory.update()

    def reinforce(self):
        """Adds 5 to a territory forces for better defence. Doesn't affect a value of the territory"""
        self.frame_territory.itemconfig(tagOrId="force", text=str(self.value) + "+5")
        if not self.is_reinforced:
            self.is_reinforced = True
        else:
            self.is_reinforced = False
            self.frame_territory.itemconfig(tagOrId="force", text=str(self.value))
        self.frame_territory.update()

    def use_trait(self):
        if not self.is_used:
            self.frame_territory.itemconfig(tagOrId="trait", fill="grey")
            self.is_used = True
        else:
            self.frame_territory.itemconfig(tagOrId="trait", fill="black")
            self.is_used = False

    def clear(self):
        self.frame_territory.configure(bg=self.color)
        self.frame_territory.update()

    def t_place(self):
        self.trait = random_trait()
        self.frame_territory = tk.Canvas(self.window, width=150, height=150, relief=tk.GROOVE, borderwidth=5,
                                         bg=self.color, highlightbackground="black")
        self.frame_territory.place(x=self.coords[0], y=self.coords[1])
        self.frame_territory.rowconfigure(0, weight=1)
        self.frame_territory.rowconfigure(1, weight=1)
        self.frame_territory.rowconfigure(2, weight=1)
        self.frame_territory.grid_propagate(False)
        self.frame_territory.create_text(80, 20, text=name_builder(), font=("Helvetica", 10), width=140)
        self.frame_territory.create_text(80, 105, text=self.value, font=("Helvetica", 18), tags="force")
        self.frame_territory.create_text(80, 55, text="?", font=("Helvetica", 10), width=140, justify="center", tags="trait")

        btn_red = tk.Button(self.frame_territory, text=" ", bg="#e6605e", command=self.change_color_red, height=1,
                            width=2, font=("Helvetica", 10))
        btn_red.grid(row=2, column=0, padx=8, pady=2, sticky="SW")

        btn_blue = tk.Button(self.frame_territory, text=" ", bg="#8687eb", command=self.change_color_blue, height=1,
                             width=2, font=("Helvetica", 10))
        btn_blue.grid(row=2, column=3, padx=12, pady=2, sticky="SE")

        btn_reinforce = tk.Button(self.frame_territory, text="R", bg=self.color, command=self.reinforce, height=1,
                                  width=2, font=("Helvetica", 10))
        btn_reinforce.grid(row=3, column=2, padx=4, pady=8, sticky="S")

        btn_clear = tk.Button(self.frame_territory, text="C", bg=self.color, command=self.clear, height=1,
                              width=2, font=("Helvetica", 10))
        btn_clear.grid(row=3, column=1, padx=4, pady=8, sticky="S")

        btn_use = tk.Button(self.frame_territory, text="T", bg=self.color, command=self.use_trait, height=1,
                            width=2, font=("Helvetica", 10))
        btn_use.grid(row=3, column=0, padx=4, pady=8, sticky="S")

        field_custom_force=tk.Entry(self.frame_territory, bd=2, width=2, bg=self.color, font=("Helvetica", 10), justify="center")
        field_custom_force.grid(row=3, column=3, padx=4, pady=8)
