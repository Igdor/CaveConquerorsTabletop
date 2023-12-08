import tkinter as tk
from Mechanics import create_trait_list, name_builder, set_item_texture

#  Field constructors


class Player:
    """This class used to create starting point on the field for each player.
     It also used as a holder of player data: amount of units and score."""
    instances = []

    def __init__(self, window, coords: list[int, int], forces: int, color: str, type: str, name: str):
        self.window = window
        self.coords = coords
        self.forces = forces
        self.color = color
        self.type = type
        self.position = None
        self.name = name
        self.icon = None
        self.player_forces = None
        self.player_name_field = None
        self.__class__.instances.append(self)

    def place_player(self):
        self.position = tk.Canvas(self.window, width=150, height=150, relief=tk.GROOVE, borderwidth=5, bg=self.color,
                                  highlightbackground="black")
        self.position.place(x=self.coords[0], y=self.coords[1])

        self.player_name_field = tk.Entry(self.position, bd=4, width=12, bg=self.color, font=("Helvetica", 10), justify="center")
        self.player_name_field.insert(0, self.name)
        player_score = tk.Entry(self.position, bd=4, width=4, bg=self.color, font=("Helvetica", 10), justify="center")
        player_score_label = tk.Label(self.position, text="Score", bd=4, width=6, bg=self.color, font=("Helvetica", 12),
                                      justify="center")
        if self.type == "dwarf":
            self.player_forces = tk.Label(self.position, bd=4, width=6, text=self.forces, bg=self.color,
                                          font=("Helvetica", 12), )
            player_forces_label = tk.Label(self.position, text="Units", bd=2, width=4, bg=self.color, font=("Helvetica", 12),
                                           justify="center")

            btn_add_forces = tk.Button(self.position, text="+", bg=self.color, command=self.add_units, height=1,
                                       width=1, font=("Helvetica", 10))
            btn_subtract_forces = tk.Button(self.position, text="-", bg=self.color, command=self.subtract_units, height=1,
                                            width=1, font=("Helvetica", 10))

            cbx_ability_dwarf = tk.Checkbutton(self.position, text="Rush", variable=self.name, bg=self.color, activebackground=self.color, font=("Helvetica", 12))
            cbx_ability_dwarf.select()

            self.position.create_window(50, 80, window=player_forces_label)
            self.position.create_window(50, 110, window=self.player_forces)
            self.position.create_window(25, 110, window=btn_subtract_forces)
            self.position.create_window(75, 110, window=btn_add_forces)
            self.position.create_window(50, 140, window=cbx_ability_dwarf)
            if self.name == "Player 1":
                self.icon = set_item_texture("Dwarf1.png", (80, 80))
            else:
                self.icon = set_item_texture("Dwarf2.png", (80, 80))
            self.position.create_image(120, 115, image=self.icon)
        else:
            goblin_territory_note = tk.Label(self.position, text="Max 3\rterritories", bd=2, width=6, bg=self.color, font=("Helvetica", 10),
                                             justify="center")
            cbx_ability_goblin = tk.Checkbutton(self.position, text="Sneak", variable=self.name, bg=self.color, activebackground=self.color, font=("Helvetica", 12))
            cbx_ability_goblin.select()
            self.position.create_window(50, 90, window=goblin_territory_note)
            self.position.create_window(50, 130, window=cbx_ability_goblin)
            self.icon = set_item_texture("Goblin.png", (80, 80))
            self.position.create_image(120, 115, image=self.icon)

        self.position.create_window(82, 20, window=self.player_name_field)
        self.position.create_window(50, 50, window=player_score_label)
        self.position.create_window(115, 50, window=player_score)

    def add_units(self):
        self.forces += 1
        self.player_forces.configure(text=self.forces)

    def subtract_units(self):
        self.forces -= 1
        self.player_forces.configure(text=self.forces)

    def get_name(self):
        self.name = self.player_name_field.get()
        return self.name



class Territory:
    """This class is used for creation of 'caves', forming a game field from square territories.
    Each territory has a name, trait (initially hidden) and value, and can be claimed by player, which is reflected
     by changing color of the territory. It also can be reinforced by player, adding temporary forces"""
    instances = []

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
        self.menu_color = None
        self.__class__.instances.append(self)

    def __str__(self):
        return f"{self.coords}, {self.name}, {self.value}, {self.trait}, {self.color}, {self.is_reinforced}"

    def change_color(self, color):
        """This function assign a territory to a player of corresponding color. It also reveals the hidden trait"""
        self.frame_territory.configure(bg=color)
        self.frame_territory.itemconfig(tagOrId="trait", text=self.trait)
        self.menu_color.config(background=color)
        self.frame_territory.configure()
        self.frame_territory.update()

    def reinforce(self):
        """Adds 5 to a territory forces for better defence. Doesn't affect a value of the territory"""
        self.frame_territory.itemconfig(tagOrId="force", text=str(self.value) + "(R)")
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

    def t_place(self):
        self.frame_territory = tk.Canvas(self.window, width=120, height=120, relief=tk.GROOVE, borderwidth=5,
                                         bg=self.color, highlightbackground="black")
        self.frame_territory.place(x=self.coords[0], y=self.coords[1])
        self.frame_territory.rowconfigure(0, weight=1)
        self.frame_territory.rowconfigure(1, weight=1)
        self.frame_territory.rowconfigure(2, weight=1)
        self.frame_territory.grid_propagate(False)
        self.frame_territory.create_text(65, 80, text=self.value, font=("Helvetica", 16), tags="force")
        self.frame_territory.create_text(65, 50, text="?", font=("Helvetica", 9), width=140, tags="trait")

        self.menu_color = tk.Menubutton(self.frame_territory, text=self.name, relief="raised", background=self.color,
                                        activebackground=self.color, justify="center", border=0)
        self.menu_color.menu = tk.Menu(self.menu_color, tearoff=0, background=self.color)
        self.menu_color["menu"] = self.menu_color.menu

        self.menu_color.menu.add_command(label=Player.get_name(Player.instances[0]), command=lambda: self.change_color("#e6605e"), background="#e6605e")
        self.menu_color.menu.add_command(label=Player.get_name(Player.instances[1]), command=lambda: self.change_color("#8687eb"), background="#8687eb")
        self.menu_color.menu.add_command(label=Player.get_name(Player.instances[2]), command=lambda: self.change_color("#316127"), background="#316127")
        self.menu_color.menu.add_command(label="Clear", command=lambda: self.change_color(self.color), background=self.color)
        self.menu_color.place(x=65, y=10, anchor="n")

        btn_reinforce = tk.Button(self.frame_territory, text="R", bg=self.color, command=self.reinforce, height=1,
                                  width=2, font=("Helvetica", 10))

        btn_use = tk.Button(self.frame_territory, text="T", bg=self.color, command=self.use_trait, height=1,
                            width=2, font=("Helvetica", 10))
        field_custom_force = tk.Entry(self.frame_territory, bd=2, width=2, bg=self.color, font=("Helvetica", 10), justify="center")
        btn_reinforce.place(x=35, y=125, anchor="s")
        btn_use.place(x=70, y=125, anchor="s")
        field_custom_force.place(x=105, y=125, anchor="s")


