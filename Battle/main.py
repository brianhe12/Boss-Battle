from classes.game import Person, bcolors
import time
# Spells
magic = [{"name": "Fire", "cost": 10, "dmg": 100},
        {"name": "Thunder", "cost": 12, "dmg": 124},
        {"name": "Blizzard", "cost": 10, "dmg": 100}]


player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

# Battle Sequence
running = True
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    # time.sleep(1.5)
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

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP to cast Spell" + bcolors.ENDC)
            continue
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)

        print("Current MP:", current_mp)
        print(bcolors.OKBLUE + "\n" + spell + " deals", magic_dmg, "points of damage.", bcolors.ENDC)



# Just get Enemy to Attack for Now
    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage.")


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
        print("Your HP:", bcolors.BOLD + bcolors.FAIL, str(player.get_hp()), "/", bcolors.ENDC, bcolors.OKGREEN, str(max_hp), bcolors.ENDC, bcolors.OKBLUE, "Your MP:", current_mp, "/", max_mp, bcolors.ENDC)
        print(bcolors.HEADER + bcolors.BOLD + bcolors.FAIL, "CRITICAL!!!", bcolors.ENDC)
    elif (current_hp > (max_hp/5) and (current_hp != 0)):
        print("Your HP:", bcolors.OKGREEN, str(player.get_hp()), "/", str(max_hp), bcolors.ENDC, "Your MP:", bcolors.OKBLUE, current_mp, "/", max_mp, bcolors.ENDC)

    #End of Game
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print("Your HP:", bcolors.BOLD + bcolors.FAIL, current_hp, bcolors.ENDC, "/", max_hp, bcolors.OKBLUE, "Your MP:", current_mp, "/", max_mp, bcolors.ENDC)

        print(bcolors.FAIL + bcolors.BOLD + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False




