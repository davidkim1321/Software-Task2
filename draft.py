class Entity:
    def __init__(self, name: str, health: int, attack: int, e_weapon: str, e_armour:str, skills: str):
        self.is_alive = True
        self.name = name
        self.health = health
        self.attack = attack
        self.equipped_weapon = e_weapon
        self.equipped_armour = e_armour
        self.skills = skills

hero = Entity('Adam', 100, 20, 'holy sword', 'holy armour')

print(hero.name)

class Player(Entity):
    def __init__(self, strength: int, agility: int, level: int):
        self.strength = strength
        self.agility = strength
        self.inventory = []
        self.level = 0
        self.experience_gauge = 0

class Enemy(Entity):
    def __init__(self, xp_drop, item_drop):
        self.experience_drop = xp_drop
        self.item_drop = item_drop

minotaur= Enemy('Minotaur', 50, 10, 'sword' 'holy armour', '', 10, 'hide')
print(minotaur.xp_drop)
class Items:
    def __init__(self, attack, defence, health, strength, agility):
        self.attack = attack
        self.defence = defence
        self.health = health
        self.strength = strength
        self.agility = agility
class weapon(Items):
    def __init__(self, attack, strength, agility):



class List_of_skills:
    def __init__(self, attack):
        self.attack = attack


        


