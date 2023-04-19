import random

print()
print("Welcome to the character generator!")
print()
print("Let's name the brave adventurers: ")
print()

# The user should determine 5 character names
character1 = input("Character 1: ")
character2 = input("Character 2: ")
character3 = input("Character 3: ")
character4 = input("Character 4: ")
character5 = input("Character 5: ")
print()

# If the user has named all characters this will be confirmed here
print("***YOUR CHARACTERS ARE COMPLETE***")
print()

# Here the roles for player 1 are assigned randomly
role_number = random.randint(1, 3)

if role_number == 1:
    char_role = "Warrior!"

elif role_number == 2:
    char_role = "WIZARD!"

elif role_number == 3:
    char_role = "Potato!"


# Stats of the characters between 5 and 10 are assigned
print('"' + character1 + '"', "is a ", char_role)

strength = random.randint(5, 10)
magic = random.randint(5, 10)
health = random.randint(5, 10)

# The selected character is multiplied by 3
if char_role == "Warrior!":
    strength *= 3
elif char_role == "WIZARD!":
    magic *= 3
elif char_role == "Potato!":
    health *= 3

# Randomly select the format for printing the stats
format_choice = random.random()
if format_choice < 0.1:
    # Print stats in binary format
    print("Strength:", bin(strength))
    print("Magic:", bin(magic))
    print("Health:", bin(health))
elif format_choice < 0.2:
    # Print stats in hex format
    print("Strength:", hex(strength))
    print("Magic:", hex(magic))
    print("Health:", hex(health))
else:
    # Print stats in decimal format
    print("Strength:", strength)
    print("Magic:", magic)
    print("Health:", health)

# print("Strength:", strength)
# print("Magic:", magic)
# print("Health:", health)

print()
print("---------")
print()

# Here the roles for player 2 are assigned randomly
role_number = random.randint(1, 3)

if role_number == 1:
    char_role = "Warrior!"

elif role_number == 2:
    char_role = "WIZARD!"

elif role_number == 3:
    char_role = "Potato!"


# Stats of the characters between 5 and 10 are assigned
print('"' + character2 + '"', "is a ", char_role)

strength = random.randint(5, 10)
magic = random.randint(5, 10)
health = random.randint(5, 10)

# The selected character is multiplied by 3
if char_role == "Warrior!":
    strength *= 3
elif char_role == "WIZARD!":
    magic *= 3
elif char_role == "Potato!":
    health *= 3

# Randomly select the format for printing the stats
format_choice = random.random()
if format_choice < 0.1:
    # Print stats in binary format
    print("Strength:", bin(strength))
    print("Magic:", bin(magic))
    print("Health:", bin(health))
elif format_choice < 0.2:
    # Print stats in hex format
    print("Strength:", hex(strength))
    print("Magic:", hex(magic))
    print("Health:", hex(health))
else:
    # Print stats in decimal format
    print("Strength:", strength)
    print("Magic:", magic)
    print("Health:", health)

# print("Strength:", strength)
# print("Magic:", magic)
# print("Health:", health)

print()
print("---------")
print()

# Here the roles for player 3 are assigned randomly
role_number = random.randint(1, 3)

if role_number == 1:
    char_role = "Warrior!"

elif role_number == 2:
    char_role = "WIZARD!"

elif role_number == 3:
    char_role = "Potato!"


# Stats of the characters between 5 and 10 are assigned
print('"' + character3 + '"', "is a ", char_role)

strength = random.randint(5, 10)
magic = random.randint(5, 10)
health = random.randint(5, 10)

# The selected character is multiplied by 3
if char_role == "Warrior!":
    strength *= 3
elif char_role == "WIZARD!":
    magic *= 3
elif char_role == "Potato!":
    health *= 3

# Randomly select the format for printing the stats
format_choice = random.random()
if format_choice < 0.1:
    # Print stats in binary format
    print("Strength:", bin(strength))
    print("Magic:", bin(magic))
    print("Health:", bin(health))
elif format_choice < 0.2:
    # Print stats in hex format
    print("Strength:", hex(strength))
    print("Magic:", hex(magic))
    print("Health:", hex(health))
else:
    # Print stats in decimal format
    print("Strength:", strength)
    print("Magic:", magic)
    print("Health:", health)

# print("Strength:", strength)
# print("Magic:", magic)
# print("Health:", health)

print()
print("---------")
print()

# Here the roles for player 4 are assigned randomly
role_number = random.randint(1, 3)

if role_number == 1:
    char_role = "Warrior!"

elif role_number == 2:
    char_role = "WIZARD!"

elif role_number == 3:
    char_role = "Potato!"


# Stats of the characters between 5 and 10 are assigned
print('"' + character4 + '"', "is a ", char_role)

strength = random.randint(5, 10)
magic = random.randint(5, 10)
health = random.randint(5, 10)

# The selected character is multiplied by 3
if char_role == "Warrior!":
    strength *= 3
elif char_role == "WIZARD!":
    magic *= 3
elif char_role == "Potato!":
    health *= 3

# Randomly select the format for printing the stats
format_choice = random.random()
if format_choice < 0.1:
    # Print stats in binary format
    print("Strength:", bin(strength))
    print("Magic:", bin(magic))
    print("Health:", bin(health))
elif format_choice < 0.2:
    # Print stats in hex format
    print("Strength:", hex(strength))
    print("Magic:", hex(magic))
    print("Health:", hex(health))
else:
    # Print stats in decimal format
    print("Strength:", strength)
    print("Magic:", magic)
    print("Health:", health)

# print("Strength:", strength)
# print("Magic:", magic)
# print("Health:", health)

print()
print("---------")
print()

# Here the roles for player 5 are assigned randomly
role_number = random.randint(1, 3)

if role_number == 1:
    char_role = "Warrior!"

elif role_number == 2:
    char_role = "WIZARD!"

elif role_number == 3:
    char_role = "Potato!"


# Stats of the characters between 5 and 10 are assigned
print('"' + character5 + '"', "is a ", char_role)

strength = random.randint(5, 10)
magic = random.randint(5, 10)
health = random.randint(5, 10)

# The selected character is multiplied by 3
if char_role == "Warrior!":
    strength *= 3
elif char_role == "WIZARD!":
    magic *= 3
elif char_role == "Potato!":
    health *= 3

# Randomly select the format for printing the stats
format_choice = random.random()
if format_choice < 0.1:
    # Print stats in binary format
    print("Strength:", bin(strength))
    print("Magic:", bin(magic))
    print("Health:", bin(health))
elif format_choice < 0.2:
    # Print stats in hex format
    print("Strength:", hex(strength))
    print("Magic:", hex(magic))
    print("Health:", hex(health))
else:
    # Print stats in decimal format
    print("Strength:", strength)
    print("Magic:", magic)
    print("Health:", health)

# print("Strength:", strength)
# print("Magic:", magic)
# print("Health:", health)

print()
print("---------")
print()
