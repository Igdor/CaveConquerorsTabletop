import random
from PIL import Image, ImageTk
import json


def read_config(section):
    with open('config.json', 'r') as file:
        config = json.load(file)[section]
        return config


def set_item_texture(texture: str, size: tuple):
    texture = Image.open("Resources/" + texture)
    texture = texture.resize(size)
    texture = ImageTk.PhotoImage(texture)
    return texture


def name_builder():
    """This function makes a list with random names for territories."""
    first_words = ["Deep ", "Rocky ", "Damp ", "Abundant ", "Rich ", "Dark ", "Twisted ", "Echoing ", "Howling ", "Mineral "]
    second_words = ["Cave", "Shaft", "Chasm", "Pass", "Depths", "Corridors", "Mines", "Ways", "Stones", "Passage"]
    terr_names = []
    while len(terr_names) < 15:
        name = str(random.choice(first_words) + random.choice(second_words))
        if name not in terr_names:
            terr_names.append(name)
        else:
            continue
    return terr_names


def create_trait_list():
    """This function is served to apply a unique trait to each territory. Used trait is removed from the list"""
    traits = read_config("traits")
    trait_list = []
    while sum(traits.values()) > 0:
        for key in traits:
            if traits[key] == 0:
                continue
            trait_list.append(key)
            traits[key] -= 1
    return trait_list



