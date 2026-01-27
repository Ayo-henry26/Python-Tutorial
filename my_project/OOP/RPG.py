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
        super().__init__(name, health=100, attack_power=25)
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
        super().__init__(name="Oburo the Goblin King", health=75, attack_power=15)
        
class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Ragna the Dragon Lord", health=150, attack_power=30)
        
class Dungeon:
    def __init__(self):
        self.player = None
        self.enemy_types = [Goblin, Dragon]
        
    def start(self):
        print("==============Welcome to VOID DUNGEON==============")
        name = input("Enter your name: Yuusha ")
        self.player = Player(name)
        
        
    def spawn_enemy(self):
        enemy_class = random.choice(self.enemy_types)
        self.current_enemy = enemy_class()
        print(f"\nA wild {self.current_enemy.name} appeared!")
        
        
    def battle_loop(self):
        while self.player.is_alive() and self.current_enemy.is_alive():
            action = input("\nDo you want Attack[A] or Run[R]? ").lower()
            
            if action == 'a':
                self.player.attack(self.current_enemy)
                
        
        
        

    
    
        
        