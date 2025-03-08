
import random
import time

gold = 0
player_health = 100
MONEY_CLASS = []
WEAPON_CLASS = []
PURCHASES_AND_POWERUPS = []
PRIMARY_WEAPON_CLASS = []
SECONDARY_WEAPON_CLASS = []
assassin_name = ""
XP = 250


def set_single_item(class_list, item):
    class_list.clear()
    class_list.append(item)

def starting_screen():
    global assassin_name, gold

    print("KINGDOM OF THE FALLEN: I")
    time.sleep(0.85)
    print("Version: BETA 1.1")
    time.sleep(1)
    print(f"Running starting scripts...starting KotF...\n")
    time.sleep(1)

    def create_character():
        global gold, assassin_name
        
        print("\n== CREATE YOUR CHARACTER ==\n")
        assassin_name = input("Your Assassin Name: ")

        print("\n== SOCIAL & FINANCIAL CLASSES ==")
        print("1. Elites (100 Gold) - EASY")
        print("2. Merchant (50 Gold) - MEDIUM")
        print("3. Peasant (25 Gold) - HARD")
        
        while True:
            #AI did this try thing.
            try:
                choice = int(input("Choose your class (1/2/3): "))
                if choice in [1, 2, 3]:
                    gold = {1: 100, 2: 50, 3: 25}[choice]
                    MONEY_CLASS.append(["Elites", "Merchant", "Peasant"][choice - 1])
                    break
                else:
                    print("Invalid choice, select 1, 2, or 3.")
            except ValueError:
                print("Invalid input, enter a number (1/2/3).")

        weapons = {
            'Primary': {1: "Dual Daggers", 2: "Hidden Blade", 3: "Longsword", 4: "Bow and Arrow", 5: "Poisoned Claw"},
            'Secondary': {1: "Throwing Knives", 2: "Smoke Bombs", 3: "Dart Gun", 4: "Mini Crossbow", 5: "Whip Dagger"}
        }
        
        #AI Made this btw, i couldn't get it to work..:(
        for w_type, w_list in weapons.items():
            print(f"\n== {w_type.upper()} WEAPONS ==")
            for key, value in w_list.items():
                print(f"{key}. {value}")
            while True:
                try:
                    choice = int(input(f"Choose your {w_type.lower()} weapon (1-5): "))
                    if choice in w_list:
                        if w_type == 'Primary':
                            set_single_item(PRIMARY_WEAPON_CLASS, w_list[choice])
                        else:
                            set_single_item(SECONDARY_WEAPON_CLASS, w_list[choice])
                        break
                    else:
                        print("Invalid choice, select 1-5.")
                except ValueError:
                    print("Invalid input, enter a number (1-5).")

    create_character()

    print("\n== CHARACTER SUMMARY ==")
    print(f"ASSASSIN'S NAME: {assassin_name}")
    print(f"CLASS: {MONEY_CLASS[0]}")
    print(f"PRIMARY WEAPON: {PRIMARY_WEAPON_CLASS[0] if PRIMARY_WEAPON_CLASS else 'None'}")
    print(f"SECONDARY WEAPON: {SECONDARY_WEAPON_CLASS[0] if SECONDARY_WEAPON_CLASS else 'None'}")
    print("\nHit ENTER to continue")
    cont33 = input("")
    
    main_selector()


