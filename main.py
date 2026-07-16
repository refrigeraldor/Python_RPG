# import libraries
import os
import random
import time

# player stats
player_x = 0
player_y = 0
player_attack = 10
player_defense = 7
player_speed = 10
player_level = 1
player_exp = 0
player_hp = 100
player_max_hp = 100
exp_to_lvl_up = 2

items = ["potion", "potion", "super potion", "super potion"]

y_index = 0

game = True
wildChance = 0

# enemy stats
enemies = ["snake", "bear", "dragon"]
enemy_attack = 0
enemy_defense = 0
enemy_speed = 0
exp_to_give = 0
enemy_hp = 1
enemy_max_hp = 0
enemy_level = 0

# map grid
mapGrid = [
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    
]

# battle intro animation
def battleIntro():
    clear_screen()
    time.sleep(0.1)
    for i in range(1, 9):
        print("○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○")
        time.sleep(0.05)
    time.sleep(1)
    clear_screen()
    battle()

# level up the player and update their stats
def levelUp():
    global player_attack
    global player_defense
    global player_speed
    global player_hp
    global player_max_hp
    global player_exp
    global exp_to_lvl_up
    global player_level

    clear_screen()
    player_level += 1
    print(f"You leveled up to level {player_level}!")
    time.sleep(1)
    print("You grew a bit stronger!")
    time.sleep(1)

    # update player stats
    player_attack += 3
    player_defense += 2
    player_speed += 2
    player_exp = 0
    player_max_hp += 15
    player_hp = player_max_hp
    exp_to_lvl_up += 2

