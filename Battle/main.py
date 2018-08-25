from classes.game import Person, bcolors
import time
# Spells
magic = [{"name": "Fire", "cost": 10, "dmg": 60},
        {"name": "Thunder", "cost": 15, "dmg": 80},
        {"name": "Blizzard", "cost": 10, "dmg": 60}]


player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

# Battle Sequence
running = True
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    time.sleep(1.5)
    print("=======================")
    player.choose_action()
    choice = int(input())
    index = choice - 1
    print("You choose", player.actions[index] + "!")

# If player choose 1 to attack
    if choice == 1:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())

    time.sleep(1.5)

# Just get Enemy to Attack for Now
    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage. Player HP:", player.get_hp())






