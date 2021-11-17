
import random
import math
import time
import sys
import os


#FUNTIONS THAT ONLY RUN ONCE, TO SETUP  OR END THE GAME 
def intro():    #Introduced the game
    print("Welcome to my game")
    print("\nPress Enter To Begin Your Journey\n")
    input("-->") 
def createClass(): #1: Blacksmith, #2: Hunter, #3 Scholar
    classes = {1:"blacksmith", 2:"hunter", 3:"scholar"}
    print("\nWhom may we call you?\n")
    heroName = input('-->')
    while heroName == '':
        heroName = input("Whom may we call you?")
    
    
    print(f"\nWelcome {heroName}, where do you come from?")
    print("\nBlacksmith(1): You come from a long line of blacksmiths. Every since you were a child\nyou were swinging a hammer. This will no doubt come in handy for the path that lay\nahead. You dont swing a hammer for no reason of course. You are not your father yet,\nbut you can craft some basic weapons and armor to aid you.")
    print("\nHunter(2): Your father died when you were young.\nFishing and hunting are skills you have learned in order to survive and\nbringing your bow and arror to the forest is your meditation.\nYour mother and sister have fended for yourselves in a small fishing village which seldom\nventures outside its terratory, and you dont plan to anytime soon...")
    print("\nScholar(3): You are a bastard child to a nobel family. Ashamed by your mother, you were hidden away in the library.\nYour time there has made you and exceptionaly fast learner.\nAlthough you have read about great warriors, you are not one yourself.\nPerhaps you will find other ways to defend yourself, but why would you, you are apart of a nobel estate afterall...\n")
    
    a = input('-->')
    while a != "1" and a != "2" and a != "3":
        print("invalid selection")
        a = input('-->')
    
    if a == "1":
        #Passed to hero class
        heroType = 1
        heromax_hp = 100
        herodefence = 10
        Hstamina = 75
        HfireResist = 15
        HfrostResist = 15
        HpoisenResist = 15
        Hcooldown = 5
        
        #Pass to skillTree class
        HmeleeSkill = 10
        HrangedSkill = 0
        HintelligenceSkill = 0
        HfishingSkill = 0
        HcraftingSkill = 10
        HenduranceSkill = 0
        HluckSkill = 5
        HalchemySkill = 0
        input("\nPress Enter to Continue\n")
        
    elif a == "2":
        #Passed to hero class
        heroType = 2
        heromax_hp = 100
        herodefence = 10
        Hstamina = 60
        HfireResist = 0
        HfrostResist = 0
        HpoisenResist = 5
        Hcooldown = 3
        
        #Pass to skillTree class
        HmeleeSkill = 0
        HrangedSkill = 10
        HintelligenceSkill = 0
        HfishingSkill = 10
        HcraftingSkill = 0
        HenduranceSkill = 0
        HluckSkill = 5
        HalchemySkill = 0
    else:
        #Passed to hero class
        heroType = 3
        heromax_hp = 100
        herodefence = 10
        Hstamina = 45
        HfireResist = 0
        HfrostResist = 0
        HpoisenResist = 0
        Hcooldown = 7
        
        #Pass to skillTree class
        HmeleeSkill = 2
        HrangedSkill = 2
        HintelligenceSkill = 10
        HfishingSkill = 2
        HcraftingSkill = 2
        HenduranceSkill = 0
        HluckSkill = 10
        HalchemySkill = 5
        
        input("\nPress Enter to Continue\n")
        

    
    return (heroName, heroType, heromax_hp, herodefence, HmeleeSkill, HrangedSkill, HintelligenceSkill, HfishingSkill, HcraftingSkill, HenduranceSkill, HluckSkill, Hstamina, HfireResist, HfrostResist, HpoisenResist, Hcooldown, HalchemySkill) 
def updateStats(player, clock1, actions, travels, heroInventory, stock, skills, fire):   #run during startDay1()
    player.moveMelee(skills.getMeleeSkill())
    player.moveRanged(skills.getRangedSkill())
    player.moveIntelligence(skills.getIntelligenceSkill())
    player.moveFishing(skills.getFishingSkill())
    player.setCrafting(skills.getCraftingSkill())
    player.moveLuck(skills.getLuckSkill())
    player.moveAlchemy(skills.getAlchemySkill())