# enemy name,attack,defense,speed,exp to give,hp,lvl
def battle():
    global enemy_attack
    global enemy_defense
    global enemy_speed
    global exp_to_give
    global enemy_hp
    global enemy_max_hp
    global enemy_level

    global player_attack
    global player_defense
    global player_speed
    global player_hp
    global player_max_hp
    global player_exp
    global exp_to_lvl_up
    global player_level


    enemy = random.choice(enemies)
    print(f"A wild {enemy} appears!")
    
    stat_list = []

    # read enemy stats from the file
    with open("enemyStats.txt", "r") as stats:
        for line in stats:
            if line.startswith(enemy):
                stat_list = line.strip().split(",")
                break
    
    # assign enemy stats from the list
    # enemy name,attack,defense,speed,exp to give,hp,lowest_lvl,highest_lvl
    if stat_list:
        enemy_attack = int(stat_list[1])
        enemy_defense = int(stat_list[2])
        enemy_speed = int(stat_list[3])
        exp_to_give = int(stat_list[4])
        enemy_hp = int(stat_list[5])
        enemy_max_hp = enemy_hp
        enemy_level = random.randint(int(stat_list[6]), int(stat_list[7]))
    time.sleep(1)

    # battle loop
    while enemy_hp != 0:
        print(f"""
            What will you do?
            ===============================
            Your Health: {player_hp}/{player_max_hp} | Lvl.{player_level}
            Foe Health: {enemy_hp}/{enemy_max_hp} | Lvl.{enemy_level}
            ===============================
            Attack (a) | Item (i) | Run (r)
            ===============================
        """)

        choice = input()

        # clear the screen and display the battle options
        if choice == "a":
            clear_screen()
            print(f"""
                Choose a move.
                ===============================
                Stab (s) | Fendente (f)
                ===============================
            """)

            choice = input()
            clear_screen()
            if player_speed > enemy_speed:
                # player attacks first (player is faster)
                if choice == "s":
                    print('You used stab!')
                    time.sleep(1)
                    damageNum =  round((player_attack * 10) / enemy_defense) + random.randint(-1,3)
                    enemy_hp -= damageNum
                    print(f'It did {damageNum} damage!')
                    time.sleep(1)

                elif choice == "f":
                    print('You used fendente!')
                    time.sleep(1)
                    damageNum =  round((player_attack * 15) / enemy_defense) + random.randint(-1,3)
                    enemy_hp -= damageNum
                    print(f'It did {damageNum} damage!')
                    time.sleep(1)

                # check if the enemy is defeated
                if enemy_hp < 0 or enemy_hp == 0:
                    enemy_hp = 0
                    print(f"You defeated the wild {enemy}!")
                    time.sleep(1)
                    print(f"You gained {exp_to_give} exp point(s)!")
                    player_exp += exp_to_give

                    if player_exp > exp_to_lvl_up or player_exp == exp_to_lvl_up:
                        levelUp()
                        break
                    else:
                        break

                # enemy attacks second (player is faster)
                print(f"The wild {enemy} used strike!")
                time.sleep(1)
                damageNum = round((enemy_attack * 5 * enemy_level) / player_defense) + random.randint(-1, 3)
                player_hp -= damageNum
                print(f'It did {damageNum} damage!')
                time.sleep(1)

            else:
                # enemy attacks first (enemy is faster)
                print(f"The wild {enemy} used strike!")
                time.sleep(1)
                damageNum = round((enemy_attack * 5 * enemy_level) / player_defense) + random.randint(-1, 3)
                player_hp -= damageNum
                print(f'It did {damageNum} damage!')
                time.sleep(1)

                # player attacks second (player is slower)
                if choice == "s":
                    print('You used stab!')
                    time.sleep(1)
                    damageNum =  round((player_attack * 5 * enemy_level) / enemy_defense) + random.randint(-1,3)
                    enemy_hp -= damageNum
                    print(f'It did {damageNum} damage!')
                    time.sleep(1)

                elif choice == "f":
                    print('You used fendente!')
                    time.sleep(1)
                    damageNum =  round((player_attack * 7 * enemy_level) / enemy_defense) + random.randint(-1,3)
                    enemy_hp -= damageNum
                    print(f'It did {damageNum} damage!')
                    time.sleep(1)

                # check if the enemy is defeated
                if enemy_hp < 0 or enemy_hp == 0:
                    enemy_hp = 0
                    print(f"You defeated the wild {enemy}!")
                    time.sleep(1)
                    print(f"You gained {exp_to_give} exp point(s)!")
                    player_exp += exp_to_give

                    if player_exp > exp_to_lvl_up or player_exp == exp_to_lvl_up:
                        levelUp()
                        break
                    else:
                        break
            
            clear_screen()

        # attempt to flee from the battle
        elif choice == "r":
            fleeChance = random.randint(0, 2)
            # check if the flee attempt was successful
            if fleeChance == 2:
                print("You couldn't escape!")
                time.sleep(1)

                clear_screen()

                print(f"The wild {enemy} used strike!")
                time.sleep(1)
                damageNum = round((enemy_attack * 5) / player_defense) + random.randint(-1, 3)
                player_hp -= damageNum
                print(f'It did {damageNum} damage!')
                time.sleep(1)

            elif fleeChance != 2:
                print("You sucessfully escaped!")
                time.sleep(1)
                break
        
        elif choice == "i":
            clear_screen()
            
            # display the items in the player's inventory and prompt them to choose one
            print("Choose an item to use.")
            print("======================")
            for index, item in enumerate(items):
                print(f"{item} | no.{index}")
            print("======================")
            choice = int(input())

            clear_screen()

            # check which item the player chose and apply its effect
            if items[choice] == "potion":
                items.pop(choice)
                print("You used a potion. It healed 20 HP.")
                player_hp += 20
                if player_hp > player_max_hp:
                    player_hp = player_max_hp
            
            elif items[choice] == "super potion":
                items.pop(choice)
                print("You used a super potion. It healed 50 HP.")
                player_hp += 50
                if player_hp > player_max_hp:
                    player_hp = player_max_hp

            print(f"The wild {enemy} used strike!")
            time.sleep(1)
            damageNum = round((enemy_attack * 5) / player_defense) + random.randint(-1, 3)
            player_hp -= damageNum
            print(f'It did {damageNum} damage!')
            time.sleep(1)
            

def createMap():
    global y_index
    y_index = 0
    for y in mapGrid:
        for x in y:
            if x == player_x and y_index == player_y:
                print("[@]", end="")
            elif x == 5 and y_index == 3:
                print("[o]", end="")

            else:
                print("[-]", end="")

        y_index +=1

        print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def userInput():
    global player_x
    global player_y
    global wildChance

    # get user input for movement
    move = input()
    if move == "w":
        if player_y - 1 < 0:
            return
        else:
            player_y -= 1

    elif move == "s":
        if player_y + 1 > 6:
            return
        else:
            player_y += 1

    elif move == "d":
        if player_x + 1 > 6:
            return
        else:
            player_x += 1

    elif move == "a":
        if player_x - 1 < 0:
            return
        else:
            player_x -= 1
    
    # chance of a wild encounter
    wildChance = random.randint(1, 5)
    if wildChance == 5:
        battleIntro()

# start game
clear_screen()
createMap()

# main game loop
while game:
    clear_screen()
    createMap()
    userInput()