def shop():
    global gold
    
    print("\n== WELCOME TO THE SHOP ==")
    print("1. Health Increaser (+50 HP) - 120 Gold")
    print("=PRIMARY WEAPON UPGRADES=")
    print("     2A: Primary Upgrade Class I (+5 damage) - 50 Gold")
    print("     2B: Primary Upgrade Class II (+10 damage) - 100 Gold")
    print("     2C: Primary Upgrade Class III (+15 damage) - 150 Gold")
    print("3: Secondary Upgrade Class I (+2.5 damage) - 25 Gold")
    print("EXIT: Leave the shop\n")
    
    while True:
        choice = input("Select an option: ")
        choice.lower()
        
        upgrades = {
            "1": (120, "HEALTH INCREASER (+50 HP)"),
            "2a": (50, "PRIMARY UPGRADE CLASS I"),
            "2b": (100, "PRIMARY UPGRADE CLASS II"),
            "2c": (150, "PRIMARY UPGRADE CLASS III"),
            "3a": (25, "SECONDARY UPGRADE CLASS I")
        }
        
        if choice in upgrades:
            cost, upgrade = upgrades[choice]
            if gold >= cost:
                gold -= cost
                PURCHASES_AND_POWERUPS.append(upgrade)
                print(f"Purchased: {upgrade}")
            else:
                calc_difference = cost - gold
                print(f"Not enough gold. You need {calc_difference} more.")
        elif choice == "exit":
            time.sleep(1)
            print("\nReturning to main menu selector...")
            time.sleep(1.5)
            main_selector()
            break
        else:
            print("Invalid choice.")


def select_game():
    global XP
    
    print("\n")
    print("=== GAME SELECTOR ===")
    print("EASY - A water beast comes out of the water and tries to kill you and your friend, Toolshookself.")
    print("       GAME INFO: minimum damage: 8, maximum damage: 32. PLAYER HEALTH: 100. Setting: alongside a beach.")
    print("       ALLOWED WEAPONS: primary weapon & secondary weapon. ")
    print("       ALLIES ALLOWED?: no")
    print("       REQIREMENTS: none")
    print("MEDIUM - You and your two friends go into an abandoned dungeon. But it's really not abandoned. ")
    print("       GAME INFO: minimum damage: [n1], maximum damage: [n2], PLAYER HEALTH: 175. Setting: abandoned dungeon.")
    print("       ALLIES ALLOWED?: yes (2)")
    print("       REQIREMENTS: none")
    print("HARD - The characters find themselves outside of a hatch that leads to an large underground chamber. ")
    print("       ALLOWED WEAPONS: primary & secondary weapons")
    print("       ALLIES ALLOWED?: yes")
    print("       REQIREMENTS: none")
    print("BOSS BATTLE - you challenge a boss to a boss battle. If the character wins, the character gets rewards.")
    print("       ALLIES ALLOWED?: no")
    print("       ALLOWED WEAPONS: primary & secondary weapons")
    print("       REQIREMENTS: 250 XP")
    game_sl_input = input("CHOOSE GAME:")    
    game_sl_input.lower() 

    if game_sl_input in ["easy", "beginner"]:
        battle1()
    elif game_sl_input in ["medium", "intermediate"]:
        battle2()
    elif game_sl_input in ["hard", "pro"]:
        battle3()
    elif game_sl_input in ["boss", "boss battle"]:
        boss_battle()
    else:
        print(f"'{game_sl_input}' is an invalid choice, please select again.")
        select_game() 