def gameOver(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    
    print('\nYou have died')
    print('You finished with the following stats:\n')
    
    exit()   

#OBJECTS IN THE GAME
class Clock:
    def __init__(self, day):
        self.day = int(day)
        self.start = 480 #minutes (8 am)
        self.time = 480
        self.end = 1440 #minutes in a day
        #To keep track of days
        self.day1 = True
        self.day2 = False
        self.day3 = False
        self.day4 = False
        self.day5 = False
        self.day6 = False
        self.day7 = False
        self.day8 = False
        self.day9 = False
        self.day10 = False

        #herb gathering/growing rates
        self.dragonLillyCounter = 0
        self.coldSnapCounter = 0
        self.poisenIvyCounter = 0
        self.crimsonPetalCounter = 0
        #brewing rates
        self.healingPotionCounter = 0
        self.fireResistPotionCounter = 0
        self.frostResistPotionCounter = 0
        self.poisenResistPotionCounter = 0
        self.currentlyBrewing = []
        self.finishedBrewing = []
        #misc
        self.mealCounter = 0
        self.hasStudied = False
        
    #herb gathering/growing rates
    def moveDragonLillyCounter(self, amt):
        self.dragonLillyCounter += amt
    def moveColdSnapCounter(self, amt):
        self.coldSnapCounter += amt
    def movePoisenIvyCounter(self, amt):
        self.poisenIvyCounter += amt
    def moveCrimsonPetalCounter(self, amt):
        self.crimsonPetalCounter += amt
    #brewing rates
    def moveHealingPotionCounter(self, amt):
        self.healingPotionCounter += amt
    def moveFireResistPotionCounter(self, amt):
        self.fireResistPotionCounter += amt
    def moveFrostResistPotionCounter(self, amt):
        self.frostResistPotionCounter += amt
    def movePoisenResistPotionCounter(self, amt):
        self.poisenResistPotionCounter += amt
    #meal
    def moveMealCounter(self, amt):
        self.mealCounter += amt
    
     
    def getStart(self):
        return self.start
    def getEnd(self):
        return self.end
    def getTime(self):
        return self.time
    def getDay(self):
        return self.day
    def setDay(self, day):
        self.day = day
    def setTime(self, time):
        self.time = time
    def addTime(self, addedTime):
        self.time += addedTime
    def addDay(self):
        self.day += 1
        self.hasStudied = False
        
        #Removing Herb Timers
        self.dragonLillyCounter -= 1
        if self.dragonLillyCounter < 0:
            self.dragonLillyCounter = 0
        self.coldSnapCounter -= 1
        if self.coldSnapCounter < 0:
            self.coldSnapCounter = 0
        self.poisenIvyCounter -= 1
        if self.poisenIvyCounter < 0:
            self.poisenIvyCounter = 0
        self.crimsonPetalCounter -= 1
        if self.crimsonPetalCounter < 0:
            self.crimsonPetalCounter = 0
        
        #Removing Brewing timers
        self.healingPotionCounter -= 1
        if self.healingPotionCounter < 0:
            self.healingPotionCounter = 0
        if self.healingPotionCounter == 0 and 'healing potion' in self.currentlyBrewing:
            self.currentlyBrewing.remove('healing potion')
            self.finishedBrewing.append('healing potion')
        
        
        self.fireResistPotionCounter -= 1
        if self.fireResistPotionCounter < 0:
            self.fireResistPotionCounter = 0
        if self.fireResistPotionCounter == 0 and 'fire resist potion' in self.currentlyBrewing:
            self.currentlyBrewing.remove('fire resist potion')
            self.finishedBrewing.append('fire resist potion')
        
        
        
        self.frostResistPotionCounter -= 1
        if self.frostResistPotionCounter < 0:
            self.frostResistPotionCounter = 0
        if self.frostResistPotionCounter == 0 and 'frost resist potion' in self.currentlyBrewing:
            self.currentlyBrewing.remove('frost resist potion')
            self.finishedBrewing.append('frost resist potion')
        
        
        
        self.poisenResistPotionCounter -= 1
        if self.poisenResistPotionCounter < 0:
            self.poisenResistPotionCounter = 0
        if self.poisenResistPotionCounter == 0 and 'poisen resist potion' in self.currentlyBrewing:
            self.currentlyBrewing.remove('poisen resist potion')
            self.finishedBrewing.append('poisen resist potion')
        
        
        
        self.mealCounter -= 1
        if self.mealCounter < 0:
            self.mealCounter = 0
        

    def timeLeft(self):
        timeLeft = self.end - self.time
        return timeLeft
    def __repr__(self):
        return (f"It is day {self.getDay()}, the time is {self.getTime()}:00")
class ActionMenu: #action menu gets updated each time you arrive to a location
    def __init__(self):
        self.actions = []
    def clearActions(self):
        self.actions = []
    def addAction(self, action):
        self.actions.append(action)  
class TravelMenu: #Keeps track of where you can go. Keeps track if you have been to locations
    def __init__(self):
        self.locations = []
        
        self.visitedHut = False
        self.visitedVillage = False
        self.visitedHuntingTavern = False
        self.visitedForest = False
        self.visitedCave = False
        self.visitedRiver = False
        self.visitedMeadows = False
        self.visitedGraveyard = False
        self.visitedCrypt = False 
        
        self.visitedCrossroads = False
        self.visitedOutskirts = False
        self.visitedSmithsTavern = False
        self.visitedSmithsHome = False
        self.visitedForge = False
        self.visitedWoodstand = False
        self.visitedSwamp = False
        self.visitedAnimalDen = False
        self.visitedGlacialCavern = False
        
        self.visitedTownSquare = False
        self.visitedTownTavern = False
        self.visitedHerbGarden = False
        self.visitedBrewingStand = False
        self.visitedManor = False
        self.visitedServantsQuarters = False
        self.visitedLibrary = False
        self.visitedSecretPassage = False
        self.visitedTunnels = False

        #Quest Helpers
        self.secretPassage = False
        self.crawledThroughSewers = False
        self.forceThroughSecretPassage = False
        self.forceThroughSewers = False
        self.explainedRumors = True
        self.talkedAboutCrypt = False
        self.talkedAboutGlacialCavern = False
        self.canEnterTunnels = False
        self.tellAboutTownRumor = False 
        
        #FOR DEV TESTING
        self.travelTimes = True
        
    def clearLocations(self):
        self.locations = []
    def addLocation(self, location):
        self.locations.append(location)
class Location:    #currently not in use, maybe used to keep track of items at a location, maybe make it a sub class of Inventory
    def __init__(self):
        self.items = []  
class Hero:      #(self, Hname, Htype, Hmax_hp, Hdefence):
    def __init__(self, Hname, Htype, Hmax_hp, Hdefence, Hstamina, HfireResist, HfrostResist, HpoisenResist, Hcooldown):
        #Not a part of the skill tree
        self.name = Hname
        self.type = Htype
        self.location = ''
        self.max_hp = Hmax_hp           #only gets updated on a level up     
        self.hp = Hmax_hp
        self.defence = Hdefence         #only gets updated on armor equip/unequip
        self.maxHunger = 100            #only gets updated on a level up     
        self.hunger = 50             
        
        #For combat only
        self.maxStamina = Hstamina
        self.stamina = Hstamina
        self.fireResist = HfireResist
        self.frostResist = HfrostResist
        self.poisenResist = HpoisenResist
        self.specialCooldown = Hcooldown
        
        #Exp and level up 
        self.level = 1                  #only gets updated on a level up     
        self.expPoints = 0              #only gets updated on a level up     
        self.exp = 0
        self.lvlthresholds = [10, 20, 30, 40, 50, 60, 70, 80, 100, 120, 140, 160, 180, 200, 220, 230, 240, 260, 280, 300, 330, 360, 390, 420, 450, 480, 510, 550, 600, 650, 600, 700, 800, 900, 1000]
        
        #The stats involved with the skill tree
        self.melee = 0            
        self.ranged = 0                 
        self.intelligence = 0           
        self.fishing = 0
        self.crafting = 0
        self.luck = 0   
        self.alchemy = 0   
        
        
        #Misc
        self.hasPrayed = False
      
    #Combat
    def isDead(self):
        if self.hp <= 0:
            return True
        else:
            return False
    def getSpecialCooldown(self):
        return self.specialCooldown
    def getMaxStamina(self):
        return self.maxStamina
    def getStamina(self):
        return self.stamina
    def moveStamina(self, amt):
        self.stamina += amt
        if self.stamina < 0:
            self.stamina = 0
        if self.stamina > self.maxStamina:
            self.stamina = self.maxStamina
    def getFireResist(self):
        return self.fireResist
    def moveFireResist(self, amt):
        self.fireResist += amt
    def getFrostResist(self):
        return self.frostResist
    def moveFrostResist(self, amt):
        self.frostResist += amt
    def getPoisenResist(self):
        return self.poisenResist
    def movePoisenResist(self, amt):
        self.poisenResist += amt   
        
        
    #Not a part of the skill tree    
    def getName(self):
        return self.name
    def getType(self):
        return self.type 
    def getLocation(self):
        return self.location
    def setLocation(self, location):
        self.location = str(location)
    def getMax_hp(self):
        return self.max_hp
    def setMax_hp(self, new_max_hp):
        self.max_hp = new_max_hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp
    def getHP(self):
        return self.hp    
    def setHP(self, new_hp):
        self.hp = new_hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        
    def getDefence(self):
        return self.defence
    def moveDefence(self, amt):
        self.defence += amt
    def getMaxHunger(self):
        return self.maxHunger
    def addHunger(self, amount):
        self.hunger += amount
        if self.hunger > self.maxHunger:
            self.hunger = self.maxHunger
        if self.hunger < 0:
            self.hunger = 0
    def getHunger(self):
        return self.hunger
    def setHunger(self, amount):
        self.hunger = amount
    
    #Exp and level up     
    def addLevel(self):
        self.level += 1
    def getLevel(self):
        return self.level
    def getExpPoints(self):
        return self.expPoints
    def useExpPoint(self):
        self.expPoints += -1
    def getExp(self):
        return self.exp
    def addExp(self, added):
        self.exp += added
        while self.exp >= self.lvlthresholds[0]: #this levels us up the lvl threshold, maybe move this to a global function
            self.expPoints += 5   #consider making this dynamic like the level thresholds, need to get to balancing stage first
            self.lvlthresholds.pop(0)  
            self.level += 1
            self.maxHunger += 5
            self.max_hp += 5  
    
    #The stats involved with the skill tree
    def getMelee(self):
        return self.melee    
    def moveMelee(self, amt):
        self.melee += amt
    def getRanged(self):
        return self.ranged
    def moveRanged(self, amt):
        self.ranged += amt
    def getIntelligence(self):
        return self.intelligence
    def moveIntelligence(self, amt):
        self.intelligence += amt
    def getFishing(self):
        return self.fishing
    def moveFishing(self, amt):
        self.fishing += amt
    def getCrafting(self):
        return self.crafting
    def setCrafting(self, new_crafting):
        self.crafting = new_crafting
    def getLuck(self):
        return self.luck
    def moveLuck(self, amt):
        self.luck += amt   
    def moveAlchemy(self, amt):
        self.alchemy += amt
    def getAlchemy(self):
        return self.alchemy
    def __repr__(self):
        return f" Name: {self.name}   Level: {self.level} "
class Inventory:  #inventory of the hero
    def __init__(self):
        #Quests
        self.currentQuests = []
        self.completedQuests = []
        self.questItems = []
        
        #Always display these
        self.melee = []
        self.ranged = []
        self.magic = []
        self.armor = []
        self.charm = []
        self.gold = 0

        #Raw Material:Only displayer if you have them
        self.sticks = 0
        self.logs = 0
        self.iron = 0
        self.steel = 0
        self.fiber = 0
        self.fish = 0
        self.berries = 0
        self.bait = 0
        self.pelt = 0
        self.oil = 0
        self.ironOre = 0
        self.steelOre = 0
        self.dragonLilly = 0
        self.coldSnap = 0
        self.poisenIvy = 0
        self.crimsonPetal = 0
        self.deerMeat = 0
        self.raw_material = {'sticks':self.sticks, 'logs':self.logs, 'iron':self.iron, 'steel':self.steel, 'fiber':self.fiber, 'fish':self.fish, 'berries':self.berries, 'deer meat':self.deerMeat, 'bait':self.bait, 'pelt': self.pelt, 'oil': self.oil, 'iron ore':self.ironOre, 'steel ore': self.steelOre, 'dragon lilly': self.dragonLilly, 'cold snap': self.coldSnap, 'poisen ivy': self.poisenIvy, 'crimson petal': self.crimsonPetal}

        #Cooked food: Onlye displayer if you have them
        self.cookedFish = 0
        self.berryStew = 0
        self.meal = 0
        self.cookedDeer = 0
        self.cookedFood = {'cooked fish':self.cookedFish, 'berry stew':self.berryStew, 'meal': self.meal, 'cooked deer': self.cookedDeer}
        
        #Combat (potions will go here as well)
        self.woodenArrows = 0
        self.ironArrows = 0
        self.steelArrows = 0
        self.flamingArrows = 0
        self.arrows = {'wooden arrows': self.woodenArrows,'iron arrows': self.ironArrows, 'steel arrows': self.steelArrows, 'flaming arrows': self.flamingArrows}
        self.weakHealingPotion = 0
        self.mediumHealingPotion = 0
        self.strongHealingPotion = 0
        self.fireResistPotion = 0
        self.frostResistPotion = 0
        self.poisenResistPotion = 0
        self.potions = {'weak healing potion': self.weakHealingPotion, 'medium healing potion': self.mediumHealingPotion, 'strong healing potion': self.strongHealingPotion, 'fire resist potion': self.fireResistPotion, 'frost resist potion': self.frostResistPotion, 'poisen resist potion': self.poisenResistPotion}
        
        #Armor:
        self.leatherArmor = 0
        self.ironArmor = 0
        self.steelArmor = 0
        self.allArmor = {'leather armor': self.leatherArmor, 'iron armor': self.ironArmor, 'steel armor': self.steelArmor}
        self.armorDefences = {'leather armor': 10, 'iron armor': 20, 'steel armor': 30}
        
        
        #Weapons:
        self.fishingPole = 0
        self.woodenBow = 0
        self.huntersBow = 0   #sold at smiths shop only, requires iron to craft
        self.bowOfFire = 0   #all arrows apply fire damage
        self.smithsHammer = 0
        self.steelHammer = 0
        self.hammerOfIce = 0   #apply frost and restore stamina
        self.lexicon = 0   #get in the libraries secret room
        self.morellonomicon = 0  #Can be purchased for a shit load of gold
        self.necronomicon = 0   #dropped by the necromancer
        self.weapons = {'fishing pole': self.fishingPole, 'wooden bow': self.woodenBow, 'hunters bow': self.huntersBow, 'bow of fire': self.bowOfFire, 'smiths hammer': self.smithsHammer, 'steel hammer': self.steelHammer, 'hammer of ice': self.hammerOfIce, 'lexicon': self.lexicon, 'morellonomicon': self.morellonomicon, 'necronomicon': self.necronomicon}
        self.weaponDamages = {'fishing pole': 2, 'wooden bow': 5, 'hunters bow': 10, 'bow of fire': 30, 'smiths hammer': 10, 'steel hammer': 25, 'hammer of ice': 50, 'lexicon': 10, 'morellonomicon': 20, 'necronomicon': 50}
        
        
        #Charms:
        self.rabbitsFoot = 0 #increases luck
        self.crimsonAmulet = 0 #increase HP
        #self.vialOfSalt = 0 #increase
        #self.ribbonOf = 0
        self.allCharms = {'rabbits foot': self.rabbitsFoot, 'crimson amulet': self.crimsonAmulet}
        self.charmAmounts = {'rabbits foot': 5, 'crimson amulet': 25}

    #Charms  
    def declareAllCharms(self):
        self.allCharms = {'rabbits foot': self.rabbitsFoot, 'crimson amulet': self.crimsonAmulet}
    def moveRabbitsFoot(self, amt):
        self.rabbitsFoot += amt
        self.declareAllCharms()
    def moveCrimsonAmulet(self, amt):
        self.crimsonAmulet += amt
        self.declareAllCharms()
    
    #Weapons
    def declareWeapons(self):
        self.weapons = {'fishing pole': self.fishingPole, 'wooden bow': self.woodenBow, 'hunters bow': self.huntersBow, 'bow of fire': self.bowOfFire, 'smiths hammer': self.smithsHammer, 'steel hammer': self.steelHammer, 'hammer of ice': self.hammerOfIce, 'lexicon': self.lexicon, 'morellonomicon': self.morellonomicon, 'necronomicon': self.necronomicon}
    def moveFishingPole(self, amt):
        self.fishingPole += amt
        self.declareWeapons()
    def moveWoodenBow(self, amt):
        self.woodenBow += amt
        self.declareWeapons()
    def moveHuntersBow(self, amt):
        self.huntersBow += amt
        self.declareWeapons()
    def moveBowOfFire(self, amt):
        self.bowOfFire += amt
        self.declareWeapons()
    def moveSmithsHammer(self, amt):
        self.smithsHammer += amt
        self.declareWeapons()
    def moveSteelHammer(self, amt):
        self.steelHammer += amt
        self.declareWeapons()
    def moveHammerOfIce(self, amt):
        self.hammerOfIce += amt
        self.declareWeapons()
    def moveLexicon(self, amt):
        self.lexicon += amt
        self.declareWeapons()
    def moveMorellonomicon(self, amt):
        self.morellonomicon += amt
        self.declareWeapons()
    def moveNecronomicon(self, amt):
        self.necronomicon += amt
        self.declareWeapons()
    #Armor
    def declareArmor(self):
        self.allArmor = {'leather armor': self.leatherArmor, 'iron armor': self.ironArmor, 'steel armor': self.steelArmor}
    def moveLeatherArmor(self, amt):
        self.leatherArmor += amt
        self.declareArmor()
    def moveIronArmor(self, amt):
        self.ironArmor += amt
        self.declareArmor()
    def moveSteelArmor(self, amt):
        self.steelArmor += amt
        self.declareArmor()
    #Gold
    def getGold(self):
        return self.gold
    def moveGold(self, amt):
        self.gold += amt
    def addGold(self, gold_added):
        self.gold += gold_added
    #Combat
    def moveWoodenArrows(self, amt):
        self.woodenArrows += amt
        self.arrows = {'wooden arrows': self.woodenArrows,'iron arrows': self.ironArrows, 'steel arrows': self.steelArrows, 'flaming arrows': self.flamingArrows}
    def moveIronArrows(self, amt):
        self.ironArrows += amt
        self.arrows = {'wooden arrows': self.woodenArrows,'iron arrows': self.ironArrows, 'steel arrows': self.steelArrows, 'flaming arrows': self.flamingArrows}
    def moveSteelArrows(self, amt):
        self.steelArrows += amt
        self.arrows = {'wooden arrows': self.woodenArrows,'iron arrows': self.ironArrows, 'steel arrows': self.steelArrows, 'flaming arrows': self.flamingArrows}
    def moveFlamingArrows(self, amt):
        self.flamingArrows += amt
        self.arrows = {'wooden arrows': self.woodenArrows,'iron arrows': self.ironArrows, 'steel arrows': self.steelArrows, 'flaming arrows': self.flamingArrows}
    def moveWeakHealingPotion(self, amt):
        self.weakHealingPotion += amt
        self.potions = {'weak healing potion': self.weakHealingPotion, 'medium healing potion': self.mediumHealingPotion, 'strong healing potion': self.strongHealingPotion, 'fire resist potion': self.fireResistPotion, 'frost resist potion': self.frostResistPotion, 'poisen resist potion': self.poisenResistPotion}
    def moveMediumHealingPotion(self, amt):
        self.mediumHealingPotion += amt
        self.potions = {'weak healing potion': self.weakHealingPotion, 'medium healing potion': self.mediumHealingPotion, 'strong healing potion': self.strongHealingPotion, 'fire resist potion': self.fireResistPotion, 'frost resist potion': self.frostResistPotion, 'poisen resist potion': self.poisenResistPotion}
    def moveStrongHealingPotion(self, amt):
        self.strongHealingPotion += amt
        self.potions = {'weak healing potion': self.weakHealingPotion, 'medium healing potion': self.mediumHealingPotion, 'strong healing potion': self.strongHealingPotion, 'fire resist potion': self.fireResistPotion, 'frost resist potion': self.frostResistPotion, 'poisen resist potion': self.poisenResistPotion}
    def moveFireResistPotion(self, amt):
        self.fireResistPotion += amt
        self.potions = {'weak healing potion': self.weakHealingPotion, 'medium healing potion': self.mediumHealingPotion, 'strong healing potion': self.strongHealingPotion, 'fire resist potion': self.fireResistPotion, 'frost resist potion': self.frostResistPotion, 'poisen resist potion': self.poisenResistPotion}
    def moveFrostResistPotion(self, amt):
        self.frostResistPotion += amt
        self.potions = {'weak healing potion': self.weakHealingPotion, 'medium healing potion': self.mediumHealingPotion, 'strong healing potion': self.strongHealingPotion, 'fire resist potion': self.fireResistPotion, 'frost resist potion': self.frostResistPotion, 'poisen resist potion': self.poisenResistPotion}
    def movePoisenResistPotion(self, amt):
        self.poisenResistPotion += amt
        self.potions = {'weak healing potion': self.weakHealingPotion, 'medium healing potion': self.mediumHealingPotion, 'strong healing potion': self.strongHealingPotion, 'fire resist potion': self.fireResistPotion, 'frost resist potion': self.frostResistPotion, 'poisen resist potion': self.poisenResistPotion}
    #Raw materials 
    def declareRawItems(self):
        self.raw_material = {'sticks':self.sticks, 'logs':self.logs, 'iron':self.iron, 'steel':self.steel, 'fiber':self.fiber, 'fish':self.fish, 'berries':self.berries, 'deer meat':self.deerMeat,'bait':self.bait, 'pelt': self.pelt, 'oil': self.oil, 'iron ore':self.ironOre, 'steel ore': self.steelOre, 'dragon lilly': self.dragonLilly, 'cold snap': self.coldSnap, 'poisen ivy': self.poisenIvy, 'crimson petal': self.crimsonPetal}
    def moveSticks(self, amt):
        self.sticks += amt
        self.declareRawItems()
    def moveLogs(self, amt):
        self.logs += amt
        self.declareRawItems()
    def moveIron(self, amt):
        self.iron += amt
        self.declareRawItems()
    def moveSteel(self, amt):
        self.steel += amt
        self.declareRawItems()
    def moveFiber(self, amt):
        self.fiber += amt
        self.declareRawItems()
    def moveFish(self, amt):
        self.fish += amt
        self.declareRawItems()
    def moveBerries(self, amt):
        self.berries += amt
        self.declareRawItems()
    def getFish(self):
        return self.fish
    def getBerries(self):
        return self.berries
    def getDeerMeat(self):
        return self.deerMeat
    def moveDeerMeat(self, amt):
        self.deerMeat += amt
        self.declareRawItems()
    def moveBait(self, amt):
        self.bait += amt
        self.declareRawItems()
    def movePelt(self, amt):
        self.pelt += amt
        self.declareRawItems()
    def moveOil(self, amt):
        self.oil += amt
        self.declareRawItems()
    def moveIronOre(self, amt):
        self.ironOre += amt
        self.declareRawItems()
    def moveSteelOre(self, amt):
        self.steelOre += amt
        self.declareRawItems()
    def moveDragonLilly(self, amt):
        self.dragonLilly += amt
        self.declareRawItems()
    def moveColdSnap(self, amt):
        self.coldSnap += amt
        self.declareRawItems()
    def movePoisenIvy(self, amt):
        self.poisenIvy += amt
        self.declareRawItems()
    def moveCrimsonPetal(self, amt):
        self.crimsonPetal += amt
        self.declareRawItems()
    #Cooked Food
    def moveCookedFish(self, amt):
        self.cookedFish += amt
        self.cookedFood = {'cooked fish':self.cookedFish, 'berry stew':self.berryStew, 'meal': self.meal, 'cooked deer': self.cookedDeer}
    def moveBerryStew(self, amt):
        self.berryStew += amt
        self.cookedFood = {'cooked fish':self.cookedFish, 'berry stew':self.berryStew, 'meal': self.meal, 'cooked deer': self.cookedDeer} 
    def moveMeal(self, amt):
        self.meal += amt
        self.cookedFood = {'cooked fish':self.cookedFish, 'berry stew':self.berryStew, 'meal': self.meal, 'cooked deer': self.cookedDeer}
    def moveCookedDeer(self, amt):
        self.cookedDeer += amt
        self.cookedFood = {'cooked fish':self.cookedFish, 'berry stew':self.berryStew, 'meal': self.meal, 'cooked deer': self.cookedDeer}  
class SkillTree: #contains the hero's levelable skills, used for the level up
    def __init__(self, HmeleeSkill, HrangedSkill, HintelligenceSkill, HfishingSkill, HcraftingSkill, HenduranceSkill, HluckSkill, HalchemySkill):
        #These value are passed in from createClass() and are type dependent
        self.meleeSkill = HmeleeSkill
        self.rangedSkill = HrangedSkill
        self.intelligenceSkill = HintelligenceSkill
        self.fishingSkill = HfishingSkill
        self.craftingSkill = HcraftingSkill
        self.enduranceSkill = HenduranceSkill
        self.luckSkill = HluckSkill
        self.alchemy = HalchemySkill
    
    def levelMeleeSkill(self):
        self.meleeSkill += 1
    def levelRangedSkill(self):
        self.rangedSkill += 1
    def levelIntelligenceSkill(self):
        self.intelligenceSkill += 1
    def levelFishingSkill(self):
        self.fishingSkill += 1
    def levelCraftingSkill(self):
        self.craftingSkill += 1
    def levelLuckSkill(self):
        self.luckSkill += 1  
    def levelEnduranceSkill(self):
        self.enduranceSkill += 1
    def levelAlchemySkill(self):
        self.alchemy += 1    
        
    def getMeleeSkill(self):
        return self.meleeSkill
    def getRangedSkill(self):
        return self.rangedSkill
    def getIntelligenceSkill(self):
        return self.intelligenceSkill
    def getFishingSkill(self):
        return self.fishingSkill
    def getCraftingSkill(self):
        return self.craftingSkill
    def getEnduranceSkill(self):
        return self.enduranceSkill
    def getLuckSkill(self):
        return self.luckSkill
    def getAlchemySkill(self):
        return self.alchemy
    
    def takeDrink(self):
        self.intelligenceSkill -= 1
        self.enduranceSkill += 1
class Fire: #handles home fire, cooking fuel, and forge fuel
    def __init__(self):
        self.lit = False
        self.fuel = 0
        self.fuelMax = 10
        self.cookingFuel = 0
        self.forgeFuel = 0
        self.brewingFuel = 0
        
    def addFuel(self, amt): #home fire
        self.fuel += amt
        if self.fuel > self.fuelMax:
            self.fuel = self.fuelMax
        if self.fuel < 0:
            self.fuel = 0
    
    def getCookingFuel(self):
        return self.cookingFuel
    def addCookingFuel(self, amt):
        self.cookingFuel += amt
        if self.cookingFuel < 0:
            self.cookingFuel = 0        
    
    def getForgeFuel(self):
        return self.forgeFuel
    def addForgeFuel(self, amt):
        self.forgeFuel += amt
        if self.forgeFuel < 0:
            forgeFuel = 0
            
    def getBrewingFuel(self):
        return self.brewingFuel
    def addBrewingFuel(self, amt):
        self.brewingFuel += amt
        if self.brewingFuel < 0:
            brewingFuel = 0

#COMBAT (self, name, maxHP, meleeDefence, rangedDefence, fireResist, frostResist, poisenResist, attack, elementAttack, elementAmt, stamina):
class Enemy:
    def __init__(self, name, maxHP, meleeDefence, rangedDefence, fireResist, frostResist, poisenResist, attack, elementAttack, elementAmt, stamina):
        self.name = name
        self.maxHP = maxHP
        self.HP = maxHP
        self.meleeDefence = meleeDefence
        self.rangedDefence = rangedDefence
        self.fireResist = fireResist
        self.frostResist = frostResist
        self.poisenResist = poisenResist
        self.attack = attack
        self.elementAttack = elementAttack
        self.stamina = stamina
        self.maxStamina = stamina
        self.elementAmt = elementAmt
        
    def getMaxHP(self):
        return self.maxHP
    def isDead(self):
        if self.HP <= 0:
            return True
        else:
            return False
    def getName(self):
        return self.name
    def getHP(self):
        return self.HP
    def getMaxHP(self):
        return self.maxHP
    def moveHP(self, amt):
        self.HP += amt
    def getMeleeDefence(self):
        return self.meleeDefence
    def getRangedDefence(self):
        return self.rangedDefence
    def getFireResist(self):
        return self.fireResist
    def getFrostResist(self):
        return self.frostResist
    def getPoisenResist(self):
        return self.poisenResist
    def getAttack(self):
        return self.attack
    def getElementAttack(self):
        return self.elementAttack
    def getElementAmt(self):
        return self.elementAmt
    def getStamina(self):
        return self.stamina
    def moveStamina(self, amt):
        self.stamina += amt
        if self.stamina < 0:
            self.stamina = 0
        if self.stamina > self.maxStamina:
            self.stamina = self.maxStamina
    def getMaxStamina(self):
        return self.maxStamina
def battle(opponent, player, clock1, actions, travels, heroInventory, stock, skills, fire):   #opponent must be an enemy object
    turn_counter = 1
    poisen_counter_player = 0
    poisen_amount_player= player.getIntelligence()/4  #poisen damage scales off of intelligence, adjust this formula
    poisen_counter_enemy = 0
    poisen_amount_enemy = opponent.getAttack()  
    player_cooldown = 0
    player_cooldown_max = player.getSpecialCooldown()
    end_turn = False
    meleeStaminaUsage = 15  #Balance this
    rangedStaminaUsage = 10  #Balance this
    enemyStaminaUsage = 10
    available_arrows = []
    escaped = False
    playerBaseFireResist = player.getFireResist()   #these are here because potions will increase players stats during combat, and these will be used to reset their resistances at the end of the fight
    playerBaseFrostResist = player.getFrostResist()
    playerBasePoisenResist = player.getPoisenResist()
    
    
    #MAIN COMBAT LOOP
    while player.isDead() != True and opponent.isDead() != True:
        print(f'\nBATTLE\nTurn: {turn_counter}')
        
        #Apply Poisen To Player
        if poisen_counter_player > 0:
            applyPoisen(player, poisen_amount_enemy)
            poisen_counter_player -= 1
            checkDeath(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        print(f'\n{player.getName()}')
        print(f"Health: {player.getHP()} / {player.getMax_hp()}")
        print(f"Stamina: {player.getStamina()} / {player.getMaxStamina()}")
        print(f'Defence: {player.getDefence()}')
        print(f"Fire Resist: {player.getFireResist()}\nFrost Resist: {player.getFrostResist()}\nPoisen Resist: {player.getPoisenResist()}")
        
        print(f'\n{opponent.getName()}')
        print(f"Health: {opponent.getHP()} / {opponent.getMaxHP()}")
        print(f"Stamina: {opponent.getStamina()} / {opponent.getMaxStamina()}")
        print(f"Melee Resist: {opponent.getMeleeDefence()}\nRanged Resist: {opponent.getRangedDefence()}")
        print(f"Fire Resist: {opponent.getFireResist()}\nFrost Resist: {opponent.getFrostResist()}\nPoisen Resist: {opponent.getPoisenResist()}")

        print(f'\nSelect Action:')
        print(f'(M) Melee Attack')
        print(f'(R) Ranged Attack')
        print(f'(A) Magic Attack')
        print(f'(P) Use Potion')
        print(f'(E) Rest')
        playerFrostEffect, playerFireEffect, playerPoisenEffect, playerMagicDamage = 0, 0, 0, 0
        hasAnArrow = hasArrows(heroInventory)
        hasAPotion = hasPotions(heroInventory)

        a = input('-->')  
        while a.lower() != 'm' and a.lower() != 'r' and a.lower() != 'a' and a.lower() != 'h' and a.lower() != 'e' and a.lower() != 'w' and a.lower() != 'p':
            a = input('-->')   
        #MELEE COMBAT
        if a.lower() == 'm': 
            if player.getStamina() < meleeStaminaUsage:
                print('You dont have enough stamina')
            else:
                if len(heroInventory.melee) == 0:  
                    print('\nYou attack with your fists!.')
                    damage = skills.getMeleeSkill()  #fist damage based off of bass melee skill
                    chance = random.randint(0,0)   #currently not doing this
                    if chance > player.getLuck():
                        damage = 0
                        print('You missed the enemy!')
                        player.moveStamina(-1 * meleeStaminaUsage)
                        print(f'You lost {meleeStaminaUsage} stamina!')
                        end_turn = True
                    else:
                        opponent.moveHP(-1*damage)
                        player.moveStamina(-1 * meleeStaminaUsage)
                        print(f'{player.getName()}: -{meleeStaminaUsage} stamin')
                        print(f'{opponent.getName()}: -{damage} HP')
                        end_turn = True
                else: #player attacks with their melee weapon
                    print(f'You attack with your {heroInventory.melee[0]}') #need a function to calc. damage based on your melee + enemy melee resistances
                    damage, frostEffect = meleeDamage(player.getMelee(), player.getLuck(), player.getStamina(), opponent.getMeleeDefence(), meleeStaminaUsage, heroInventory, opponent.getFrostResist())
                    opponent.moveHP(-1 * damage)
                    print(f'{opponent.getName()}: -{damage} HP')
                    player.moveStamina(-1 * meleeStaminaUsage)
                    print(f'{player.getName()}: -{meleeStaminaUsage} stamina')
                    if frostEffect > 0:
                        print(f'{opponent.getName()}: -{frostEffect} stamina from hammer of ice')
                        opponent.moveStamina(-1 * frostEffect)
                    end_turn = True
        #RANGED COMBAT    
        elif a.lower() == 'r' and len(heroInventory.ranged) == 0:   #if you have no ranged weapon equiped, choose something else
            print(f'You dont have a ranged weapon equiped')
        elif a.lower() == 'r' and not hasAnArrow:   #if you have a bow but dont have any arrows
            print(f'You dont have any arrows')        
        elif a.lower() == 'r':   #if you have a bow and also have arrows
            if player.getStamina() < rangedStaminaUsage:
                print('You dont have enough stamina')
            else:
                print('You attack with your bow!')
                damage, fireDamage = rangedDamange(player.getRanged(), player.getLuck(), player.getStamina(), opponent.getRangedDefence(), rangedStaminaUsage, opponent.getFireResist(), heroInventory)
                opponent.moveHP(-1 * damage)
                print(f'{opponent.getName()}: -{damage} HP from arrow')
                if fireDamage > 0:
                    print(f'{opponent.getName()}: -{fireDamage} HP from fire')
                    opponent.moveHP(-1 * fireDamage)
                player.moveStamina(-1 * rangedStaminaUsage)
                print(f'{player.getName()}: -{rangedStaminaUsage} stamina')
                end_turn = True
        
        #POTION USAGE
        elif a.lower() == 'p' and not hasAPotion:  #you try to use a potion but have no potions
            print('You do not have any potions')
        elif a.lower() == 'p':  #you try to use a potion and you have a potion
            usePotions(heroInventory, player)
            end_turn = True
        
        #RESTING
        elif a.lower() == 'e':
            print(f'\nYou rest to catch your breath.')
            stamina_gained = player.getMaxStamina() - player.getStamina()
            player.moveStamina(stamina_gained)     
            print(f'+{stamina_gained} stamina')
            end_turn = True
       
        #MAGIC COMBAT 
        elif a.lower() == 'a':       
            if len(heroInventory.magic) == 0:
                print('You dont have a tomb equiped.')  
            else:
                playerFrostEffect, playerFireEffect, playerPoisenEffect, playerMagicDamage, necroEffect = magicAttack(player, player.getIntelligence(), opponent.getFireResist(), opponent.getFrostResist(), heroInventory)
                end_turn = True
        
            #Apply Magic Effects to Enemy
            if playerFrostEffect > 0:
                print(f'{opponent.getName()}: -{playerFrostEffect} stamina from frost')
                opponent.moveStamina(-1*playerFrostEffect)
            if playerFireEffect > 0:
                print(f'{opponent.getName()}: -{playerFireEffect} HP from fire')
                opponent.moveHP(-1*playerFireEffect)
            if playerPoisenEffect > 0:
                print(f'You poisened the {opponent.getName()} for {playerPoisenEffect} turns!')
                poisen_counter_enemy += playerPoisenEffect
            if  playerMagicDamage > 0:
                print(f'{opponent.getName()}: -{playerMagicDamage} HP from magic')
                opponent.moveHP(-1*playerMagicDamage)   
            if necroEffect > 0:
                print(f'{opponent.getName()}: -{necroEffect} HP from necronomicons poisen damage')
            #print(f'{opponent.getName()} {opponent.getHP()}/{opponent.getMaxHP()} HP')
            #print(f'{opponent.getName()} {opponent.getStamina()}/{opponent.getMaxStamina()} Stamina')          

        #ENEMY ATTACK
        if end_turn == True:
            #Apply Poisen Damage to the Enemy
            if poisen_counter_enemy > 0:
                enemy_poisen_damage = math.ceil(poisen_amount_player - ((poisen_amount_player * 0.9) * (opponent.getPoisenResist()/100)))
                if opponent.getPoisenResist() > 100:
                    enemy_poisen_damage = math.ceil(poisen_amount_player * 0.1)
                opponent.moveHP(-1*enemy_poisen_damage)
                if 'necronomicon' in heroInventory.magic:
                    print(f'{opponent.getName()}: -{enemy_poisen_damage} HP from Necronomicon Poisen')
                else:
                    print(f'{opponent.getName()}: -{enemy_poisen_damage} HP from lingering poisen')
                poisen_counter_enemy -= 1
            print(f'\n{opponent.getName()} attacks!:')
            if opponent.getStamina() < enemyStaminaUsage:   #opponent doesnt have any stamina left
                print(f'{opponent.getName()} needs to rest to regain stamina.')
                stamina_gain = opponent.getMaxStamina() - opponent.getStamina()
                print(f'{opponent.getName()}: +{stamina_gain} stamina')
                opponent.moveStamina(stamina_gain)
            else:
                opponent_damage, fireBonus, frostBonus, poisenBonus = opponentDamage(opponent.getAttack(), opponent.getElementAttack(), player.getDefence(), player.getFireResist(), player.getFrostResist(), opponent.getElementAmt())  #opponent does have stamina left and attacks
                print(f'{player.getName()}: -{opponent_damage} HP from attack')
                if fireBonus > 0:
                    print(f'{player.getName()}: -{fireBonus} HP from fire')
                if frostBonus >0:
                    print(f'{player.getName()}: -{frostBonus} stamina from frost')
                if poisenBonus >0 and poisen_counter_player == 0:
                    print(f'{player.getName()}: poisend for {poisenBonus} turns')
                    poisen_counter_player += poisenBonus
                opponent.moveStamina(-1*enemyStaminaUsage)
                print(f'{opponent.getName()}: -{enemyStaminaUsage} stamina from attacking')    
                player.setHP(player.getHP() - opponent_damage)  #take normal damage
                player.setHP(player.getHP() - fireBonus)   #take fire damage
                player.moveStamina(-1*frostBonus)   #take frost, stamina damage
            input('\n\nPress enter to continue\n')
            turn_counter += 1
            end_turn = False
    checkDeath(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    player.poisenResist =playerBasePoisenResist
    player.frostResist = playerBaseFrostResist
    player.fireResist = playerBaseFireResist
    stamina_gained = player.getMaxStamina() - player.getStamina()
    player.moveStamina(stamina_gained)
    giveLoot(heroInventory, player, opponent.getMaxHP())    
def meleeDamage(playerMelee, playerLuck, currentPlayerStamina, enemyMeleeDefense, meleeStaminaUsage, heroInventory, enemyFrostResist):
    damage = math.ceil(playerMelee - ((playerMelee * 0.9) * (enemyMeleeDefense/100))) #at 100 resistance, take only 10% of the damage. above 100 resistance does nothing more for you
    if enemyMeleeDefense > 100:
        damage = math.ceil(playerMelee * 0.1)
    hammerFrostEffect = 0
    frostEffect = 0
    if 'hammer of ice' in heroInventory.melee:   #Has the frost hammer equipedd
        hammerFrostEffect += math.ceil(heroInventory.weaponDamages['hammer of ice']/2) #####BALANCE THIS##### - currently 50/25 = 26
        frostEffect = math.ceil(hammerFrostEffect - ((hammerFrostEffect * 0.9) * (enemyFrostResist/100)))
        if enemyFrostResist > 100:
            frostEffect = math.ceil(hammerFrostEffect * 0.1)
    
    return damage, frostEffect
def rangedDamange(playerRanged, playerLuck, currentPlayerStamina, enemyRangedDefense, rangedStaminaUsage, enemyFireResist, heroInventory):  
    available_choices = []
    print('\nSelect an arrow to use.\n')
    wooden_arrows = heroInventory.arrows['wooden arrows']
    iron_arrows = heroInventory.arrows['iron arrows']
    steel_arrows = heroInventory.arrows['steel arrows']
    flaming_arrows = heroInventory.arrows['flaming arrows']
    damage = 0
    fireBonus = 0
    arrowDamage = 0
    fireDamage = 0
    
    if wooden_arrows > 0:
        print(f'(W) Wooden Arrows --- {wooden_arrows}')
        available_choices.append('w')
    if iron_arrows > 0:
        print(f'(I) Iron Arrows --- {iron_arrows}') 
        available_choices.append('i')    
    if steel_arrows > 0:
        print(f'(S) Steel Arrows --- {steel_arrows}')
        available_choices.append('s')
    if flaming_arrows > 0:
        print(f'(F) Flaming Arrows --- {flaming_arrows}')
        available_choices.append('f')
        
    a = input('-->')
    
    while a.lower() not in available_choices:
        a = input('-->')
    if a.lower() == 'w':
        heroInventory.moveWoodenArrows(-1)
        arrowDamage +=10
    elif a.lower() == 'i':
        heroInventory.moveIronArrows(-1)
        arrowDamage += 30
    elif a.lower() == 's':
        heroInventory.moveSteelArrows(-1)
        arrowDamage += 50
    else:
        heroInventory.moveFlamingArrows(-1)
        arrowDamage += 30
        fireBonus += 40
    if 'bow of fire' in heroInventory.ranged:
        fireBonus = math.ceil(heroInventory.weaponDamages['bow of fire']/2)
    
    net_damage = arrowDamage + math.ceil(playerRanged*.6) #added this so arrow damage matters more
    damage = math.ceil(net_damage - ((net_damage * 0.9) * (enemyRangedDefense/100)))
    if enemyRangedDefense > 100:
        damage = math.ceil(net_damage * 0.1)
    
    if fireBonus > 0:
        fireDamage = math.ceil(fireBonus - ((fireBonus * 0.9) * (enemyFireResist/100)))
        if enemyFireResist > 100:
            fireDamage = math.ceil(fireBonus * 0.1)
    
    return damage, fireDamage  
def usePotions(heroInventory, player):
    weakHealingPotion_HP = 25
    mediumHealingPotion_HP = 50
    strongHealingPotion_HP = 100
    fireResistPotion_resist = 50
    frostResistPotion_resist = 60
    poisenResistPotion_resist = 70
    
    #Stamnia potion???
    
    available_choices = []
    print(f'\nSelect a potion to use\n')
    
    
    weakHealingPotion = heroInventory.weakHealingPotion
    if weakHealingPotion > 0:
        available_choices.append('w')
        print(f'(W) Weak Healing Potion')
    mediumHealingPotion = heroInventory.mediumHealingPotion
    if mediumHealingPotion > 0:
        available_choices.append('m')
        print(f'(M) Medium Healing Potion')
    strongHealingPotion = heroInventory.strongHealingPotion
    if strongHealingPotion > 0:
        available_choices.append('s')
        print(f'(S) Strong Healing Potion')
    fireResistPotion = heroInventory.fireResistPotion
    if fireResistPotion > 0:
        available_choices.append('f')
        print(f'(F) Fire Resist Potion')
    frostResistPotion = heroInventory.frostResistPotion
    if frostResistPotion > 0:
        available_choices.append('r')
        print(f'(R) Frost Resist Potion')
    poisenResistPotion = heroInventory.poisenResistPotion
    if poisenResistPotion > 0:
        available_choices.append('p')
        print(f'(P) Poisen Resist Potion')
    
    a = input('-->')
    
    while a not in available_choices:
        a = input('-->')
    print('')
    if a.lower() == 'w':
        heroInventory.moveWeakHealingPotion(-1)
        print(f'You use a weak healing potion')
        print(f'+ {weakHealingPotion_HP} HP')
        player.setHP(player.getHP() + weakHealingPotion_HP)
    elif a.lower() == 'm':
        heroInventory.moveMediumHealingPotion(-1)
        print(f'You use a medium healing potion')
        print(f'+ {mediumHealingPotion_HP} HP')
        player.setHP(player.getHP() + mediumHealingPotion_HP)
    elif a.lower() == 's':
        heroInventory.moveStrongHealingPotion(-1)
        print(f'You use a strong healing potion')
        print(f'+ {strongHealingPotion_HP} HP')
        player.setHP(player.getHP() + strongHealingPotion_HP)
    elif a.lower() == 'f':
        heroInventory.moveFireResistPotion(-1)
        print(f'You use a fire resist potion')
        print(f'+ {fireResistPotion_resist} fire resistance')
        player.moveFireResist(fireResistPotion_resist)
    elif a.lower() == 'r':
        heroInventory.moveFrostResistPotion(-1)
        print(f'You use a frost resist potion')
        print(f'+ {frostResistPotion_resist} frost resistance')
        player.moveFrostResist(frostResistPotion_resist)
    elif a.lower() == 'p':
        heroInventory.movePoisenResistPotion(-1)
        print(f'You use a poisen resist potion')
        print(f'+ {poisenResistPotion_resist} poisen resistance')
        player.movePoisenResist(poisenResistPotion_resist)
def applyPoisen(player, poisen_amount):
    poisen_damage = poisen_amount - player.getPoisenResist()
    poisen_damage = math.ceil(poisen_amount - ((poisen_amount * 0.9) * (player.getPoisenResist()/100)))
    if player.getPoisenResist() > 100:
        poisen_damage = math.ceil(poisen_amount * 0.1)

    if poisen_damage < 0:
        poisen_damage = 0
    player.setHP(player.getHP() - poisen_damage)
    print(f'\n{player.getName()} -{poisen_damage} HP from lingering poisen')
def opponentDamage(enemyAttack, enemyAttacktype, playerDefence, playerFireResist, playerFrostResist, elementAmount):
    damage = 0
    fireDamage = 0
    frostEffect = 0
    poisenCounters = 0
    damage = math.ceil(enemyAttack - ((enemyAttack * 0.9) * (playerDefence/100)))  #see balancing spreadsheet for formula info
    if playerDefence > 100:
         damage = math.ceil(enemyAttack * 0.1)
    if enemyAttacktype == 'fire':
        fireDamage = math.ceil(elementAmount - ((elementAmount * 0.9) * (playerFireResist/100)))
        if playerFireResist > 100:
            fireDamage = math.ceil(elementAmount * 0.1)
    elif enemyAttacktype == 'frost':
        frostEffect = math.ceil(elementAmount - ((elementAmount * 0.9) * (playerFrostResist/100)))
        if playerFrostResist > 100:
            frostEffect = math.ceil(elementAmount * 0.1)
    elif enemyAttacktype == 'poisen':
        poisenCounters += elementAmount
        
    ###########Potentail add one more type for the last boss which would apply all three##########
    
    #print(f'damage: {damage}')
    #print(f'fireDamage: {fireDamage}')
    #print(f'frostEffect: {frostEffect}')
    #print(f'poisenCounters: {poisenCounters}')

    return damage, fireDamage, frostEffect, poisenCounters    
def magicAttack(player, playerIntelligence, enemyFireResist, enemyFrostResist, heroInventory):
        playerMagicDamage = math.ceil(playerIntelligence/3)
        playerFrostEffect = 0
        playerFireEffect = 0
        playerPoisenEffect = 0
        necroEffect = 0
        print(f'\nSelect Magic Attack')
        print('(F) Fire')
        print('(R) Frost')
        print('(P) Poisen')
        
        a = input('-->')
        while a.lower() != 'f' and a.lower() != 'r' and a.lower() != 'p':
            a = input('-->')
        
        if a.lower() == 'f':
            fireBaseAmount = playerIntelligence/4
            playerFireEffect = math.ceil(fireBaseAmount - ((fireBaseAmount * .9) * (enemyFireResist/100)))
            if enemyFireResist > 100:
                playerFireEffect = math.ceil(fireBaseAmount * .1)
             
        if a.lower() == 'r':
            frostBaseAmount = playerIntelligence/3
            playerFrostEffect += math.ceil(frostBaseAmount - ((frostBaseAmount * .9) * (enemyFrostResist/100)))
            if enemyFrostResist > 100:
                playerFrostEffect = math.ceil(frostBaseAmount * .1)
                
        if a.lower() == 'p':
            playerPoisenEffect += math.ceil(playerIntelligence/6)
            
        if 'necronomicon' in heroInventory.magic:
            playerPoisenEffect += math.ceil(heroInventory.weaponDamages['necronomicon']/10) 

        return playerFrostEffect, playerFireEffect, playerPoisenEffect, playerMagicDamage, necroEffect
def giveLoot(heroInventory, player, enemyMaxHP):
    if enemyMaxHP < 50:
        loot = ['oil', 'pelt', 'fiber', 'logs']
        lootAmt = {'oil':1, 'pelt':1, 'fiber':4, 'logs':2}
        gold = random.randint(1,5)
    
    elif enemyMaxHP >= 50 and enemyMaxHP < 100:
        loot = ['weak healing potion','weak healing potion','weak healing potion','poisen ivy', 'cold snap', 'iron ore', 'crimson petal', 'wooden arrow']
        lootAmt = {'weak healing potion':1,'poisen ivy':1, 'cold snap':1, 'iron ore':1, 'crimson petal':1, 'wooden arrow': 3}
        gold = random.randint(5,10)
    
    elif enemyMaxHP >= 100 and enemyMaxHP < 200:
        loot = ['medium healing potion','medium healing potion', 'medium healing potion', 'iron', 'pelt', 'steel ore', 'cooked deer', 'iron arrow']
        lootAmt = {'medium healing potion': 1, 'iron':1, 'pelt':3, 'steel ore': 1, 'cooked deer': 1, 'iron arrow': 4}
        gold = random.randint(10,20)
    
    elif enemyMaxHP >= 200:
        loot = ['strong healing potion','strong healing potion','strong healing potion', 'fire resist potion', 'frost resist potion', 'poisen resist potion', 'flaming arrow']
        lootAmt = {'strong healing potion': 1, 'fire resist potion':1, 'frost resist potion':1, 'poisen resist potion': 1, 'flaming arrow': 5}
        gold = random.randint(20,30)

    
    choice = random.randint(0, len(loot)-1)
    item = loot[choice]
    amt = lootAmt[item]
    
    print('\nThe enemy dropped loot')
    print(f'+{lootAmt[item]} {item}')
    print(f'+{gold} gold')
    heroInventory.moveGold(gold)
    
    if item == 'oil':
        heroInventory.moveOil(amt)
    elif item == 'pelt':
        heroInventory.movePelt(amt)
    elif item == 'fiber':
        heroInventory.moveFiber(amt)
    elif item == 'logs':
        heroInventory.moveLogs(amt)
    elif item == 'weak healing potion':
        heroInventory.moveWeakHealingPotion(amt)
    elif item == 'poisen ivy':
        heroInventory.movePoisenIvy(amt)
    elif item == 'cold snap':
        heroInventory.moveColdSnap(amt)
    elif item == 'iron ore':
        heroInventory.moveIronOre(amt)
    elif item == 'crimson petal':
        heroInventory.moveCrimsonPetal(amt)
    elif item == 'wooden arrow':
        heroInventory.moveWoodenArrows(amt)
    elif item == 'medium healing potion':
        heroInventory.moveMediumHealingPotion(amt)
    elif item == 'iron':
        heroInventory.moveIron(amt)
    elif item == 'steel ore':
        heroInventory.moveSteelOre(amt)
    elif item == 'cooked deer':
        heroInventory.moveCookedDeer(amt)
    elif item == 'iron arrow':
        heroInventory.moveIronArrows(amt)
    elif item == 'strong healing potion':
        heroInventory.moveStrongHealingPotion(amt)
    elif item == 'fire resist potion':
        heroInventory.moveFireResistPotion(amt)
    elif item == 'frost resist potion':
        heroInventory.moveFrostResistPotion(amt)
    elif item == 'poisen resist potion':
        heroInventory.movePoisenResistPotion(amt)
    elif item == 'flaming arrow':
        heroInventory.moveFlamingArrows(amt)
   
    input('\npress enter to continue\n')


#MAIN MENU: CORE OF THE GAME
def giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire):  #Displays options, executes one based on user input (core of the game)
    checkDeath(player, clock1, actions, travels, heroInventory, stock, skills, fire)  #check if they starved to death
    checkExp(player, clock1,  actions, travels, heroInventory, stock, skills, fire)  #Check if the player leveled up
    checkTime(player, clock1,  actions, travels, heroInventory, stock, skills, fire)    #Check if the player passed out 

    #Displays the main menus

    displayTime(clock1, player)
    print(f"Health: {player.getHP()} / {player.getMax_hp()}\nHunger: {player.getHunger()} / {player.getMaxHunger()}")
    displayFire(fire)
    print(f'Gold: {heroInventory.getGold()}\n')
    displayPlayerMenu()                                                                                 
    displayActions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
    displayTravels(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
    checkCanEnterTunnels(heroInventory, travels) #See if theyve beating the crypt/glacier bosses

    #Matches the player's input to any action or place in the game
    a = input('\n-->')
    
    if travels.forceThroughSecretPassage == True:
        if a.lower() != 'secret passage':
            print(f'\n{player.getName()}, you need to leave through the secret passage!')
            giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            travels.forceThroughSecretPassage = False
            travels.forceThroughSewers = True
            secretPassage(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    
    if travels.forceThroughSewers == True:
        if a.lower() != 'crawl through sewers':
            print(f'\n{player.getName()}, you need to exit through the sewers!')
            giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            travels.forceThroughSewers = False
            crawlThroughSewers(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    
    #FOR DEV TESTING:
    if a.lower() == 'battle':
        while True:
            graveyardZombie = Enemy('Undead', 200, 0,0, 0, 0, 0, 0,'none', 0, 100)
            battle(graveyardZombie, player, clock1, actions, travels, heroInventory, stock, skills, fire)
    if a.lower() == 'get quests':
        heroInventory.completedQuests.append('investigate the crypt')
        heroInventory.completedQuests.append('Clear out the glacial cavern')
    if a.lower() == 'exp':
        player.addExp(100)
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    if a.lower() == 'testing':
        player.addExp(100)
        heroInventory.moveSteelArmor(1)
        heroInventory.moveSteelHammer(1)
        heroInventory.moveHuntersBow(1)
        heroInventory.moveMorellonomicon(1)
        heroInventory.moveIronArrows(20)
        heroInventory.moveFlamingArrows(20)
        heroInventory.moveStrongHealingPotion(10)
        heroInventory.moveFireResistPotion(10)
        heroInventory.moveFrostResistPotion(10)
        heroInventory.movePoisenResistPotion(10)
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
        
    #Options the player can always access
    if a.lower() == "i":  
        displayInventory(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
        print("(X): Back\n")
        a = input("-->")
        
        while a.lower() != 'x' and a.lower() != 'e' and a.lower() != 'u':
            a = input("-->")
        if a.lower() == 'x':
            giveOptions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
        elif a.lower() == 'e':
            equipItems(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
        else:
            unequipItems(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'c':
        displayCombat(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
        print("\n(X): Back")
        a = input("-->")
        while a.lower() != 'x':
            a = input("-->")
        giveOptions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
    
    elif a.lower() == "k":
        displaySkills(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
        print("\n(X): Back")
        a = input("-->")
        while a.lower() != 'x':
            a = input("-->")
        giveOptions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == "s":
        displayStats(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
        print("\n(X): Back")
        a = input("-->")
        while a.lower() != 'x':
            a = input("-->")
        giveOptions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)   
    elif a.lower() == 'e':
        eat(player, clock1,  actions, travels, heroInventory, stock, skills, fire) 
    elif a.lower() == 'q':
        displayQuests(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
        print("\n(X): Back")
        a = input("-->")
        while a.lower() != 'x':
            a = input("-->")
        giveOptions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)        
    
    #ACTIONS MENU: Options the player can access only if in the current ACTIONS MENU
    elif a.lower() in actions.actions:      
        if a.lower() == 'cook':
            cook(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'gather sticks':
            gatherSticks(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'sleep':
            sleep(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'gather fiber':
            gatherFiber(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'go fishing':
            goFishing(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'pick berries':
            pickBerries(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'light fire':
            lightFire(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'enter hunter shop':
            goShoppingHunter(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'enter hunting tavern':
            enterHuntingTavern(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
        elif a.lower() == 'enter smiths tavern':
            enterSmithsTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        elif a.lower() == 'enter town tavern':
            enterTownTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        elif a.lower() == 'enter smiths shop':
            goShoppingSmith(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'enter town shop':
            goShoppingScholar(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'mine steel ore':
            mineSteelOre(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'chop wood':
            chopWood(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'mine iron ore':
            mineIronOre(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'pray':
            pray(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'gather pelt':
            gatherPelt(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'gather oil':
            gatherOil(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'smelt ore':
            smeltOre(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'gather herbs':
            gatherHerbs(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'use workbench':
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'brew potions':
            brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'gather meal':
            gatherMeal(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'study':
            study(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'crawl through sewers':
            crawlThroughSewers(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'hunt deer':
            huntDeer(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    
    #TRAVEL MENU: Options the player can access only if in the current travel menu
    elif a.lower() in travels.locations:
        if a.lower() == 'forest':
            forest(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'hut':
            hut(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'cave':
            cave(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'river':
            river(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'meadows':
            meadows(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'graveyard':
            graveyard(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'crypt':
            crypt(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'village':
            village(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'crossroads':
            crossroads(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'outskirts':
            outskirts(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower () == 'smiths home':
            smithsHome(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'swamp':
            swamp(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower () == 'forge':
            forge(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'wood stand':
            woodStand(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'glacial cavern':
            glacialCavern(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'animal den':
            animalDen(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'town square':
            townSquare(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'library':
            library(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'secret passage':
            secretPassage(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'tunnels':
            tunnels(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'manor':
            manor(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'servants quarters':
            servantsQuarters(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'herb garden':
            herbGarden(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'glacial passage':
            glacialPassage(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    #If their input is not in any menu, give them the menu again
    else:
        giveOptions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)

#MENU FUNCTIONS: 
def displayTime(clock1, player):
    current_min =  clock1.time % 60
    current_hour = math.floor(clock1.time / 60)
    til_dark_min = clock1.timeLeft() % 60
    til_dark_hour = math.floor(clock1.timeLeft() / 60)
    print(f"\nDay:{clock1.getDay()}")
    if current_min == 0:
        print(f"Current Time: {current_hour}:{current_min}0")
    else:
        print(f"\nCurrent Time: {current_hour}:{current_min}")
    
    if til_dark_min == 0:
        print(f"Time Left Until Dark {til_dark_hour}:{til_dark_min}0")
    else:
        print(f"Time Left Until Dark {til_dark_hour}:{til_dark_min}")
    print(f'Location: {player.getLocation().capitalize()}\n')
def displayFire(fire):
    print(f"Fire: {fire.fuel} / {fire.fuelMax}")
def displayPlayerMenu():
        print("Player:")
        print("(I) Inventory")
        print("(C) Combat")
        print("(S) Current Stats")
        print("(K) Skills")
        print("(E) Eat")
        print('(Q) Quests')
def displayActions(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    print("\nActions:")
    for i in actions.actions:
        print(i.capitalize())           
def displayTravels(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    print("\nTravel To:")
    for i in travels.locations:
        print(i.capitalize())
def displayInventory(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    print("\nRaw Materials")
    for i in heroInventory.raw_material.keys():
        if heroInventory.raw_material[i] > 0:
            print(f"({heroInventory.raw_material[i]}) {i.capitalize()}")
    print("\nFood")
    for i in heroInventory.cookedFood.keys():
        if heroInventory.cookedFood[i] >0:
            print(f"({heroInventory.cookedFood[i]}) {i.capitalize()}")
    print("\nArmor")
    for i in heroInventory.allArmor.keys():
        if heroInventory.allArmor[i] > 0:
            print(f"({heroInventory.allArmor[i]}) {i.capitalize()}")  
    print("\nWeapons")
    for i in heroInventory.weapons.keys():
        if heroInventory.weapons[i] > 0:
            print(f"({heroInventory.weapons[i]}) {i.capitalize()}")   
    print("\nCharms")
    for i in heroInventory.allCharms.keys():
        if heroInventory.allCharms[i] > 0:
            print(f"({heroInventory.allCharms[i]}) {i.capitalize()}") 
    print(f"\nCurrently Equiped:\nMelee: {heroInventory.melee}\nRanged: {heroInventory.ranged}\nMagic: {heroInventory.magic}\nArmor: {heroInventory.armor}\nCharm: {heroInventory.charm}\n\n(E): Equip Items\n(U): Unequip Items")        
def displayCombat(player, clock1,  actions, travels, heroInventory, stock, skills, fire):
    print('\nRESISTANCES')
    print(f'Fire ----> {player.getFireResist()}')
    print(f'Frost ---> {player.getFrostResist()}')
    print(f'Poisen --> {player.getPoisenResist()}')
    print(f'\nARROWS')
    for i in heroInventory.arrows.keys():
        if heroInventory.arrows[i] > 0:
            print(f'{i.capitalize()} ---> {heroInventory.arrows[i]}') 
    print(f'\nPOTIONS')
    for i in heroInventory.potions.keys():
        if heroInventory.potions[i] > 0:
            print(f'{i.capitalize()} ---> {heroInventory.potions[i]}')
def displayStats(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    print(f"\nHealth --------> {player.getHP()} / {player.getMax_hp()}")
    print(f'Hunger --------> {player.getHunger()} / {player.getMaxHunger()}')
    print(f"Defence -------> {player.getDefence()}")
    
    print(f"\nMelee ---------> {player.getMelee()}")
    print(f'Ranged --------> {player.getRanged()}')
    print(f'Intelligence --> {player.getIntelligence()}')
    print(f'Fishing -------> {player.getFishing()}')
    print(f'Crafting ------> {player.getCrafting()}')
    print(f'Luck ----------> {player.getLuck()}')
    print(f'Alchemy -------> {player.getAlchemy()}')
def displaySkills(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    print(f"Level: {player.getLevel()}")
    print(f"Exp: {player.getExp()} / {player.lvlthresholds[0]}")
    print(f"\nMelee: {skills.getMeleeSkill()}\nRanged: {skills.getRangedSkill()}\nIntelligence: {skills.getIntelligenceSkill()}\nFishing: {skills.getFishingSkill()}\nCrafting: {skills.getCraftingSkill()}\nEndurance: {skills.getEnduranceSkill()}\nLuck: {skills.getLuckSkill()}\nAlchemy: {skills.getAlchemySkill()}")
def displayQuests(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    current = []
    completed = []
    items = []
    for i in heroInventory.currentQuests:
        current.append(i)
    for i in heroInventory.completedQuests:
        completed.append(i)
    for i in heroInventory.questItems:
        items.append(i)
    #Print current quests
    if len(current) == 0:
        print('\nCurrent Quests:\nNone')   
    else:
        print('\nCurrent Quests:')
        for i in current:
            print(f'{i.capitalize()}')
    
    #Print completed quests
    if len(completed) == 0:
        print('\nCompleted Quests:\nNone')
    else:
        print('\nCompleted Quests:')
        for i in completed:
            print(f'{i.capitalize()}')
    
    #Print quest items
    if len(items) == 0:
        print('\nQuest Items:\nNone')
    else:
        print('\nQuest Items:')
        for i in items:
            print(f'{i.capitalize()}')
    
    
#CHECKER FUNCTION:
def checkTime(player, clock1, actions, travels, heroInventory, stock, skills, fire):  #checks if the player is pasts midnight, then passout
    #print("CHECKING TIME")
    if clock1.getTime() > clock1.getEnd():
        passout(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
    elif clock1.timeLeft() <= 0:
        passout(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
    elif clock1.timeLeft() <= 180:
        print('\nIts starting to get dark, you should should get to sleep soon') 
def checkDay(player, clock1, actions, travels, heroInventory, stock, skills, fire):  #Checks what day it is after you sleep, then trigger that days introduction
    if clock1.getDay() == 2:
        startDay2(player, clock1,  heroInventory, stock, actions, travels, skills, fire)
    elif clock1.getDay() == 3:
        startDay3(player, clock1,  heroInventory, stock, actions, travels, skills, fire)
    elif clock1.getDay() == 4:
        startDay4(player, clock1,  heroInventory, stock, actions, travels, skills, fire)
    elif clock1.getDay() == 5:
        startDay5(player, clock1,  heroInventory, stock, actions, travels, skills, fire)
    elif clock1.getDay() == 6:
        startDay6(player, clock1,  heroInventory, stock, actions, travels, skills, fire)
    elif clock1.getDay() == 7:
        startDay7(player, clock1,  heroInventory, stock, actions, travels, skills, fire)
    elif clock1.getDay() == 8:
        startDay8(player, clock1,  heroInventory, stock, actions, travels, skills, fire)
    elif clock1.getDay() == 9:
        startDay9(player, clock1,  heroInventory, stock, actions, travels, skills, fire)
    elif clock1.getDay() == 10:
        startDay10(player, clock1,  heroInventory, stock, actions, travels, skills, fire)
def checkExp(player, clock1, actions, travels, heroInventory, stock, skills, fire):  #check if the player leveled up
    if player.getExpPoints() > 0:
        levelUp(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
def checkDeath(player, clock1, actions, travels, heroInventory, stock, skills, fire):  #check if player is dead
    if player.getHP() <= 0:
        gameOver(player, clock1,  actions, travels, heroInventory, stock, skills, fire)   
def checkHunger(player, time_passed, action_type, fire):  #check if hunger is zero, then reduce HP by amount of time spent at zero hunger
    if player.getHunger() <= 0:
        player.setHunger(0)
        damage = math.ceil(time_passed /30)  #balance :lose 1 HP every 30min that you are hungry
        player.setHP(player.getHP() - damage)        
        print(f"-{damage} HP")
def checkFire(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    if fire.fuel >= fire.fuelMax:
        fire.fuel = fire.fuelMax
    if fire.fuel < 0:
        fire.fuel = 0
    
    if fire.fuel > 0:
        fire.lit = True
    else:
        fire.lit = False
def hasArrows(heroInventory):
    available_arrows = []
    for i in heroInventory.arrows.keys():
        if heroInventory.arrows[i] >0:
            available_arrows.append(i)
    if len(available_arrows) > 0:
        return True
    else:
        return False
def hasPotions(heroInventory):
    available_potions = []
    for i in heroInventory.potions.keys():
        if heroInventory.potions[i] > 0:
            available_potions.append(i)
    if len(available_potions) > 0:
        return True
    else:
        return False
def checkCanEnterTunnels(heroInventory, travels):
    if 'investigate the crypt' in heroInventory.completedQuests and 'Clear out the glacial cavern' in heroInventory.completedQuests:
        travels.canEnterTunnels = True
        if travels.tellAboutTownRumor == False:
            print('\nThere are rumors going around at the town\'s tavern')
            input('press enter to continue')
            travels.tellAboutTownRumor = True

#UNIQUE FUNCTIONS:
def getHungry(player, addedTime, action, fire):   #reduces player hunger based on amount of time
    printMessage = True
    if player.getHunger() <= 0:
        printMessage = False
    hunger_amount = math.floor(addedTime * -.07)   #lose 0.07 hunger per minute. or 100 hunger per day. balance this number
    player.addHunger(hunger_amount)
    if printMessage == True:       #Only print this out if they didnt already have zero hunger.
        print(f"-{abs(hunger_amount)} hunger")
def passout(player, clock1, actions, travels, heroInventory, stock, skills, fire):  #bring player to their home, they take damage based on time past midnght
    #Make player take damage
    time_over = math.ceil(abs(clock1.timeLeft()/60) + 1)  #either 0, or negative. Largest you can go over is however long the longest tasks takes. (~1-4 usually)
    time_over_minutes = clock1.timeLeft() % 60
    time_over_hours = -1 * math.floor(clock1.timeLeft() / 60)
    damage = math.ceil((time_over * 25) *.55)  #this will require balancing
    player.setHP(player.getHP() - damage)   #player takes damage
    print(f"{player.getName()} passed out from exhaustion. Nearby villagers dragged him to his bed")
    print(f"You took {damage} damage for working {time_over_hours} hours and {time_over_minutes} minutes past midnight.")
    checkDeath(player, clock1, actions, travels, heroInventory, stock, skills, fire)  #check if they died
    
    
    #Then reset the player at their original home
    a = input("Press enter to wake up")
    clock1.setTime(clock1.getStart())
    clock1.addDay()
    checkDay(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    
    
    if player.getType() == 1:
        smithsHome(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif player.getType() == 2:
        hut(player, clock1, heroInventory, stock, actions, travels, skills, fire)   
    else:
        manor(player, clock1, heroInventory, stock, actions, travels, skills, fire)
def levelUp(player, clock1, actions, travels, heroInventory, stock, skills, fire): #levels the player up, lets them increase their skills
    if player.getExpPoints() == 0:
        print("No more points to spend")
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    else:
        print(f"\n{player.getName()}, you leveled up!")
        print("Spend your points to level your skills")
        print(f"{player.getExpPoints()} points remaining\n")
        print(f"\nMelee(M): {skills.getMeleeSkill()}\nRanged(R): {skills.getRangedSkill()}\nIntelligence(I): {skills.getIntelligenceSkill()}\nFishing(F): {skills.getFishingSkill()}\nCrafting(C): {skills.getCraftingSkill()}\nEndurance(E): {skills.getEnduranceSkill()}\nLuck(L): {skills.getLuckSkill()}\nAlchemy(A): {skills.getAlchemySkill()}")
        a = input('-->')
       
        if a.lower() == 'm':
            skills.levelMeleeSkill()
            player.moveMelee(1)
            player.useExpPoint()
            levelUp(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        elif a.lower() == 'r':
            skills.levelRangedSkill()
            player.moveRanged(1)
            player.useExpPoint()
            levelUp(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        elif a.lower() == 'i':
            skills.levelIntelligenceSkill()
            player.moveIntelligence(1)
            player.useExpPoint()
            levelUp(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        elif a.lower() == 'f':
            skills.levelFishingSkill()
            player.moveFishing(1)
            player.useExpPoint()
            levelUp(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        elif a.lower() == 'c':
            skills.levelCraftingSkill()
            player.setCrafting(player.getCrafting() + 1)
            player.useExpPoint()
            levelUp(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        elif a.lower() == 'e':
            levelEnduranceSkill(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            player.useExpPoint()
            levelUp(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        elif a.lower() == 'l':
            skills.levelLuckSkill()
            player.moveLuck(1)
            player.useExpPoint()
            levelUp(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        elif a.lower() == 'a':
            skills.levelAlchemySkill()
            player.moveAlchemy(1)
            player.useExpPoint()
            levelUp(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
        
        else:
            levelUp(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def levelEnduranceSkill(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    skills.enduranceSkill += 1
    player.moveFireResist(1)
    player.movePoisenResist(1)
    player.moveFrostResist(1)
    print(f'\nResistances Increased')
def equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    equipable_items = []
    
    print('\nWhat would you like to equip?')
    #displays armor and qty in inventory
    print('\nArmor:')
    for i in heroInventory.allArmor.keys():
        if heroInventory.allArmor[i] > 0:
            equipable_items.append(i)
            print(f"{i.capitalize()}: {heroInventory.allArmor[i]}")
    print('\nWeapons:')
    for i in heroInventory.weapons.keys():
        if heroInventory.weapons[i] > 0:
            equipable_items.append(i)
            print(f"{i.capitalize()}: {heroInventory.weapons[i]}")
    print('\nCharms:')
    for i in heroInventory.allCharms.keys():
        if heroInventory.allCharms[i] > 0:
            equipable_items.append(i)
            print(f"{i.capitalize()}: {heroInventory.allCharms[i]}")
    print('')      
    print(f"Currently Equiped:\nMelee: {heroInventory.melee}\nRanged: {heroInventory.ranged}\nMagic: {heroInventory.magic}\nArmor: {heroInventory.armor}\nCharm: {heroInventory.charm}")   
    if len(equipable_items) == 0:
        print('\nYou have nothing to equip')
    print('(X): Back')
    a = input('-->')
    
    if a.lower() in equipable_items:
        #MELEE
        if a.lower() == 'fishing pole':
            if len(heroInventory.melee) > 0:  #unique
                print('\nYou already have a melee weapon equiped')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'fishing'   #unique
                stat_amount = heroInventory.weaponDamages['fishing pole']       #unique
                heroInventory.moveFishingPole(-1)    #unique
                heroInventory.melee.append(a.lower())  #unique
                player.moveFishing(stat_amount)       #unique
                print(f'\nFishing Pole equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'smiths hammer':
            if skills.getMeleeSkill() < 1:
                print('\nMelee skill too low')
                print(f'Melee Skill {skills.getMeleeSkill()}/1')
                input('press enter to continue')
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            if len(heroInventory.melee) > 0:  #unique
                print('\nYou already have a melee weapon equiped')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'melee'   #unique
                stat_amount = heroInventory.weaponDamages['smiths hammer']       #unique
                heroInventory.moveSmithsHammer(-1)    #unique
                heroInventory.melee.append(a.lower())  #unique
                player.moveMelee(stat_amount)       #unique
                print(f'\nSmiths Hammer equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'steel hammer':
            if skills.getMeleeSkill() < 10:
                print('\nMelee skill too low')
                print(f'Melee Skill {skills.getMeleeSkill()}/10')
                input('press enter to continue')
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            if len(heroInventory.melee) > 0:  #unique
                print('\nYou already have a melee weapon equiped')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'melee'   #unique
                stat_amount = heroInventory.weaponDamages['smiths hammer']       #unique
                heroInventory.moveSteelHammer(-1)    #unique
                heroInventory.melee.append(a.lower())  #unique
                player.moveMelee(stat_amount)       #unique
                print(f'\nSteel Hammer equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'hammer of ice':
            if skills.getMeleeSkill() < 15:
                print('\nMelee skill too low')
                print(f'Melee Skill {skills.getMeleeSkill()}/15')
                input('press enter to continue')
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            if len(heroInventory.melee) > 0:  #unique
                print('\nYou already have a melee weapon equiped')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'melee'   #unique
                stat_amount = heroInventory.weaponDamages['hammer of ice']       #unique
                heroInventory.moveHammerOfIce(-1)    #unique
                heroInventory.melee.append(a.lower())  #unique
                player.moveMelee(stat_amount)       #unique
                print(f'\nHammer of Ice equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        #RANGED WEAPONS
        if a.lower() == 'wooden bow':  #Equip wooden bow
            if skills.getRangedSkill() < 1:
                print('\nRanged skill too low')
                print(f'Ranged Skill {skills.getRangedSkill()}/1')
                input('press enter to continue')
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            if len(heroInventory.ranged) > 0:  #unique
                print('\nYou already have a ranged weapon equiped')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'ranged'   #unique
                stat_amount = heroInventory.weaponDamages['wooden bow']       #unique
                heroInventory.moveWoodenBow(-1)    #unique
                heroInventory.ranged.append(a.lower())  #unique
                player.moveRanged(stat_amount)       #unique
                print(f'\nWooden Bow equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'hunters bow':  #Equip hunters bow
            if skills.getRangedSkill() < 10:
                print('\nRanged skill too low')
                print(f'Ranged Skill {skills.getRangedSkill()}/10')
                input('press enter to continue')
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            if len(heroInventory.ranged) > 0:  #unique
                print('\nYou already have a ranged weapon equiped')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'ranged'   #unique
                stat_amount = heroInventory.weaponDamages['hunters bow']       #unique
                heroInventory.moveHuntersBow(-1)    #unique
                heroInventory.ranged.append(a.lower())  #unique
                player.moveRanged(stat_amount)       #unique
                print(f'\nHunters Bow equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)    
        if a.lower() == 'bow of fire':
            if skills.getRangedSkill() < 20:
                print('\nRanged skill too low')
                print(f'Ranged Skill {skills.getRangedSkill()}/20')
                input('press enter to continue')
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            if len(heroInventory.ranged) > 0:  #unique
                print('\nYou already have a ranged weapon equiped')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'ranged'   #unique
                stat_amount = heroInventory.weaponDamages['bow of fire']       #unique
                heroInventory.moveBowOfFire(-1)    #unique
                heroInventory.ranged.append(a.lower())  #unique
                player.moveRanged(stat_amount)       #unique
                print(f'\nBow of Fire equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)    
        #MAGIC
        if a.lower() == 'lexicon':
            if skills.getIntelligenceSkill() < 1:
                print('\nIntelligence skill too low')
                print(f'Intelligence Skill {skills.getIntelligenceSkill()}/1')
                input('press enter to continue')
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            
            if len(heroInventory.magic) > 0:  #unique
                print('\nYou already have a maigc book equiped!')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'intelligence'   #unique
                stat_amount = heroInventory.weaponDamages['lexicon']       #unique
                heroInventory.moveLexicon(-1)    #unique
                heroInventory.magic.append(a.lower())  #unique
                player.moveIntelligence(stat_amount)       #unique
                print(f'\nLexicon equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)  
        if a.lower() == 'morellonomicon':
            if skills.getIntelligenceSkill() < 10:
                print('\nIntelligence skill too low')
                print(f'Intelligence Skill {skills.getIntelligenceSkill()}/10')
                input('press enter to continue')
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            
            
            if len(heroInventory.magic) > 0:  #unique
                print('\nYou already have a tomb equiped!')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'intelligence'   #unique
                stat_amount = heroInventory.weaponDamages['morellonomicon']       #unique
                heroInventory.moveMorellonomicon(-1)    #unique
                heroInventory.magic.append(a.lower())  #unique
                player.moveIntelligence(stat_amount)       #unique
                print(f'\nMorellonomicon equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)   
        if a.lower() == 'necronomicon':
            if skills.getIntelligenceSkill() < 20:
                print('\nIntelligence skill too low')
                print(f'Intelligence Skill {skills.getIntelligenceSkill()}/20')
                input('press enter to continue')
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            if len(heroInventory.magic) > 0:  #unique
                print('\nYou already have a tomb equiped!')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'intelligence'   #unique
                stat_amount = heroInventory.weaponDamages['necronomicon']       #unique
                heroInventory.moveNecronomicon(-1)    #unique
                heroInventory.magic.append(a.lower())  #unique
                player.moveIntelligence(stat_amount)       #unique
                print(f'\nNecronomicon equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        #ARMOR
        if a.lower() == 'leather armor':  #Equip leather armor
            if len(heroInventory.armor) > 0:  #unique
                print('\nYou already have armor equiped')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'defence'   #unique
                stat_amount = heroInventory.armorDefences['leather armor']       #unique
                heroInventory.moveLeatherArmor(-1)    #unique
                heroInventory.armor.append(a.lower())  #unique
                player.moveDefence(stat_amount)       #unique
                print(f'\nLeather Armor equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'iron armor':  #Equip leather armor
            if len(heroInventory.armor) > 0:  #unique
                print('\nYou already have armor equiped')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'defence'   #unique
                stat_amount = stat_amount = heroInventory.armorDefences['iron armor']       #unique
                heroInventory.moveIronArmor(-1)    #unique
                heroInventory.armor.append(a.lower())  #unique
                player.moveDefence(stat_amount)       #unique
                print(f'\nIron Armor equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'steel armor':  #Equip leather armor
            if len(heroInventory.armor) > 0:  #unique
                print('\nYou already have armor equiped')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'defence'   #unique
                stat_amount = stat_amount = heroInventory.armorDefences['steel armor']       #unique
                heroInventory.moveSteelArmor(-1)    #unique
                heroInventory.armor.append(a.lower())  #unique
                player.moveDefence(stat_amount)       #unique
                print(f'\nSteel Armor equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)

        #CHARMS
        if a.lower() == 'rabbits foot':  #Equip rabbitss foot
            if len(heroInventory.charm) > 0:  #unique
                print('\nYou already a charm equiped')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'luck'   #unique
                stat_amount = heroInventory.charmAmounts['rabbits foot']       #unique
                heroInventory.moveRabbitsFoot(-1)    #unique, removes item from inventory
                heroInventory.charm.append(a.lower())  #unique, adds item to equiped list
                player.moveLuck(stat_amount)       #unique, adds the stats to player
                print(f'\nRabbits Foot equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'crimson amulet':  
            if len(heroInventory.charm) > 0:  #unique
                print('\nYou already a charm equiped')  #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                item_stat = 'HP'   #unique
                stat_amount = stat_amount = heroInventory.charmAmounts['crimson amulet']       #unique
                heroInventory.moveCrimsonAmulet(-1)    #unique, removes item from inventory
                heroInventory.charm.append(a.lower())  #unique, adds item to equiped list
                player.setMax_hp(player.getMax_hp() + stat_amount)       #unique, adds the stats to player
                print(f'\nCrimson Amulet equiped.\n+{stat_amount} {item_stat}\n')   #unique
                equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    
    elif a.lower() == 'x':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    else:
        print('\nYou dont have any of those left.')
        equipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    print('\nWhat would you like to unequip?')
    #Check if they have anything equiped at all
    equiped_equipment = []
    if len(heroInventory.melee) > 0:
        equiped_equipment.append(heroInventory.melee[0])
    if len(heroInventory.ranged) > 0:
        equiped_equipment.append(heroInventory.ranged[0])
    if len(heroInventory.magic) > 0:   
        equiped_equipment.append(heroInventory.magic[0])
    if len(heroInventory.armor) > 0:    
        equiped_equipment.append(heroInventory.armor[0])
    if len(heroInventory.charm) > 0:    
        equiped_equipment.append(heroInventory.charm[0])
    if len(equiped_equipment) == 0:
        print('\nYou have nothing to unequip')
    
    print(f"Currently Equiped:\nMelee: {heroInventory.melee}\nRanged: {heroInventory.ranged}\nMagic: {heroInventory.magic}\nArmor: {heroInventory.armor}\nCharm: {heroInventory.charm}")
    print('\n(X): Back\n')
    a = input('-->')
    #Unequip the equipments
    if a.lower() in equiped_equipment:
        #MELEE 
        if a.lower() == 'fishing pole':
            item_stat = 'fishing'
            stat_amount = heroInventory.weaponDamages['fishing pole']
            heroInventory.moveFishingPole(1)
            heroInventory.melee.pop(0)
            player.moveFishing(-1*stat_amount)
            print(f"\nFishing Pole unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'smiths hammer':
            item_stat = 'melee'
            stat_amount = heroInventory.weaponDamages['smiths hammer']
            heroInventory.moveSmithsHammer(1)
            heroInventory.melee.pop(0)
            player.moveMelee(-1*stat_amount)
            print(f"\nSmiths Hammer unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'steel hammer':
            item_stat = 'melee'
            stat_amount = heroInventory.weaponDamages['steel hammer']
            heroInventory.moveSteelHammer(1)
            heroInventory.melee.pop(0)
            player.moveMelee(-1*stat_amount)
            print(f"\nSteel Hammer unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'hammer of ice':
            item_stat = 'melee'
            stat_amount = heroInventory.weaponDamages['hammer of ice']
            heroInventory.moveHammerOfIce(1)
            heroInventory.melee.pop(0)
            player.moveMelee(-1*stat_amount)
            print(f"\nHammer of Ice unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        #RANGED WEAPONS
        if a.lower() == 'wooden bow':
            item_stat = 'ranged'
            stat_amount = heroInventory.weaponDamages['wooden bow']
            heroInventory.moveWoodenBow(1)
            heroInventory.ranged.pop(0)
            player.moveRanged(-1*stat_amount)
            print(f"\nWooden Bow unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'hunters bow':
            item_stat = 'ranged'
            stat_amount = heroInventory.weaponDamages['hunters bow']
            heroInventory.moveHuntersBow(1)  #add item back to our inventory
            heroInventory.ranged.pop(0)    #remove item from equiped list
            player.moveRanged(-1*stat_amount)   #remove the items stats
            print(f"\nHunters Bow unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'bow of fire':
            item_stat = 'ranged'
            stat_amount = heroInventory.weaponDamages['bow of fire']
            heroInventory.moveBowOfFire(1)  #add item back to our inventory
            heroInventory.ranged.pop(0)    #remove item from equiped list
            player.moveRanged(-1*stat_amount)   #remove the items stats
            print(f"\nBow of Fire unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)  
        #MAGIC
        if a.lower() == 'lexicon':
            item_stat = 'intelligence'
            stat_amount = heroInventory.weaponDamages['lexicon']
            heroInventory.moveLexicon(1)  #add item back to our inventory
            heroInventory.magic.pop(0)    #remove item from equiped list
            player.moveIntelligence(-1*stat_amount)   #remove the items stats
            print(f"\nLexicon unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'morellonomicon':
            item_stat = 'intelligence'
            stat_amount = heroInventory.weaponDamages['morellonomicon']
            heroInventory.moveMorellonomicon(1)  #add item back to our inventory
            heroInventory.magic.pop(0)    #remove item from equiped list
            player.moveIntelligence(-1*stat_amount)   #remove the items stats
            print(f"\nMorellonomicon unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'necronomicon':
            item_stat = 'intelligence'
            stat_amount = heroInventory.weaponDamages['necronomicon']
            heroInventory.moveNecronomicon(1)  #add item back to our inventory
            heroInventory.magic.pop(0)    #remove item from equiped list
            player.moveIntelligence(-1*stat_amount)   #remove the items stats
            print(f"\nNecronomicon unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        #ARMOR
        if a.lower() == 'leather armor':
            item_stat = 'defence'
            stat_amount = heroInventory.armorDefences['leather armor']
            heroInventory.moveLeatherArmor(1)  #add item back to our inventory
            heroInventory.armor.pop(0)    #remove item from equiped list
            player.moveDefence(-1*stat_amount)   #remove the items stats
            print(f"\nLeather Armor unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'iron armor':
            item_stat = 'defence'
            stat_amount = heroInventory.armorDefences['iron armor']
            heroInventory.moveIronArmor(1)  #add item back to our inventory
            heroInventory.armor.pop(0)    #remove item from equiped list
            player.moveDefence(-1*stat_amount)   #remove the items stats
            print(f"\nIron Armor unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'steel armor':
            item_stat = 'defence'
            stat_amount = heroInventory.armorDefences['steel armor']
            heroInventory.moveSteelArmor(1)  #add item back to our inventory
            heroInventory.armor.pop(0)    #remove item from equiped list
            player.moveDefence(-1*stat_amount)   #remove the items stats
            print(f"\nSteel Armor unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        #CHARMS:
        if a.lower() == 'rabbits foot':
            item_stat = 'luck'
            stat_amount = heroInventory.charmAmounts['rabbits foot']
            heroInventory.moveRabbitsFoot(1)  #add item back to our inventory
            heroInventory.charm.pop(0)    #remove item from equiped list
            player.moveLuck(-1*stat_amount)   #remove the items stats
            print(f"\nRabbits Foot unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        if a.lower() == 'crimson amulet':
            item_stat = 'luck'
            stat_amount = heroInventory.charmAmounts['crimson amulet']
            heroInventory.moveRabbitsFoot(1)  #add item back to our inventory
            heroInventory.charm.pop(0)    #remove item from equiped list
            player.setMax_hp(player.getMax_hp() - stat_amount)   #remove the items stats
            print(f"\nRabbits Foot unequiped.\n-{stat_amount} {item_stat}")
            unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'x':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    else:
        unequipItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def goFishing(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    action_time = 180            #Unique                                                                 
    action_amount = 1           #Unique                                                                     
    action_name = 'fish'       #Unique , for dialouge
    action_type = 'fishing'   #Unique, for dialouge 
    action_exp = 1              #Unique
    
    print(f"Current fishing stat: {player.getFishing()}")
    print(f'Going fishing will take 3 hours.')
    print('Continue? (y/n)')
    
    
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'y':
        if heroInventory.bait == 0:
            print('You dont have any bait')
            input('press enter to continue')
            giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        elif 'fishing pole' not in heroInventory.melee:
            print('You dont have a fishing pole equiped')
            input('press enter to continue')
            giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            fail_chance = random.randint(0, 25) #balance this number
            if fail_chance > player.getFishing():
                print('You got a bite but failed to real the fish in')
                print('-1 bait')
                heroInventory.moveBait(-1)
                clock1.addTime(action_time) #add time
                getHungry(player, action_time, action_type, fire)  #take hunger away from player
                checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
                input('press enter to continue')
                giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                heroInventory.moveBait(-1)
                heroInventory.moveFish(action_amount)          #Unique, give them the items
                print(f"\n+1 fish")   
                if player.getFishingSkill > 20:
                    heroInventory.moveFish(action_amount)
                    print(f"\n+1 extra fish")
                print(f"+{action_exp} EXP")
                print('-1 bait')                
                player.addExp(action_exp)   #gives player exp
                clock1.addTime(action_time) #add time
                getHungry(player, action_time, action_type, fire)  #take hunger away from player
                checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
                input('press enter to continue')
                giveOptions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
def smeltOre(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    stick_amount = heroInventory.sticks
    log_amount = heroInventory.logs
    iron_ore_amount = heroInventory.ironOre
    steel_ore_amount = heroInventory.steelOre

    print(f"\nWhat will you smelt:")
    print(f"Forge Fuel: {fire.getForgeFuel()}\n")
    print(f"(A) Add Fuel")
    print(f"(I) Iron: 5 Fuel")
    print(f"(S) Steel: 10 Fuel")
    print(f"(X) Back\n")
    a = input('-->')
    while a.lower() not in ['a', 'i', 's', 'x']:
        a = input('-->')
    
    if a.lower() == 'i':  #smelt iron
        action_time = 60            #Unique                                                                 
        action_amount = 1           #Unique                                                                     
        action_name = 'iron'       #Unique 
        action_type = 'smelting'   #Unique, for dialouge 
        action_exp = 3              #Unique
        print(f"Smelting iron ore will take 1 hour.")
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
            
        if a.lower() == 'y':
            if fire.getForgeFuel() < 5:  #Balance
                print("You need to add fuel")
                input('press enter to continue')
                smeltOre(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            if iron_ore_amount > 0:
                fire.addForgeFuel(-5)
                heroInventory.moveIronOre(-1)  #Unique 
                heroInventory.moveIron(1)  #Unique 
                player.addExp(action_exp)   #gives player exp
                
                clock1.addTime(action_time) #add time
                getHungry(player, action_time, action_type, fire)  #take hunger away from player
                checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
                print(f"You have smelted iron ore")  #Unique 
                print(f'+{action_exp} EXP')
                input('press enter to continue')
                smeltOre(player, clock1, heroInventory, stock, actions, travels, skills, fire) #Unique 
            else:
                print("You dont have any iron ore")
                input('press enter to continue')
                smeltOre(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'n':
            smeltOre(player, clock1, heroInventory, stock, actions, travels, skills, fire)

    elif a.lower() == 's':  #smelt steel
        action_time = 120            #Unique                                                                 
        action_amount = 1           #Unique                                                                     
        action_name = 'steel'       #Unique 
        action_type = 'smelting'   #Unique, for dialouge 
        action_exp = 5              #Unique
        print(f"Smelting steel ore will take 2 hours.")
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'y':
            if fire.getForgeFuel() < 10:  #Balance
                print("You need to add fuel")
                input('press enter to continue')
                smeltOre(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            if steel_ore_amount > 0:
                fire.addForgeFuel(-10)
                heroInventory.moveSteelOre(-1)  #Unique 
                heroInventory.moveSteel(1)  #Unique 
                player.addExp(action_exp)   #gives player exp
                
                clock1.addTime(action_time) #add time
                getHungry(player, action_time, action_type, fire)  #take hunger away from player
                checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
                print(f"You have smelted steel ore")  #Unique 
                print(f'+{action_exp} EXP')
                input('press enter to continue')               
                smeltOre(player, clock1, heroInventory, stock, actions, travels, skills, fire) #Unique 
            else:
                print("You dont have any steel ore")
                input('press enter to continue')
                smeltOre(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'n':
            smeltOre(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'a':
        addForgeFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'x':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire) 
def useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if 'smiths hammer' not in heroInventory.melee and 'steel hammer' not in heroInventory.melee and 'hammer of ice' not in heroInventory.melee:
        print('\nYou need a hammer equiped to use the workbench')
        input('press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
    craftables = ['x','wooden arrow', 'iron arrow', 'steel arrow', 'flaming arrow', 'wooden bow', 'hunters bow', 'smiths hammer', 'steel hammer', 'leather armor', 'iron armor', 'steel armor', 'fishing pole']
    print('\nWhat would you like to craft?')
    print(f'Crafting Skill: {player.getCrafting()}')
    

    wooden_arrow_craft = {'sticks': 5, 'fiber': 5}
    iron_arrow_craft = {'sticks': 5, 'fiber': 5, 'iron': 1, 'oil': 1}
    steel_arrow_craft = {'sticks': 5, 'fiber': 5, 'steel': 1, 'oil': 2}
    flaming_arrow_craft = {'sticks': 5, 'fiber': 5, 'steel': 1, 'iron': 1, 'oil': 5}
    
    fishing_pole_craft = {'sticks': 10, 'fiber': 10}
    smiths_hammer_craft = {'logs': 1, 'fiber': 10, 'iron': 2, 'oil': 1}
    steel_hammer_craft = {'logs': 1, 'fiber': 10, 'steel': 2, 'oil': 1}
    wooden_bow_craft = {'sticks': 10, 'fiber': 10}
    hunters_bow_craft = {'logs': 5, 'fiber': 25, 'steel': 2, 'oil': 1, }
    
    leather_armor_craft = {'pelt': 1, 'fiber': 15}
    iron_armor_craft = {'pelt': 2, 'fiber': 20, 'iron': 2, 'oil': 1}
    steel_armor_craft = {'pelt': 4, 'fiber': 25, 'steel': 2, 'oil': 3}
    
    print('\nARROWS')
    print(f'wooden arrow x10 -----> sticks {heroInventory.sticks}/5 --- fiber {heroInventory.fiber}/5')
    print(f'iron arrow x10 -------> sticks {heroInventory.sticks}/5 --- fiber {heroInventory.fiber}/5 --- iron  {heroInventory.iron}/1 --- oil {heroInventory.oil}/1')
    print(f'steel arrow x10 ------> sticks {heroInventory.sticks}/5 --- fiber {heroInventory.fiber}/5 --- steel {heroInventory.steel}/1 --- oil {heroInventory.oil}/2')
    print(f'flaming arrow x10 ----> sticks {heroInventory.sticks}/5 --- fiber {heroInventory.fiber}/5 --- steel {heroInventory.steel}/1 --- iron {heroInventory.iron}/1 ---  oil {heroInventory.oil}/3')
   
    print('\nWEAPONS')
    print(f'wooden bow ----------> sticks {heroInventory.sticks}/10 --- fiber {heroInventory.fiber}/10')
    print(f'smiths hammer -------> logs {heroInventory.logs}/1 ------ fiber {heroInventory.fiber}/10 --- iron {heroInventory.iron}/2 ---- oil {heroInventory.oil}/1')
    print(f'steel hammer --------> logs {heroInventory.logs}/1 ------ fiber {heroInventory.fiber}/10 --- steel {heroInventory.steel}/2 --- oil {heroInventory.oil}/1')
    print(f'hunters bow ---------> logs {heroInventory.logs}/5 ------ fiber {heroInventory.fiber}/25 --- steel {heroInventory.steel}/2 --- oil {heroInventory.oil}/1')
    print(f'fishing pole --------> sticks {heroInventory.sticks}/10 --- fiber {heroInventory.fiber}/10')

    print('\nARMOR')
    print(f'leather armor -------> pelt {heroInventory.pelt}/1 ---- fiber {heroInventory.fiber}/15')
    print(f'iron armor ----------> pelt {heroInventory.pelt}/2 --- fiber {heroInventory.fiber}/20 --- iron {heroInventory.iron}/2 ---- oil {heroInventory.oil}/1')
    print(f'steel armor ---------> pelt {heroInventory.pelt}/4--- fiber {heroInventory.fiber}/25 --- steel {heroInventory.steel}/2--- oil {heroInventory.oil}/3')
    
    print('\n(X) Back')
    a = input('-->')
    while a.lower() not in craftables:
        a = input('-->')
    if a.lower() == 'wooden arrow':
        action_time = 60           #Unique                                                                 
        reduced_time = action_time
        action_amount = 10           #Unique                                                                     
        action_name = 'wooden arrow'       #Unique 
        action_type = 'crafting'   #Unique, for dialouge 
        action_exp = 5              #Unique
        print(f'Crafting {action_amount} {action_name}s will take 1 hour.')
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'y':
            for i in wooden_arrow_craft.keys(): #unique
                if heroInventory.raw_material[i] < wooden_arrow_craft[i]:   #unique, checks if you have the raw material
                    print(f'You dont have enough {i}.')
                    useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            heroInventory.moveSticks(-1 * wooden_arrow_craft['sticks'])   #unique
            heroInventory.moveFiber(-1 * wooden_arrow_craft['fiber'])     #unique
            heroInventory.moveWoodenArrows(action_amount)         #unique
            
            print(f"\n+{action_amount} {action_name}s")   
            print(f"+{action_exp} EXP")                 
            player.addExp(action_exp)   #gives player exp
            clock1.addTime(reduced_time) #add time
            getHungry(player, reduced_time, action_type, fire)  #take hunger away from player
            checkHunger(player, reduced_time, action_type, fire)    #see if they have no hunger, then they take damag
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if a.lower() == 'iron arrow':
        if skills.getCraftingSkill() < 5:   #=
                print('\nCrafting skill too low')
                print(f'Crafting Skill {skills.getCraftingSkill()}/5')
                input('press enter to continue')
                useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        
        action_time = 90            #Unique                                                                 
        action_amount = 10           #Unique                                                                     
        reduced_time = action_time
        action_name = 'iron arrow'       #Unique 
        action_type = 'crafting'   #Unique, for dialouge 
        action_exp = 5              #Unique
        print(f'Crafting {action_amount} {action_name}s will take 1.5 hours.')
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'y':
            for i in iron_arrow_craft.keys(): #unique
                if heroInventory.raw_material[i] < iron_arrow_craft[i]:   #unique, checks if you have the raw material
                    print(f'You dont have enough {i}.')
                    useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            heroInventory.moveIron(-1 * iron_arrow_craft['iron'])   #unique
            heroInventory.moveFiber(-1 * iron_arrow_craft['fiber'])     #unique
            heroInventory.moveSticks(-1 * iron_arrow_craft['sticks'])   #unique
            heroInventory.moveOil(-1 * iron_arrow_craft['oil'])     #unique
            
            
            heroInventory.moveIronArrows(action_amount)         #unique
            
            print(f"\n+{action_amount} {action_name}s")   
            print(f"+{action_exp} EXP")                 
            player.addExp(action_exp)   #gives player exp
            clock1.addTime(reduced_time) #add time
            getHungry(player, reduced_time, action_type, fire)  #take hunger away from player
            checkHunger(player, reduced_time, action_type, fire)    #see if they have no hunger, then they take damag
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if a.lower() == 'steel arrow':
        if skills.getCraftingSkill() < 10:   #=
                print('\nCrafting skill too low')
                print(f'Crafting Skill {skills.getCraftingSkill()}/10')
                input('press enter to continue')
                useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        
        
        action_time = 120            #Unique                                                                 
        reduced_time = action_time
        action_amount = 10           #Unique                                                                     
        action_name = 'steel arrow'       #Unique 
        action_type = 'crafting'   #Unique, for dialouge 
        action_exp = 5              #Unique
        print(f'Crafting {action_amount} {action_name}s will take 2 hours.')
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'y':
            for i in steel_arrow_craft.keys(): #unique
                if heroInventory.raw_material[i] < steel_arrow_craft[i]:   #unique, checks if you have the raw material
                    print(f'You dont have enough {i}.')
                    useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            heroInventory.moveSteel(-1 * steel_arrow_craft['steel'])   #unique
            heroInventory.moveFiber(-1 * steel_arrow_craft['fiber'])     #unique
            heroInventory.moveSticks(-1 * steel_arrow_craft['sticks'])   #unique
            heroInventory.moveOil(-1 * steel_arrow_craft['oil'])     #unique
            
            
            heroInventory.moveSteelArrows(action_amount)         #unique
            
            print(f"\n+{action_amount} {action_name}s")   
            print(f"+{action_exp} EXP")                 
            player.addExp(action_exp)   #gives player exp
            clock1.addTime(reduced_time) #add time
            getHungry(player, reduced_time, action_type, fire)  #take hunger away from player
            checkHunger(player, reduced_time, action_type, fire)    #see if they have no hunger, then they take damag
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if a.lower() == 'flaming arrow':
        if skills.getCraftingSkill() < 15:   #=
                print('\nCrafting skill too low')
                print(f'Crafting Skill {skills.getCraftingSkill()}/15')
                input('press enter to continue')
                useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        
        action_time = 150            #Unique                                                                 
        reduced_time = action_time
        action_amount = 10           #Unique                                                                     
        action_name = 'flaming arrow'       #Unique 
        action_type = 'crafting'   #Unique, for dialouge 
        action_exp = 5              #Unique
        print(f'Crafting {action_amount} {action_name}s will take 2.5 hours.')
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'y':
            for i in flaming_arrow_craft.keys(): #unique
                if heroInventory.raw_material[i] < flaming_arrow_craft[i]:   #unique, checks if you have the raw material
                    print(f'You dont have enough {i}.')
                    useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            heroInventory.moveSteel(-1 * flaming_arrow_craft['steel'])   #unique
            heroInventory.moveIron(-1 * flaming_arrow_craft['iron'])   #unique
            heroInventory.moveFiber(-1 * flaming_arrow_craft['fiber'])     #unique
            heroInventory.moveSticks(-1 * flaming_arrow_craft['sticks'])   #unique
            heroInventory.moveOil(-1 * flaming_arrow_craft['oil'])     #unique
            
            
            heroInventory.moveFlamingArrows(action_amount
            )         #unique
            
            print(f"\n+{action_amount} {action_name}s")   
            print(f"+{action_exp} EXP")                 
            player.addExp(action_exp)   #gives player exp
            clock1.addTime(reduced_time) #add time
            getHungry(player, reduced_time, action_type, fire)  #take hunger away from player
            checkHunger(player, reduced_time, action_type, fire)    #see if they have no hunger, then they take damag
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if a.lower() == 'wooden bow':
        action_time = 120            #Unique                                                                 
        reduced_time = action_time
        action_amount = 1           #Unique                                                                     
        action_name = 'wooden bow'       #Unique 
        action_type = 'crafting'   #Unique, for dialouge 
        action_exp = 5              #Unique
        print(f'Crafting a {action_name} will take 2 hours.')
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'y':
            for i in wooden_bow_craft.keys(): #unique
                if heroInventory.raw_material[i] < wooden_bow_craft[i]:   #unique, checks if you have the raw material
                    print(f'You dont have enough {i}.')
                    useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            heroInventory.moveFiber(-1 * wooden_bow_craft['fiber'])     #unique
            heroInventory.moveSticks(-1 * wooden_bow_craft['sticks'])   #unique
            
            
            heroInventory.moveWoodenBow(1)         #unique
            
            print(f"\n+{action_amount} {action_name}")   
            print(f"+{action_exp} EXP")                 
            player.addExp(action_exp)   #gives player exp
            clock1.addTime(reduced_time) #add time
            getHungry(player, reduced_time, action_type, fire)  #take hunger away from player
            checkHunger(player, reduced_time, action_type, fire)    #see if they have no hunger, then they take damag
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if a.lower() == 'hunters bow':
        if skills.getCraftingSkill() < 15:   #=
                print('\nCrafting skill too low')
                print(f'Crafting Skill {skills.getCraftingSkill()}/15')
                input('press enter to continue')
                useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        action_time = 240            #Unique                                                                 
        reduced_time = action_time
        action_amount = 1           #Unique                                                                     
        action_name = 'hunters bow'       #Unique 
        action_type = 'crafting'   #Unique, for dialouge 
        action_exp = 5              #Unique
        print(f'Crafting a {action_name} will take 4 hours.')
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'y':
            for i in hunters_bow_craft.keys(): #unique
                if heroInventory.raw_material[i] < hunters_bow_craft[i]:   #unique, checks if you have the raw material
                    print(f'You dont have enough {i}.')
                    useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            heroInventory.moveFiber(-1 * hunters_bow_craft['fiber'])     #unique
            heroInventory.moveLogs(-1 * hunters_bow_craft['logs'])   #unique
            heroInventory.moveOil(-1 * hunters_bow_craft['oil'])   #unique
            heroInventory.moveSteel(-1 * hunters_bow_craft['steel'])   #unique
            
            
            heroInventory.moveHuntersBow(1)         #unique
            
            print(f"\n+{action_amount} {action_name}")   
            print(f"+{action_exp} EXP")                 
            player.addExp(action_exp)   #gives player exp
            clock1.addTime(reduced_time) #add time
            getHungry(player, reduced_time, action_type, fire)  #take hunger away from player
            checkHunger(player, reduced_time, action_type, fire)    #see if they have no hunger, then they take damag
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if a.lower() == 'smiths hammer':
        action_time = 120            #Unique                                                                 
        reduced_time = action_time
        action_amount = 1           #Unique                                                                     
        action_name = 'smiths hammer'       #Unique 
        action_type = 'crafting'   #Unique, for dialouge 
        action_exp = 5              #Unique
        print(f'Crafting a {action_name} will take 2 hours.')
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'y':
            for i in smiths_hammer_craft.keys(): #unique
                if heroInventory.raw_material[i] < smiths_hammer_craft[i]:   #unique, checks if you have the raw material
                    print(f'You dont have enough {i}.')
                    useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            heroInventory.moveFiber(-1 * smiths_hammer_craft['fiber'])     #unique
            heroInventory.moveLogs(-1 * smiths_hammer_craft['logs'])   #unique
            heroInventory.moveOil(-1 * smiths_hammer_craft['oil'])   #unique
            heroInventory.moveIron(-1 * smiths_hammer_craft['iron'])   #unique
            
            
            heroInventory.moveSmithsHammer(1)         #unique
            
            print(f"\n+{action_amount} {action_name}")   
            print(f"+{action_exp} EXP")                 
            player.addExp(action_exp)   #gives player exp
            clock1.addTime(reduced_time) #add time
            getHungry(player, reduced_time, action_type, fire)  #take hunger away from player
            checkHunger(player, reduced_time, action_type, fire)    #see if they have no hunger, then they take damag
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if a.lower() == 'steel hammer':
        if skills.getCraftingSkill() < 15:   #=
                print('\nCrafting skill too low')
                print(f'Crafting Skill {skills.getCraftingSkill()}/10')
                input('press enter to continue')
                useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        
        action_time = 240            #Unique                                                                 
        reduced_time = action_time
        action_amount = 1           #Unique                                                                     
        action_name = 'steel hammer'       #Unique 
        action_type = 'crafting'   #Unique, for dialouge 
        action_exp = 5              #Unique
        print(f'Crafting a {action_name} will take 4 hours.')
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'y':
            for i in steel_hammer_craft.keys(): #unique
                if heroInventory.raw_material[i] < steel_hammer_craft[i]:   #unique, checks if you have the raw material
                    print(f'You dont have enough {i}.')
                    useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            heroInventory.moveFiber(-1 * steel_hammer_craft['fiber'])     #unique
            heroInventory.moveLogs(-1 * steel_hammer_craft['logs'])   #unique
            heroInventory.moveOil(-1 * smiths_hammer_craft['oil'])   #unique
            heroInventory.moveSteel(-1 * steel_hammer_craft['steel'])   #unique
            
            
            heroInventory.moveSteelHammer(1)         #unique
            
            print(f"\n+{action_amount} {action_name}")   
            print(f"+{action_exp} EXP")                 
            player.addExp(action_exp)   #gives player exp
            clock1.addTime(reduced_time) #add time
            getHungry(player, reduced_time, action_type, fire)  #take hunger away from player
            checkHunger(player, reduced_time, action_type, fire)    #see if they have no hunger, then they take damag
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if a.lower() == 'leather armor':
        action_time = 120            #Unique                                                                 
        reduced_time = action_time
        action_amount = 1           #Unique                                                                     
        action_name = 'leather armor'       #Unique 
        action_type = 'crafting'   #Unique, for dialouge 
        action_exp = 5              #Unique
        print(f'Crafting {action_name} will take 2 hours.')
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'y':
            for i in leather_armor_craft.keys(): #unique
                if heroInventory.raw_material[i] < leather_armor_craft[i]:   #unique, checks if you have the raw material
                    print(f'You dont have enough {i}.')
                    useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            heroInventory.moveFiber(-1 * leather_armor_craft['fiber'])     #unique
            heroInventory.movePelt(-1 * leather_armor_craft['pelt'])   #unique
            heroInventory.moveLeatherArmor(1)         #unique
            
            if 'Craft leather armor' in heroInventory.currentQuests:
                print('\nQuest Complete: Craft leather armor')
                heroInventory.currentQuests.remove('Craft leather armor')
                heroInventory.completedQuests.append('Craft leather armor')
                print('+5 EXP')
                print('+10 gold')
                print('+1 berry stew')
                heroInventory.moveBerryStew(1)
                input('press enter to continue')
                player.addExp(5)
                heroInventory.moveGold(10)
            
            print(f"\n+{action_amount} {action_name}")   
            print(f"+{action_exp} EXP")                 
            player.addExp(action_exp)   #gives player exp
            clock1.addTime(reduced_time) #add time
            getHungry(player, reduced_time, action_type, fire)  #take hunger away from player
            checkHunger(player, reduced_time, action_type, fire)    #see if they have no hunger, then they take damag
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if a.lower() == 'iron armor':
        if skills.getCraftingSkill() < 10:   #=
                print('\nCrafting skill too low')
                print(f'Crafting Skill {skills.getCraftingSkill()}/10')
                input('press enter to continue')
                useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        action_time = 240            #Unique                                                                 
        reduced_time = action_time
        action_amount = 1           #Unique                                                                     
        action_name = 'iron armor'       #Unique 
        action_type = 'crafting'   #Unique, for dialouge 
        action_exp = 5              #Unique
        print(f'Crafting {action_name} will take 4 hours.')
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'y':
            for i in iron_armor_craft.keys(): #unique
                if heroInventory.raw_material[i] < iron_armor_craft[i]:   #unique, checks if you have the raw material
                    print(f'You dont have enough {i}.')
                    useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            heroInventory.moveFiber(-1 * iron_armor_craft['fiber'])     #unique
            heroInventory.movePelt(-1 * iron_armor_craft['pelt'])   #unique
            heroInventory.moveOil(-1 * iron_armor_craft['oil'])   #unique
            heroInventory.moveIron(-1 * iron_armor_craft['iron'])   #unique  
            heroInventory.moveIronArmor(1)         #unique            
            print(f"\n+{action_amount} {action_name}")   
            print(f"+{action_exp} EXP")                 
            player.addExp(action_exp)   #gives player exp
            clock1.addTime(reduced_time) #add time
            getHungry(player, reduced_time, action_type, fire)  #take hunger away from player
            checkHunger(player, reduced_time, action_type, fire)    #see if they have no hunger, then they take damag
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if a.lower() == 'steel armor':
        if skills.getCraftingSkill() < 15:   #=
                print('\nCrafting skill too low')
                print(f'Crafting Skill {skills.getCraftingSkill()}/10')
                input('press enter to continue')
                useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        
        action_time = 360            #Unique                                                                 
        reduced_time = action_time
        action_amount = 1           #Unique                                                                     
        action_name = 'steel armor'       #Unique 
        action_type = 'crafting'   #Unique, for dialouge 
        action_exp = 5              #Unique
        print(f'Crafting {action_name} will take 6 hours.')
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'y':
            for i in steel_armor_craft.keys(): #unique
                if heroInventory.raw_material[i] < steel_armor_craft[i]:   #unique, checks if you have the raw material
                    print(f'You dont have enough {i}.')
                    useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            heroInventory.moveFiber(-1 * steel_armor_craft['fiber'])     #unique
            heroInventory.movePelt(-1 * steel_armor_craft['pelt'])   #unique
            heroInventory.moveOil(-1 * steel_armor_craft['oil'])   #unique
            heroInventory.moveSteel(-1 * steel_armor_craft['steel'])   #unique
            heroInventory.moveSteelArmor(1)         #unique 
            print(f"\n+{action_amount} {action_name}")   
            print(f"+{action_exp} EXP")                 
            player.addExp(action_exp)   #gives player exp
            clock1.addTime(reduced_time) #add time
            getHungry(player, reduced_time, action_type, fire)  #take hunger away from player
            checkHunger(player, reduced_time, action_type, fire)    #see if they have no hunger, then they take damag
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if a.lower() == 'fishing pole':
        action_time = 60            #Unique                                                                 
        reduced_time = action_time
        action_amount = 1           #Unique                                                                     
        action_name = 'fishing pole'       #Unique 
        action_type = 'crafting'   #Unique, for dialouge 
        action_exp = 5              #Unique
        print(f'Crafting a {action_name} will take 1 hours.')
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'y':
            for i in fishing_pole_craft.keys(): #unique
                if heroInventory.raw_material[i] < fishing_pole_craft[i]:   #unique, checks if you have the raw material
                    print(f'You dont have enough {i}.')
                    useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            heroInventory.moveFiber(-1 * fishing_pole_craft['fiber'])     #unique
            heroInventory.moveSticks(-1 * fishing_pole_craft['sticks'])   #unique 
            heroInventory.moveFishingPole(1)         #unique           
            print(f"\n+{action_amount} {action_name}")   
            print(f"+{action_exp} EXP")                 
            player.addExp(action_exp)   #gives player exp
            clock1.addTime(reduced_time) #add time
            getHungry(player, reduced_time, action_type, fire)  #take hunger away from player
            checkHunger(player, reduced_time, action_type, fire)    #see if they have no hunger, then they take damag
            useWorkbench(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'x':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    print(f"\nWhat will you brew:")
    print(f'Alchemy Level: {player.getAlchemy()}')
    print(f"Brewing Fuel: {fire.getBrewingFuel()}\n")
    print(f"(A) Add Fuel")
    print(f"(H) Healing Potion -------> 5 Fuel")
    print(f"(F) Fire Resist Potion ---> 10 Fuel")
    print(f"(R) Frost Resist Potion --> 10 Fuel")
    print(f"(P) Poisen Resist Potion--> 10 Fuel")
    print(f"(X) Back")
    a = input('-->')
    while a.lower() not in ['a', 'h', 'f', 'r', 'p', 'x']:
        a = input('-->')

    if a.lower() == 'a':  #add fuel
        addBrewingFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'h': #brew healing potion
        action_time = 60            #Unique                                                                 
        action_amount = 1           #Unique                                                                     
        action_name = 'healing potion'       #Unique 
        action_type = 'brewing'   #Unique, for dialouge 
        action_exp = 4              #Unique
        print(f"Brewing a health potion will take 1 hour.")
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'y':
            if fire.getBrewingFuel() < 5:  #Balance, requires 
                print('\nYou need to add fuel')
                print(f"Brewing Fuel: {fire.getBrewingFuel()} / 5 ")
                input('press enter to continue')
                brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            if heroInventory.crimsonPetal > 0:
                fire.addBrewingFuel(-5)
                heroInventory.moveCrimsonPetal(-1)  #Unique 
                if player.getAlchemy() == 0:
                    print('\nYour alchemy skills are too low, you failed at brewing healing potion.')
                    input('press enter to continue')
                    brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
                elif player.getAlchemy() > 0 and player.getAlchemy() <= 10:
                    heroInventory.moveWeakHealingPotion(1)
                    print(f'\n+1 Weaking Healing Potion')

                elif player.getAlchemy() > 10 and player.getAlchemy() <= 20:
                    heroInventory.moveMediumHealingPotion(1)
                    print(f'\n+1 Medium Healing Potion')

                elif player.getAlchemy() > 20 :
                    heroInventory.moveStrongHealingPotion(1)
                    print(f'\n+1 Strong Healing Potion')

                print(f'+{action_exp} EXP')
                input('press enter to continue')
                if 'Brew a healing potion' in heroInventory.currentQuests:
                    print('\nQuest Complete: Brew a healing potion')
                    heroInventory.currentQuests.remove('Brew a healing potion')
                    heroInventory.completedQuests.append('Brew a healing potion')
                    print('+10 EXP')
                    player.addExp(10)
                    heroInventory.moveGold(10)
                    print('+10 Gold')
                    input('press enter to continue')
                player.addExp(action_exp)   #gives player exp
                clock1.addTime(action_time) #add time
                getHungry(player, action_time, action_type, fire)  #take hunger away from player
                checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
                brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire) #Unique 
            else:
                print("You dont have any crimson petals")
                input('press enter to continue')
                brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'n':
            brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'f': #brew fire resist
        action_time = 60            #Unique                                                                 
        action_amount = 1           #Unique                                                                     
        action_name = 'fire resist potion'       #Unique 
        action_type = 'brewing'   #Unique, for dialouge 
        action_exp = 4              #Unique
        print(f"Brewing a {action_name} will take 1 hours.")
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'y':
            if fire.getBrewingFuel() < 10:  #Balance, requires 
                print('\nYou need to add fuel')
                print(f"Brewing Fuel: {fire.getBrewingFuel()} / 10 ")
                input('press enter to continue')
                brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            if heroInventory.dragonLilly > 0:
                fire.addBrewingFuel(-5)
                heroInventory.moveDragonLilly(-1)  #Unique 
                print(f"+1 Fire Resist Potion")  #Unique 
                print(f'+{action_exp} EXP')
                heroInventory.moveFireResistPotion(1)
                player.addExp(action_exp)   #gives player exp
                clock1.addTime(action_time) #add time
                getHungry(player, action_time, action_type, fire)  #take hunger away from player
                checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
                input('press enter to continue')
                brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire) #Unique 
            else:
                print("You dont have any dragon lilly.")
                input('press enter to continue')
                brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'n':
            brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'r': #brew frost resist
        action_time = 60            #Unique                                                                 
        action_amount = 1           #Unique                                                                     
        action_name = 'frost resist potion'       #Unique 
        action_type = 'brewing'   #Unique, for dialouge 
        action_exp = 4              #Unique
        print(f"Brewing a {action_name} will take 1 hour.")
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'y':
            if fire.getBrewingFuel() < 10:  #Balance, requires 
                print('\nYou need to add fuel')
                print(f"Brewing Fuel: {fire.getBrewingFuel()} / 10")
                input('press enter to continue')
                brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            if heroInventory.coldSnap > 0:
                fire.addBrewingFuel(-5)
                heroInventory.moveColdSnap(-1)  #Unique 
                print(f"+1 Frost Resist Potion")  #Unique 
                print(f'+{action_exp} EXP')
                heroInventory.moveFrostResistPotion(1)
                player.addExp(action_exp)   #gives player exp
                clock1.addTime(action_time) #add time
                getHungry(player, action_time, action_type, fire)  #take hunger away from player
                checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage 
                input('press enter to continue')
                brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire) #Unique 
            else:
                print("You dont have any cold snap.")
                input('press enter to continue')
                brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'n':
            brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'p': #brew poisen resist
        action_time = 60            #Unique                                                                 
        action_amount = 1           #Unique                                                                     
        action_name = 'poisen resist potion'       #Unique 
        action_type = 'brewing'   #Unique, for dialouge 
        action_exp = 4              #Unique
        print(f"Brewing a {action_name} will take 1 hour.")
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'y':
            if fire.getBrewingFuel() < 10:  #Balance, requires 
                print('\nYou need to add fuel')
                print(f"Brewing Fuel: {fire.getBrewingFuel()} / 10 ")
                input('press enter to continue')
                brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            if heroInventory.poisenIvy > 0:
                fire.addBrewingFuel(-5)
                heroInventory.movePoisenIvy(-1)  #Unique 
                print(f"+1 Poisen Resist Potion")  #Unique 
                print(f'+{action_exp} EXP')
                heroInventory.movePoisenResistPotion(1)
                player.addExp(action_exp)   #gives player exp
                clock1.addTime(action_time) #add time
                getHungry(player, action_time, action_type, fire)  #take hunger away from player
                checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
                input('press enter to continue')
                brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire) #Unique 
            else:
                print("You dont have any poisen ivy snap.")
                input('press enter to continue')
                brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'n':
            brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'x': #go back
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def gatherMeal(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if clock1.mealCounter == 1:
        print(f'\nMeal is not ready until tomorrow.')
        input('press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif clock1.mealCounter == 0:
        print(f"\n+1 meal")                 
        heroInventory.moveMeal(1)    #Unique   
        clock1.moveMealCounter(1)
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)     
def gatherHerbs(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    #'gather dragon lilly', 'gather cold snap', 'gather poisen ivy', 'gather crimson petal'
    print(f'\nTimers:')
    print(f'Dragon Lilly: {clock1.dragonLillyCounter}')
    print(f'Cold Snap: {clock1.coldSnapCounter}')
    print(f'Poisen Ivy: {clock1.poisenIvyCounter}')
    print(f'Crimson Petal: {clock1.crimsonPetalCounter}')
    
    print(f'\nAvailable Herbs to Gather:')
    available_options = ['x']
    if clock1.dragonLillyCounter == 0:
        print(f'(D) Dragon Lilly')
        available_options.append('d')
    if clock1.coldSnapCounter == 0:
        print(f'(C) Cold Snap')
        available_options.append('c')
    if clock1.poisenIvyCounter == 0:
        print(f'(P) Poisen Ivy')
        available_options.append('p')
    if clock1.crimsonPetalCounter == 0:
        print(f'(R) Crimson Petal')
        available_options.append('r')
    print(f'\n(X) Back\n')    

    a = input('-->')
    while a.lower() not in available_options:
        a = input('-->')
    if a.lower() == 'd':
        gatherDragonLilly(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        gatherHerbs(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'c':
        gatherColdSnap(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        gatherHerbs(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'p':
        gatherPoisenIvy(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        gatherHerbs(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'r':
        gatherCrimsonPetal(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        gatherHerbs(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'x':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def gatherDragonLilly(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    action_time = 60           #Unique                                                                 
    action_amount = 1           #Unique                                                                     
    action_name = 'dragon lilly'      #Unique 
    action_type = 'gathering'
    action_exp = 1              #Unique
    print(f'Gathering {action_name} will take 1 hour.')
    print('Continue? (y/n)')
    
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        pass
    elif a.lower() == 'y':
        print(f"\n+{action_amount} {action_name}")     
        print(f"+{action_exp} EXP")            
        player.addExp(action_exp)           #gives player exp
        clock1.addTime(action_time)         #add time to the clock
        getHungry(player, action_time, action_type, fire)      #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        heroInventory.moveDragonLilly(action_amount)    #Unique
        clock1.moveDragonLillyCounter(2)
def gatherColdSnap(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    action_time = 60           #Unique                                                                 
    action_amount = 1           #Unique                                                                     
    action_name = 'cold snap'      #Unique 
    action_type = 'gathering'
    action_exp = 1              #Unique
    print(f'Gathering {action_amount} {action_name} will take 1 hour.')
    print('Continue? (y/n)')
    
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        pass
    elif a.lower() == 'y':
        print(f"\n+{action_amount} {action_name}")     
        print(f"+{action_exp} EXP")            
        player.addExp(action_exp)           #gives player exp
        clock1.addTime(action_time)         #add time to the clock
        getHungry(player, action_time, action_type, fire)      #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        heroInventory.moveColdSnap(action_amount)    #Unique
        clock1.moveColdSnapCounter(2)
def gatherPoisenIvy(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    action_time = 60           #Unique                                                                 
    action_amount = 1           #Unique                                                                     
    action_name = 'poisen ivy'      #Unique 
    action_type = 'gathering'
    action_exp = 1              #Unique
    print(f'Gathering {action_amount} {action_name} will take 1 hour.')
    print('Continue? (y/n)')
    
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        pass
    elif a.lower() == 'y':
        print(f"\n+{action_amount} {action_name}")     
        print(f"+{action_exp} EXP")            
        player.addExp(action_exp)           #gives player exp
        clock1.addTime(action_time)         #add time to the clock
        getHungry(player, action_time, action_type, fire)      #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        heroInventory.movePoisenIvy(action_amount)    #Unique
        clock1.movePoisenIvyCounter(2)
def gatherCrimsonPetal(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    action_time = 60           #Unique                                                                 
    action_amount = 1           #Unique                                                                     
    action_name = 'crimson petal'      #Unique 
    action_type = 'gathering'
    action_exp = 1              #Unique
    print(f'Gathering {action_amount} {action_name} will take 1 hour.')
    print('Continue? (y/n)')
    
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        pass
    elif a.lower() == 'y':
        print(f"\n+{action_amount} {action_name}")     
        print(f"+{action_exp} EXP")            
        player.addExp(action_exp)           #gives player exp
        clock1.addTime(action_time)         #add time to the clock
        getHungry(player, action_time, action_type, fire)      #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        heroInventory.moveCrimsonPetal(action_amount)    #Unique
        clock1.moveCrimsonPetalCounter(2)
def travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if travels.travelTimes == True:
        action_time = 10 #STATIC TRAVEL TIME BETWEEN ZONES
        action_type = 'traveling'
        clock1.addTime(action_time)         #add time to the clock
        getHungry(player, action_time, action_type, fire)      #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage


#SURVIVAL ACTIONS
def addBrewingFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    print(f"\nChoose fuel to add.")
    print(f"Brewing Fuel: {fire.getBrewingFuel()}\n")
    print(f"(S) Sticks:{heroInventory.sticks}")
    print(f"(L) Logs:{heroInventory.logs}")
    print("(X) Back\n")
    a = input('-->')
    
    if a.lower() == 's':
        if heroInventory.sticks <= 0:
            print("\nYou have no sticks")
            addBrewingFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        else:
            heroInventory.moveSticks(-1)
            fire.addBrewingFuel(1)
            addBrewingFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire)   
    elif a.lower() == 'l':
        if heroInventory.logs <= 0:
           print("\nYou have no logs")
           addBrewingFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        else:
            heroInventory.moveLogs(-1)
            fire.addBrewingFuel(4)
            addBrewingFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'x':
        brewPotions(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    else:
        addBrewingFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire)
def addForgeFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    print(f"\nChoose fuel to add.")
    print(f"Forge Fuel: {fire.getForgeFuel()}\n")
    print(f"(S) Sticks:{heroInventory.sticks}")
    print(f"(L) Logs:{heroInventory.logs}")
    print("(X) Back\n")
    a = input('-->')
    
    if a.lower() == 's':
        if heroInventory.sticks <= 0:
            print("\nYou have no sticks")
            addForgeFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        else:
            heroInventory.moveSticks(-1)
            fire.addForgeFuel(1)
            addForgeFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire)       
    elif a.lower() == 'l':
        if heroInventory.logs <= 0:
           print("\nYou have no logs")
           addForgeFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        else:
            heroInventory.moveLogs(-1)
            fire.addForgeFuel(4)
            addForgeFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif a.lower() == 'x':
        smeltOre(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    else:
        addForgeFuel(player, clock1, heroInventory, stock, actions, travels, skills, fire)
def sleep(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    heal_bonus = 0
    addedTime = 480  #sleep for 480 minutes (8 hours)
    action = 'sleeping'

    #First we heal the player if they had fire and hunger in the morning
    fire.addFuel(-4)  #balance :fire loses 5 fuel per day
    checkFire(player, clock1, actions, travels, heroInventory, stock, skills, fire) #fire just needs to be lit, doesnt matter how much fuel is in it
    
    if fire.lit == True:
        heal_bonus += 1
        print(f"The fire burned all night.")
        print(f"Fire healing bonus: 50 HP")
    else:
        print(f"\nYou were freezing in the night.")
        print(f"Fire healing bonus: 0 HP")

    time_passed = math.ceil(addedTime * -.07)  #lose 0.07 hunger per minute. Balance how much hunger you would lose in the night (33 currently). This equation should be the same as the one in getHungry()
    hunger_after_sleeping = player.getHunger() + time_passed  #(hunger - 33) currently, times_passed is negative, makes the player lose life based on how much hunger they slept with, if it ran out during the night
    damage = 0
    if hunger_after_sleeping < 0:  #then they take damage based on the difference. ex: if they had 10 hunger and they lose 33 from sleeping, they damage damage for the -23 hunger they are left with
        damage += hunger_after_sleeping
        print(f"You lost {-1*hunger_after_sleeping} HP for sleeping hungry.")
        ("Hunger Bonus: 0 HP")
    else: #this means the player didnt get hungry in the night
        heal_bonus += 1
        print(f"You slept through the night without getting hungry")
        print("Hunger Bonus: 50 HP")

    player.addHunger(math.ceil(addedTime * -.07))
    heal_amount = 50 * heal_bonus  #balance this heal amount
    player.setHP(player.getHP() + damage)   # player takes damage for each hunger after sleeping
    player.setHP(player.getHP() + heal_amount)  #heal the player
    checkDeath(player, clock1, actions, travels, heroInventory, stock, skills, fire)  #see if that killed you
    net_HP = heal_amount + damage
    print(f"\nNet HP: {net_HP}")
    
    clock1.setTime(clock1.getStart())  #set time to next day
    clock1.addDay()
    checkDay(player, clock1, actions, travels, heroInventory, stock, skills, fire)  #trigger that day's unique events
    input('press enter to continue')
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def cook(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    print(f"\nWhat will you cook:")
    print(f"Cooking Fuel: {fire.getCookingFuel()}")
    print(f"\n(A) Add Fuel")
    print(f"(S) Berry Stew ---> 1 Fuel")
    print(f"(F) Cooked fish --> 4 Fuel")
    print(f"(D) Cooked Deer --> 10 Fuel")
    print(f"\n(X) Back\n")
    a = input('-->')
    while a.lower() not in ['a','f','s','d','x']:
        a = input('-->')
        
    #Cook fish
    if a.lower() == 'f':
        action_time = 60            #Unique                                                                 
        action_amount = 1           #Unique                                                                     
        action_name = 'cook'       #Unique 
        action_type = 'cooking'   #Unique, for dialouge 
        action_exp = 2              #Unique
        print(f"Cooking a fish will take 1 hour.")
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y','n']:
            a = input('-->')
        if a.lower() == 'y':
            if fire.getCookingFuel() < 4:  #Balance, requires 4 fuel to cook a fish
                print("You need to add fuel")
                cook(player,  clock1, heroInventory, stock, actions, travels, skills, fire)
            if heroInventory.getFish() > 0:
                fire.addCookingFuel(-4)
                heroInventory.moveFish(-1)  #Unique 
                heroInventory.moveCookedFish(1)  #Unique 
                player.addExp(action_exp)   #gives player exp
                
                if 'Cook a fish.' in heroInventory.currentQuests:
                    print('\nQuest Completed: Cook a fish.')
                    print('+10 EXP')
                    print('+15 gold')
                    heroInventory.moveGold(15)
                    player.addExp(10)
                    heroInventory.currentQuests.remove('Cook a fish.')
                    heroInventory.completedQuests.append('Cook a fish.')

                print(f"\n+1 Cooked Fish")  #Unique 
                print(f'+{action_exp} EXP')
                clock1.addTime(action_time) #add time
                getHungry(player, action_time, action_type, fire)  #take hunger away from player
                checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
                
                cook(player,  clock1, heroInventory, stock, actions, travels, skills, fire) #Unique 
            else:
                print("You dont have any fish")
                cook(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'n':
            cook(player, clock1, heroInventory, stock, actions, travels, skills, fire)
  
    #Cook berry stew
    elif a.lower() == 's':
        action_time = 30            #Unique                                                                 
        action_amount = 1           #Unique                                                                     
        action_name = 'cook'       #Unique 
        action_type = 'cooking'   #Unique, for dialouge 
        action_exp = 1              #Unique
        print(f"Cooking berries will take {action_time} minutes.")
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y','n']:
            a = input('-->')
        if a.lower() == 'y':
            if fire.getCookingFuel() < 1:
                print("You need to add fuel")
                cook(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            if heroInventory.getBerries() > 0:
                fire.addCookingFuel(-1)
                heroInventory.moveBerries(-1)  #Unique 
                heroInventory.moveBerryStew(1)  #Unique 
                print(f"\n+1 Berry Stew")  #Unique 
                print(f'+{action_exp} EXP')
                player.addExp(action_exp)   #gives player exp
                clock1.addTime(action_time) #add time
                getHungry(player, action_time, action_type, fire)  #take hunger away from player
                checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
                
                cook(player, clock1, heroInventory, stock, actions, travels, skills, fire)  #Unique 
            else:
                print("You dont have any berries")  #Unique 
                cook(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'n':
            cook(player, clock1, heroInventory, stock, actions, travels, skills, fire)

    #Cook deer meat
    elif a.lower() == 'd':
        action_time = 120           #Unique                                                                 
        action_amount = 1           #Unique                                                                     
        action_name = 'cook'       #Unique 
        action_type = 'cooking'   #Unique, for dialouge 
        action_exp = 3              #Unique
        print(f"Cooking deer meat will take 2 hours.")
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y','n']:
            a = input('-->')
        if a.lower() == 'y':
            if fire.getCookingFuel() < 10:
                print("You need to add fuel")
                cook(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            if heroInventory.getDeerMeat() > 0:
                fire.addCookingFuel(-10)
                heroInventory.moveDeerMeat(-1)  #Unique 
                heroInventory.moveCookedDeer(1)  #Unique 
                print(f"\n+1 Cooked Deer")  #Unique 
                player.addExp(action_exp)   #gives player exp
                print(f'+{action_exp} EXP')
                clock1.addTime(action_time) #add time
                getHungry(player, action_time, action_type, fire)  #take hunger away from player
                checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
                
                cook(player, clock1, heroInventory, stock, actions, travels, skills, fire)  #Unique 
            else:
                print("You dont have any deer meat")  #Unique 
                cook(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif a.lower() == 'no':
            cook(player, clock1, heroInventory, stock, actions, travels, skills, fire)

    #Go back
    elif a.lower() == 'x':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    #Add fuel
    elif a.lower() == 'a':
        addCookingFuel(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def addCookingFuel(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    print(f"Choose fuel to add.")
    print(f"Cooking Fuel: {fire.getCookingFuel()}")
    print(f"(S) Sticks:{heroInventory.sticks}")
    print(f"(L) Logs:{heroInventory.logs}")
    print("(X) Back")
    a = input('-->')
    
    if a.lower() == 's':
        if heroInventory.sticks <= 0:
            print("You have no sticks")
            addCookingFuel(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveSticks(-1)
            fire.addCookingFuel(1)
            addCookingFuel(player, clock1, actions, travels, heroInventory, stock, skills, fire)            
    elif a.lower() == 'l':
        if heroInventory.logs <= 0:
           print("You have no logs")
           addCookingFuel(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveLogs(-1)
            fire.addCookingFuel(4)
            addCookingFuel(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'x':
        cook(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    else:
        addCookingFuel(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def lightFire(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    stick_amount = heroInventory.sticks
    log_amount = heroInventory.logs
    
    #Check if they have any sticks or logs
    if stick_amount == 0 and log_amount == 0:
        print("You have nothing to light the fire with")
        input('press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    
    #if the player has either sticks or logs
    else:  
        displayFire(fire)   #show player the current fuel
        print(f"Fire looses 4 fuel in the night")
        print("What will you use to light the fire?")
        print(f"(S) Sticks: {stick_amount}")
        print(f"(L) Logs : {log_amount}")
        print("(X): Back\n")
    
    a = input("-->")
    
    if a.lower() == 's':
        if stick_amount == 0:
            print("You dont have any sticks")
            lightFire(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        else:
            heroInventory.moveSticks(-1)   #remove the stick from inventory
            fire.fuel += 1 #balance, logs will give more fuel. Add fuel to fire
            checkFire(player, clock1, actions, travels, heroInventory, stock, skills, fire)  #check fuel and lit status
            lightFire(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        
    elif a.lower() == 'l':
        if log_amount == 0:
            print("You dont have any logs")
            lightFire(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        else:
            heroInventory.moveLogs(-1)
            fire.fuel += 5 #balance, logs will give more fuel
            checkFire(player, clock1, actions, travels, heroInventory, stock, skills, fire)  #check fuel and lit status
            lightFire(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    
    elif a.lower() == 'x':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
 
    else:
        lightFire(player, clock1, heroInventory, stock, actions, travels, skills, fire)
def eat(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    #Figure out what food they have in inventory
    available_food = []
    for i in heroInventory.cookedFood.keys():
        if heroInventory.cookedFood[i] >0:
            available_food.append(i.lower())
    if len(available_food) == 0:
        print("You have nothing left to eat")
        input('press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    
    #If they have some food, let them choose what to eat
    else:
        print(f"\nCurrent Hunger: {player.getHunger()} / {player.getMaxHunger()}")
        print("What will you eat?\n")
        for i in available_food:
            print(f'({heroInventory.cookedFood[i]}) {i.capitalize()}')

        print('\n(X): Back')
        a = input("-->")
        while a.lower() not in ['cooked fish', 'berry stew', 'meal', 'cooked deer', 'x']:
            a = input("-->")
        if a.lower() in available_food:
            if a.lower() == 'cooked fish':
                heroInventory.moveCookedFish(-1)
                player.addHunger(100)
                print(f"+100 hunger")
                eat(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            elif a.lower() == 'berry stew':
                heroInventory.moveBerryStew(-1)
                player.addHunger(50)
                print(f"+50 hunger")
                eat(player, clock1, actions, travels, heroInventory, stock, skills, fire)  
            elif a.lower() == 'meal':
                heroInventory.moveMeal(-1)
                player.addHunger(100)
                print(f"+75 hunger")
                eat(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            elif a.lower() == 'cooked deer':
                heroInventory.moveCookedDeer(-1)
                player.addHunger(200)
                print(f"+200 hunger")
                eat(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        elif a.lower() == 'x':
            giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)

#SHOPPING
#all shop's stockpiles
class Stockpile:    
    def __init__(self):
        self.shopItems = {'logs':4,'bait':1,'iron ore':10,'pelt':10,'oil':15,'cooked fish':15,'berry stew':10,'fishing pole':15,'wooden bow':75, 'hunters bow': 300, 'leather armor':30,'rabbits foot':50,'crimson amulet':75,'lexicon':100,'morellonomicon':300,'smiths hammer':25, 'steel hammer': 300,'iron armor':150, 'steel armor': 300, 'wooden arrows':5,'iron arrows':15,'steel arrows':30, 'flaming arrows': 40, 'weak healing potion':10, 'medium healing potion':25, 'strong healing potion':50,'fire resist potion':25,'frost resist potion':25,'poisen resist potion':25}

#Hunter shop
def goShoppingHunter(player, clock1, heroInventory, stock, actions, travels, skills, fire): 
    print(f"\nGold: {heroInventory.getGold()}")
    print(f"Welcome, {player.getName()} to the hunter's shop")
    print("(B) Buy")
    print("(S) Sell")
    print("(X) Back\n")
    a = input('-->')
    if a.lower() == 'b':
        buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 's':
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'x':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def goShoppingSmith(player, clock1, heroInventory, stock, actions, travels, skills, fire): 
    print(f"\nGold: {heroInventory.getGold()}")
    print(f"Welcome, {player.getName()} to the smiths's shop")
    print("(B) Buy")
    print("(S) Sell")
    print("(X) Back\n")
    a = input('-->')
    if a.lower() == 'b':
        buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 's':
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'x':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def goShoppingScholar(player, clock1, heroInventory, stock, actions, travels, skills, fire): 
    print(f"\nGold: {heroInventory.getGold()}")
    print(f"Welcome, {player.getName()} to the town's shop")
    print("(B) Buy")
    print("(S) Sell")
    print("(X) Back\n")
    a = input('-->')
    if a.lower() == 'b':
        buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 's':
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'x':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    available_items = []
    for i in stock.shopItems.keys():
        available_items.append(i)       
 
    print(f'RAW MATERIALS')
    print(f'logs -----------------> {heroInventory.getGold()}/{stock.shopItems["logs"]} gold')
    print(f'bait -----------------> {heroInventory.getGold()}/{stock.shopItems["bait"]} gold')
    print(f'iron ore -------------> {heroInventory.getGold()}/{stock.shopItems["iron ore"]} gold')
    print(f'pelt -----------------> {heroInventory.getGold()}/{stock.shopItems["pelt"]} gold')
    print(f'oil ------------------> {heroInventory.getGold()}/{stock.shopItems["oil"]} gold')
    print(f'\nFOOD')
    print(f'cooked fish ----------> {heroInventory.getGold()}/{stock.shopItems["cooked fish"]} gold')
    print(f'berry stew -----------> {heroInventory.getGold()}/{stock.shopItems["berry stew"]} gold')
    print(f'\nWEAPONS')
    print(f'smiths hammer ----------> {heroInventory.getGold()}/{stock.shopItems["smiths hammer"]} gold')
    print(f'steel hammer -----------> {heroInventory.getGold()}/{stock.shopItems["steel hammer"]} gold')
    print(f'wooden bow -------------> {heroInventory.getGold()}/{stock.shopItems["wooden bow"]} gold')
    print(f'hunters bow ------------> {heroInventory.getGold()}/{stock.shopItems["hunters bow"]} gold')
    print(f'fishing pole -----------> {heroInventory.getGold()}/{stock.shopItems["fishing pole"]} gold')
    print(f'lexicon ----------------> {heroInventory.getGold()}/{stock.shopItems["lexicon"]} gold')
    print(f'morellonomicon ---------> {heroInventory.getGold()}/{stock.shopItems["morellonomicon"]} gold')
    print(f'\nARMOR')
    print(f'leather armor ----------> {heroInventory.getGold()}/{stock.shopItems["leather armor"]} gold')
    print(f'iron armor -------------> {heroInventory.getGold()}/{stock.shopItems["iron armor"]} gold')
    print(f'steel armor ------------> {heroInventory.getGold()}/{stock.shopItems["steel armor"]} gold')
    print(f'\nARROWS')
    print(f'wooden arrows x10 -------> {heroInventory.getGold()}/{stock.shopItems["wooden arrows"]} gold')
    print(f'iron arrows x10 ---------> {heroInventory.getGold()}/{stock.shopItems["iron arrows"]} gold')
    print(f'steel arrows x10 --------> {heroInventory.getGold()}/{stock.shopItems["steel arrows"]} gold')
    print(f'flaming arrows x10 --------> {heroInventory.getGold()}/{stock.shopItems["flaming arrows"]} gold')
    print(f'\nPOTIONS')
    print(f'weak healing potion -----> {heroInventory.getGold()}/{stock.shopItems["weak healing potion"]} gold')
    print(f'medium healing potion ---> {heroInventory.getGold()}/{stock.shopItems["medium healing potion"]} gold')
    print(f'strong healing potion ---> {heroInventory.getGold()}/{stock.shopItems["strong healing potion"]} gold')
    print(f'frost resist potion -----> {heroInventory.getGold()}/{stock.shopItems["frost resist potion"]} gold')
    print(f'fire resist potion ------> {heroInventory.getGold()}/{stock.shopItems["fire resist potion"]} gold')
    print(f'poisen resist potion ----> {heroInventory.getGold()}/{stock.shopItems["poisen resist potion"]} gold')
    print(f"Gold: {heroInventory.getGold()}")
    print('(X) Back')
    a = input('-->')
    while a.lower() not in available_items and a.lower() != 'x':
        a = input('-->')
    if a.lower() == 'x':
        if player.getLocation() == 'village':
            goShoppingHunter(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif player.getLocation() == 'outskirts':
            goShoppingSmith(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        else:
            goShoppingScholar(player, clock1, heroInventory, stock, actions, travels, skills, fire)

    elif a.lower() == 'logs':  #unique
        if heroInventory.getGold() < stock.shopItems['logs']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['logs'])  #unique
            heroInventory.moveLogs(1)   #unique
            print('You bought a log')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'bait':  #unique
        if heroInventory.getGold() < stock.shopItems['bait']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['bait'])  #unique
            heroInventory.moveBait(1)   #unique
            print('You bought bait')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'pelt':  #unique
        if heroInventory.getGold() < stock.shopItems['pelt']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['pelt'])  #unique
            heroInventory.movePelt(1)   #unique
            print('You bought pelt')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'oil':  #unique
        if heroInventory.getGold() < stock.shopItems['oil']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['oil'])  #unique
            heroInventory.moveOil(1)   #unique
            print('You bought oil')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'iron ore':  #unique
        if heroInventory.getGold() < stock.shopItems['iron ore']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['iron ore'])  #unique
            heroInventory.moveIronOre(1)   #unique
            print('You bought iron ore')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'cooked fish':  #unique
        if heroInventory.getGold() < stock.shopItems['cooked fish']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['cooked fish'])  #unique
            heroInventory.moveCookedFish(1)   #unique
            print('You bought cooked fish')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'berry stew':  #unique
        if heroInventory.getGold() < stock.shopItems['berry stew']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['berry stew'])  #unique
            heroInventory.moveBerryStew(1)   #unique
            print('You bought berry stew')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'wooden arrows':  #unique
        if heroInventory.getGold() < stock.shopItems['wooden arrows']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['wooden arrows'])  #unique
            heroInventory.moveWoodenArrows(10)   #unique
            print('You bought wooden arrows')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'iron arrows':  #unique
        if heroInventory.getGold() < stock.shopItems['iron arrows']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['iron arrows'])  #unique
            heroInventory.moveIronArrows(10)   #unique
            print('You bought iron arrows')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'steel arrows':  #unique
        if heroInventory.getGold() < stock.shopItems['steel arrows']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['steel arrows'])  #unique
            heroInventory.moveSteelArrows(10)   #unique
            print('You bought steel arrows')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'flaming arrows':  #unique
        if heroInventory.getGold() < stock.shopItems['flaming arrows']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['flaming arrows'])  #unique
            heroInventory.moveFlamingArrows(10)   #unique
            print('You bought flaming arrows')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'weak healing potion':  #unique
        if heroInventory.getGold() < stock.shopItems['weak healing potion']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['weak healing potion'])  #unique
            heroInventory.moveWeakHealingPotion(1)   #unique
            print('You bought weak healing potion')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'medium healing potion':  #unique
        if heroInventory.getGold() < stock.shopItems['medium healing potion']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['medium healing potion'])  #unique
            heroInventory.moveMediumHealingPotion(1)   #unique
            print('You bought a medium healing potion')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'strong healing potion':  #unique
        if heroInventory.getGold() < stock.shopItems['strong healing potion']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['strong healing potion'])  #unique
            heroInventory.moveStrongHealingPotion(1)   #unique
            print('You bought a strong healing potion')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'fire resist potion':  #unique
        if heroInventory.getGold() < stock.shopItems['fire resist potion']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['fire resist potion'])  #unique
            heroInventory.moveFireResistPotion(1)   #unique
            print('You bought fire resist potion')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'frost resist potion':  #unique
        if heroInventory.getGold() < stock.shopItems['frost resist potion']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['frost resist potion'])  #unique
            heroInventory.moveFrostResistPotion(1)   #unique
            print('You bought frost resist potion')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'poisen resist potion':  #unique
        if heroInventory.getGold() < stock.shopItems['poisen resist potion']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['poisen resist potion'])  #unique
            heroInventory.movePoisenResistPotion(1)   #unique
            print('You bought poisen resist potion')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'leather armor':  #unique
        if heroInventory.getGold() < stock.shopItems['leather armor']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['leather armor'])  #unique
            heroInventory.moveLeatherArmor(1)   #unique
            print('You bought leather armor')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'iron armor':  #unique
        if heroInventory.getGold() < stock.shopItems['iron armor']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['iron armor'])  #unique
            heroInventory.moveIronArmor(1)   #unique
            print('You bought iron armor')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'steel armor':  #unique
        if heroInventory.getGold() < stock.shopItems['steel armor']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['steel armor'])  #unique
            heroInventory.moveSteelArmor(1)   #unique
            print('You bought steel armor')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'wooden bow':  #unique
        if heroInventory.getGold() < stock.shopItems['wooden bow']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['wooden bow'])  #unique
            heroInventory.moveWoodenBow(1)   #unique
            print('You bought a wooden bow')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'hunters bow':  #unique
        if heroInventory.getGold() < stock.shopItems['hunters bow']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['hunters bow'])  #unique
            heroInventory.moveHuntersBow(1)   #unique
            print('You bought a hunters bow')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'smiths hammer':  #unique
        if heroInventory.getGold() < stock.shopItems['smiths hammer']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['smiths hammer'])  #unique
            heroInventory.moveSmithsHammer(1)   #unique
            print('You bought smiths hammer')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'steel hammer':  #unique
        if heroInventory.getGold() < stock.shopItems['steel hammer']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['steel hammer'])  #unique
            heroInventory.moveSteelHammer(1)   #unique
            print('You bought a steel hammer')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'lexicon':  #unique
        if heroInventory.getGold() < stock.shopItems['lexicon']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['lexicon'])  #unique
            heroInventory.moveLexicon(1)   #unique
            print('You bought a lexicon')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'morellonomicon':  #unique
        if heroInventory.getGold() < stock.shopItems['morellonomicon']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['morellonomicon'])  #unique
            heroInventory.moveMorellonomicon(1)   #unique
            print('You bought a morellonomicon')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'rabbits foot':  #unique
        if heroInventory.getGold() < stock.shopItems['rabbits foot']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['rabbits foot'])  #unique
            heroInventory.moveRabbitsFoot(1)   #unique
            print('You bought rabbits foot')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'crimson amulet':  #unique
        if heroInventory.getGold() < stock.shopItems['crimson amulet']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['crimson amulet'])  #unique
            heroInventory.moveCrimsonAmulet(1)   #unique
            print('You bought a crimson amulet')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'fishing pole':  #unique
        if heroInventory.getGold() < stock.shopItems['fishing pole']: #unique
            print('You dont have enough gold')
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-1*stock.shopItems['fishing pole'])  #unique
            heroInventory.moveFishingPole(1)   #unique
            print('You bought a fishing pole')   #unique
            buyItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    selling_prices = {'logs':2,'dragon lilly':10,'cold snap':10,'poisen ivy':10,'crimson petal':10,'iron ore':5,'steel ore':10,'oil':10,'fiber':1,'iron':20,'steel':30,'fish':5,'berries':3,'pelt':5,'cooked fish':15, 'deer meat':5, 'cooked deer': 40, 'berry stew':6,'wooden bow':30,'hunters bow':100,'smiths hammer':15,'steel hammer':100,'lexicon':50,'morellonomicon':100,'leather armor':25,'iron armor':75,'steel armor':100,'rabbits foot':40,'crimson amulet':60,'wooden arrows':1 ,'iron arrows':3,'steel arrows':4,'flaming arrows':6,'weak healing potion':8,'medium healing potion':25,'strong healing potion':45,'fire resist potion':15,'frost resist potion':15,'poisen resist potion':15}
    available_rawMaterial = []
    available_cookedFood = []
    available_weapons = []
    available_armor = []
    available_charms = []
    available_arrows = []
    available_potions = []
    
    #Add raw materials to available sell list
    for i in heroInventory.raw_material.keys():
        if i != 'sticks' and i != 'bait' and heroInventory.raw_material[i] > 0:  #cant sell sticks or bait
            available_rawMaterial.append(i)
    #Add cooked food to available sell list
    for i in heroInventory.cookedFood.keys():
        if i != 'meal' and heroInventory.cookedFood[i] > 0:  #cant sell meal
            available_cookedFood.append(i)
    #Add weapons to available sell list
    for i in heroInventory.weapons.keys():
        if i != 'hammer of ice' and i != 'bow of fire' and i != 'necronomicon' and i != 'fishing pole' and heroInventory.weapons[i] > 0:   #cant sell boss weapons
            available_weapons.append(i)
    #Add armor to available sell list
    for i in heroInventory.allArmor.keys():
        if heroInventory.allArmor[i] > 0:
            available_armor.append(i)
    #Add charms to available sell list
    for i in heroInventory.allCharms.keys():
        if heroInventory.allCharms[i] > 0:
            available_charms.append(i)
    #Add potions to available sell list
    for i in heroInventory.potions.keys():
        if heroInventory.potions[i] > 0:
            available_potions.append(i)
    #Add arrows to available sell list
    for i in heroInventory.arrows.keys():
        if heroInventory.arrows[i] > 0:
            available_arrows.append(i)
            
    print("\nWhat would you like to sell?")
    print(f"Current Gold: {heroInventory.getGold()}")

    #Display raw material for sale
    if len(available_rawMaterial) > 0:
        print('\nRAW MATERIALS')
    for i in available_rawMaterial: #you should see have many of that item you have
        print(f"({heroInventory.raw_material[i]}) {i.capitalize()} --- {selling_prices[i]} gold")
    
    #Display cooked food for sale
    if len(available_cookedFood) > 0:
        print('\nCOOKED FOOD')
    for i in available_cookedFood: #you should see have many of that item you have
        print(f"({heroInventory.cookedFood[i]}) {i.capitalize()} --- {selling_prices[i]} gold")  
    
    #Display weapons for sale    
    if len(available_weapons) > 0:
        print('\nWEAPONS')
    for i in available_weapons: #you should see have many of that item you have
        print(f"({heroInventory.weapons[i]}) {i.capitalize()} --- {selling_prices[i]} gold")  
    
    #Display armor for sale    
    if len(available_armor) > 0:
        print('\nARMOR')
    for i in available_armor: #you should see have many of that item you have
        print(f"({heroInventory.allArmor[i]}) {i.capitalize()} --- {selling_prices[i]} gold")  
        
    #Display potions for sale    
    if len(available_potions) > 0:
        print('\nPOTIONS')
    for i in available_potions: #you should see have many of that item you have
        print(f"({heroInventory.potions[i]}) {i.capitalize()} --- {selling_prices[i]} gold")  
        
    #Display charms for sale    
    if len(available_charms) > 0:
        print('\nCHARMS')
    for i in available_charms: #you should see have many of that item you have
        print(f"({heroInventory.allCharms[i]}) {i.capitalize()} --- {selling_prices[i]} gold")  
    
    print('\n(X) Back\n')
    a = input('-->')
    print('')
    #If your input matches an item available for sale, sell it
    while a.lower() not in available_rawMaterial and a.lower() not in available_cookedFood and a.lower() not in available_weapons and a.lower() not in available_armor and a.lower() not in available_potions and a.lower() not in available_charms and a.lower() != 'x':
        a = input('-->')
    if a.lower() == 'logs':
        heroInventory.moveLogs(-1)
        heroInventory.moveGold(selling_prices['logs'])
        print(f"Sold log for {selling_prices['logs']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'fiber':
        heroInventory.moveFiber(-1)
        heroInventory.moveGold(selling_prices['fiber'])
        print(f"Sold fiber for {selling_prices['fiber']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'iron':
        heroInventory.moveIron(-1)
        heroInventory.moveGold(selling_prices['iron'])
        print(f"Sold iron for {selling_prices['iron']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'steel':
        heroInventory.moveSteel(-1)
        heroInventory.moveGold(selling_prices['steel'])
        print(f"Sold steel for {selling_prices['steel']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'pelt':
        heroInventory.movePelt(-1)
        heroInventory.moveGold(selling_prices['pelt'])
        print(f"Sold pelt for {selling_prices['pelt']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'oil':
        heroInventory.moveOil(-1)
        heroInventory.moveGold(selling_prices['oil'])
        print(f"Sold oil for {selling_prices['oil']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'iron ore':
        heroInventory.moveIronOre(-1)
        heroInventory.moveGold(selling_prices['iron ore'])
        print(f"Sold iron ore for {selling_prices['iron ore']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'steel ore':
        heroInventory.moveSteelOre(-1)
        heroInventory.moveGold(selling_prices['steel ore'])
        print(f"Sold steel ore for {selling_prices['steel ore']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'dragon lilly':
        heroInventory.moveDragonLilly(-1)
        heroInventory.moveGold(selling_prices['dragon lilly'])
        print(f"Sold dragon lilly for {selling_prices['dragon lilly']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'cold snap':
        heroInventory.moveColdSnap(-1)
        heroInventory.moveGold(selling_prices['cold snap'])
        print(f"Sold dragon lilly for {selling_prices['cold snap']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'poisen ivy':
        heroInventory.movePoisenIvy(-1)
        heroInventory.moveGold(selling_prices['poisen ivy'])
        print(f"Sold poisen ivy for {selling_prices['poisen ivy']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'crimson petal':
        heroInventory.moveCrimsonPetal(-1)
        heroInventory.moveGold(selling_prices['crimson petal'])
        print(f"Sold crimson petal for {selling_prices['crimson petal']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'wooden arrows':
        heroInventory.moveWoodenArrows(-1)
        heroInventory.moveGold(selling_prices['wooden arrows'])
        print(f"Sold wooden arrow for {selling_prices['wooden arrows']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'iron arrows':
        heroInventory.moveIronArrows(-1)
        heroInventory.moveGold(selling_prices['iron arrows'])
        print(f"Sold iron arrow for {selling_prices['iron arrows']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'steel arrows':
        heroInventory.moveSteelArrows(-1)
        heroInventory.moveGold(selling_prices['steel arrows'])
        print(f"Sold steel arrow for {selling_prices['steel arrows']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'flaming arrows':
        heroInventory.moveFlamingArrows(-1)
        heroInventory.moveGold(selling_prices['flaming arrows'])
        print(f"Sold flaming arrow for {selling_prices['flaming arrows']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'weak healing potion':
        heroInventory.moveWeakHealingPotion(-1)
        heroInventory.moveGold(selling_prices['weak healing potion'])
        print(f"Sold weak healing potion for {selling_prices['weak healing potion']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'medium healing potion':
        heroInventory.moveMediumHealingPotion(-1)
        heroInventory.moveGold(selling_prices['medium healing potion'])
        print(f"Sold weak healing potion for {selling_prices['medium healing potion']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'strong healing potion':
        heroInventory.moveStrongHealingPotion(-1)
        heroInventory.moveGold(selling_prices['strong healing potion'])
        print(f"Sold weak healing potion for {selling_prices['strong healing potion']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'fire resist potion':
        heroInventory.moveFireResistPotion(-1)
        heroInventory.moveGold(selling_prices['fire resist potion'])
        print(f"Sold fire resist potion for {selling_prices['fire resist potion']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'frost resist potion':
        heroInventory.moveFrostResistPotion(-1)
        heroInventory.moveGold(selling_prices['frost resist potion'])
        print(f"Sold frost resist potion for {selling_prices['frost resist potion']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'poisen resist potion':
        heroInventory.movePoisenResistPotion(-1)
        heroInventory.moveGold(selling_prices['poisen resist potion'])
        print(f"Sold poisen resist potion for {selling_prices['poisen resist potion']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'fish':
        heroInventory.moveFish(-1)
        heroInventory.moveGold(selling_prices['fish'])
        print(f"Sold fish for {selling_prices['fish']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'berries':
        heroInventory.moveBerries(-1)
        heroInventory.moveGold(selling_prices['berries'])
        print(f"Sold berries for {selling_prices['berries']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'cooked fish':
        heroInventory.moveCookedFish(-1)
        heroInventory.moveGold(selling_prices['cooked fish'])
        print(f"Sold cooked fish for {selling_prices['cooked fish']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'deer meat':
        heroInventory.moveDeerMeat(-1)
        heroInventory.moveGold(selling_prices['deer meat'])
        print(f"Sold deer meat for {selling_prices['deer meat']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'cooked deer':
        heroInventory.moveCookedDeer(-1)
        heroInventory.moveGold(selling_prices['cooked deer'])
        print(f"Sold cooked deer for {selling_prices['cooked deer']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'berry stew':
        heroInventory.moveBerryStew(-1)
        heroInventory.moveGold(selling_prices['berry stew'])
        print(f"Sold berry stew for {selling_prices['berry stew']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'wooden bow':
        heroInventory.moveWoodenBow(-1)
        heroInventory.moveGold(selling_prices['wooden bow'])
        print(f"Sold wooden bow for {selling_prices['wooden bow']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'hunters bow':
        heroInventory.moveHuntersBow(-1)
        heroInventory.moveGold(selling_prices['hunters bow'])
        print(f"Sold hunters bow for {selling_prices['hunters bow']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'smiths hammer':
        heroInventory.moveSmithsHammer(-1)
        heroInventory.moveGold(selling_prices['smiths hammer'])
        print(f"Sold smiths hammer for {selling_prices['smiths hammer']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'steel hammer':
        heroInventory.moveSteelHammer(-1)
        heroInventory.moveGold(selling_prices['steel hammer'])
        print(f"Sold steel hammer for {selling_prices['steel hammer']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'lexicon':
        heroInventory.moveLexicon(-1)
        heroInventory.moveGold(selling_prices['lexicon'])
        print(f"Sold lexicon for {selling_prices['lexicon']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'morellonomicon':
        heroInventory.moveMorellonomicon(-1)
        heroInventory.moveGold(selling_prices['morellonomicon'])
        print(f"Sold morellonomicon for {selling_prices['morellonomicon']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'fishing pole':
        heroInventory.moveFishingPole(-1)
        heroInventory.moveGold(selling_prices['fishing pole'])
        print(f"Sold fishing pole for {selling_prices['fishing pole']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'leather armor':
        heroInventory.moveLeatherArmor(-1)
        heroInventory.moveGold(selling_prices['leather armor'])
        print(f"Sold leather armor for {selling_prices['leather armor']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'iron armor':
        heroInventory.moveIronArmor(-1)
        heroInventory.moveGold(selling_prices['iron armor'])
        print(f"Sold iron armor for {selling_prices['iron armor']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'steel armor':
        heroInventory.moveSteelArmor(-1)
        heroInventory.moveGold(selling_prices['steel armor'])
        print(f"Sold steel armor for {selling_prices['steel armor']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'rabbits foot':
        heroInventory.moveRabbitsFoot(-1)
        heroInventory.moveGold(selling_prices['rabbits foot'])
        print(f"Sold rabbits foot for {selling_prices['rabbits foot']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'crimson amulet':
        heroInventory.moveCrimsonAmulet(-1)
        heroInventory.moveGold(selling_prices['crimson amulet'])
        print(f"Sold crimson amulet for {selling_prices['crimson amulet']} gold.")
        sellItems(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'x':
        if player.getLocation() == 'village':
            goShoppingHunter(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        elif player.getLocation() == 'outskirts':
            goShoppingSmith(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        else: 
            goShoppingScholar(player, clock1, heroInventory, stock, actions, travels, skills, fire)

#TAVERN
def enterHuntingTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedHuntingTavern == False:
        if player.getType() == 1:
            print('Welcome to the tavern blacksmith, who might you be?')
            input('press enter to tell him your name')
            print(f'Hello {player.getName()}, nice to meet you')
            print('Its not often blacksmiths come down this way')
            print('Unless its to bring fish back to their village')
            print('But you seem well equiped to handle yourself')
            print('Perhaps you could help us with something')
            input('press enter to continue\n')
            print('Theres a graveyard past the meadows that we go to pray to')
            print('However, as of late, we have had to lock the gates around it')
            print('One of the elder claim that his dead father was walking around the grounds!')
            print('I dont have time to leave the infor such nonsense')
            print('But I would really appretiate it if you could go check it out')
            input('press enter to continue')
        elif player.getType() == 2:
            print(f'Hey {player.getName()}, its good to see you again')
            print('You know that crazy old elder who keeps going on about the end times?')
            print('Well now hes locked the graveyard up because he claims his dead father is walking around!')
            print('Can you please run over there and see who must be messing with him')
            input('press enter to continue\n')
        else:
            print('Welcome to the tavern, stranger')
            print('Wait a second, you look like a scholar, but all the way down here?')
            print('You must be the scholar who escaped the city we have been getting messages about')
            print('Your father seems pretty worried about you')
            print('But you are old enough to make your own choices now')
            print('You also must be able to handle yourself quite well')
            print('You must be the one who took out those bandits')
            print('press enter to tell them about the bandits')
            print('Well then maybe you could help us out with something')
            print('Theres a graveyard past the meadows that we go to pray to')
            print('However, as of late, we have had to lock the gates around it')
            print('One of the elder claim that his dead father was walking around the grounds!')
            print('I dont have time to leave the infor such nonsense')
            print('But I would really appretiate it if you could go check it out')
            input('press enter to continue')
        print('Here take this key, but make sure you have a way to defend yourself just in case...')
        b = input('\nPress Enter to Take Key')
        print('\nQuest: Investigate the graveyard')
        print('You recieved the graveyard key')
        input('\npress enter to continue')
        heroInventory.questItems.append('graveyard key')   #add key to inventory to unlock graveyard gate
        heroInventory.currentQuests.append('investigate the graveyard')
        travels.visitedHuntingTavern = True
        
    if 'investigate the graveyard' in heroInventory.completedQuests:
        print(f'{player.getName()}, youre back!')
        print('What happend down at the graveyard?')
        input('press enter to tell them what happened\n')
        print('I guess the elder was right about what he saw')
        print('Perhaps hes right about the rest of his theory..')
        print('He believes its the end times, and that a powerful, dark force is acting right under out noses')
        print('Perhaps it has something to do with what is down in that crypt')
        print('Here, take this key, theres nobody whom should have it more than you')
        input('press enter to take key')
        print('\nItem recieved: crypt key')
        heroInventory.questItems.append('crypt key')
        print('Quest: investigate the crypt')
        heroInventory.currentQuests.append('investigate the crypt')
        input('\npress enter to continue')
        print('\nBut be warned, if what the elder says is true, then you must be prepared to go down there')
        print('If you havent yet, you should go see the blacksmiths and get some better gear')
        print('Also, I heard the town gate is opened now, you should see if you can get some potions to help you as well')
        
    
    
    
    if 'investigate the crypt' in heroInventory.completedQuests:
        if travels.talkedAboutCrypt == False:
            print(f'\n{player.getName()}, we heard you entered the crypt!')
            print('Tell us what happend!')
            input('press enter to tell the what happened')
            
            print('\nA necromancer? Holding that book you have?')
            print('That book is evil!, shouts the elder from across the room')
            print('It should be burned!')
            input('press enter to continue')
            
            print('\nNo! Use the book against them! someone else shouts')
            print(f'Theres nobody else better suited to use the power in that book than {player.getName()}')
            print('Besides, if what you all say about the dark forces is true, then hell need everything he can get')
            input('press enter to continue')
            
            print('\nThe room grows silent')
            print(f'{player.getName()}, if what the elders say is true, then its not just going to be undead you are fighting')
            print('All creatures of choas will come forth')
            print('You need to stay prepared, and find out how to end it')
            print('If you havent already, the other villages are sure to know something else going on')
            print('Stay safe')
            input('press enter to continue\n')
            travels.talkedAboutCrypt = True
        
    
    
    print('\n(B) Buy drink for 10 gold')
    print('(X) Back')
    
    a = input('-->')
    
    while a.lower() not in ['b', 'x']:
        a = input('-->')
        
    if a.lower() == 'x':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'b':
        if heroInventory.getGold() < 10:
            print('You dont have enough gold')
            enterHuntingTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-10)
            print('-10 Gold')
            print('You drink a strong spirit')
            
            if skills.getIntelligenceSkill() == 0:
                print('Your brain is already as dull as can be')
                enterHuntingTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                print('-1 Intelligence')
                print('+1 Endurance')
                skills.takeDrink()
                enterHuntingTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire)  
def enterSmithsTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    if clock1.day2 != True:
        print('The smiths Tavern is closed today.')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedSmithsTavern == False:
        travels.visitedSmithsTavern = True
        if player.getType() == 1: #blacksmith
            print(f'{player.getName().capitalize()}, good to see you again, I hope the forge has been treating you well.')

        if player.getType() == 2: #hunter
            print(f'\nWhats a hunter like you doing up here?')
            print(f'Nevermind that, youre probably here to buy from the blacksmiths.')
            print(f'Not that you could afford it anyways.')
            input('press enter to continue')
            
        if player.getType() == 3: #scholar
            print(f'Whats a scholar doing down here?')
            print(f'You must be who the gaurds keep asking about.')
            print(f'Dont worry, I am not one to help the gaurds out.')
            print(f'But be careful while youre wandering around.')
            print('press enter to continue')
  
        print(f'There have been some strange rumors going on about some place beyond the swamps.')
        print(f'Someone reports that the glacier there has cracked open.')
        print(f'I think it was probably some kind of earth quake.')
        print(f'Some people are conviced it leads directly to the bottom of hell.')
        input('press enter to continue')
        print(f'\nI wouldnt be to worried about the nonsense from the elders though.')
        print(f'But could you at least go look so I can shut them up?')   
        print(f'Make sure you prepare before you go, I have heard of people getting frostbite down there.') 
        print('I heard the town has a place to make frost resistance potions.')
        print('\nQuest: Investigate the glacial cavern')
        heroInventory.currentQuests.append('Investigate the glacial cavern')
        input('press enter to continue')
    
   
    if 'Investigate the glacial cavern' in heroInventory.completedQuests and 'Clear out the glacial cavern' not in heroInventory.currentQuests and 'Clear out the glacial cavern' not in heroInventory.completedQuests:
        print(f'So what did you find down there?')
        input('Press enter to tell them what happened')
        print(f'A frost atronach? I thought those went extinct long ago.')
        print(f'But you killed one! So I am sure you can kill more of them.')
        print(f'Why dont you go and clear out the cavern of the rest of them.')
        print(f'Who knows what they would do if they made it to town...')
        print(f'But i wouldnt go there without protection from the frost')
        print('I hear the town has an herb garden, youre sure to find what you need there')
        print('\nQuest: Clear out the glacial cavern')
        heroInventory.currentQuests.append('Clear out the glacial cavern')
    
    if 'Clear out the glacial cavern' in heroInventory.completedQuests:
        if travels.talkedAboutGlacialCavern == False:
            print(f'\n{player.getName()} youre back! And we heard the cavern was cleared?')
            print(f'What did you find?')
            input('Press enter to tell them what you found.')
            print('An elder speaks up...')
            print('I tried to warn you all!')
            print('The devil himself is back on earth, bringing those creatures back to do his work.')
            print(f'Nonsense! Someone yells. If that was the devil then {player.getName()} couldnt have killed him.')
            print(f'Well hes gone now, the elder replys, what does it matter now...')
            travels.talkedAboutGlacialCavern = True
        
        
        
        
    print('\n(B) Buy drink for 10 gold')
    print('(X) Back')
    
    a = input('-->')
    
    while a.lower() not in ['b', 'x']:
        a = input('-->')
        
    if a.lower() == 'x':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'b':
        if heroInventory.getGold() < 10:
            print('You dont have enough gold')
            enterHuntingTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-10)
            print('-10 Gold')
            print('You drink a strong spirit')
            
            if skills.getIntelligenceSkill() == 0:
                print('Your brain is already as dull as can be')
                enterHuntingTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                print('-1 Intelligence')
                print('+1 Endurance')
                skills.takeDrink()
                enterHuntingTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def enterTownTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire):
    if clock1.day3 == False:
        print('The tavern is closed today')
        input('press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedTownTavern == False:
        if player.getType() == 1: #blacksmith
            print('\nWelcome blacksmith, I see they finally starting letting you through again.')
            print('Have you seen the scholar around here?')
            print('He seems to have escaped through the sewers they say.')
            print('Good for him I say, you know they never let scholars leave the town?')
            print('I dont know what they teach them in the library but it must be important')
            input('press enter to continue\n')
            
        elif player.getType() == 2: #hunter
            print('\nWelcome hunter, what brings you all the way up here?.')
            print('Hopefully youve brought some of that meat I hear so much about!')
            print('Say, have you seen the scholar on your travels?')
            print('He seems to have escaped through the sewers they say.')
            print('Good for him I say, you know they never let scholars leave the town?')
            print('I dont know what they teach them in the library but it must be important')
            input('press enter to continue\n')
            
        elif player.getType() == 3:
            print(f'\nHey {player.getName()}, youre back!')
            print('The town gaurds were watching the wall all day and night for you')
            print('But at least you showed them you deserve to be able to leave as you please')
            input('press enter to continue')
        travels.visitedTownTavern = True
    
    if travels.canEnterTunnels == True:
        if travels.explainedRumors == True:
            print(f'\n{player.getName()}, listen, there are rumors about what has been going on in the tunnels under the library')
            print('A servant snuck down there and saw it.')
            print('The elders have been using some kind of magic locked inside those old books')
            print('But this seems differnet, it seems darker..')
            print('He said he saw a dragon!')
            input('press enter to continue\n')
            print('It seemed crazy at first, but have you heard what is happening around us?')
            print('The hunters say their dead are walking around!')
            print('And the smiths say the extinct frost atronachs have risen again!')
            print('And now dragons are crawling out of the ground into the tunnels?!')
            input('press enter to continue\n')
            print('It seems to unlikely to be just a coincidence..')
            print('I think the dark forces the elders speak of have something to do with it...')
            print('You need to go see whats at the end of the tunnels')
            print('It may give us answers as to what is happening around us')
            input('press enter to continue\n')
            print('Quest: Investigate the tunnels')
            heroInventory.currentQuests.append('investigate the tunnels')
            input('press enter to continue')
            travels.explainedRumors = False
    
    
    if 'investigate the tunnels' in heroInventory.completedQuests:
        print(f'\n{player.getName()}, youre back!')
        print('Tell us, were there really dragons down there?')
        input('press enter to tell them what happened')
        
        print('\nHow did they get down there?')
        print('Perhaps they crawled through the sewers')
        print('Or perhaps they were drawn to the gold they keep down there')
        print('They were supposed to be extinct!')
        input('press enter to continue')
        
        print('\nWhat the elders have been saying must be true!')
        print('They have been speaking of an old prophecy')
        print('One day the old god of chaos would return...')
        print('...And with him, creatures and monsters would roam the overworld...')
        print('Bringing choas and destruction to all')
        input('press enter to continue')
        
        print('\nBut you have been able to fight back')
        print('You must bring and end to this, for the sake of us all')
        print('You have saved the hunters, the smiths, and now the town...')
        print('But this will never end until the old god is put down')
        input('Press enter to continue')
        
        print('\nTake this, its an old scroll from the back of the library')
        print('I took it when I started hearing the rumors')
        print('I didnt believe them, but now I know for sure')
        print('Take this scroll to the graveyard, and pray to the old god')
        print('He will surely answer to you after what youve already done to his forces')
        print('But first, make sure you have everything possible at your disposal before you face him...')
        input('press enter to take the scroll of chaos')
        
        print('\nQuest Recieved: Face the Old God of Chaos')
        heroInventory.currentQuests.append('face the old god of chaos')
        heroInventory.questItems.append('scroll of chaos')
        print('Item Recieved: Scroll of Choas')
        input('\npress enter to continue')
        
    
    print('\n(B) Buy drink for 10 gold')
    print('(X) Back')
    
    a = input('-->')
    
    while a.lower() not in ['b', 'x']:
        a = input('-->')
        
    if a.lower() == 'x':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'b':
        if heroInventory.getGold() < 10:
            print('You dont have enough gold')
            enterHuntingTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        else:
            heroInventory.moveGold(-10)
            print('-10 Gold')
            print('You drink a strong spirit')
            
            if skills.getIntelligenceSkill() == 0:
                print('Your brain is already as dull as can be')
                enterHuntingTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire)
            else:
                print('-1 Intelligence')
                print('+1 Endurance')
                skills.takeDrink()
                enterHuntingTavern(player, clock1, actions, travels, heroInventory, stock, skills, fire)

#GATHERING ACTIONS: Add time to clock, and items to inventory
def gatherSticks(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    action_time = 60          #Unique                                                                 
    action_amount = 5           #Unique                                                                     
    action_name = 'sticks'      #Unique 
    action_type = 'gathering'
    action_exp = 1              #Unique
    print(f'Gathering {action_amount} {action_name} will take 1 hour.')
    print('Continue? (y/n)')
    
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        giveOptions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'y':
        print(f"\n{action_amount} {action_name} gathered")     
        print(f"+{action_exp} EXP")            
        player.addExp(action_exp)           #gives player exp
        clock1.addTime(action_time)         #add time to the clock
        getHungry(player, action_time, action_type, fire)      #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        heroInventory.moveSticks(action_amount)    #Unique   
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def gatherFiber(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    action_time = 30            #Unique                                                                 
    action_amount = 5           #Unique                                                                     
    action_name = 'fiber'       #Unique 
    action_type = 'gathering'   #Unique, for dialouge 
    action_exp = 2              #Unique
    print(f'Gathering {action_amount} {action_name} will take 30 minutes.')
    print('Continue? (y/n)')
    
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        giveOptions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'y':
        heroInventory.moveFiber(action_amount)          #Unique, give them the fiber 
        print(f"\n{action_amount} {action_name} gathered")   
        print(f"+{action_exp} EXP")                 
        player.addExp(action_exp)   #gives player exp
        clock1.addTime(action_time) #add time
        getHungry(player, action_time, action_type, fire)  #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        giveOptions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
def pickBerries(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    action_time = 90            #Unique                                                                 
    action_amount = 1           #Unique                                                                     
    action_name = 'berries'       #Unique 
    action_type = 'gathering'   #Unique, for dialouge 
    action_exp = 2              #Unique
    print(f'Gathering berries will take 1.5 hour.')
    print('Continue? (y/n)')
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'y':
        heroInventory.moveBerries(action_amount)          #Unique, give them the fiber 
        print(f"\nBerries gathered")   
        print(f"+{action_exp} EXP")                 
        player.addExp(action_exp)   #gives player exp
        clock1.addTime(action_time) #add time
        getHungry(player, action_time, action_type, fire)  #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def mineSteelOre(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if player.getCrafting() < 10:
        print('Mining steel requires at least level 10 crafting.')
        input('press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    
    action_time = 180            #Unique                                                                 
    action_amount = 2           #Unique                                                                     
    action_name = 'steel ore'       #Unique 
    action_type = 'mining'   #Unique, for dialouge 
    action_exp = 10              #Unique
    print(f'Mining steel ore will take 3 hours')
    print('Continue? (y/n)')
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    
    if a.lower() == 'n':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'y':
        heroInventory.moveSteelOre(action_amount)          #Unique, give them the fiber 
        print(f"\n+{action_amount} {action_name}")   
        print(f"+{action_exp} EXP")                 
        player.addExp(action_exp)   #gives player exp
        clock1.addTime(action_time) #add time
        getHungry(player, action_time, action_type, fire)  #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def chopWood(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    action_time = 120            #Unique                                                                 
    action_amount = 5           #Unique                                                                     
    action_name = 'wood'       #Unique 
    action_type = 'chopping'   #Unique, for dialouge 
    action_exp = 2              #Unique
    print(f'Chopping wood will take 2 hours.')
    print('Continue? (y/n)')
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'y':
        heroInventory.moveLogs(action_amount)          #Unique, give them the fiber 
        print(f"\n{action_amount} {action_name} gathered")   
        print(f"+{action_exp} EXP")                 
        player.addExp(action_exp)   #gives player exp
        clock1.addTime(action_time) #add time
        getHungry(player, action_time, action_type, fire)  #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def mineIronOre(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if player.getCrafting() < 10:
        print('Mining steel requires at least level 10 crafting.')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    
    action_time = 120            #Unique                                                                 
    action_amount = 2           #Unique                                                                     
    action_name = 'iron ore'       #Unique 
    action_type = 'mining'   #Unique, for dialouge 
    action_exp = 3              #Unique
    print(f'Mining iron ore will take 2 hours.')
    print('Continue? (y/n)')
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'y':
        heroInventory.moveIronOre(action_amount)          #Unique, give them the fiber 
        print(f"\n{action_amount} {action_name} gathered")   
        print(f"+{action_exp} EXP")                 
        player.addExp(action_exp)   #gives player exp
        clock1.addTime(action_time) #add time
        getHungry(player, action_time, action_type, fire)  #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def gatherPelt(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    print('\nYou step into the creatures den')
    input('press enter to fight')
    
    if clock1.day3 == False:
        animals = ['fox', 'deer', 'wolf']
        choice = animals[random.randint(0, len(animals) - 1)]
    else:
        animals = ['bear', 'wolf', 'wolverine']
        choice = animals[random.randint(0, len(animals) - 1)]

    bear = Enemy('Bear', 75, 0, 10, 0, 30, 15, 30, 'none', 0, 75)
    wolf = Enemy('Wolf', 50, 0, 0, 0, 15, 5, 20, 'none', 0, 50)
    fox = Enemy('Fox', 25, 0, 10, 0, 0, 20, 10, 'none', 0, 30)
    deer = Enemy('Deer', 35, 0, 15, 0, 0, 0, 15, 'none', 0, 100)
    wolverine = Enemy('Wolverine', 55, 15, 20, 20, 20, 20, 15, 'none', 0, 65)
    
    if choice == 'bear':
        battle(bear, player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif choice == 'wolf':
        battle(wolf, player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif choice == 'fox':
        battle(fox, player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif choice == 'deer':
        battle(deer, player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif choice == 'wolverine':
        battle(wolverine, player, clock1, actions, travels, heroInventory, stock, skills, fire)
    
    print('\nThe beast falls\n')
    print('+2 EXP')
    player.addExp(2)
    
    action_time = 180           #Unique                                                                 
    action_amount = 1           #Unique                                                                     
    action_name = 'pelt'       #Unique 
    action_type = 'gathering'   #Unique, for dialouge 
    action_exp = 2              #Unique
    print(f'Harvesting a pelt will take 3 hours.')
    print('Continue? (y/n)')
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'y':
        heroInventory.movePelt(action_amount)          #Unique, give them the fiber 
        print(f"\n+{action_amount} {action_name}")   
        print(f"+{action_exp} EXP")                 
        player.addExp(action_exp)   #gives player exp
        clock1.addTime(action_time) #add time
        getHungry(player, action_time, action_type, fire)  #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        input('press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def gatherOil(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    action_time = 120            #Unique                                                                 
    action_amount = 2           #Unique                                                                     
    action_name = 'oil'       #Unique 
    action_type = 'gathering'   #Unique, for dialouge 
    action_exp = 1              #Unique
    print(f'Gathering oil will take 2 hours.')
    print('Continue? (y/n)')
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'y':
        heroInventory.moveOil(action_amount)          #Unique, give them the fiber 
        print(f"\n{action_amount} {action_name} gathered")   
        print(f"+{action_exp} EXP")                 
        player.addExp(action_exp)   #gives player exp
        clock1.addTime(action_time) #add time
        getHungry(player, action_time, action_type, fire)  #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def huntDeer(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if len(heroInventory.ranged) == 0:
        print('You need a ranged weapon equiped to hunt deer')
        input('press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    if hasArrows(heroInventory) == False:
        print('You dont have any arrows to hunt with')
        input('press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    
    action_time = 360          #Unique                                                                 
    action_amount = 1           #Unique                                                                     
    action_name = 'deer meet and pelt'      #Unique 
    action_type = 'gathering'
    action_exp = 4             #Unique
    print(f'Hunting deer will take 6 hours')
    print('Continue? (y/n)')
    
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        giveOptions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'y':
        available_choices = []
        print('\nSelect an arrow to use.\n')
        wooden_arrows = heroInventory.arrows['wooden arrows']
        iron_arrows = heroInventory.arrows['iron arrows']
        steel_arrows = heroInventory.arrows['steel arrows']
        flaming_arrows = heroInventory.arrows['flaming arrows']
        
        
        if wooden_arrows > 0:
            print(f'(W) Wooden Arrows --- {wooden_arrows}')
            available_choices.append('w')
        if iron_arrows > 0:
            print(f'(I) Iron Arrows --- {iron_arrows}') 
            available_choices.append('i')    
        if steel_arrows > 0:
            print(f'(S) Steel Arrows --- {steel_arrows}')
            available_choices.append('s')
        if flaming_arrows > 0:
            print(f'(F) Flaming Arrows --- {flaming_arrows}')
            available_choices.append('f')
            
        a = input('-->')
        while a.lower() not in available_choices:
            a = input('-->')
        print('')
        if a.lower() == 'w':
            heroInventory.moveWoodenArrows(-1)
            print('-1 Wooden Arrow')
        elif a.lower() == 'i':
            heroInventory.moveIronArrows(-1)
            print('-1 Iron Arrow')
        elif a.lower() == 's':
            heroInventory.moveSteelArrows(-1)
            print('-1 Steel Arrow')
        else:
            heroInventory.moveFlamingArrows(-1)
            print('-1 Flaming Arrow')
        

        print(f"+{action_amount} deer meat")     
        print(f"+{action_amount} pelt")   
        print(f"+{action_exp} EXP")            
        player.addExp(action_exp)           #gives player exp
        clock1.addTime(action_time)         #add time to the clock
        getHungry(player, action_time, action_type, fire)      #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        heroInventory.moveDeerMeat(action_amount)    #Unique   
        heroInventory.movePelt(1)
        input('\npress enter to continue\n')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)

#MISC ACTIONS:
def pray(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    action_time = 60            #Unique                                                                 
    action_amount = 1           #Unique                                                                     
    action_name = ''       #Unique 
    action_type = 'praying'   #Unique, for dialouge 
    action_exp = 0              #Unique
    print(f'Praying will take 1 hour')
    print('Continue? (y/n)')
    
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a.lower() == ('-->')
        
    if a.lower() == 'n':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'y':
        if player.hasPrayed == False:
            if 'scroll of chaos' in heroInventory.questItems:
                print('The scroll of chaos hums with energy')
                print('If you pray to the old god, there will be no going back.')
                print('Pray to the God of Chaos? (y/n)')
                a = input('-->')
                while a.lower() not in ['y', 'n']:
                    a = input('-->')
                if a.lower() == 'y':
                    finalbattle(player, clock1, heroInventory, stock, actions, travels, skills, fire)

            print('You kneel to pray.')
            print('What do you pray for?')
            print('\n(P) Your ancestors protection')
            print('(W) Your ancestors wit')
            print('(F) Your ancestors good fortune\n')
           
            a = input('-->')
            
            while a.lower() not in ['p', 'w', 'f']:
                a = input('-->')
            if a.lower() == 'p':
                player.moveDefence(3)           
                print('\n+3 Defence Permanently') 
                player.hasPrayed = True  
            elif a.lower() == 'w':
                player.moveIntelligence(3)           
                print('\n+3 Intelligence Permanently') 
                player.hasPrayed = True
            else:
                player.moveLuck(3)           
                print('\n+3 Luck Permanently') 
                player.hasPrayed = True
        else:
            if 'scroll of chaos' in heroInventory.questItems:
                print('The scroll of chaos hums with energy')
                print('If you pray to the old god, there will be no going back.')
                print('Pray to the God of Chaos? (y/n)')
                a = input('-->')
                while a.lower() not in ['y', 'n']:
                    a = input('-->')
                if a.lower() == 'y':
                    finalbattle(player, clock1, heroInventory, stock, actions, travels, skills, fire)
            print('You pray to your ancestors to bring good fortune')  
        input('\npress enter to continue')
        player.addExp(action_exp)   #gives player exp
        clock1.addTime(action_time) #add time
        getHungry(player, action_time, action_type, fire)  #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def study(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if clock1.hasStudied == True:
        print('You only have the energy to study once a day')
        input('press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    action_time = 480          #Unique                                                                 
    action_amount = 0           #Unique                                                                     
    action_name = ''      #Unique 
    action_type = ''
    action_exp = 1              #Unique
    print(f'Studying will take 8 hours.')
    print('Continue? (y/n)')
    
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        giveOptions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
    elif a.lower() == 'y':
        print(f"\nYou pour through old, tattered books until your eyes grow tired.")     

        print(f"+{action_exp} EXP")            
        print('+2 Intelligence')
        clock1.hasStudied = True
        player.moveIntelligence(2)
        player.addExp(action_exp)           #gives player exp
        clock1.addTime(action_time)         #add time to the clock
        getHungry(player, action_time, action_type, fire)      #take hunger away from player
        checkHunger(player, action_time, action_type, fire)    #see if they have no hunger, then they take damage
        input('press enter to continue')
        if 'study' in heroInventory.currentQuests:
            print('\nQuest Complete: Study')
            print('+10 EXP')
            player.addExp(10)
            print('+10 Gold')
            heroInventory.moveGold(10)
            heroInventory.currentQuests.remove('study')
            heroInventory.completedQuests.append('study')
            input('press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def crawlThroughSewers(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if player.getType() != 3:  #only the scholar can get out through the sewers
        print('You are too big to fit through the sewers')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    print('\nYou never had great strength, but at least you are small enough to slip through the sewer grate')
    
    if travels.crawledThroughSewers == False: #as the scholar you can travel through the sewer if you want, but only fight the rat once
       print('As you make your way through the passage, you hear hissing..')
       print('A giant hungry sewer rat approached')
       input('press enter to defend yourself!')
       #COMBAT (self, name, maxHP, meleeDefence, rangedDefence, fireResist, frostResist, poisenResist, attack, elementAttack, elementAmt, stamina):
       sewerRat = Enemy('Sewer rat', 50, 15, 15, 0, 0, 0, 10, 'none', 0, 30)
       battle(sewerRat, player, clock1, actions, travels, heroInventory, stock, skills, fire)
       print('\nWith the rat cleared out you make your way out of the sewers and into the outskirts.')
       print('Its the first time youve been outside the town walls')
       print('Now its time for you to find out what these \'dark forces\' are the elders keep mentioning...')
       input('press enter to continue')
       travels.crawledThroughSewers = True
       print('\nQuest Complete: Escape through the sewers')
       heroInventory.currentQuests.remove('escape through the sewers')
       heroInventory.completedQuests.append('escape through the sewers')
       print('+10 EXP')
       print('+10 Gold')
       heroInventory.moveGold(10)
       player.addExp(10)
    outskirts(player, clock1, heroInventory, stock, actions, travels, skills, fire)
def finalbattle(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    print('\nthe final battle starts now')
    input('press enter to continue')
    print('You kneel to the ground, and open the scroll')
    print('The ground begins to tremble, the the sky darkens')
    print('You can hear the sounds of the undead moaning in their graves beneath your feet')
    input('press enter to continue')
    
    print('\nThe Old God appears')
    print('He stretches his arm out towards the ground')
    print('The wind stops, the meadow grass slows')
    print('The birds go silent')
    print('You hold your breath..')
    input('press enter to continue')
    
    print('\nYou hear the sound of the ground crack')
    print('Creatures of choas form from the dirt around you.')
    print('He has challenged you...')
    print('Will you accept his challenge?')
    input('Press enter to accept')
    
    
    #(self, name, maxHP, meleeDefence, rangedDefence, fireResist, frostResist, poisenResist, attack, elementAttack, elementAmt, stamina)
    
    creature1 = Enemy('Chaotic Undead', 150, 25, 25, 0, 15, 30, 30, 'poisen', 10, 125)
    creature2 = Enemy('Chaotic Atronach', 200, 20, 5, 0, 100, 10, 30, 'frost', 30, 250)
    creature3 = Enemy('Chaotic Dragon', 250, 0, 25, 40, 15, 30, 25, 'fire', 40, 200)
    GodOfChaos = Enemy('God of Chaos', 500, 20, 20, 20, 20, 20, 50, 'none', 40, 300)
    
    
    print('\nThe God falls to the ground')
    print('The creates around him turn to ash..')
    print('The ash falls gently through the air')
    print('The sun overtakes the clouds')
    print('The wind breaks the silence.')
    print('And the chaos is cleansed')
    input('Press Enter to Burn the Scroll')
    
    endCredits(player, clock1, heroInventory, stock, actions, travels, skills, fire)
def endCredits(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    print(f'\nCongrats {player.getName()}, you beat the game')
    print(f'DAY ------> {clock1.getDay()}')
    print(f'TIME -----> {clock1.getTime()}')
    print(f'LEVEL ----> {player.getLevel()}')
    
    input('Press enter to close')

#LOCATIONS: These update the travel and action menus with the location's options
def hut(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if player.getType() != 2 and travels.visitedHut == False:
        print(f'You knock on the door of a village hunter. Smoke rising out of the huts top, it feels warms, and smells of cooked fish and berries.')
        print(f'The hunter opens the doors. Greets {player.getName()}, I heard you entered town. Word travels fast in a small village like this.')
        if player.getType() == 1:
            print(f'Its not often a skilled blacksmith comes south from the outskirts. I heard the nearby cave is filled with a fine metal.')
            print(f'Feel free to use the extra bed and cooking pot. Make sure to keep the fire going at night though, it can get chilly.')
        if player.getType() == 3:    
            print(f'A nobel scholar like yourself coming to a little hunting village like this?')
            print(f'That must be why the gaurds decided to open the town gate now, in hopes to hear word of your whereabouts.')
            print(f'Feel free to use the extra bed and cooking pot. Make sure to keep the fire going at night though, it can get chilly.')
        print('\nQuest: Cook a fish.')
        input('press enter to continue')
        heroInventory.currentQuests.append('Cook a fish.')
    
    
    travels.visitedHut = True
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('hut')
    location_routes = ['forest', 'river', 'meadows', 'village']
    location_actions = ['sleep', 'cook', 'light fire']
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)
    
    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def river(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedRiver == False:
        print('\nThe sound of the water calms you.')
        print('The river is one of the main sources of food for the continent')
        print('Not all who cast their line can secure the catch however.')
        travels.visitedRiver = True
        input('press enter to continue')
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('river')
    location_routes = ['hut']
    location_actions = ['go fishing']
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def forest(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedForest == False:
        print('\nThe light of the sun is trapped in the canopy above your head')
        print('The sound of the wind is replaced by the hum of insects and birds')
        print('You feel connected to the trees around you')
        travels.visitedForest = True
        input('press enter to continue')
    
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('forest')
    location_routes = ['hut', 'cave']
    location_actions = ['gather sticks', 'hunt deer']
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def cave(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    print('\nCaves can be a dangerous place to explore')
    print('Are you sure you want to enter? (y/n)')
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower () == 'n':
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedCave == False:
        print('\nThe air sticks to your skin')
        print('Darkness swallows your view')
        print('Something smells rotten...')
        travels.visitedCave = True
        input('press enter to continue')
    
    
#name, maxHP, meleeDefence, rangedDefence, fireResist, frostResist, poisenResist, attack, elementAttack, elementAmt, stamina):
    nameOptions = ['Cave Troll', 'Stone Golemn', 'Rapid Gremlin']
    elementAttackOptions = ['fire', 'frost', 'poisen']
    
    
    nameChoice = nameOptions[random.randint(0,2)]
    maxHPOptions = random.randint(50,150)
    meleeDefenceOptions = random.randint(0,30)
    rangedDefenceOptions = random.randint(0,20)
    fireResistOptions = random.randint(0,20)
    frostResistOptions = random.randint(0,20)
    poisenResistOptions = random.randint(0,20)
    attackOptions = random.randint(10, 30)
    elementChoice = elementAttackOptions[random.randint(0,2)]
    elementAmountOptions = random.randint(1,10)
    staminaOptions = random.randint(50, 150)
    
    caveEnemy = Enemy(nameChoice,maxHPOptions,meleeDefenceOptions,rangedDefenceOptions,fireResistOptions,frostResistOptions,poisenResistOptions,attackOptions,elementChoice,elementAmountOptions,staminaOptions)
    battle(caveEnemy, player, clock1, actions, travels, heroInventory, stock, skills, fire)

    
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('cave')
    location_routes = ['forest']
    location_actions = ['mine steel ore']
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def meadows(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedMeadows == False:
        print('\nThe grasses sway together, as if putting on a performace')
        print('You feel calm')
        print('You have no worries here')
        travels.visitedMeadows = True
        input('press enter to continue')
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('meadows')
    location_routes = ['hut', 'graveyard']
    location_actions = ['gather fiber', 'pick berries']
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def graveyard(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)   
   #Check if the gate is unlocked
    if 'graveyard key' not in heroInventory.questItems:
        print('A locked gate blocks you from entering the graveyard.\nIts probably better this way anyways, who knows what is making those crunching sounds in the distance...')
        input('press enter to continue')
        giveOptions(player, clock1,  actions, travels, heroInventory, stock, skills, fire)
    
    #Check if its the player's first time enter
    if travels.visitedGraveyard == False:
        print('\nYou open the gate with the key the tavern folk gave you.')
        print('You can hear and old groaning man walking about.')
        print('As you approch him he turns to look at you')
        print('You can smell the decaying flesh loosely attached to him')
        print('It seems the dead man got up and walked out of the crypt!')
        print('He appears to be smelling you...')
        print('He turns and runs at you!')
        input('\npress enter to defend yourself!\n')
        graveyardZombie1 = Enemy('Undead', 150, 20,20, 0, 0, 50, 20,'poisen', 5, 100)
        battle(graveyardZombie1, player, clock1, actions, travels, heroInventory, stock, skills, fire)
        print('The undead falls at your feet')
        print('You should probably go tell the people at the tavern what has happened here')
        input('press enter to continue')
        print('\nQuest Complete: Investigate the graveyard')
        print('+20 EXP')
        print('+75 Gold')
        input('\npress enter to continue')
        heroInventory.moveGold(75)
        player.addExp(20)
        heroInventory.currentQuests.remove('investigate the graveyard')
        heroInventory.completedQuests.append('investigate the graveyard')
        travels.visitedGraveyard = True
    
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('graveyard')
    location_routes = ['meadows', 'crypt']
    location_actions = ['pray']
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def crypt(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if 'crypt key' not in heroInventory.questItems:
        print('The crypt is locked by a key, probably best this way for now...')
        input('press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)

    if travels.visitedCrypt == False:
    
        print('\nYou should be well prepared before entering the crypt.')
        print('There is no turning back')
        print('continue? (y/n)')
        
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
        print('\nYou walk down the damp steps of the crypt')
        print('You can hear the groans of the undead echo through the walls')
        print('As the light of sun fades away, dimly light torches flicker against the stone')
        print('You approuch the undead')
        input('press enter to defend yourself\n')
        #(name, maxHP, meleeDefence, rangedDefence, fireResist, frostResist, poisenResist, attack, elementAttack, elementAmt, stamina):
        cryptUndead1 = Enemy('Undead', 100, 0, 20, 0, 30, 50, 25, 'poisen', 3, 80)
        battle(cryptUndead1, player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
        print('The undead falls at your feet')
        print('You swear you can recognize him, but his face to too decayed to know for sure')
        print('There is only one path ahead')
        input('press enter to continue\n')
        
        print('The passage opens into a large room filled with now empty caskets')
        print('Some of these undead are carrying around torches')
        print('Some were burried in their armor as they died in war')
        input('press enter to fight\n')
        
        cryptUndead2 = Enemy('Torch Weilding Undead', 125, 10, 0, 20, 0, 0, 25, 'fire', 15, 100)
        cryptUndead3 = Enemy('Torch Weilding Undead', 50, 0, 0, 0, 0, 0, 50, 'fire', 20, 80)
        cryptUndead4 = Enemy('Armored Unded', 150, 50, 50, 30, 0, 30, 25, 'none', 0, 115)
        
        battle(cryptUndead2, player, clock1, actions, travels, heroInventory, stock, skills, fire)
        battle(cryptUndead3, player, clock1, actions, travels, heroInventory, stock, skills, fire)
        battle(cryptUndead4, player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
        print('\nThe group of undead fall to your feet, finally at peace once again')
        print('The crypt seems to have just one more room')
        print('As you open the gate you can feel an energy in the air')
        print('This must be what the elders were talking about, the forces...')
        input('press enter to continue\n')
        
        print('You see various body parts spread accross the room')
        print('They seems to be arranged in a circle, for some kind of ritual')
        print('Candle light flickers against the cold flesh')
        print('A large, dark figure sits in the middle of them, chanting softly')
        print('He looks up, almost as if was was expecting you')
        input('press enter to continue\n')
        
        print('You will never stop his work, he says')
        print('The force is inevitable')
        print('Do not try to stop it')
        print('There is only one way this can end, with you as another one of my soilders')
        print('He opens a large book, one made of flesh, and starts to read from it')
        input('press enter to fight!\n')
        
        necromancer = Enemy('The Necromancer', 300, 15, 0, 0, 25, 15, 20, 'poisen', 10, 100)
        battle(necromancer, player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
        print('\nThe necromancers body turns to ash')
        print('Only the book he was holding remains')
        input('press enter to take the book\n')
        
        print('You took the necronomicon')
        print('+1 necronomicon')
        heroInventory.moveNecronomicon(1)
        input('press enter to continue\n')
        
        print('Quest Complete: Investigate the crypt')
        heroInventory.currentQuests.remove('investigate the crypt')
        heroInventory.completedQuests.append('investigate the crypt')
        print('+25 EXP')
        player.addExp(25)
        print('+50 gold')
        heroInventory.moveGold(50)
        input('press enter to continue\n')
        
        print('You exit the crypt')
        print('You should probably go tell the tavern folk what happend')
        travels.visitedCrypt = True
    else:
        print('\nYou have no reason to go back in there')
        input('press enter to continue')
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def village(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedVillage == False:
        print('\nThe sound of trade, commition, and drinking fill your ears')
        print('Smells of gutted deer and mead fill your nose')
        print('Nobody seems to notice you')
        travels.visitedVillage = True
        input('press enter to continue')    

   #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('village')
    location_routes = ['hut', 'crossroads']
    location_actions = ['enter hunter shop', 'enter hunting tavern']
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def crossroads(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if clock1.day3 == False:
        print('The crossroads caravan is closed on the weekend')
        input('Press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)

    if travels.visitedCrossroads == False:
        print(f'\nThe crossroads can be a dangerous place.')
        print(f'Theres word of bandits demanding ransoms down the road.')
        print(f'Make sure you are prepared before you try to get through.\n')
        print('Continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y','n']:
            a = input('-->')
        if a.lower() == 'n':
            giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)  
        
        print(f'\nYou arrive at the crossroads, and important spot for trade caravans.')
        print(f'Suddenly, bandits jump out of the brush!')
        print(f'They demand randsom.\n')
        print('Pay 100 gold? (y/n)')
        a = input('-->')
        while a not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'y':
            if heroInventory.getGold() < 100:
                print('\nYou dont have enough gold to pay them!')
                print('If you aint payin with gold, then well have to sell the clothes off your dead body...')
                input('Press enter to defend yourself!\n')
            else:
                heroInventory.moveGold(-100)
                print('-100 Gold')
                print('You pay the bandits their gold.')
                print('Well if he has that much gold, imagine what else he got!')
                input('Press enter to defend yourself!\n')
        elif a.lower() == 'n':
            print('If you aint payin with gold, then well have to sell the clothes off your dead body...')
            input('Press enter to defend yourself!')

        #COMBAT (self, name, maxHP, meleeDefence, rangedDefence, fireResist, frostResist, poisenResist, attack, elementAttack, elementAmt, stamina):
        bandit1 = Enemy('Bandit', 100, 10, 10, 10, 10, 0, 15, 'none', 0, 50)
        battle(bandit1, player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
        print('\nYou slayed the bandits...')
        print('Quest Complete: Travel the crossroads')
    

        print('+50 gold')
        print('+10 EXP')
        
        heroInventory.moveGold(50)
        player.addExp(10)
        travels.visitedCrossroads = True
        print('\nThese bandits may be dead, but it wouldnt be the first time someone cleared them out')
        print('There will always be a chance that the come back here while youre passing through.')
        
    else:
        if random.randint(0, 0) == 0: #Thought i wanted this to be RNG, but now I think everytime
            print('Enemy bandits jump from the bushes!')
            print('They seek revenge for their freinds you have killed!')
            input('Press enter to defend yourself!')
            bandit1 = Enemy('Bandit', 100, 10, 10, 10, 10, 0, 15, 'none', 0, 50)
            battle(bandit1, player, clock1, actions, travels, heroInventory, stock, skills, fire)
            print('\nYou slayed the  bandits!')
            print('+25 gold')
            print('+10 EXP')
            heroInventory.moveGold(25)
            player.addExp(10)

    if 'Travel the crossroads' in heroInventory.currentQuests:
        print('\nQuest Complete: Travel the crossroads')
        print('+15 gold')
        print('+10 EXP')
        heroInventory.moveGold(15)
        player.addExp(10)
        heroInventory.currentQuests.remove('Travel the crossroads')
        heroInventory.completedQuests.append('Travel the crossroads')
        input('press enter to continue')
        
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('crossroads')
    location_routes = ['village', 'outskirts']
    location_actions = []
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def outskirts(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    
    if clock1.day4 == False and player.getLocation() == 'town square': #trying to leave town before day 3
        print('\nThe town gates are locked and you cannot get to the outskirts')
        input('Press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedOutskirts == False:
        print('\nThe outskirts ly just outside the walls of the town')
        print('Sounds of lively anvils pierce your thought')
        print('There is no time for commotion, only work')
        travels.visitedOutskirts = True
        input('press enter to continue')
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('outskirts')
    location_routes = ['smiths home', 'crossroads', 'town square']
    location_actions = ['enter smiths shop', 'enter smiths tavern']
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def smithsHome(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if player.getType() != 1 and travels.visitedSmithsHome == False:
        print(f'You knock on the door of a black smith. You can hear the sound of the hammer meeting the anvil.')
        print(f'Your nose stings of fumes coming off the forge. Maybe you could use that to your advantage.')
        if player.getType() == 2:
            print(f'You must be a hunter no doubt from the south. Your type comes here often to look for new gear, although rarely can afford it.')
            print(f'Feel free to use the bed, but keep the fire goin will ya, and stay out of my way when im working.')
        if player.getType() == 3:    
            print(f'You must be the scholar the gaurds are fussing about.')
            print(f'I heard ya escaped through the sewers, but the gaurds didnt even believe me.')
            print(f'Feel free to use the bed, but keep the fire goin will ya, and stay out of my way when im working.')

        print('\nQuest: Craft leather armor.')
        heroInventory.currentQuests.append('Craft leather armor')
        input('press enter to continue')
    travels.visitedSmithsHome = True
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('smiths home')
    location_routes = ['outskirts', 'forge', 'wood stand', 'swamp']
    location_actions = ['sleep', 'light fire', 'use workbench']
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def swamp(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedSwamp == False:
        print('\nSwamp gas bellows up from your feat')
        print('The swamp is grotesque, but filled with resources')
        print('Just watch your step')
        travels.visitedSwamp = True
        input('press enter to continue')
    
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('swamp')
    
    if travels.visitedSmithsTavern == False:
        location_routes = ['smiths home', 'animal den']
    else:
        location_routes = ['smiths home', 'animal den', 'glacial cavern']
    
    location_actions = ['mine iron ore', 'gather oil', 'gather fiber']
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def forge(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedForge == False:
        print('\nA comfortable place for any smith')
        print('A simple device for transforming the earths material')
        print('If you fuel its flame')
        travels.visitedForge = True
        input('press enter to continue')
    
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('forge')
    location_routes = ['smiths home']
    location_actions = ['smelt ore']
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def woodStand(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedWoodstand == False:
        print('\nA simple place to chop wood')
        print('The best way to start any day')
        travels.visitedWoodstand = True
        input('press enter to continue')
        
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('wood stand')
    location_routes = ['smiths home']
    location_actions = ['chop wood', 'gather sticks']
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def glacialCavern(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if travels.visitedGlacialCavern == False:
        print(f'\nAs the swamp slowy turns to ice you see it.')
        print(f'A narrow passage has formed in the ice.')
        print(f'As you approach you here faint voices coming from the cavern.')
        print(f'Before you are able to make out the words something moves towards you!')
        input('Press enter to defend yourself!')
        glacialCavernFrostAtronach = Enemy('Frost Atronach', 100, 10, 25, 0, 200, 30, 20, 'frost', 20, 100)
        battle(glacialCavernFrostAtronach, player, clock1, actions, travels, heroInventory, stock, skills, fire)
        print(f'\nThe atronach falls before you, crumbling into snow.')
        print(f'You didnt think the children tails were true. Everyone thought they all died long ago.')
        print(f'But it seems they didnt go extinct, but rather, went underground.')
        print(f'Why then, have they come out now? It seems like the earthquake couldnt be just a coincidence.')
        print(f'Nevertheless, I should report back to the tavern folks.')
        print(f'There will surely be more of these things to come, you better be prepared...')
        print(f'\nQuest Complete: Investigate the glacial cavern')
        heroInventory.currentQuests.remove('Investigate the glacial cavern')
        heroInventory.completedQuests.append('Investigate the glacial cavern')
        print('+10 EXP')
        player.addExp(10)
        travels.visitedGlacialCavern = True
        
    

    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('glacial cavern')
    if 'Clear out the glacial cavern' in heroInventory.currentQuests:
        location_routes = ['swamp', 'glacial passage']
    else:
        location_routes = ['swamp']
    location_actions = []
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def glacialPassage(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    print('\nAs you approach the passage, you can hear the grinding of ice and crunching of snow.')
    print('There will be many enemies to fight as you make your way through the passage.')
    print('You better be ready.')
    print('Continue? (y/n)')
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        swamp(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    
    print('As you enter the passage, you can see what was causing the noises your heard.')
    print('The atronachs were rising straight out of the ground.')
    print('Its not that they have been dormant all these year...')
    print('...but it seems like something must be bringing them back.')
    
    glacialPassageFrostAtronach = Enemy('Frost Atronach', 150, 15, 30, 0, 250, 35, 25, 'frost', 25, 125)
    battle(glacialPassageFrostAtronach, player, clock1, actions, travels, heroInventory, stock, skills, fire)
    
    print('\nThat was seems stronger than the last.')
    print('\nIts also getting colder with each step, perhaps thats why...')
    print('You can either continue through the passage, or run away.')
    print('Will you continue? (y/n)')
    
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        swamp(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    
    print('You continue through a dark narrow passage of ice.')
    print('As you squeeze through the ice you can here the crunching of ice behind you.')
    print('It seems the atronach you killed is starting to regenerate in the ice.')
    print('Hopefully you find answer at the end of the cavern...')
    print('\nThe passage opens to a larger chamber with three of the things lumbering around.')
    print('Theres no going back now.')
    
    chamberAtronach1 = Enemy('Frost Atronach', 100, 40, 0, 10, 275, 35, 35, 'frost', 25, 150)
    chamberAtronach2 = Enemy('Frost Atronach', 200, 0, 35, 25, 275, 0, 15, 'frost', 30, 150)
    chamberAtronach3 = Enemy('Frost Atronach', 250, 10, 10, 10, 275, 10, 20, 'frost', 40, 150)
    
    battle(chamberAtronach1, player, clock1, actions, travels, heroInventory, stock, skills, fire)
    print('\nFirst once down, now for the next one.')
    battle(chamberAtronach2, player, clock1, actions, travels, heroInventory, stock, skills, fire)
    print('\nThats the second one down. Only one more to go.')
    battle(chamberAtronach3, player, clock1, actions, travels, heroInventory, stock, skills, fire)
    print('\nThe chamber is clear now.')
    print('It looks like theres only one more room just around the corner.')
    print('It gets even colder as you approach.')
    print('And it feels like theres some kind of energy in the air....')
    print('You can either continue to the final chamber, or run away.')
    print('Will you continue? (y/n)')
    
    a = input('-->')
    while a.lower() not in ['y', 'n']:
        a = input('-->')
    if a.lower() == 'n':
        swamp(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        
    print('As you enter the final chamber you find yourself looking at an alter...')
    print('With a creature at it. It has the body of an atronach, but face of a man, and old man...')
    print('He appears to be reading from and old tomb, the alter glows with energy.')
    print('How did get here? And why?')
    print('He looks up and sees you.')
    print('You ventured quite far to get here, but you will never interrupt his work, he says...')
    input('Press enter to battle')
    
    
    elderAtronach = Enemy('Elder Atronach', 300, 25, 25, 0, 500, 25, 50, 'frost', 50, 250)
    battle(elderAtronach, player, clock1, actions, travels, heroInventory, stock, skills, fire)
    print('\nYou slayed the elder atronach.')
    print('\nBut who was he talking about when I approached him?')
    print('Perhaps I should talk with the other taverns to see if others know.')
    print('Before you leave you notice the alter more closely, a great hammer lays upon it.')
    input('Press enter to take the hammer.')
    print('Item recieved: Hammer of Ice')
    heroInventory.moveHammerOfIce(1)
    input('Press enter to continue')
    print('\nQuest Complete: Clear the glacial cavern')
    player.addExp(25)
    print('+25 EXP')

    heroInventory.currentQuests.remove('Clear out the glacial cavern')
    heroInventory.completedQuests.append('Clear out the glacial cavern')
    swamp(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    
    
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('glacial passage')
    location_routes = []
    location_actions = []
    
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)

    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def animalDen(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedAnimalDen == False:
        print('\nSmells of wet hair and droppings surround you')
        print('This is a common place for many animals to take shelter')
        print('You should keep your mind sharp when entering')
        travels.visitedAnimalDen = True
        input('press enter to continue')
    
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('animal den')
    location_routes = ['swamp']
    location_actions = ['gather pelt']
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)
    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def townSquare(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if clock1.day4 == False and player.getLocation() == 'outskirts': #trying to get into town before day 3
        print('\nThe town gates are locked and you cannot get into town.')
        input('Press enter to continue')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    
    if travels.visitedTownSquare == False:
        print('\nThe town square is filled with busy bodies')
        print('Some of them in fine clothing and jewlery')
        print('The rest of them carry around their things')
        print('Gaurds keep watch')
        travels.visitedTownSquare = True
        input('press enter to continue')
        
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('town square')
    location_routes = ['outskirts', 'library', 'manor', 'herb garden']
    location_actions = ['enter town shop', 'enter town tavern']
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)
    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def library(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedLibrary == False:
        print('\nYears of knowledge from the old ones line the shelves')
        print('Dim candle light and hushed walls make it easy to concentrate')
        print('You feel as if theres more to this place than first glance')
        travels.visitedLibrary = True
        input('press enter to continue')
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('library')
    if travels.secretPassage == False:
        location_routes = ['town square']
    else:
        location_routes = ['town square', 'secret passage']
    
    
    
    location_actions = ['study']
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)
    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def secretPassage(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedSecretPassage == False:
        print('\nAs you open the false door of the library shelf you enter a dimly lit room')
        print('The room is filled with books which are mostly locked up')
        print('However one book seemed to have been read recently, as its laying open near a reading chair')
        input('press enter to pick up the book')    
        travels.visitedSecretPassage = True
        print('\nYou equiped a lexicon')
        heroInventory.magic.append('lexicon')
        print('As you look upon the pages you feel an energy flow through your finger tips')
        if player.getType() == 3:
            print('Its no wonder the elders hid these back here')
            print('And no wonder they are so keen to have me keep studying')
            print('I should probably keep this book close')
        input('press enter to continue')
        
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('secret passage')
    location_routes = ['library', 'tunnels']
    location_actions = ['crawl through sewers']
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)
    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def tunnels(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if 'investigate the tunnels' not in heroInventory.currentQuests and 'investigate the tunnels' not in heroInventory.completedQuests:
        print('\nYou hear strange noises and smell something burning coming from the dark tunnel')
        print('The servants mentioned that I should stay away from from here for now...')
        input('press enter to continue\n')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
    if 'investigate the tunnels' in heroInventory.completedQuests:
        print('\nYou have no more reasons to go down here')
        input('press enter to continue\n')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
    if 'investigate the tunnels' in heroInventory.currentQuests:
        print('\nYou should be well prepared before entering these tunnels')
        print('There is no turning back')
        print('continue? (y/n)')
        a = input('-->')
        while a.lower() not in ['y', 'n']:
            a = input('-->')
        if a.lower() == 'n':
            giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
        print('\nYou make your way down the narrows, winding steps beneath the library')
        print('With each step you can feel the heat rising')
        print('You hear the sounds of claws scraping againg the stone floors') 
        print('Dragons have been extince for hundreds of years, are they really here now?')
        input('press enter to continue\n')
        
        print('The steps end at a long dark tunnel of stone')
        print('Flames light up the rock faces')
        print('It appears to be a nesting ground for the lizard like creatures')
        print('One seems to be interested in what you taste like')
        input('press enter to defend yourself!\n')
        
        #name, maxHP, meleeDefence, rangedDefence, fireResist, frostResist, poisenResist, attack, elementAttack, elementAmt, stamina):
        dragon1 = Enemy('Dragon hatchling', 75, 0, 30, 100, 0, 30, 10, 'fire', 25, 75)
        battle(dragon1, player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
        print('\nThe baby dragon is killed')
        print('But he was young, it looks like they get larger the further back you go')
        print('And it seems killing it didnt make the rest of the group happy...')
        input('press enter to press on\n')
        
        dragon2 = Enemy('Baby dragon', 100, 0, 50, 100, 0, 35, 15, 'fire', 35, 85)
        dragon3 = Enemy('Adult dragon', 150, 0, 65, 100, 0, 45, 15, 'fire', 50, 100)
        
        battle(dragon2, player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
        print('\nIt looks like the mother is not happy...')
        input('press enter to continue')
        battle(dragon3, player, clock1, actions, travels, heroInventory, stock, skills, fire)
        
        print('\nThe nest is defeated')
        print('But something is missing')
        print('Where is the father?')
        input('press enter to continue')
        
        print('\nSuddenly, you hear the load roar of what must be the father..')
        print('The hair on your face singes at the heat')
        input('press enter to end this')
        
        dragon4 = Enemy('Dragon Father', 250, 0, 100, 100, 0, 55, 25, 'fire', 50, 150)
        battle(dragon4, player, clock1, actions, travels, heroInventory, stock, skills, fire)
        print('\nAs the body of the beast fall limp you see something glimmer behind him...')
        print('Under a pile of gold coins ly a great bow')
        input('press enter to pick up the bow')
        
        print('\n+1 bow of fire')
        heroInventory.moveBowOfFire(1)
        input('press enter to continue')
        
        print('\nQuest Complete: investigate the tunnels')
        print('+30 EXP')
        print('+75 Gold')
        heroInventory.moveGold(75)
        player.addExp(30)
        heroInventory.currentQuests.remove('investigate the tunnels')
        heroInventory.completedQuests.append('investigate the tunnels')
        input('press enter to continue')
        
        print('\nAs you make your way out the way you came you hear a voice')
        print('\'You willll neverrr stopp the inevitableeeee....\'')
        print('The voice fades away')
        print('You should probably tell the people at the towns tavern what happend')
        input('press enter to continue\n')
        townSquare(player, clock1, heroInventory, stock, actions, travels, skills, fire)
def manor(player, clock1, heroInventory, stock, actions, travels, skills, fire):

    if player.getType() != 3 and travels.visitedManor == False:
        print(f'You walk into the doors of a great manor, nobody notices, they must think you are a servant.')
        print(f'A young scholar approaches you.')
        if player.getType() == 1:
            print(f'Wow, you must be a blacksmith from the outskirts! How cool, my father never lets me leave the town walls...')
            print(f'Thats why I snuck out through the sewers, the gaurds wernt happy about it though.')
            print(f'If anyone asks, you are my servant. That way you can use the library and herb garden.')
            print(f'Oh, and feel free to use the extra beds here as well.')
        if player.getType() == 2:    
            print(f'Wow, you must be a hunter from the south! What are you doing way up here?')
            print(f'My father would kill me if I ever went that far from town, he never lets me leave.')
            print(f'Thats why I snuck out through the sewers, the gaurds wernt happy about it though.')
            print(f'If anyone asks, you are my servant. That way you can use the library and herb garden.')
            print(f'Oh, and feel free to use the extra beds here as well.')
    
        print('\nQuest: Brew a healing potion.')
        heroInventory.currentQuests.append('Brew a healing potion')
    travels.visitedManor = True
    
    
    
       
    
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('manor')
    location_routes = ['town square', 'servants quarters']
    location_actions = ['sleep', 'light fire']
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)
    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def servantsQuarters(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    if player.getType() != 3:
        print('This servants quarters is only available to servants and their scholars')
        giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedServantsQuarters == False:
        print('\nThese are the quarters of your families servants')
        print('You can occasionaly grab a meal here to stay full')
        print('You have more important things to worry about than cooking a meal')
        travels.visitedServantsQuarters = True
        input('press enter to continue')
    
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('servants quarters')
    location_routes = ['manor']
    location_actions = ['gather meal']
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)
    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)
def herbGarden(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    travelTime(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    if travels.visitedHerbGarden == False:
        print('\nStrange but curious smells taunt you')
        print('Vibrant medicinal herbs are grown here')
        print('Be sure not to pick too many at once, so they can grown back')
        travels.visitedHerbGarden = True
        input('press enter to continue')
    
    #DEFINES PLACES AND ACTIONS YOU CAN GO/DO UNIQUE TO THIS LOCATION
    player.setLocation('herb garden')
    location_routes = ['town square']
    location_actions = ['brew potions', 'gather herbs', 'gather sticks']
    #UPDATES THE MENUS BASED ON THE LOCATION
    travels.clearLocations()
    for i in location_routes:
        travels.addLocation(i)
    actions.clearActions()
    for j in location_actions:
        actions.addAction(j)
    #THEN WE GIVE THE PLAYER THEIR OPTIONS
    giveOptions(player, clock1, actions, travels, heroInventory, stock, skills, fire)

#DAILY INTRODUCTIONS: These will be how we trigger unique daily events and progress through the story
def startDay1(player, clock1, heroInventory, stock, actions, travels, skills, fire):  
    updateStats(player, clock1, actions, travels, heroInventory, stock, skills, fire) 
    if player.getType() == 1:
        print("\nDay 1")
        print("\nYou spend your days near the forge with your father, learning how to shape metal to get by.\nYour mother died along side your little brother at birth.\nYour father grows sicker by the day from years of working with harsh materials.\nYou ofter wonder what you will make of yourself when the day comes, where you must venture out on your own.\n")
        print('Quest: Craft leather armor.')
        heroInventory.currentQuests.append('Craft leather armor')
        heroInventory.melee.append('smiths hammer')
        print('smiths hammer equiped')
        input('press enter to continue')
    
    elif player.getType() == 2:
        print("\nDay 1")
        print("\nYour only concern is keeping food stores full, and enjoying the simple things in life, the birds, the grass, and the wind.\nYou dont have any reason to leave. Your mother and sister enjoy the tribe you are apart of.\nSo what is there to worry about....?\n")
        print('Quest: Cook a fish.')
        heroInventory.currentQuests.append('Cook a fish.')
        input('press enter to continue')
    else:
        print("\nDay 1")
        print('You are the son of a nobel family living in a thriving town.\nThe stone walls surrounding the town keep those rich enough to live inside safe.\nThe guards rarely open the gate except for emergencies and trade.')
        print('You are never aloud to leave the town, as its much too dangerous for a boy like yourself.')
        print('Instead you are expected to study in the library, and practice your alchemy.')
        input('Press enter to continue')
        print('\nQuest: Brew a healing potion.')
        print('Quest: Study.')
        heroInventory.currentQuests.append('Brew a healing potion')
        heroInventory.currentQuests.append('study')
        input('press enter to continue')        
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
        print(f'But you should be small enough to get out through the sewers and find out what people are saying out there.')
        print('\nQuest: Escape through the sewers')
        heroInventory.currentQuests.append('escape through the sewers')
        travels.secretPassage = True

def startDay3(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    clock1.day3 = True
    if player.getType() == 1: 
        print("\nIts the start of a new week, the crossroads caravan should be open now.")
        print('Quest: Travel the crossroads')
        heroInventory.currentQuests.append('Travel the crossroads')
    elif player.getType() == 2:
        print("\nIts the start of a new week, the crossroads caravan should be open now.")
        print('Quest: Travel the crossroads')
        heroInventory.currentQuests.append('Travel the crossroads') 
    else:
        if travels.crawledThroughSewers == False:
            print('\nWhat are you still doing here?!')
            print('Didnt you see the lantern by the passage in the library?')
            print('Here let me bring you over there now')
            input('Press enter to continue\n')
            print('Also, its a great time to leave as the crossroads caravan should be open now')
            print('It will let you pass down to the huting village')
            print('Apparently food is abundent down there')
            print('\nQuest: Travel the crossroads')
            heroInventory.currentQuests.append('Travel the crossroads') 
            input('Press enter to continue\n')
            travels.forceThroughSecretPassage = True
            library(player, clock1, heroInventory, stock, actions, travels, skills, fire)
        else:
            print("\nIts the start of a new week, the crossroads caravan should be open now.")
            print('Quest: Travel the crossroads')
            input('Press enter to continue')
            heroInventory.currentQuests.append('Travel the crossroads')   

def startDay4(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    clock1.day4 = True
    print('\nTheres word that the town gates are opened to the public now')
    print('Apparently they are concerned about a scholar who went missing.')
    travels.secretPassage = True

    
    if player.getType() == 3:
        print('\nIt looks like they figured out I escaped.')
        print('Well its the first time I every got any of there attention')
        print('At least now they will let me travel freely in and out of the walls')
        input('press enter to continue')
        print('')
def startDay5(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    clock1.day5 = True
def startDay6(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    clock1.day6 = True
def startDay7(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    clock1.day7 = True
def startDay8(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    clock1.day8 = True
def startDay9(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    clock1.day9 = True
def startDay10(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    clock1.day10 = True
def startDay11(player, clock1, heroInventory, stock, actions, travels, skills, fire):
    clock1.day11 = True
    
    
    
#MAIN PUTS IT ALL TOGETHER    
def main():
    #generateLocations()
    intro()                          #intro the game
    class_data = createClass()       #generate your player
    player = Hero(class_data[0], class_data[1], class_data[2], class_data[3], class_data[11], class_data[12], class_data[13], class_data[14], class_data[15])
    skills = SkillTree(class_data[4], class_data[5], class_data[6], class_data[7], class_data[8], class_data[9], class_data[10], class_data[16])  #generate the skill tree
    clock1 = Clock(1)             #generate the game clock
    actions = ActionMenu()                   #generate the action menu
    travels = TravelMenu()                   #generate the travel menu
    heroInventory = Inventory()      #generate the hero's inventory
    stock = Stockpile()              #generate the hero's stockpile
    fire = Fire()   #generate the fire
    
    
    startDay1(player, clock1, heroInventory, stock, actions, travels, skills, fire)  #Introduce the first day
        
    if player.getType() == 1:
        smithsHome(player, clock1, heroInventory, stock, actions, travels, skills, fire)
    elif player.getType() == 2:
        hut(player, clock1, heroInventory, stock, actions, travels, skills, fire)        #Begin the player at their hut, this will eventually go inside of startDay1() once the other characters are developed more
    else:
        manor(player, clock1, heroInventory, stock, actions, travels, skills, fire)

if __name__ == "__main__":      #execute only if run as a script
    main()