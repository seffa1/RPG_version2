# region Imports
from collections import Counter
import classes
from classes import Clock
from classes import Player
from classes import Action_Menu
from classes import Travel_Menu
from classes import Player_Menu
from classes import Equip_Menu
from classes import Location
from classes import Shop
from classes import Weapon
from classes import Raw_Material
import sys
from dialogue import Dialogue
import os
# from functools import cache
# endregion
sys.setrecursionlimit(100000)

# region GLOBAL OBJECTS
player = Player('')
clock = Clock()
action_menu = Action_Menu('action')
travel_menu = Travel_Menu('travel')
player_menu = Player_Menu('player')


# endregion


# region Utility Functions
def clear():
    os.system('cls')


def pause():
    input("press enter to continue")


def select():
    a = input("----->")
    return a


def character_creation(player):
    clear()
    print("Welcome to my game")
    print("\nPress Enter To Begin Your Journey\n")
    pause()
    clear()
    print("Whom may we call you?\n")
    a = select()
    while a.lower() == '':
        print('Whom may we call you?\n')
        a = select()
    player.name = a
    clear()
    print(f"Welcome {player.name}, where do you come from?")
    print(
        "\n(1) -----> BLACKSMITH <----- (1)\n"
        "You come from a long line of blacksmiths.\n"
        "Every since you were a child you were swinging a hammer.\n"
        "This will no doubt come in handy for the path that lay ahead.\n"
        "You dont swing a hammer for no reason of course.\n"
        "You are not your father yet, but you can craft some basic weapons and armor to aid you.\n"

        "\n(2) -----> HUNTER <----- (2)\n"
        "Your father died when you were young.\n"
        "Fishing and hunting are skills you have learned in order to survive and\n"
        "bringing your bow and arror to the forest is your meditation.\n"

        "\n(3) -----> SCHOLAR <----- (3)\n"
        "You are a bastard child to a nobel family.\n"
        "Ashamed by your mother, you were hidden away in the library.\n"
        "Your time there has made you and exceptionally fast learner.\n"
        "Although you have read about great warriors, you are not one yourself.\n"
        "Perhaps you will find other ways to defend yourself, but why would you, you are apart of a nobel estate afterall...\n"
    )
    a = select()
    while a.lower() not in ['1', '2', '3']:
        a = select()
    clear()
    if a.lower() == '1':  # blacksmith stats
        player_stats = {'type': 1, 'melee': 15, 'intelligence': 2, 'archery': 0, 'defence': 0,
                        'health': 125, 'mana': 0, 'stamina': 125}
    elif a.lower() == '2':  # hunter stats
        player_stats = {'type': 2, 'melee': 1, 'intelligence': 5, 'archery': 10, 'defence': 0,
                        'health': 100, 'mana': 20, 'stamina': 100}
    else:  # scholar stats
        player_stats = {'type': 3, 'melee': 1, 'intelligence': 15, 'archery': 1, 'defence': 0,
                        'health': 75, 'mana': 100, 'stamina': 75}
    player.type = player_stats['type']
    player.melee = player_stats['melee']
    player.intelligence = player_stats['intelligence']
    player.archery = player_stats['archery']
    player.defence = player_stats['defence']
    player.health = player_stats['health']
    player.mana = player_stats['mana']
    player.stamina = player_stats['stamina']
    clear()