def battle2():
    # JAYCE'S NOTE: Intermediate/medium intensity battle
    global player_health
    global XP
    player_health = 175
    
    def game_duration(start_time):
        elapsed_time = time.time() - start_time  
        xp_gain = int(elapsed_time) * 25 
        return int(elapsed_time), xp_gain
    
    def b2_info():
        print("")
        time.sleep(1)
        print("MEDIUM - You and your two friends go into an abandoned dungeon. But it's really not abandoned. ")
        time.sleep(0.75)
        print("       GAME INFO: minimum damage: [n1], maximum damage: [n2], PLAYER HEALTH: 175. Setting: abandoned dungeon.")
        time.sleep(0.75)
        print("       ALLIES ALLOWED?: yes (2)")
        print("Hit any button to continue.")
        input("")
        time.sleep(0.75)
        print("\n\n")
        time.sleep(0.85)
        print("SELECTED BATTLE MODE: Medium/Intermediate")
        time.sleep(0.5)
        print("BACKSTORY: Your character is dumb enough to want to take two of his friends (Avalon, Hywell, and Orryn) along into an 'abandoned' dungeon where they are greeted with three waves of three creatures who are trying to kill the three humans.")
        print("Press ENTER to continue.")
        input("")
        time.sleep(0.5)
    b2_info()
    

    allies = {
        "Avalon": {"health": 150, "primary": "Longsword", "primary_attack_damage": random.randint(25, 35), "secondary": "Mini Crossbow", "secondary_attack_damage": random.randint(35, 45)},
        "Hywell": {"health": 125, "primary": "Dual Daggers", "primary_attack_damage": random.randint(35, 50), "secondary": "Throwing Knives", "secondary_attack_damage": random.randint(15, 33)},
        "Orryn": {"health": 210, "primary": "Bow and Arrow", "primary_attack_damage": random.randint(35, 120), "secondary": "Dart Gun", "secondary_attack_damage": random.randint(15, 50)},
    }


    enemies = [
        {"name": "Enemy 1", "health": 140, "weapon": "Rusted Axe", "attack_damage": random.randint(15, 50)},
        {"name": "Enemy 2", "health": 120, "weapon": "Poisoned Dagger", "attack_damage": random.randint(20, 40)},
        {"name": "Enemy 3", "health": 160, "weapon": "Spiked Club", "attack_damage": random.randint(25, 55)},
    ]
    
    def fight_enemy(enemy):
        global player_health
        global XP 
        start_time = time.time() 
        print(f"\nThe enemy attacks with {enemy['weapon']}.")

        while enemy["health"] > 0 and player_health > 0:
            elapsed_time, xp_gained = game_duration(start_time)
            XP += xp_gained  

            damage = random.randint(15, enemy["attack_damage"])
            player_health -= damage
            print(f"YOUR OPPONENT STRIKES, you lose {damage} HP. (Your health: {player_health}/175)")

            if player_health <= 0:
                print("\nGAME OVER. YOU DIED.")
                print(f"Time Elapsed: {elapsed_time} seconds")
                print(f"XP Gained: {XP}") 
                XP -= 75 
                time.sleep(1)
                print("\nReturning to main menu selector...")
                time.sleep(1.5)
                main_selector()

            print("\nYOUR TURN: Choose your attack")
            ally_choice = input("1. Avalon ||| 2. Hywell ||| 3. Orryn: ")
            
            if ally_choice == "1":
                attack_choice = int(input("Choose attack: 1 - Primary (Longsword), 2 - Secondary (Mini Crossbow): "))
                if attack_choice == 1:
                    damage = allies["Avalon"]["primary_attack_damage"]
                elif attack_choice == 2:
                    damage = allies["Avalon"]["secondary_attack_damage"]
                else:
                    print("Invalid choice, skipping your turn.")
                    continue
            elif ally_choice == "2":
                attack_choice = int(input("Choose attack: 1 - Primary (Dual Daggers), 2 - Secondary (Throwing Knives): "))
                if attack_choice == 1:
                    damage = allies["Hywell"]["primary_attack_damage"]
                elif attack_choice == 2:
                    damage = allies["Hywell"]["secondary_attack_damage"]
                else:
                    print("Invalid choice, skipping your turn.")
                    continue
            elif ally_choice == "3":
                attack_choice = int(input("Choose attack: 1 - Primary (Bow and Arrow), 2 - Secondary (Dart Gun): "))
                if attack_choice == 1:
                    damage = allies["Orryn"]["primary_attack_damage"]
                elif attack_choice == 2:
                    damage = allies["Orryn"]["secondary_attack_damage"]
                else:
                    print("Invalid choice, skipping your turn.")
                    continue
            else:
                print(f"Invalid ally choice '{ally_choice}', skipping your turn.")
                continue

            enemy["health"] -= damage
            print(f"\nYOU ATTACK, dealing {damage} HP. (Enemy health: {enemy['health']})")

            if enemy["health"] <= 0:
                gained_gold =+ random.randint(75, 175)
                
                time.sleep(1.5)
                print(f"\n\nYOU DEFEATED THE ENEMY!")
                print(f"Time Elapsed: {elapsed_time} seconds")
                print(f"XP Gained: {XP}") 
                print(f"GOLD GAINED: {gained_gold}")
                XP += 75  
                time.sleep(1)
                print("\nReturning to main menu selector...")
                time.sleep(1.5)
                main_selector()

    for enemy in enemies:
        fight_enemy(enemy)

    print("\nWAVE ONE CLEARED...")
    time.sleep(1.5)
    print("WAVE 2 APPROACHING...")
    time.sleep(1)

    
    wave_2_enemies = [
        {"name": "Flaming Sword", "health": 180, "weapon": "Flaming Sword", "attack_damage": 60},
        {"name": "Crossbow", "health": 150, "weapon": "Crossbow", "attack_damage": 50},
        {"name": "Battle Axe", "health": 170, "weapon": "Battle Axe", "attack_damage": 65},
    ]

    for enemy in wave_2_enemies:
        fight_enemy(enemy)

    print("\nWAVE 2 CLEARED")
    time.sleep(0.5)
    print("WAVE 3 IS NOW APPROACHING...")
    time.sleep(1)

    
    wave_3_enemies = [
        {"name": "Dark Magic Staff", "health": 200, "weapon": "Dark Magic Staff", "attack_damage": 75},
        {"name": "Greatsword", "health": 220, "weapon": "Greatsword", "attack_damage": 80},
        {"name": "Demonic Claws", "health": 250, "weapon": "Demonic Claws", "attack_damage": 90},
    ]

    for enemy in wave_3_enemies:
        fight_enemy(enemy)

    print(f"\nCONGRATULATIONS! You survived the dungeon battle, your remaining health {player_health}/175")

