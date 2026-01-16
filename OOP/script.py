class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print(f"{self.name} says Woof!")

class Owner:
    def __init__(self, name, address, contact_number):
        self .name = name
        self.address = address
        self.contact_number = contact_number

owner1 = Owner("Alice", "123 Maple St", "555-1234")
dog1 = Dog("Buddy", "Golden Retriever", owner1)
print(dog1.owner.name)

owner2 = Owner("Bob", "456 Oak St", "555-5678")
dog2 = Dog("Max", "Beagle", owner2)
print(dog2.owner.name)

######################################################
#Traditional way to make the data protected or private and use getters and setters
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email #Protected Attribute
        self.password = password