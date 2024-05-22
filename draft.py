class Entity:
    def __init__(self, name: str, health: int, strength: int, stamina: int, agility: int, intelligence: int, resistance: int, mainattack: str, attackdamage: int, weapon: str, skill1: str, skill2: str, skill3: str, skill4: str, skill5: str, XPdrop: int, Itemdrop: str):
        self.name = name
        self.health = health
        self.strength = strength
<<<<<<< HEAD
        self.agility = strength
        self.inventory = []
        self.level = 0
        self.experience_gauge = 0

class Enemy(Entity):
    def __init__(self, xp_drop, item_drop):
        self.experience_drop = xp_drop
        self.item_drop = item_drop

minotaur= Enemy('Minotaur', 50, 10, 'sword', 'holy armour', '', 10, 'hide')
print(minotaur.xp_drop)
class Items:
    def __init__(self, attack, defence, health, strength, agility):
        self.attack = attack
        self.defence = defence
        self.health = health
        self.strength = strength
=======
        self.stamina = stamina
>>>>>>> aeba2cd11a09d1a3bb08a858daa81417b00fbdd9
        self.agility = agility
        self.intelligence = intelligence
        self.resistance = resistance
        self.mainattack = mainattack
        self.attackdamage = attackdamage
        self.is_alive = True
        self.equipped_weapon = weapon
        self.skills = [skill1,skill2,skill3,skill4,skill5]
    
    skill1 = "Punch"
    skill2 = "Dodge"
    skill3 = "Block"
    skill4 = "Parry"
    skill5 = "Snipe"

class Manticore(Entity):
    def speak(self):
        print("Growl...")

x = Manticore ("Thorn", 5, 85)
x.speak()  