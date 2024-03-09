import math, random


class Ship:
    def __init__(self, name, hull, firepower, accuracy):
        self.name = name
        self.hull = hull
        self.firepower = firepower
        self.accuracy = accuracy
        self.dead = False


def random_number(min, max):
    while True:
        randomNum = math.floor(random.random() * (max + 1))
        if randomNum >= min and randomNum <= max:
            return randomNum


player = Ship("USS Schwarzenegger", 20, 5, 0.7)
aliens = []

for x in range(random_number(6, 10)):
    alien = Ship(
        (f"Alien {x + 1}"),
        random_number(3, 6),
        random_number(2, 4),
        (random_number(60, 80) / 100),
    )
    aliens.append(alien)

# --------- Created Ships --------- #


def getInput():
    result = input("[a]ttack or [r]etreat? ")
    print(result)
    if result == "a":
        attack(player, pickAlien())

    if result == "r":
        quitGame()

    print("wrong input")
    winCondition()


def ranges_random_tipping_point(low, high):
    while True:
        threshold = random.random()
        if threshold >= low and threshold <= high:
            # print(threshold)
            return threshold


def calculate_accuracy(low, high):
    above = 0
    below = 0
    for x in range(10000):
        accuracy = ranges_random_tipping_point(0.6, 0.8)
        threshold = ranges_random_tipping_point(low, high)
        if accuracy > threshold:
            above = above + 1
        elif accuracy < threshold:
            below = below + 1
    print(above, below)


calculate_accuracy(0.4, 1)


def attack(attacker, target):
    if attacker != player:
        text = input("Alien ship attacks!")
    damage = attacker.accuracy * attacker.firepower
    target.hull = target.hull - damage
    if target.hull <= 0:
        target.dead = True
        print(
            f"{attacker.name} caused {damage} damage to {target.name}. {target.name} died."
        )
        if attacker == player:
            winCondition()
        else:
            quitGame()

    else:
        print(
            f"{attacker.name} caused {damage} damage to {target.name}. {target.name} survived with {target.hull} HP"
        )
        if attacker == player:
            attack(pickAlien(), player)
        else:
            getInput()


def quitGame():
    print("Game over")


def allDead():
    for alien in aliens:
        if alien.dead == False:
            return False

    return True


def winCondition():
    if allDead() == True:
        print("You won")
    else:
        getInput()


def pickAlien():
    for alien in aliens:
        if alien.dead == False:
            return alien


# getInput()
