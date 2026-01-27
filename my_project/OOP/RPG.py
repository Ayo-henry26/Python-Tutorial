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
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        print(f"\n>> {self.name} swings their sword at {enemy.name}!")
        enemy.take_damage(damage)
        
        
class Enemy(Entity):
    def attack(self, player):
        damage = random.randint(self.attack_power - 2, self.attack_power + 2)
        print(f">> {self.name} attacks {player.name}!")
        player.take_damage(damage)
        
class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Oburo the Goblin King", health=75, attack_power=10)
        
class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Ragna the Dragon Lord", health=150, attack_power=25)
        

        
    
    
        
        