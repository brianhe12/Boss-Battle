from classes.game import Person, bcolors
import random
import time
# Spells
magic = [{"name": "Blaze", "cost": 10, "dmg": 120},
        {"name": "Lightning", "cost": 15, "dmg": 100},
        {"name": "Blizzard", "cost": 8, "dmg": 70}]


player = Person(430, 70, 60, 34, magic)
enemy = Person(1300, 70, 45, 25, magic)

#Status's
status = "None"
frozen_status_count = 0
burn_status_count = 0
para_status_count = 0

para_skip = False
frozen_skip = False

# Battle Sequence
running = True
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("=======================")
    player.choose_action()
    choice = int(input())
    index = choice - 1
    print("You choose", player.actions[index] + "!")

# If Player choose 1 to Attack
    if choice == 1:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")

# If Player chooses to use Magic
    elif choice == 2:
        player.choose_spell()
        magic_choice = int(input()) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        # See if we have enough MP
        current_mp = player.get_mp()
        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP to cast Spell" + bcolors.ENDC)
            continue

        # If we have enough MP, see which status each spell could inflict
        if magic_choice == 0: #fire
            burn_status_count = burn_status_count + 2
            status = "BURNED"

        elif magic_choice == 1: #paralyzed
            para_status_count = para_status_count + 2
            status = "PARA"

        elif magic_choice == 2: #frozen
            frozen_status_count = frozen_status_count + 2
            status = "FROZEN"

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)

    elif choice == 3:
        player.heal()

    if (status == "PARA") and (para_status_count > 0):
        para_skip = True
        #print("Enemy Paralyzed")
        para_status_count = para_status_count - 1

    elif(status == "PARA") and (para_status_count == 0):
        #print("Enemy Snapped Out of It!")
        para_skip = False
        status = "None"


    if (status == "FROZEN") and (frozen_status_count == 0):
        #print("Enemy thawed")
        frozen_skip = False
        status = "None"

    elif (status == "FROZEN") and (frozen_status_count > 0):
        frozen_skip = True
        #print("Enemy Frozen")
        print("Enemy took 10 Frozen Damage")
        enemy.take_damage(10)
        frozen_status_count = frozen_status_count - 1

    if (para_skip == False) or (frozen_skip == False): # both false means enemy is normal
        # Just get Enemy to Attack for Now
        enemy_choice = 1
        enemy_dmg = enemy.generate_damage()
        player.take_damage(enemy_dmg)
        print("Enemy attacks for", enemy_dmg, "points of damage.")

    else:
        print("Enemy is Immobilized")

    # Status Effects
    if burn_status_count > 0:
        enemy.take_damage(20)
        print("Enemy took 20 Burn Damage!")
        para_skip = False
        frozen_skip = False
        burn_status_count = burn_status_count - 1

    # Makes this a little interesting...
    if (enemy.get_hp() < enemy.get_max_hp() / 6) and (status == "FROZEN"):
        enemy.enemy_heal()

    # Battle Stats

    # Enemy Stats
    enemy_current_hp = enemy.get_hp()
    enemy_max_hp = enemy.get_max_hp()
    enemy_current_mp = enemy.get_mp()
    enemy_max_mp = enemy.get_max_mp()
    print("Enemy HP:",bcolors.FAIL, enemy_current_hp, "/", enemy_max_hp, bcolors.ENDC, "Enemy MP:", bcolors.OKBLUE, enemy_current_mp, "/", enemy_max_mp, bcolors.ENDC)


    # Player Stats
    current_mp = player.get_mp()
    max_mp = player.get_max_mp()
    current_hp = player.get_hp()
    max_hp = player.get_max_hp()

    if (current_hp < (max_hp/5)) and (current_hp != 0):
        print("Your HP:", bcolors.BOLD + bcolors.FAIL, current_hp, "/", bcolors.ENDC, bcolors.OKGREEN, max_hp, bcolors.ENDC, bcolors.OKBLUE, "Your MP:", current_mp, "/", max_mp, bcolors.ENDC)
        print(bcolors.HEADER + bcolors.BOLD + bcolors.FAIL, "CRITICAL!!!", bcolors.ENDC)
    elif (current_hp > (max_hp/5) and (current_hp != 0)):
        print("Your HP:", bcolors.OKGREEN, current_hp, "/", max_hp, bcolors.ENDC, "Your MP:", bcolors.OKBLUE, current_mp, "/", max_mp, bcolors.ENDC)

    #End of Game
    if ((player.get_hp() == 0) or ((enemy_current_hp == 0) and (current_hp == 0))):
        print("Your HP:", bcolors.BOLD + bcolors.FAIL, current_hp, bcolors.ENDC, "/", max_hp, "Your MP:", bcolors.OKBLUE, current_mp, "/", max_mp, bcolors.ENDC)

        print(bcolors.FAIL + bcolors.BOLD + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False

    elif enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False