def startDay1(player):
    if player.type == 1:
        print("Day 1")
        print(
            "\nYou spend your days near the forge with your father, learning how to shape metal to get by.\n"
            "Your mother died along side your little brother at birth.\n"
            "Your father grows sicker by the day from years of working with harsh materials.\n"
            "You ofter wonder what you will make of yourself when the day comes, where you must venture out on your own.\n")
        pause()
        clear()
        player.add_quest('craft leather armor')
        # need to a add getting a hammer
        # print('smiths hammer equipped')


    elif player.type == 2:
        print("Day 1")
        print(
            "\nYour only concern is keeping food stores full, and enjoying the simple things in life, the birds, the grass, and the wind.\n"
            "You dont have any reason to leave. Your mother and sister enjoy the tribe you are apart of.\n"
            "So what is there to worry about....?\n")
        pause()
        clear()
        player.add_quest('cook a fish')


    else:
        print("Day 1")
        print(
            '\nYou are the son of a nobel family living in a thriving town.\n'
            'The stone walls surrounding the town keep those rich enough to live inside safe.\n'
            'The guards rarely open the gate except for emergencies and trade.\n'
            'You are never aloud to leave the town, as its much too dangerous for a boy like yourself.\n'
            'Instead you are expected to study in the library, and practice your alchemy.\n')
        pause()
        clear()
        player.add_quest('brew a healing potion')
        player.add_quest('study')
    return travel(hut)