def battle3():
    # JAYCE'S NOTE: Very hard battle.
    global player_health
    player_health = 150 

    def b3_info():
        print("\n\n")
        time.sleep(0.85)
        print("HARD - The characters find themselves outside of a hatch that leads to an large underground chamber. ")
        time.sleep(0.75)
        print("       ALLOWED WEAPONS: primary & secondary weapons")
        time.sleep(0.75)
        print("       ALLIES ALLOWED?: yes")
        time.sleep(0.75)
        print("SELECTED BATTLE MODE: Hard/Intense")
        time.sleep(0.5)
        print("BACKSTORY: You and your two other beings walk aross a hatch that they all fall into a very large chamber. They have to figure out how to get out, but they are going to be hit with three waves of creatures in order to get out of the chamber. If they win, they get out. If they don't, they die.")
        print("Press ENTER to continue.")
        input("")
        time.sleep(0.75)
    b3_info()

    avalon_health = 150
    avalon_primary = "Longsword"
    avalon_primary_attack_damage = random.randint(25, 40)
    avalon_secondary = "Mini Crossbow"
    avalon_secondary_attack_damage = random.randint(35, 55)

    hywell_health = 125
    hywell_primary = "Dual Daggers"
    hywell_primary_attack_damage = random.randint(40, 60)
    hywell_secondary = "Throwing Knives"
    hywell_secondary_attack_damage = random.randint(20, 40)

    orryn_health = 210
    orryn_primary = "Bow and Arrow"
    orryn_primary_attack_damage = random.randint(40, 130)
    orryn_secondary = "Dart Gun"
    orryn_secondary_attack_damage = random.randint(25, 55)

    def fight_enemy(enemy_health, enemy_weapon, enemy_damage):
        global player_health
        print(f"\nThe enemy attacks with {enemy_weapon}.")
        
        while enemy_health > 0 and player_health > 0:
            damage = random.randint(20, enemy_damage) 
            player_health -= damage
            print(f"YOUR OPPONENT STRIKES, you lose {damage} HP. (Your health: {player_health}/150)")

            if player_health <= 0:
                time.sleep(1.5)
                print("\nGAME OVER. YOU DIED.")
                print(f"Time Elapsed: {elapsed_time} seconds")
                XP -= 75 #(JAYCE'S NOTE: THIS IS THE PENTALTY FOR DYING! EL BOZO)
                print(f"XP Gained: {XP}") 
                time.sleep(1)
                print("\nReturning to main menu selector...")
                time.sleep(1.5)
                main_selector()

            print(f"\nYOUR TURN: 1 {avalon_primary} ||| 2 {avalon_secondary}")
            attack_choice = int(input(""))

            if attack_choice == 1:
                damage = avalon_primary_attack_damage
            elif attack_choice == 2:
                damage = avalon_secondary_attack_damage
            else:
                print(f"'{attack_choice}' is invalid => skipping your turn.")
                continue

            enemy_health -= damage
            print(f"\nYOU ATTACK, dealing {damage} HP. (Enemy health: {enemy_health})")

            if enemy_health <= 0:
                print("YOU DEFEATED THE ENEMY!")
                time.sleep(1)
                print("\nReturning to main menu selector...")
                time.sleep(1.5)
                main_selector()


    fight_enemy(180, "Rusted Axe", 55)
    fight_enemy(160, "Poisoned Dagger", 45)
    fight_enemy(200, "Spiked Club", 60)

    print("\nWAVE ONE CLEARED...")
    time.sleep(1.5)
    print("WAVE 2 APPROACHING...")
    time.sleep(1)


    fight_enemy(230, "Flaming Sword", 80)
    fight_enemy(220, "Crossbow", 70)
    fight_enemy(240, "Battle Axe", 85)

    print("\nWAVE 2 CLEARED...")
    time.sleep(0.5)
    print("WAVE 3 IS NOW APPROACHING...")
    time.sleep(1)


    fight_enemy(300, "Dark Magic Staff", 95)
    fight_enemy(350, "Greatsword", 100)
    fight_enemy(400, "Demonic Claws", 120)

    print(f"\nCONGRATULATIONS! You survived the dungeon battle, your remaining health: {player_health}/150")


