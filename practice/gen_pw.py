import random
def gen_pw():
    names = ["Ayomide", "Laryea", "Henry", "Sowah"]
    symbols = ["@", "$", "_", "-", "#"]
    positions = ["student", "staff"]
    name = random.choice(names)
    symbol = random.choice(symbols)
    position = random.choice(positions)
    number = random.randint(10, 99)
    pw = f"{name}{symbol}{position}{number}"
    return pw
print(gen_pw())