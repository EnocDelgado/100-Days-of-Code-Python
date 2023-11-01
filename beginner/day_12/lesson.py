# DAY 12

#! Local & Global Scope

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")


# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength)

#Global Scope
player_health = 10

def drink_potion():
    player_health - 2
    print(player_health)

drink_potion()
print(player_health)


#! There is no Block Scope

gamel_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if gamel_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


#! Modify Global Variable

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies inside function {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

enemies = 1

def increase_enemies():
    print(f"Enemies inside function {enemies}")
    return enemies + 1

increase_enemies()
print(f"Enemies outside function: {enemies}")


#! Glocal Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"