def main_selector():
    global gold
    global XP
    
    while True:
        print("")
        print(f"== {assassin_name.upper()}'S STATISTICS == ")
        print(f"GOLD: {gold}")
        print(f"XP: {XP}")
        print("")
        print("==GAME TRAJECTORY CONTROLS ==")
        print("1. Enter a battle")
        print("   1B: Enter Boss Battle")
        print("2. Enter the shop")
        print("3. Info about the game")
        print("4. How to Play (different than info.)")
        print("5. END GAME")
        
        choice = input("Choose an option: ")
        choice.lower() 
        
        if choice == "1" or choice == "enter a battle":
            time.sleep(1)
            select_game()
            break
        elif choice == "1B" or choice == "enter boss battle":
            time.sleep(1)
            boss_battle()
            break
        elif choice == "2" or choice == "enter the shop":
            time.sleep(1)
            shop()
            break
        elif choice == "3" or choice == "info":
            time.sleep(1)
            print("\n")
            print("Enjoy this AI-written info about my game!")
            time.sleep(1)
            print("In Kingdom of the Fallen: I, you create your assassin by selecting a name, class, and weapons. Your journey begins with battles where you can use your primary and secondary weapons to defeat enemies. You earn gold to upgrade your health and weapons at the shop, enhancing your abilities for tougher challenges ahead. Make key decisions in battle, manage your resources, and fight to survive in this action-packed RPG!")
            input("Press ANY KEY to loop back to the selector.")
        elif choice == "4" or choice == "how to play":
            time.sleep(1)
            print("\n")
            print("Enjoy this ChatGPT made text on how to play my game.")
            time.sleep(2)
            print("""
How to Play Kingdom of the Fallen: I

1. Create Your Character: 
(This process is already done.)
   - Choose your assassin's name.
   - Select a class: Elites (easy), Merchant (medium), or Peasant (hard).
   - Pick your primary and secondary weapons from a variety of choices.

2. Battle Enemies: 
   - Engage in battles, like facing a water beast. Use your weapons to attack and defend.
   - Your health will decrease with each attack, so manage your resources wisely.
   - Defeat enemies to progress and gain rewards.

3. Visit the Shop:
   - Use your gold to buy health boosts or upgrade your weapons.
   - Choose between primary and secondary upgrades to enhance your damage output.
   - Be careful with your spending to ensure you're ready for tougher battles.

4. Make Strategic Decisions: 
   - Choose your next move wisely—whether to fight or shop. Each decision impacts your survival.
   - Keep an eye on your health and gold, and plan your upgrades accordingly.

Stay sharp, manage your resources, and defeat powerful foes to become the ultimate assassin!
""")
            input("Press ANY KEY to loop back to the selector.")

        elif choice == "5" or "end game":
            print("")
            print("ARE 100% SURE YOU WOULD LIKE TO END THE GAME? Everything (XP and gold) will be reset. You can not get this back at any point!")
            print("Please type 'yes' in all uppercase.")
            end_game_input = input("")
            
            if end_game_input == "YES":
                print("")
                print("GAME ENDED.")
                break
            
        # else:
            # print("Invalid choice. Please enter 1 or 2.")


