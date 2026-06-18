xp = 0

def add_xp(amount):

    global xp

    xp += amount

    level = xp // 100

    print(f"\nXP Gained: {amount}")
    print(f"Total XP: {xp}")
    print(f"Level: {level}")