import json
import logging


class Item:
    def __init__(self, idx, stats):
        self.index = idx
        self.stats = stats
        self.cost = int(stats["cost"])
        self.name = stats["name"]
        self.attributes = stats["attributes"]


class Character:
    def __init__(self, idx, stats):
        self.index = idx
        # {"size": "small", "Species": "Mouse", "Cost": " 24p", "M": " d6", "S": " d6 ", "B": "d4 ", "R": "d6 ", "N": "d6 ", "C": "d6", "A": " d6 ", "F": "d6", "P": " d6", "Skills": ""}
        self.size = stats["size"]
        self.species = stats["size"]
        self.cost = int(stats["Cost"].replace("p", ""))
        self.stats = stats
        self.M = stats["M"]
        self.S = stats["S"]
        self.B = stats["B"]
        self.R = stats["R"]
        self.N = stats["N"]
        self.C = stats["C"]
        self.A = stats["A"]
        self.F = stats["F"]
        self.P = stats["P"]
        self.skills = stats["Skills"]
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)
        self.cost += item.cost


class Warband:
    def __init__(self):
        self.cost = 0
        self.characters = []

    def add_character(self, character):
        if self.can_afford(character):
            self.characters.append(character)
            self.cost += character.cost
            logging.info(
                "Successfully added new character. The current warband costs %s out of 350 points",
                str(self.cost),
            )
        else:
            logging.error("Failed to add new character!")
            raise ValueError

    def can_afford(self, character):
        return self.cost + character.cost <= 350


character_objects = {}

with open("data/characters.json", "r") as chars:
    char_json = json.load(chars)
chars.close()


with open("data/items.json", "r") as item_file:
    item_json = json.load(item_file)
item_file.close()
