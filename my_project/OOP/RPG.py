import random

class Entity:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, amount_damage):
        self.health -= amount_damage
        print(f"{self.name} took {amount_damage} damage. (Health: {max(0, self.health)}/{self.max_health})")
        
    
class Player(Entity):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)
        self.inventory = []
        
    def attack(self, enemy):
        damage = 
        
    
    
        
        