def battle1():
    #JAYCE'S NOTE: Beginner/Easy battle
    global player_health
    global XP
    
    def game_duration(start_time):
        elapsed_time = time.time() - start_time  
        xp_gain = int(elapsed_time) * 25 
        return int(elapsed_time), xp_gain

    def b1_info():
        print("\n\n")
        time.sleep(0.85)
        print("SELECTED BATTLE MODE: Easy")
        time.sleep(1)
        print("EASY - A water beast comes out of the water and tries to kill you and your friend, Toolshookself.")
        time.sleep(1)
        print("       GAME INFO: minimum damage: 8, maximum damage: 32. PLAYER HEALTH: 100. Setting: alongside a beach.")
        time.sleep(1)
        print("       ALLOWED WEAPONS: primary weapon & secondary weapon. ")
        time.sleep(1)
        print("       ALLIES ALLOWED?: no")
        time.sleep(0.5)
        print("BACKSTORY: Your character is walking along the beach with his friend, Toolshook, a monster comes out of the water and is after the assassin and his friend, Toolshook. You must defend you and your friend from the water beast that came out of the water.")
        print("Press ENTER to continue.")
        con3 = input("")
        time.sleep(0.5)
    b1_info()
    
    print("\nThe water beast has swung its arm at you.")
    enemy_health = 100
    start_time = time.time() 
    
    while enemy_health > 0 and player_health > 0:
        
        elapsed_time, xp_gained = game_duration(start_time)
        XP += xp_gained  

        damage = random.randint(15, 25)
        player_health -= damage
        water_beast_random_attack_events = ["swung its arm at you.", "spit ice fire at you.", "stomped, causing you to fall over backwards due to the force.", "Blew air at you, causing you to fall."]
        select = random.choice(water_beast_random_attack_events)
        print(f"The Water Beast {select}. Causing you to lose {damage} HP.")
        print("YOUR HEALTH IS NOW: {player_health}/100)")
        
        if player_health <= 0:
            time.sleep(1.5)
            print("\nGAME OVER. YOU DIED.")
            print(f"Time Elapsed: {elapsed_time} seconds")
            XP -= 75 #(JAYCE'S NOTE: THIS IS THE PENTALTY FOR DYING! EL BOZO)
            print(f"XP Gained: {XP}") 
            time.sleep(1)
            print("\nReturning to main menu selector...")
            time.sleep(1.5)
            main_selector()
        
        print(f"\nYOUR TURN: 1 {PRIMARY_WEAPON_CLASS[0] if PRIMARY_WEAPON_CLASS else 'None'} ||| 2 {SECONDARY_WEAPON_CLASS[0] if SECONDARY_WEAPON_CLASS else 'None'}")
        attack_choice = input("")
        
        if attack_choice == "1":
            damage = random.randint(15, 35)
        elif attack_choice == "2":
            damage = random.randint(8, 15)
        else:
            print("INVALID MOVE - skipping your turn.")
            continue
        
        enemy_health -= damage
        print("\n")
        print(f"YOU ATTACK, causing {damage} HP to the water beast\n(Beast's health is now: {enemy_health}/100)")
        print("\n== HEALTH STATS: ==")
        print(f"BEAST'S HEALTH: {enemy_health}/100")
        print(f"YOUR HEALTH: {player_health}/100\n")
        
        if enemy_health <= 0:
            gained_gold =+ random.randint(75, 175)
            
            time.sleep(1.5)
            print("== END GAME STATS == ")
            print("WINNER: you")
            print(f"GAME ELAPSED TIME: {elapsed_time} seconds")
            print(f"XP GAINED: {XP}") 
            print(f"GOLD GAINED {gained_gold}")
            time.sleep(1)
            print("\nReturning to main menu selector...")
            time.sleep(1.5)
            main_selector()


