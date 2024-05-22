class Entity:    def __init__(self, name: str, health: int, attack: int, e_weapon: str, e_armour:str, skills: str):
        self.is_alive = True        self.name = name
        self.health = health        self.attack = attack
        self.equipped_weapon = e_weapon
        self.equipped_armour = e_armour
        self.skills = skills
    
    def use_skill():
        print('You used a skill')

    def printName():
        print(name)


    
    
hero = Entity('Adam', 100, 20, 'holy sword', 'holy armour','')
print(hero.name)

class Player(Entity):    def __init__(self, name: str, health: int, attack: int, e_weapon: str, e_armour:str, skills: str, strength: int, agility: int, level: int):
        super().__init__(name, health, attack, e_weapon, e_armour, skills)
        self.strength = strength        self.agility = strength
        self.inventory = []
        self.level = 0
        self.experience_gauge = 0

class Enemy(Entity):
    def __init__(self, name: str, health: int, attack: int, e_weapon: str, e_armour:str, skills: str, xp_drop: int , item_drop: str):
        super().__init__(name, health, attack, e_weapon, e_armour, skills)
        self.xp_drop = xp_drop
        self.item_drop = item_drop

minotaur= Enemy('Minotaur', 50, 10, 'sword', 'holy armour', '', 10, 'hide')
class Items:
    def __init__(self, name, attack, defence, health, strength, agility):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = healt        self.strength = strength        self.agility = agilit
        '''class weapon(Items):
    def __init__(self, attack, strength, agility):



class List_of_skills
           def __init__(self, attack):
        self.attack = attack'''

        
print(minotaur.xp_drop)

class Manticore:
    def __init__(self, name) :
        self.name = name
        self.attack = 5
        self.health = 85
        self.is_alive = True
    
class Siren:
    def __init__(self, name) :
        self.name = name
        self.attack = 
        self.health = 50
        self.is_alive = True

class Siren:
    def __init__(self, name) :
        self.name = name
        self.attack = 
        self.health = 50
        self.is_alive = True

if __name__ == "__main__":
    player = Player("Adonis")
    
    while player.is_alive:
        action = input("Enter based 'North', 'West', 'South', 'East', or 'quit' to progress the game: ").lower()
    
