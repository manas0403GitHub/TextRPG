import random
import time, os

points = random.randint(5, 10)
Health = random.randint(35, 100)
Strength = random.randint(20, 200)
i = ""
SwordsName = ["Stone Sword", "Ruby Sword", "Steel Sword", "Platinum Sword", "Gold Sword", "Diamond Sword"]
CostsofSwords = {"Stone Sword": 15, "Ruby Sword": 29, "Steel Sword": 45, "Platinum Sword": 75, "Gold Sword": 100, "Diamond Sword": 150}

SpellsName = ["Poison Spell", "Affect Spell", "Strength Spell"]
CostsofSpells = {"Poison Spell": 12, "Affect Spell": 20, "Strength Spell": 30}

typeofSword = ["Default Sword"]
typeofSpell = []

os.system('cls' if os.name == 'nt' else 'clear')
print(f"{i: ^65}TextRPG")
print("""S(Start)➡️
      Q(Quit)❌""")
menu = input("> ")

if menu == 'S':
    name = input("Name: ")
    print("")

    print(f"""Name: {name}
    Health: {Health}
    Strength: {Strength}""")

    print("Game Starts!")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        def game_loop():
            mainStart = 'Yes'
            if mainStart == 'Yes':
                print("Where do you want to go?W(Store🏪), S(Forest🌲), A(Next Side◀️), D(Next Side▶️)")
                go = input("> ")

            mainStart = 'No'
            if go == 'W':
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"Points: {points}")
                    print(f"""Welcome to the Store!🏬
                        want do you want to buy?
                        
                        SWORDS:
                            1. {SwordsName[0]}(SS): Strength- 35, Cost: {CostsofSwords['Stone Sword']} 
                            2. {SwordsName[1]}(RS): Strength- 50, Cost: {CostsofSwords['Ruby Sword']}
                            3. {SwordsName[2]}(STS): Strength- 75, Cost: {CostsofSwords['Steel Sword']}
                            4. {SwordsName[3]}(PS): Strength- 100, Cost: {CostsofSwords['Platinum Sword']}
                            5. {SwordsName[4]}(GS): Strength- 150, Cost: {CostsofSwords['Gold Sword']}
                            6. {SwordsName[5]}(DS): Strength- 200, Cost: {CostsofSwords['Diamond Sword']}
                        
                        SPELLS:
                            1. {SpellsName[0]}(PS): Strength- 20, Cost: {CostsofSpells['Poison Spell']}
                            2. {SpellsName[1]}(AS): Can affect you or the enemy, Cost: {CostsofSpells['Affect Spell']}
                            3. {SpellsName[2]}(SSS): Strength Power- 35, Cost: {CostsofSpells['Strength Spell']}
                        """)
                    
                    buy = input("N(Exit)> ")
                    if buy == 'N':
                        mainStart = 'Yes'

                    elif not points >= min(CostsofSwords.values()):
                        print("Sorry but, you don't have enough points for a sword.")
                        time.sleep(0.5)
                        print("Buy something else")
                        continue

                    elif not points >= min(CostsofSpells.values()):
                        print("Sorry but, you don't have enough points for a spell.")
                        time.sleep(0.5)
                        print("Buy something else")
                        continue

                    elif points >= CostsofSwords["Stone Sword"]:
                        print("You have buyed the Stone Sword!")
                        typeofSword.append("Stone Sword")
                        print("Contiuning...")
                        continue

                    elif points >= CostsofSwords["Ruby Sword"]:
                        print("You have buyed the Ruby Sword!")
                        typeofSword.append("Ruby Sword")
                        print("Contiuning...")
                        continue

                    elif points >= CostsofSwords["Steel Sword"]:
                        print("You have buyed the Steel Sword!")
                        typeofSword.append("Steel Sword")
                        print("Contiuning...")
                        continue
                    
                    elif points >= CostsofSwords["Platinum Sword"]:
                        print("You have buyed the Platinum Sword!")
                        typeofSword.append("Platinum Sword")
                        print("Contiuning...")
                        continue
                    
                    elif points >= CostsofSwords["Gold Sword"]:
                        print("You have buyed the Gold Sword!")
                        typeofSword.append("Gold Sword")
                        print("Contiuning...")
                        continue

                    elif points >= CostsofSwords["Diamond Sword"]:
                        print("You have buyed the Diamond Sword!")
                        typeofSword.append("Diamond Sword")
                        print("Contiuning...")
                        continue


                    if points >= CostsofSpells["Poison Spell"]:
                        print("You have buyed the Poison Spell!")
                        typeofSword.append("Diamond Sword")
                        print("Contiuning...")
                        continue

                    elif points >= CostsofSpells["Affect Spell"]:
                        print("You have buyed the Affect Spell!")
                        typeofSpell.append("Affect Spell")
                        print("Contiuning...")
                        continue

                    elif points >= CostsofSpells["Strength Spell"]:
                        print("You have buyed the Strength Spell!")
                        typeofSpell.append("Strength Spell")
                        print("Contiuning...")
                        continue

                    elif points >= CostsofSpells["Invincible Spell"]:
                        print("You have buyed the Invincible Spell!")
                        typeofSpell.append("Invincible Spell")
                        print("Contiuning...")
                        continue


            elif go == 'S':
                os.system('cls' if os.name == 'nt' else 'clear')

                print("You are in the forest")
                while True:
                    print("Where do you want to move? W(up), S(Exit), A(left), D(right)")
                    move = input("> ")

                    if move not in ['A', 'S', 'W', 'D']:
                        print("Invalid move. Please enter W, A, S, or D.")
                        continue
                    if move == 'S':
                        print("Exiting Forest")
                        time.sleep(1)

                        os.system('cls' if os.name == 'nt' else 'clear')
                        game_loop()

                    elif move == 'A':
                        print("Entering Battle...")
                        time.sleep(1.5)
                        os.system('cls' if os.name == 'nt' else 'clear')

                        enemy_names = [
        "Malgorth the Malevolent", "the Abyssal",
        "Vorax the Venomous",
        "Drakoth the Dreaded",
        "Syraxis the Shadowlord",
        "Sylvaan the Sinister"
    ]                   
                        
                        random_enemy_names = random.choice(enemy_names)
                        enemy_Health = random.randint(6, 150)
                        enemy_Strength = random.random(15, 100)
                        print(f"""Name: {random_enemy_names}
                            Health: {enemy_Health}
                            Strength: {enemy_Strength}""")
                        print("ATTACK START!")
                        if random.randint(1, 3) == 1:
                            print(f"{random_enemy_names} attacks with a sword.")
                            if enemy_Strength >= 100:
                                Health -= random.randint(5*4, 5*8)

                            elif enemy_Strength <= 100:
                                Health -= random.randint(5*2, 5*4)

                            elif enemy_Strength <= 35:
                                Health -= random.randint(3*4, 3*8)

                        elif random.randint(1, 3) == 2:
                            print(f"{random_enemy_names} blows fire.")
                            if enemy_Strength >= 100:
                                Health -= random.randint(5*6, 5*8)

                            elif enemy_Strength <= 100:
                                Health -= random.randint(5*4, 5*6)

                            elif enemy_Strength <= 35:
                                Health -= random.randint(3*5, 3*8)

                        elif random.randint(1, 3) == 3:
                            print(f"{random_enemy_names} puts a spell on you.")
                            if enemy_Strength >= 100:
                                Health -= random.randint(5*3, 5*5)

                            elif enemy_Strength <= 100:
                                Health -= random.randint(5*2, 5*4)

                            elif enemy_Strength <= 35:
                                Health -= random.randint(3*2, 3*6)

                            print("What do you want to attack with? Sword(WS), Spell(S), Exit(E)")
                            attack = input("> ")
                                
                            if attack == 'WS':
                                print("You have: ")
                                for Swords in typeofSword:
                                    print(Swords)
                                enter = input("Enter a Sword name: ")
                                print("You attack with a sword.")

                                if enter == "Default Sword":
                                    enemy_Health -= Strength*5/20 or Strength*5/40
                                    
                                elif enter == "Stone Sword":
                                    enemy_Health -= round(Strength*7/27) or round(Strength*7/47)
                                    
                                elif enter == "Ruby Sword":
                                    enemy_Health -= round(Strength*10/30) or Strength*10/40

                                elif enter == "Steel Sword":
                                    enemy_Health -= Strength*15/45 or Strength*7/40

                                elif enter == "Platinum Sword":
                                    enemy_Health -= round(Strength*20/65) or Strength*20/60

                                elif enter == "Gold Sword":
                                    enemy_Health -= round(Strength*30/95) or Strength*30/90

                                elif enter == "Diamond Sword":
                                    enemy_Health -= round(Strength*40/135) or Strength*40/130
                                    
                                elif attack == 'S':
                                    print("You attack with a spell of poison.")
                                    enemy_Health -= max(Strength*7/20, Strength*7/40)

                            elif attack == "S":
                                print("You have: ")
                                for Spells in typeofSpell:
                                    print(Spells)
                                enter = input("Enter a Spell name: ")
                                print("You attack with a sword.")

                                if enter == "Poison Spell":
                                    enemy_Health -= round(Strength*5/10) or Strength*5/10

                                elif enter == "Affect Spell":
                                    if random.randint(1, 2) == 1:
                                        enemy_Health -= round(Strength*5/10) or Strength*5/10
                                    elif random.randint(1, 2) == 2:
                                        Health -= 10 or 20

                                elif enter == "Strength Power":
                                    Strength += 20 or 30
                                
                            print(f"Enemy Health: {enemy_Health}")
                            print(f"Your Health: {Health}")
                                
                            if Health <= 0 or enemy_Health <= 0:
                                continue
                                
                            elif Health > 0:
                                game_loop()

                        elif enemy_Health >= 0:
                            print("You win!")
                            print("You get ", random.randint(15, 30), " points!")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            game_loop()

            elif go == 'A' or go == 'D':
                game_loop()  
        game_loop()      
