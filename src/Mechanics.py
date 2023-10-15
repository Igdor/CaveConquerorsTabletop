import random


traits = ["Add 5 units to your forces", "Roll dice: add or remove this much units from any player", "Add 5 units to your forces", "You can reinforce 1 territory immediately",
          "You can reinforce 1 territory immediately", "If you lost this, roll dice; for 4-6 it'll be destroyed",
          "Roll dice: add or remove this much units from any player", "On your next attack, you roll dice first", "On your next attack, you roll dice first",
          "On your next defense, roll twice", "If you lost this, roll dice; for 4-6 it'll be destroyed", "Reinforce next territory you take for free",
          "Add 5 units to your forces", "No trait", "No trait", "Roll dice: add or remove this much units from any player", "Add 5 units to your forces"]


def name_builder():
    """This function make random names for territories."""
    first_words = ["Deep ", "Rocky ", "Cavernous ", "Abundant ", "Rich ", "Dark ", "Twisted ", "Echoing ", "Howling ", "Mineral "]
    second_words = ["Cave", "Shaft", "Chasm", "Pass", "Depths", "Corridors", "Mines", "Ways", "Stones", "Passage"]

    return str(random.choice(first_words) + random.choice(second_words))


def random_trait():
    """This function is served to apply a unique trait to each territory. Used trait is removed from the list"""
    if not len(traits) == 0:
        trait = str(random.choice(traits))
        traits.remove(trait)
    else:
        trait = "No trait"
    return trait



