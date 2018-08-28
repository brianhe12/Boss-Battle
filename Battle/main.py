from classes.game import Person, bcolors
import random
import time

# Spells
magic = [{"name": "Blaze", "cost": 12, "dmg": 100},
        {"name": "Lightning", "cost": 15, "dmg": 150},
        {"name": "Frostbite", "cost": 8, "dmg": 70}]


player = Person(450, 50, 60, 34, magic)
enemy = Person(1325, 70, 45, 25, magic)


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

# Loop the Game until winner is decided
while running:
    print("=======================")
    player.choose_action()
    choice = int(input())
    index = choice - 1
    print("You choose", player.actions[index] + "!")
    print("=======================")

# If Player choose 1 to Attack
    if choice == 1:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of Damage!")

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
            print("Blaze did", magic_dmg, "Damage!")
            status = "BURNED"

        elif magic_choice == 1: #paralyzed
            para_status_count = para_status_count + 2
            print("Lightning did", magic_dmg, "Damage!")
            status = "PARA"

        elif magic_choice == 2: #frozen
            frozen_status_count = frozen_status_count + 2
            print("Frostbite did", magic_dmg, "Damage!")
            status = "FROZEN"

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)

# If Player chooses to Heal
    elif choice == 3:
        player.heal()

    #Statuses for Enemy
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
        print("Enemy took 10 Frozen Damage!")
        enemy.take_damage(10)
        frozen_status_count = frozen_status_count - 1

    #Immobilization check
    if (para_skip == False) or (frozen_skip == False): # both false means enemy is normal

        # Spells
        ene_magic = random.randint(0, 6)
        if ene_magic > 4:
            enemy_choice = 2
            magic_choice = random.randint(0,2)
            magic_dmg = enemy.generate_spell_damage(magic_choice)
            spell = enemy.get_spell_name(magic_choice)
            cost = enemy.get_spell_mp_cost(magic_choice)

            # See if we have enough MP
            current_mp = enemy.get_mp()
            if cost > current_mp:
                print(bcolors.FAIL + "Enemy tries to cast spell, but Failed!" + bcolors.ENDC)
                enemy_dmg = enemy.generate_damage()
                player.take_damage(enemy_dmg)
                print("Enemy attacks for", enemy_dmg, "points of damage.")
                pass
            else:
                # If we have enough MP, see which status each spell could inflict
                if magic_choice == 0:  # fire
                    print("Enemy casted Blaze and did", magic_dmg, "Damage!")
                    print("You took 15 Burn Damage")
                    player.take_damage(15)


                elif magic_choice == 1: # paralyzed
                    print("Enemy casted Lightning and did", magic_dmg, "Damage!")


                elif magic_choice == 2: # frozen
                    print("Enemy casted Frostbite and did", magic_dmg, "Damage!")
                    print("You took 10 Frozen Damage")
                    player.take_damage(10)


                enemy.reduce_mp(cost)
                player.take_damage(magic_dmg)

        # Normal Attack
        else:
            enemy_choice = 1
            enemy_dmg = enemy.generate_damage()
            player.take_damage(enemy_dmg)
            print("Enemy attacks for", enemy_dmg, "points of Damage!")

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
        enemy_current_mp = enemy.get_mp()
        if enemy_current_mp < 0:
            enemy_current_mp = 0
        else:
            enemy.reduce_mp(10)




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
        print("Your HP:", bcolors.BOLD + bcolors.FAIL, current_hp, "/", bcolors.ENDC, bcolors.OKGREEN, max_hp, bcolors.ENDC, "Your MP:",  bcolors.OKBLUE, current_mp, "/", max_mp, bcolors.ENDC)
        print(bcolors.HEADER + bcolors.BOLD + bcolors.FAIL, "Warning! Low HP", bcolors.ENDC)
    elif (current_hp > (max_hp/5) and (current_hp != 0)):
        print("Your HP:", bcolors.OKGREEN, current_hp, "/", max_hp, bcolors.ENDC, "Your MP:", bcolors.OKBLUE, current_mp, "/", max_mp, bcolors.ENDC)

#End of Game
    if ((player.get_hp() == 0) or ((enemy_current_hp == 0) and (current_hp == 0))):
        print("Your HP:", bcolors.BOLD + bcolors.FAIL, current_hp, bcolors.ENDC, "/", max_hp, "Your MP:", bcolors.OKBLUE, current_mp, "/", max_mp, bcolors.ENDC)

        print(bcolors.FAIL + bcolors.BOLD + "Your enemy has defeated you. You lose!" + bcolors.ENDC)
        running = False

    elif enemy.get_hp() == 0:
        print(bcolors.BOLD + bcolors.HEADER + "You win!" + bcolors.ENDC)
        running = False






