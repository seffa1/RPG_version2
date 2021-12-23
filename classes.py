from abc import ABC, abstractmethod
from collections import Counter
from collections import deque
import math
import os


# region Utility Functions
def clear():
    os.system('cls')


def select():
    a = input("----->")
    return a


def pause():
    input("Press enter to continue")


# endregion

class Clock:
    def __init__(self):
        self.day = 1
        self.time = 480
        self.end_day = 1440
        self.time_left = self.end_day - self.time
        self.minutes = self.time % 60
        self.hours = self.time // 60

    def display_time(self):
        hour_string = str(self.time // 60)
        if len(str(self.time % 60)) == 1:
            minute_string = '0' + str(self.time % 60)
        else:
            minute_string = str(self.time % 60)

        time_string = hour_string + ':' + minute_string

        print(f'Current Time: {time_string}')

        total_minutes_left = self.end_day - self.time
        minutes_left = total_minutes_left % 60
        hours_left = total_minutes_left // 60

        print(f'Time Til Dark: {hours_left} hour {minutes_left} minutes')

    def reset(self):
        self.day += 1
        self.time = 0

    def add_time(self, add_time: int):
        # This function adds time to the clock and returns the amount of time over the
        # End of the day, if any, to be used in another function
        self.time += add_time

        if self.time == self.end_day:
            self.reset()
            return 0

        if self.time > self.end_day:
            self.reset()
            return self.time - self.end_day

        else:
            return


# region Game Items
class Game_Item(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __str__(self):  # Used for inspecting the item
        pass


class Raw_Material(Game_Item):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name


class Food(Game_Item):
    def __init__(self, name, hunger_amount):
        super().__init__(self, name, )
        self.hunger_amount = hunger_amount

    def __str__(self):
        return self.name


class Weapon(Game_Item):
    def __init__(self, name, attack, scaling):
        super().__init__(name)
        self.attack = attack
        self.scaling = scaling

    def __str__(self):
        return self.name

    def show_stats(self):
        pass


class Armor(Game_Item):
    def __init__(self, name, defence, fire_resist, frost_resist, poison_resist):
        super().__init__(name, value)
        self.defence = defence
        self.fire_resist = fire_resist
        self.frost_resist = frost_resist
        self.poison_resist = poison_resist

    def __str__(self):
        pass


class Potion(Game_Item):
    def __init__(self, name, health, mana, stamina, fire_resist, frost_resist, poison_resist):
        super().__init__(name)
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.fire_resist = fire_resist
        self.frost_resist = frost_resist
        self.poison_resist = poison_resist

    def __str__(self):
        pass


class Arrow(Game_Item):
    def __init__(self, name, damage):
        super().__init__(name, value)
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.fire_resist = fire_resist
        self.frost_resist = frost_resist
        self.poison_resist = poison_resist

    def __str__(self):
        pass


# endregion


# region Locations
class Location:
    def __init__(self, name, actions, routes):
        self.__name = name
        self.__actions = actions  # list of functions
        self.__routes = routes  # list of location objects
        self.items = []  # contains objects in the area
        self.has_been_to = False

    @property
    def name(self):
        return self.__name

    @property
    def actions(self):
        return self.__actions

    @property
    def routes(self):
        return self.__routes

    def add_item(self, item):
        self.items.append(item)

    def spawn_loot(self):  # adds random loot to items
        pass


# endregion


# region Shop
class Shop:
    def __init__(self, player_gold, item_prices):
        self.gold = player_gold
        self.item_prices = item_prices

    def display_menus(self):
        print(f'Gold: {self.gold}')
        print(f'1 -----> Raw Materials')
        print(f'2 -----> Food')
        print(f'3 -----> Weapons')
        print(f'4 -----> Armor')
        print(f'5 -----> Arrows')
        print(f'6 -----> Potions')
        print(f'X -----> Back\n')

    def display_raw_material(self):
        clear()
        print(f'RAW MATERIALS')
        # print(f'1 -----> logs --------> {self.gold}/{self.item_prices["logs"]} gold')
        #  print(f'2 -----> bait --------> {self.gold}/{self.item_prices["bait"]} gold')
        print(f'3 -----> iron ore ----> {self.gold}/{self.item_prices["iron ore"]} gold')
        # print(f'4 -----> pelt --------> {self.gold}/{self.item_prices["pelt"]} gold')
        # print(f'5 -----> oil ---------> {self.gold}/{self.item_prices["oil"]} gold')
        print(f'X -----> Back\n')

    def display_food(self):
        print(f'FOOD')
        print(f'cooked fish ----------> {self.gold}/{self.item_prices["cooked fish"]} gold')
        print(f'berry stew -----------> {self.gold}/{self.item_prices["berry stew"]} gold')
        print(f'X -----> Back\n')

    def display_weapons(self):
        clear()
        print(f'WEAPONS')
        print(f'1 -----> smiths hammer ---> {self.gold}/{self.item_prices["smiths hammer"]} gold')
        # print(f'2 -----> steel hammer ----> {self.gold}/{self.item_prices["steel hammer"]} gold')
        # print(f'3 -----> wooden bow ------> {self.gold}/{self.item_prices["wooden bow"]} gold')
        # print(f'4 -----> hunters bow -----> {self.gold}/{self.item_prices["hunters bow"]} gold')
        # print(f'5 -----> fishing pole ----> {self.gold}/{self.item_prices["fishing pole"]} gold')
        # print(f'6 -----> lexicon ---------> {self.gold}/{self.item_prices["lexicon"]} gold')
        # print(f'7 -----> morellonomicon --> {self.gold}/{self.item_prices["morellonomicon"]} gold')
        print(f'X -----> Back\n')

    def display_armor(self):
        clear()
        print(f'ARMOR')
        print(f'leather armor ----------> {self.gold}/{self.item_prices["leather armor"]} gold')
        print(f'iron armor -------------> {self.gold}/{self.item_prices["iron armor"]} gold')
        print(f'steel armor ------------> {self.gold}/{self.item_prices["steel armor"]} gold')
        print(f'X -----> Back\n')

    def display_arrows(self):
        clear()
        print(f'ARROWS')
        print(f'wooden arrows x10 -------> {self.gold}/{self.item_prices["wooden arrows"]} gold')
        print(f'iron arrows x10 ---------> {self.gold}/{self.item_prices["iron arrows"]} gold')
        print(f'steel arrows x10 --------> {self.gold}/{self.item_prices["steel arrows"]} gold')
        print(f'flaming arrows x10 --------> {self.gold}/{self.item_prices["flaming arrows"]} gold')
        print(f'X -----> Back\n')

    def display_potions(self):
        print(f'POTIONS')
        print(f'weak healing potion -----> {self.gold}/{self.item_prices["weak healing potion"]} gold')
        print(f'medium healing potion ---> {self.gold}/{self.item_prices["medium healing potion"]} gold')
        print(f'strong healing potion ---> {self.gold}/{self.item_prices["strong healing potion"]} gold')
        print(f'frost resist potion -----> {self.gold}/{self.item_prices["frost resist potion"]} gold')
        print(f'fire resist potion ------> {self.gold}/{self.item_prices["fire resist potion"]} gold')
        print(f'poisen resist potion ----> {self.gold}/{self.item_prices["poisen resist potion"]} gold')
        print(f'X -----> Back\n')


# endregion


# region Character
class Character:
    def __init__(self, name):
        self.__name = name
        self.__location = None
        # Equipment
        self.main_hand = []  # these 4 things should be combined into a default dictionary
        self.off_hand = []  # equipped_items = defaultDict{weapon: '', armor: '', charm: ''}
        self.armor = []
        self.charm = []
        self.inventory = Counter()
        self.arrows = Counter()
        self.potions = Counter()
        # Stats
        self.__melee = 0
        self.__intelligence = 0
        self.__archery = 0
        self.__defence = 0
        self.__health = 0
        self.__mana = 0
        self.__stamina = 0
        self.__gold = 100

    def show_inventory(self):
        clear()
        split_inventory = {
            'raw_material': list(
                filter(lambda inventory_item: type(inventory_item) == Raw_Material, self.inventory.keys())),
            'food': list(filter(lambda inventory_item: type(inventory_item) == Food, self.inventory.keys())),
            'weapons': list(filter(lambda inventory_item: type(inventory_item) == Weapon, self.inventory.keys())),
            'armor': list(filter(lambda inventory_item: type(inventory_item) == Armor, self.inventory.keys())),
            'arrow': list(filter(lambda inventory_item: type(inventory_item) == Arrow, self.inventory.keys())),
            'potions': list(filter(lambda inventory_item: type(inventory_item) == Potion, self.inventory.keys()))
        }

        print('INVENTORY\n')
        print(f'{self.gold} x Gold\n')
        for item_type in split_inventory.keys():
            if len(split_inventory[item_type]) > 0:
                print(f'{item_type.capitalize()}')
                for item in split_inventory[item_type]:
                    print(f'{self.inventory[item]} x {item.name.title()}')  # also print item.stats
                print('')

        print('E -----> Equip Items')
        print('X -----> Back\n')

    def display_item(self, item):
        print(f'{item.name}: {self.inventory[item]}')

    def check_has_item(self, item):
        for i in self.inventory:
            if str(i.name) == str(item.name):
                return True
        return False

    def add_item(self, item):
        # if we dont have any of this item, add 1
        if not self.check_has_item(item):
            self.inventory.update({item: 1})
        else:
            self.inventory[item] += 1

    def remove_item(self, item, amount):
        self.inventory.update({item: -amount})

    def show_equiped(self):
        print('Currently Equipped:')
        print('Unequip Items (M, O, A, C)\n')

        if len(self.main_hand) == 0:
            print(f'M ---> Main Hand: {self.main_hand}')
        else:
            print(f'M ---> Main Hand: {self.main_hand[0].name}')

        if len(self.off_hand) == 0:
            print(f'O ---> Off Hand: {self.off_hand}')
        else:
            print(f'O ---> Off Hand: {self.off_hand[0].name}')

        if len(self.armor) == 0:
            print(f'A ---> Armor: {self.armor}')
        else:
            print(f'A ---> Armor: {self.armor[0].name}')
        if len(self.charm) == 0:
            print(f'C ---> Charm: {self.charm}')
        else:
            print(f'C ---> Charm: {self.armor[0].name}')

    def show_current_stats(self):
        clear()
        print('CURRENT STATS\n')
        print(f'{self.health} ---> Health')
        print(f'{self.stamina} ---> Stamina')
        print(f'{self.mana} ---> Mana\n')
        print(f'{self.melee} ---> Melee')
        print(f'{self.intelligence} ---> Intelligence')
        print(f'{self.archery} ---> Archery')
        print(f'{self.defence} ---> Defence')
        print(f'\nX ---> Back\n')

    # region Getters and Setters

    @property
    def name(self):
        # print('getting name...')
        return self.__name

    @name.setter
    def name(self, name):
        print('setting name...')
        self.__name = name

    @property
    def location(self):
        # print('getting location...')
        return self.__location

    @location.setter
    def location(self, location):
        # print('setting location...')
        self.__location = location

    # region Skills: Getters and setters
    # Skills: Getters and Setters
    @property
    def melee(self):
        # print('getting melee...')
        return self.__melee

    @melee.setter
    def melee(self, melee):
        # print('setting melee...')
        self.__melee = melee

    @property
    def intelligence(self):
        # print('getting intelligence...')
        return self.__intelligence

    @intelligence.setter
    def intelligence(self, intelligence):
        # print('setting intelligence...')
        self.__intelligence = intelligence

    @property
    def archery(self):
        # print('getting archery...')
        return self.__archery

    @archery.setter
    def archery(self, archery):
        # print('setting archery...')
        self.__archery = archery

    @property
    def defence(self):
        # print('getting defence...')
        return self.__defence

    @defence.setter
    def defence(self, defence):
        # print('setting defence...')
        self.__defence = defence

    # Stats: Getters and Setters

    @property
    def health(self):
        # print('getting health...')
        return self.__health

    @health.setter
    def health(self, health):
        # print('setting health...')
        self.__health = health

    @property
    def health(self):
        # print('getting health...')
        return self.__health

    @health.setter
    def health(self, health):
        # print('setting health...')
        self.__health = health

    @property
    def mana(self):
        # print('getting mana...')
        return self.__mana

    @mana.setter
    def mana(self, mana):
        # print('setting mana...')
        self.__mana = mana

    @property
    def stamina(self):
        # print('getting stamina...')
        return self.__stamina

    @stamina.setter
    def stamina(self, stamina):
        # print('setting stamina...')
        self.__stamina = stamina

    @property
    def gold(self):
        # print('getting gold...')
        return self.__gold

    @gold.setter
    def gold(self, gold):
        # print('setting gold...')
        self.__gold = gold
    # endregion

    # endregion


class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.__type = 0
        self.hunger = 0
        self.spell_book = []
        self.__quest_log = {}  # 'quest name': status
        self.__location = ''
        self.__exp = 0
        self.__level_thresholds = deque(
            [10, 20, 30, 40, 50, 60, 70, 80, 100, 120, 140, 160, 180, 200, 220, 230, 240, 260,
             280, 300, 330, 360, 390, 420, 450, 480, 510, 550, 600, 650, 600, 700, 800, 900, 1000, 10000])
        self.__exp_points = 0
        self.__level = 1

    def show_stats(self):
        print(f'Exp: {self.__exp} / {self.__level_thresholds[0]}')
        print(f'Health: {self.health}')
        print(f'Hunger: {self.hunger}')

    # region Getters and Setters
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, num):
        self.__type = num

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    # endregion

    # region Quest Functions
    def add_quest(self, quest_name):
        self.__quest_log[quest_name] = 'active'
        print(f'Quest Added: {quest_name.title()}')
        pause()

    def complete_quest(self, quest_name):
        self.__quest_log[quest_name] = 'complete'
        print(f'Quest Completed: {quest_name.title()}')
        pause()

    def get_current_quests(self):
        current_quests = []
        for quest, status in self.__quest_log.items():
            if status == 'active':
                current_quests.append(quest)
        return current_quests

    def get_completed_quests(self):
        completed_quests = []
        for quest, status in self.__quest_log.items():
            if status == 'complete':
                completed_quests.append(quest)
        return completed_quests

    # endregion

    def add_exp(self, exp):
        self.__exp += exp
        while self.__level_thresholds[0] <= self.__exp:
            self.__level_thresholds.popleft()
            self.__exp_points += 5
            self.__level += 1
        self.check_level_up()

    def check_level_up(self):
        if self.__exp_points > 0:
            self.level_up()

    def level_up(self):
        clear()
        print('You leveled up')
        print(f'Level: {self.__level}')
        print(f'Exp until next level: {self.__exp} / {self.__level_thresholds[0]}')

        pause()
        while self.__exp_points > 0:
            clear()
            options = {'health': self.health,
                       'mana': self.mana,
                       'stamina': self.stamina,
                       'melee': self.melee,
                       'intelligence': self.intelligence,
                       'archery': self.archery,
                       'defence': self.defence
                       }
            index_options = ['1', '2', '3', '4', '5', '6', '7']

            print(f'Exp points to spend ---> {self.__exp_points}')

            for index, stat_name in enumerate(options):
                print(f'{index + 1} ---> {stat_name}: {options[stat_name]}')

            print('')
            a = select()
            while a not in index_options: a = select()
            if a == '1':
                self.health = self.health + 4
            elif a == '2':
                self.mana = self.mana + 4
            elif a == '3':
                self.stamina = self.stamina + 4
            elif a == '4':
                self.melee = self.melee + 1
            elif a == '5':
                self.intelligence = self.intelligence + 1
            elif a == '6':
                self.archery = self.archery + 1
            elif a == '7':
                self.defence = self.defence + 1
            else:
                print('You should never get here !')
            self.__exp_points -= 1

    def __repr__(self):
        return (f'Name: {self.name}\n'
                f'Type: {self.type}\n'
                f'Location: {self.location}\n'
                f'Gold: {self.gold}')

    # What a player can do
    def travel(self, location):
        pass

    def look_around(self, location):
        pass

    def inspect_item(self, item):
        pass

    def pickup_item(self, item):  # puts it into backpack, arrow shieth, or potion pouch
        pass

    def equip_item(self, item):  # puts it into available equipment slot
        if type(item) == Weapon:
            if len(self.main_hand) > 0:
                print('You already have a weapon equipped.')
                pause()
                return False
            else:
                self.main_hand.append(item)
                return True
        elif type(item) == Armor:
            if len(self.armor) > 0:
                print('You already have armor equipped.')
                pause()
                return False
            else:
                self.armor.append(item)
                return True

    def unequip_item(self, item):  # puts it into available equipment slot
        if type(item) == Weapon:
            self.main_hand.remove(item)
        elif type(item) == Armor:
            self.armor.remove(item)

    def drop_item(self, item):
        pass

    def sell_item(self, item):
        pass

    def buy_item(self, item, price):
        print('buying item....')
        if price > self.gold:
            print('You do not have enough gold.')
            return pause()
        self.inventory.update([item])
        self.gold = self.gold - price
        print(f'You bought a {item.name} and have {self.gold} gold left')
        return pause()

    def eat_food(self, food):
        pass

    def drink_potion(self, potion):
        pass

    def attack(self):
        pass

    def block(self):
        pass

    def cast_spell(self, spell):
        pass

    def loot_corpse(self, corpse):
        pass

    def sleep(self):
        pass


class Enemy(Character):
    def __init__(self, name):
        super().__init__(name)

    # What can an enemy do
    def attack(self):
        pass

    def cast_spell(self):
        pass

    def die(self):
        pass


# endregion


# region Menus
class Menu:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return (self.__name + ' menu:').title()


class Action_Menu(Menu):
    def __init__(self, name):
        super().__init__(name)
        self.actions = {}  # gets updated with a num: action with the update_options function

    def clear_actions(self):
        self.actions = {}

    def add_action(self, number, action_function):
        self.actions[number] = action_function

    def show_menu(self):
        print(f'\n{self.name}')
        for num, action in self.actions.items(): print(f'{num} ---> {action}')


class Travel_Menu(Menu):
    def __init__(self, name):
        super().__init__(name)
        self.locations = {}  # gets updated with a num: location with the update_options function

    def clear_locations(self):
        self.locations = {}

    def update_locations(self, number, location):  # locations is a list of location objects
        self.locations[number] = location

    def show_menu(self):
        print(f'\n{self.name}')
        for num, location in self.locations.items(): print(f'{num} ---> {location}')


class Player_Menu(Menu):
    def __init__(self, name):
        super().__init__(name)
        self.options = {
            'I': 'inventory',
            'C': 'combat',
            'S': 'current_stats',
            'E': 'eat',
            'Q': 'quests'
        }

    def show_menu(self):
        print(f'\n{self.name}')
        for letter, option in self.options.items(): print(f'{letter} ---> {option}')


class Stat_Menu(Menu):
    def __init__(self, name):
        super().__init__(name)

    def show_player_stats(self):
        print(f'{player1}')


class Equip_Menu(Menu):
    def __init__(self, name, player):
        super().__init__(name)
        self.available_weapons = {}  # item : qty from player inventory
        self.available_armors = {}  # item : qty from player inventory
        self.player = player
        self.index = 1
        self.menu_options = {}  # option number: item

    def update_equipment(self):
        for item, amount in self.player.inventory.items():
            if type(item) == Weapon: self.available_weapons[item] = amount
            if type(item) == Armor: self.available_armors[item] = amount

    def display_menu(self):
        self.player.show_equiped()  # show what the player has equipped
        print('')
        if len(self.available_weapons) > 0:
            print('WEAPONS')
            for weapon, amount in self.available_weapons.items():
                print(f'{self.index} -----> {weapon} x {amount}')
                self.menu_options[str(self.index)] = weapon  # index is a string because input is strings only
                self.index += 1
        if len(self.available_armors) > 0:
            print('ARMOR')
            for armor, amount in self.available_armors.items():
                print(f'{self.index} -----> {armor} x {amount}')
                self.menu_options[str(self.index)] = weapon  # index is a string because input is strings only
                self.index += 1

        print('\nX -----> Back\n')

# endregion
