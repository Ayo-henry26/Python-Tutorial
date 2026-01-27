# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# person1 = Person("John", 30)
# person1.greet()

# person2 = Person("ALice", 27)
# person2.greet()


# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password

#     def say_hello(self, user):
#         print(
#             f"Sending message to {user.username}, Yoooo {user.username}, it's {self.username}"
#             )
        
# user1 = User("Ghost", "ghost@gmail.com", "ghost23")
# user2 = User("Shadow", "shadow,@gmail.com", "shadow45")

# user1.say_hello(user2)
import random

class Entity:
    """Base class for anything that can fight."""
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage! (Health: {max(0, self.health)}/{self.max_health})")

class Player(Entity):
    """The Hero controlled by you."""
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)
        self.inventory = []

    def attack(self, enemy):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        print(f"\n>> {self.name} swings their sword at {enemy.name}!")
        enemy.take_damage(damage)

class Enemy(Entity):
    """Base class for monsters."""
    def attack(self, player):
        damage = random.randint(self.attack_power - 2, self.attack_power + 2)
        print(f">> {self.name} attacks {player.name}!")
        player.take_damage(damage)

class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Grubby the Goblin", health=40, attack_power=8)

class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Ignis the Dragon", health=150, attack_power=25)

# --- The Game Engine (The Controller Object) ---
class DungeonGame:
    def __init__(self):
        self.player = None
        self.enemy_types = [Goblin, Dragon]

    def start(self):
        print("--- Welcome to the OOP Dungeon ---")
        name = input("Enter your Hero's name: ")
        self.player = Player(name)
        self.spawn_enemy()

    def spawn_enemy(self):
        enemy_class = random.choice(self.enemy_types)
        self.current_enemy = enemy_class()
        print(f"\nA wild {self.current_enemy.name} appeared!")
        self.battle_loop()

    def battle_loop(self):
        while self.player.is_alive() and self.current_enemy.is_alive():
            action = input("\nDo you [A]ttack or [R]un? ").lower()
            
            if action == 'a':
                self.player.attack(self.current_enemy)
                if self.current_enemy.is_alive():
                    self.current_enemy.attack(self.player)
            elif action == 'r':
                print("You escaped... for now.")
                return
            
        if self.player.is_alive():
            print(f"\nVictory! {self.current_enemy.name} has been defeated.")
        else:
            print("\nGame Over. You perished in the dungeon.")

# --- Run the Program ---
if __name__ == "__main__":
    game = DungeonGame()
    game.start()