def startDay2(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    clock1.day2 = True
    if player.getType() == 1:
        print("\nYou are awakend by low rumbling sensation.")
        print("It feels like an earthquake, but it seems to have brought a chill to the air with it.")
        print("Perhaps people in the tavern may have seen something.")

    elif player.getType() == 2:
        print("\nYou wake up to the sound of commotion outside the hut\n")

    else:
        print('\nYou are awakened by an old servant.')
        print(f'{player.getName()}, you must find a way out of this town.')
        print(f'There are rumors of dark forces arrising beyond the walls.')
        print(f'Nobody will listen to a servant, but you have always been kind to us.')
        print(f'There is a secret passage in the library, I left a lantern near by.')
        print(f'You should be able to get out through that way.')
        print(f'But stay away from the tunnels down there, we arent sure where they lead to.')
        print(f'And everday we find books burned up back there, we arent sure why yet.')
        print(
            f'But you should be small enough to get out through the sewers and find out what people are saying out there.')
        print('\nQuest: Escape through the sewers')
        heroInventory.currentQuests.append('escape through the sewers')
        travels.secretPassage = Tru


# def startDay3(player, clock1, heroInventory, stock, actions, travels, skills, fire):
#     clock1.day3 = True
#     if player.getType() == 1:
#         print("\nIts the start of a new week, the crossroads caravan should be open now.")
#         print('Quest: Travel the crossroads')
#         heroInventory.currentQuests.append('Travel the crossroads')
#     elif player.getType() == 2:
#         print("\nIts the start of a new week, the crossroads caravan should be open now.")
#         print('Quest: Travel the crossroads')
#         heroInventory.currentQuests.append('Travel the crossroads')
#     else:
#         if travels.crawledThroughSewers == False:
#             print('\nWhat are you still doing here?!')
#             print('Didnt you see the lantern by the passage in the library?')
#             print('Here let me bring you over there now')
#             input('Press enter to continue\n')
#             print('Also, its a great time to leave as the crossroads caravan should be open now')
#             print('It will let you pass down to the huting village')
#             print('Apparently food is abundent down there')
#             print('\nQuest: Travel the crossroads')
#             heroInventory.currentQuests.append('Travel the crossroads')
#             input('Press enter to continue\n')
#             travels.forceThroughSecretPassage = True
#             library(player, clock1, heroInventory, stock, actions, travels, skills, fire)
#         else:
#             print("\nIts the start of a new week, the crossroads caravan should be open now.")
#             print('Quest: Travel the crossroads')
#             input('Press enter to continue')
#             heroInventory.currentQuests.append('Travel the crossroads')
# def startDay4(player, clock1, heroInventory, stock, actions, travels, skills, fire):
#     clock1.day4 = True
#     print('\nTheres word that the town gates are opened to the public now')
#     print('Apparently they are concerned about a scholar who went missing.')
#     travels.secretPassage = True
#
#     if player.getType() == 3:
#         print('\nIt looks like they figured out I escaped.')
#         print('Well its the first time I every got any of there attention')
#         print('At least now they will let me travel freely in and out of the walls')
#         input('press enter to continue')
#         print('')
# def startDay5(player, clock1, heroInventory, stock, actions, travels, skills, fire):
#     clock1.day5 = True
# def startDay6(player, clock1, heroInventory, stock, actions, travels, skills, fire):
#     clock1.day6 = True
# def startDay7(player, clock1, heroInventory, stock, actions, travels, skills, fire):
#     clock1.day7 = True
# def startDay8(player, clock1, heroInventory, stock, actions, travels, skills, fire):
#     clock1.day8 = True
# def startDay9(player, clock1, heroInventory, stock, actions, travels, skills, fire):
#     clock1.day9 = True
# def startDay10(player, clock1, heroInventory, stock, actions, travels, skills, fire):
#     clock1.day10 = True
# def startDay11(player, clock1, heroInventory, stock, actions, travels, skills, fire):
#     clock1.day11 = True
# endregion


#  Clock functions


# region MAIN MENUS
def inventory():
    clear()
    player.show_inventory()
    a = select()
    while a not in ['x', 'X', 'e', 'E', 'u', 'U']: a = select()
    if a.lower() == 'x': give_options()
    if a.lower() == 'e': equip_items()


def equip_items():  # also unequips items
    clear()
    equip_menu = Equip_Menu('equip', player)
    equip_menu.update_equipment()
    equip_menu.display_menu()
    options = ['x', 'X']
    if len(player.main_hand) > 0: options.extend(['m', 'M'])
    if len(player.off_hand) > 0: options.extend(['o', 'O'])
    if len(player.armor) > 0: options.extend(['a', 'A'])
    if len(player.charm) > 0: options.extend(['c', 'C'])

    a = select()
    while a not in options and a not in equip_menu.menu_options.keys(): a = select()  # need to allow you to actually pick up a weapon
    if a.lower() == 'x':
        inventory()
    elif a.lower() in options:
        if a.lower() == 'm':
            item = player.main_hand[0]
        elif a.lower() == 'o':
            item = player.off_hand[0]
        elif a.lower() == 'a':
            item = player.armor[0]
        else:
            item = player.charm[0]
        player.unequip_item(item)
        player.add_item(item, 1)


    else:  # equip items
        item = equip_menu.menu_options[a]
        if player.equip_item(item):
            player.remove_item(item, 1)
            player.inventory += Counter()

    equip_items()


def combat():
    clear()
    print('You are in combat')
    pause()
    give_options()


def current_stats():
    player.show_current_stats()
    a = select()
    while a not in ['x', 'X']: a = select()
    give_options()


def eat():
    clear()
    print('You are eating')
    pause()
    give_options()


def quests():
    clear()
    print('CURRENT QUESTS:')
    for current_quest in player.get_current_quests():
        print(current_quest)

    print('\nCOMPLETED QUESTS:')
    for completed_quest in player.get_completed_quests():
        print(completed_quest)

    print('\nX ---> Back\n')

    a = select()
    while a not in ['x', 'X']: a = select()
    give_options()


# endregion


# region LOCATION ACTIONS
def sleep():
    clear()
    print('You are sleeping')
    pause()
    give_options()


def cook():
    clear()
    print('You are cooking')
    pause()
    give_options()


def light_fire():
    clear()
    print('You light the fire')
    pause()
    give_options()


def fish():
    clear()
    print('You are fishing')
    pause()
    give_options()


# @cache
def gather_sticks():
    clear()
    player.show_stats()
    clock.display_time()
    player.display_item('stick')
    print('---------')
    print("Enter to gather sticks")
    print('X ---> Back')
    a = '1'
    while a not in ['X', 'x', '']:
        a = input('--->')
    if a in ['X', 'x']:
        give_options()
    if a in ['']:
        stick = Raw_Material('stick')
        # If item not in players inventory, player.add_item
        # Else, player.update[item]
        player.add_item(stick, 3)
        clock.add_time(10)
        gather_sticks()



def hunt_deer():
    clear()
    print('You are hunting deer')
    pause()
    give_options()


def search_for_steel():
    clear()
    print('You are searching for steel')
    pause()
    give_options()


def gather_fiber():
    clear()
    print('You are gathering fiber')
    pause()
    give_options()


def pick_berries():
    clear()
    print('You are picking berries')
    pause()
    give_options()


def pray():
    clear()
    print('You are praying')
    pause()
    give_options()


# region Shopping
def enter_shop():
    clear()
    shop = Shop(player.gold, item_prices)
    options = {'B': 'Buy', 'S': 'Sell', 'X': 'Back'}
    function_map = {'B': buy_items, 'S': sell_items, 'X': give_options}
    print(f"Gold: {player.gold}")
    print(f"Welcome, {player.name} to the shop")
    for i in map(lambda key, val: f'{key} ---> {val}', options.keys(), options.values()): print(i)  # prints the options
    a = select()
    while not a.upper() in options.keys(): a = select()
    function_map[a.upper()]()


def buy_items():
    clear()
    shop = Shop(player.gold, item_prices)
    shop.display_menus()
    a = select()
    while a not in SHOP_MAP.keys(): a = select()
    SHOP_MAP[a]()
    pause()
    enter_shop()


def shop_raw_materials():
    clear()
    shop = Shop(player.gold, item_prices)
    shop.display_raw_material()
    a = select()
    while a not in SHOP_RAW_MATERIALS_MAP.keys() and a not in ['x', 'X']: a = select()
    if a == 'x' or a == 'X': buy_items()

    item = SHOP_RAW_MATERIALS_MAP[a]
    player.buy_item(item, item_prices[item.name])
    shop_raw_materials()


def shop_food():
    clear()
    shop = Shop(player.gold, item_prices)
    shop.display_food()


def shop_weapons():
    clear()
    shop = Shop(player.gold, item_prices)
    shop.display_weapons()
    a = select()
    while a not in SHOP_WEAPONS_MAP.keys() and a not in ['x', 'X']: a = select()
    if a == 'x' or a == 'X': buy_items()

    item = SHOP_WEAPONS_MAP[a]
    player.buy_item(item, item_prices[item.name])
    shop_weapons()


def shop_armor():
    shop.display_armor()


def shop_arrows():
    shop.display_arrows()


def shop_potions():
    shop.display_potions()


def sell_items():
    clear()
    print('You are selling items')
    pause()
    enter_shop()


# endregion

def enter_hunting_tavern():
    clear()
    print('You are entering the hunting tavern')
    pause()
    give_options()


# endregion


# region TRAVEL FUNCTIONS
# -----------------------> Generates and updates the main menu when you travel <------------------------- #
def update_options(location):
    global index
    index = 1

    action_menu.clear_actions()
    for action in location.actions:  # a list of action functions to be added to actions menu
        action_menu.add_action(index, action)
        index += 1

    travel_menu.clear_locations()
    for route in location.routes:  # a list of location objects
        travel_menu.update_locations(index, route)
        index += 1

    return index


def give_options():
    clear()
    print(player)
    player_menu.show_menu()
    action_menu.show_menu()
    travel_menu.show_menu()

    choices = []
    for i in range(1, index): choices.append(str(i))
    for i in player_menu.options.keys(): choices.append(i)
    print('')

    a = select()
    if type(a) is str:
        a = a.capitalize()

    # DEV TESTING
    if a == 'Test':
        get_some_stuff()
        give_options()
    # DEV TESTING

    while a not in choices:
        a = select()
        if type(a) is str:
            a = a.capitalize()

    if a in player_menu.options.keys():
        MAIN_MENU_MAP[player_menu.options[a]]()  # run the main menu functions

    elif int(a) in action_menu.actions.keys():
        FUNCTION_MAP[action_menu.actions[int(a)]]()  # run the action function

    elif int(a) in travel_menu.locations.keys():
        travel(TRAVEL_MAP[travel_menu.locations[int(a)]])  # travel to the location


def check_has_been(location):  # sees if its the first time you visited a location to give unique dialouge
    if location.has_been_to == False: location.has_been_to = True, Dialogue.show_dialogue(location.name)


def travel(location):
    player.location = location.name
    check_has_been(location)
    index = update_options(location)
    give_options()  # the options the player gets is updated # test


# endregion


# region LOCATIONS
# HUNTER LOCATIONS
hut = Location('hut', ['sleep', 'cook', 'light fire'], ['forest', 'river', 'meadows', 'village'])
river = Location('river', ['fish'], ['hut'])
forest = Location('forest', ['gather sticks', 'hunt deer'], ['hut', 'cave'])
cave = Location('cave', ['search for steel'], ['forest'])
meadows = Location('meadows', ['gather fiber', 'pick berries'], ['hut', 'graveyard'])
graveyard = Location('graveyard', ['pray'], ['meadows', 'crypt'])
# crypt = Location
village = Location('village', ['enter shop', 'enter hunting tavern'], ['hut', 'crossroads'])

# BLACK SMITH LOCATIONS
crossroads = Location('crossroads', [], ['village', 'outskirts'])

# endregion


# region ITEMS
# Raw Material
iron_ore = Raw_Material('iron ore')

# Weapons
smiths_hammer = Weapon('smiths hammer', 10, 'melee')
item_prices = {'logs': 4, 'bait': 1, 'iron ore': 10, 'pelt': 10, 'oil': 15, 'cooked fish': 15,
               'berry stew': 10,
               'fishing pole': 15, 'wooden bow': 75, 'hunters bow': 300, 'leather armor': 30,
               'rabbits foot': 50,
               'crimson amulet': 75, 'lexicon': 100, 'morellonomicon': 300, 'smiths hammer': 25,
               'steel hammer': 300, 'iron armor': 150, 'steel armor': 300, 'wooden arrows': 5,
               'iron arrows': 15,
               'steel arrows': 30, 'flaming arrows': 40, 'weak healing potion': 10,
               'medium healing potion': 25,
               'strong healing potion': 50, 'fire resist potion': 25, 'frost resist potion': 25,
               'poisen resist potion': 25}
# endregion


# region FUNCTION MAPS
MAIN_MENU_MAP = {
    'inventory': inventory,
    'combat': combat,
    'current_stats': current_stats,
    'eat': eat,
    'quests': quests,
}
FUNCTION_MAP = {
    'sleep': sleep,
    'cook': cook,
    'light fire': light_fire,
    'fish': fish,
    'gather sticks': gather_sticks,
    'hunt deer': hunt_deer,
    'search for steel': search_for_steel,
    'gather fiber': gather_fiber,
    'pick berries': pick_berries,
    'pray': pray,
    'enter shop': enter_shop,
    'enter hunting tavern': enter_hunting_tavern,
}
TRAVEL_MAP = {
    'river': river,
    'hut': hut,
    'forest': forest,
    'cave': cave,
    'meadows': meadows,
    'graveyard': graveyard,
    'village': village,
    'crossroads': crossroads
}
SHOP_MAP = {
    '1': shop_raw_materials,
    '2': shop_food,
    '3': shop_weapons,
    '4': shop_armor,
    '5': shop_arrows,
    '6': shop_potions,
    'x': enter_shop,
    'X': enter_shop
}
SHOP_RAW_MATERIALS_MAP = {
    '3': iron_ore,
}

SHOP_WEAPONS_MAP = {
    '1': smiths_hammer,
}


# endregion

# For Dev Testing
def get_some_stuff():
    print('adding stuff')
    # player.add_item(smiths_hammer, 1)
    # player.add_exp(50)
    clock.display_time()
    pause()


def main():
    character_creation(player)
    startDay1(player)


if __name__ == "__main__":
    main()
