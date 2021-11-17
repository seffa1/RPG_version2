import os
def clear():
    os.system('cls')
def pause():
    input("----->")



class Dialogue_Class:
    def __init__(self):
        self.dialogue_map = {  # make this a default dict
            'river': self.river,
            'hut': self.hut,
            'forest': self.forest,
            'cave': self.cave,
            'meadows': self.meadows,
            'graveyard': self.graveyard,
            'village': self.village,
            'crossroads': self.crossroads

        }


    def hut(self):
        clear()
        print('Unique hut dialogue here')
        pause()
    def forest(self):
        clear()
        print('The light of the sun is trapped in the canopy above your head')
        print('The sound of the wind is replaced by the hum of insects and birds')
        print('You feel connected to the trees around you')
        pause()
    def cave(self):
        clear()
        print('The air sticks to your skin')
        print('Darkness swallows your view')
        print('Something smells rotten...')
        pause()
    def river(self):
        clear()
        print('The sound of the water calms you.')
        print('The river is one of the main sources of food for the continent')
        print('Not all who cast their line can secure the catch however.')
        pause()
    def meadows(self):
        clear()
        print('The grasses sway together, as if putting on a performance')
        print('You feel calm')
        print('You have no worries here')
        pause()
    def graveyard(self):
        clear()
        print('Graveyard dialogue here')
        pause()
    def village(self):
        clear()
        print('The sound of trade, commotion, and drinking fill your ears')
        print('Smells of gutted deer and mead fill your nose')
        print('Nobody seems to notice you')
        pause()
    def crossroads(self):
        clear()
        print(f'The crossroads can be a dangerous place.')
        print(f'Theres word of bandits demanding ransoms down the road.')
        print(f'Make sure you are prepared before you try to get through.\n')
        pause()



    def show_dialogue(self, location_name):  # location name = 'river'
        return self.dialogue_map[location_name]()

Dialogue = Dialogue_Class()