def boss_battle():
    global XP
    global player_health
    player_health = 1150
    
    if XP >= 250:
        def bb_details():
            print("\n\n")
            print("== BOSS BATTLE DETAILS ==")
            print("BACKSTORY: You have challenged a boss to a fight... This is the ultimate determination of your assassin skills.")
            print("Hit ANY KEY to continue.")
            input("")
            
        bb_details()
        
        print("== BOSS BATTLE == \n")

        def game_duration(start_time):
            elapsed_time = time.time() - start_time  
            xp_gain = int(elapsed_time) * 25 
            return int(elapsed_time), xp_gain

        print("\nThe FINAL BOSS steps forward, each step the ground shakes.")
        time.sleep(1)
        initial_damage = random.randint(100, 250)
        player_health -= initial_damage
        print(f"The FINAL BOSS stomps, causing you to fall over, taking {initial_damage} damage. Leaving you with {player_health}/1150.")
        time.sleep(1)
        
        boss_health = 1350
        start_time = time.time()
        
        while boss_health > 0 and player_health > 0:
            elapsed_time, xp_gain = game_duration(start_time)
            XP += xp_gain
            
            boss_damage = random.randint(250, 350)
            player_health -= boss_damage 
            
            boss_random_attack_events = [
                "stomped again, causing you to fall over.", 
                "breathed fire at you.", 
                "swung around, swinging his massive tail at you.", 
                "made a loud roar, summoning two pterodactyls that drop acidic poop on you."
            ]
            boss_attack_event = random.choice(boss_random_attack_events)
            
            print(f"\nThe FINAL BOSS {boss_attack_event} You take {boss_damage} damage to this attack!")
            time.sleep(1)
            print(f"Your remaining health: {player_health}/1150")
            time.sleep(1)

            if player_health <= 0:
                print("\n\n")
                time.sleep(1.5)
                print("GAME OVER, YOU SUCCUMBED TO THE FINAL BOSS...")
                print(f"TIME ELAPSED: {elapsed_time} seconds")
                XP -= 250
                print(f"XP GAIN: {XP}")
                time.sleep(1)
                print("\nReturning to main menu selector...")
                time.sleep(1.5)
                main_selector()
            
            print(f"\nYOUR TURN: 1 {PRIMARY_WEAPON_CLASS[0] if PRIMARY_WEAPON_CLASS else 'None'} ||| 2 {SECONDARY_WEAPON_CLASS[0] if SECONDARY_WEAPON_CLASS else 'None'}")
            attack_choice = input("Choose your attack (1 or 2): ")

            if attack_choice == "1":
                damage = random.randint(150, 275)
            elif attack_choice == "2":
                damage = random.randint(75, 215)
            else:
                print("INVALID MOVE - Your turn has been skipped.")
                continue
            
            boss_health -= damage
            print("\n")
            print(f"YOU ATTACK: causing {damage} damage to the final boss.")
            print(f"THE FINAL BOSS NOW HAS: {boss_health}/1350")
            print(f"YOUR HEALTH: {player_health}/1150")

            if boss_health <= 0:
                gained_gold = random.randint(75, 250)
                
                print("\n\n")
                time.sleep(1.5)
                print("== END GAME STATS ==")
                print("WINNER: You")
                print(f"GAME ELAPSED TIME: {elapsed_time} seconds")
                XP += 1500
                print(f"XP GAINED: {XP}")
                print(f"GAINED GOLD: {gained_gold}")
                time.sleep(1)
                print("\nReturning to main menu selector...")
                time.sleep(1.5)
                main_selector()
        
    else:
        xp_needed_for_bb = 250 - XP
        print("Unable to fight in the boss battle. You need at least 250 XP.")
        print(f"Remaining XP needed: {xp_needed_for_bb}")


starting_screen()
