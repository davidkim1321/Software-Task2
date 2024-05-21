import tkinter as tk
from tkinter import ttk

class Entity:
    def __init__(self, name: str, health: int, attack: int, e_weapon: str, e_armour:str, skill1: str, skill2: str, skill3: str, skill4: str, skill5:str):
        self.name = name
        self.health = health
        self.attack = attack
        self.is_alive = True
        self.equipped_weapon = e_weapon
        self.equipped_armour = e_armour
        self.skills = [skill1,skill2,skill3,skill4,skill5]

        



hero = Entity('Adam', 100, 20, 'holy sword', 'holy armour', )


'''class Entity:
    def __init__(self, name, health, main_attack, weapon):
        self.name = name
        self.health = health
        self.main_attack = main_attack
        self.weapon = weapon
'''

    def attack(self, target):
        damage = self.main_attack + self.weapon.damage
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} with {self.weapon.name} causing {damage} damage.")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been defeated.")
        else:
            print(f"{self.name} takes {damage} damage and now has {self.health} health left.")

    def __str__(self):
        return f"Entity(name={self.name}, health={self.health}, main_attack={self.main_attack}, weapon={self.weapon})"

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"Weapon(name={self.name}, damage={self.damage})"

# Example usage
if __name__ == "__main__":
    sword = Weapon("Sword", 10)
    dragon = Entity("Dragon", 100, 20, sword)
    knight = Entity("Knight", 50, 15, sword)

    print(dragon)
    print(knight)

    dragon.attack(knight)
    knight.attack(dragon)
    


class item:

class Player(Entity):
    def __init__(self, level, experience, strength, agility, uses):
        self.self_level = level
        self.self_experience = experience
        self.strength = strength
        self.agility = agility
        self.number_of_skill_uses = uses
        
    def attack

    def 
        
        

class armour:

class weapon:

class List_of_skills:
    


class Enemy:


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
    
