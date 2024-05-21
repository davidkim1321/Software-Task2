class Entity:
    def __init__(self, name: str, health: int, strength: int, stamina: int, agility: int, intelligence: int, resistance: int, mainattack: str, attackdamage: int, weapon: str, skill1: str, skill2: str, skill3: str, skill4: str, skill5: str, XPdrop: int, Itemdrop: str):
        self.name = name
        self.health = health
        self.strength = strength
        self.stamina = stamina
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