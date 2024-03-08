player = {"money": 0, "tool": 0}

tools = [
    {"level": 0, "name": "Teeth", "cost": 0, "generates": 1},
    {"level": 1, "name": "Rusty scissors", "cost": 5, "generates": 5},
    {"level": 2, "name": "Old-timey Push Lawnmower", "cost": 25, "generates": 50},
    {
        "level": 3,
        "name": "Fancy Battery-Powered Lawnmower",
        "cost": 250,
        "generates": 100,
    },
    {"level": 4, "name": "Team of Starving Students", "cost": 500, "generates": 250},
]


def getInput():
    result = input("do you want to [m]ow, [u]pgrade, or [q]uit? ")

    if result == "m":
        mow()
        return 1

    if result == "u":
        upgrade()
        return 1

    if result == "q":
        quit()
        return 1

    print("no valid options given")
    getInput()


def mow():
    print("you worked")
    player["money"] += tools[player["tool"]]["generates"]
    print(f"you have ${player['money']}")
    win()


def upgrade():
    if tools[player["tool"]]["level"] == 4:
        print("no more upgrades")
        win()
    if player["money"] < tools[player["tool"] + 1]["cost"]:
        print("you don't have enough money")
        win()
    else:
        print("you upgraded")
        player["money"] - tools[player["tool"] + 1]["cost"]
        player["tool"] += 1
        print(tools[player["tool"]])
        win()


def quit():
    print("game over")


def win():
    if tools[player["tool"]]["level"] == 4 and player["money"] >= 1000:
        print("you win")
        quit()
    else:
        getInput()


getInput()
