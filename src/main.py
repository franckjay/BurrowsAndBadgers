import os
import logging
import pprint
from entities import Warband, item_json, char_json, Character, Item


def boost_stats(die: str) -> str:
    # TODO: Error handling  if you cannot go above a d12
    boost = {"d4": "d6", "d6": "d8", "d8": "d10", "d10": "d12", "d12": "d12"}
    return boost.get(die, "Error!")

def add_spells():
    return
def add_items_to_char(character: Character, wb: Warband):
    # TODO: Need to add item type checking to ensure rules aren't violated
    for idx, values in item_json.items():
        pprint.pprint(
            f"Item Number = {idx}| Name = {values['name']} | Cost {values['cost']}| {values['attributes']}"
        )

    while character.cost + wb.cost < 350:
        pprint.pprint(
            f"Current Warband Cost: {character.cost + wb.cost} out of a maximum of 350"
        )
        selection = input(
            "From the list above, please enter the Item Number of your leader or Done to exit: "
        )
        if selection == "Done":
            break
        item = Item(selection, item_json[selection])
        character.add_item(item)

    return


def create_character(
    warband: Warband, stats_dictionary: dict, is_first=False, is_second=False
) -> Character:
    for idx, values in char_json.items():
        if int(values["Cost"].replace("p", "")) + warband.cost < 350:
            pprint.pprint(
                f"Character Number = {idx}: Species - {values['Species']} and Cost {values['Cost']}"
            )

    if is_first:
        selection = input(
            "From the list above, please enter the Character Number of your leader: "
        )
        _char = stats_dictionary[selection].copy()
        stat_increase = input(
            "Increase the stats of any character trait in this list: M S B R N C A F P "
        )
        _char[stat_increase] = boost_stats(_char[stat_increase])
        skill = input("Add in a skill for your leader: ")
        # TODO: Add in a skill parsing mechanism
        _char["Skills"] += " " + skill
    elif is_second:
        selection = input(
            "From the list above, please enter the Character Number of your 2nd in Command: "
        )
        _char = stats_dictionary[selection].copy()
        stat_increase = input(
            "Increase the stats of any character trait in this list: M S B R N C A F P "
        )
        _char[stat_increase] = boost_stats(_char[stat_increase])
    else:
        selection = input(
            "From the list above, please enter the Character Number of your next warrior: "
        )
        _char = stats_dictionary[selection].copy()
    _char_obj = Character(selection, _char)
    add_items_to_char(_char_obj, warband)
    #TODO: Add in spells with add_spells(_char_obj, warband)
    return _char_obj


def main():
    wb = Warband()

    wb.add_character(create_character(wb, char_json, is_first=True))
    wb.add_character(create_character(wb, char_json, is_second=True))

    while wb.cost <= 350:
        wb.add_character(create_character(wb, char_json))


if __name__ == "__main__":
    logging.info("We will help build your Warband for Burrows and Badgers!")
    main()
