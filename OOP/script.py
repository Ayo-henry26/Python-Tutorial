from datetime import datetime

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

##########################################################################################
#GETTERS AND SETTERS IN PYTHON
#Traditional way to make the data protected or private and use getters and setters
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email #Protected Attribute
        self.__password = password #Private Attribute (Name Mangling)


    #Getter Method
    def get_email(self):
        print(f"Email accessed on {datetime.now()}")
        return self._email
    
    # Setter Method
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email

    # def clean_email(self):
    #     return self._email.strip().lower()
    
user1 = User("Ghost", "ghost@gmail.com", "ghost23")
print(user1.get_email())

user1.set_email("Ghost@gmail.com")
print(user1.get_email())
# print(user1._email) # Accessing protected attribute directly (not recommended but possible)

# print(user1.__password) # Accessing private attribute will raise an AttributeError

# print(user1.clean_email()) # Accessing protected attribute
#########################################################################################################


##################################################################################################
#USING PROPERTIES IN PYTHON
class Person:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email

person1 = Person("Kali", "kaillinux@gmail.com", "kali_123")
print(person1.email)

#Modifying the email using the setter
person1.email = "Kalilinux@gmail.com"
print(person1.email)
################################################################################################## 

##################################################################################################
#STATIC ATTRIBUTES 
class BankAccount:
    MAIN_BALANCE = 1000  # Static Attribute
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        
    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("Deposit", amount)
        else:
            print("Deposit amount must be positive.")
            
    def __log_transaction(self, transaction_type, amount):
        print(f"Transaction: {transaction_type} of ${amount} on {datetime.now()}. {self.owner}'s new balance is ${self._balance}")
                
    
    def _is_valid_amount(self, amount):
        return amount > 0
        
            
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
            
account = BankAccount("Ghost", 2000)
account.deposit(500)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(6))


#ENCAPSULATION
# class BadEncapsulation:
#     def __init__(self, balance):
#         self.balance = balance
        
        
        
        
# account = BadEncapsulation(0.0)
# account.balance = -1
# print(account.balance) 


class BetterEncapsulation:
    def __init__(self):
        self._balance = 0.0
        
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Not enough money in the account")
        self._balance -= amount
        
        
account = BetterEncapsulation()
account.deposit(1000)
print(account.balance)
account.withdraw(250)
print(account.balance)