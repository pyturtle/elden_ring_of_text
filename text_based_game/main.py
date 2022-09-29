#Name:Nathan
#Date:1/24/2022
#Program Name: RPG WORLD
#Purpose: Show rpg making skills 


#This took 10 hours everyday for 5 days. Everything in this is written from sratch nothing had been forked


#imports
import colorama
import images
import os
import random as rand
from time import sleep 
import classes
from functions import healing,bleed_ability,rage_ability,charge_ability
from functions import fear_ability,fight,slow_print,validate,add_to_inventory
from functions import stats,armoury,shop,poison_ability,bite_ability,b_bite_ability
from functions import swarm_ability,blind_ability,fire_ability,dive_ability,claw_ability
import time


cls = lambda: os.system('cls')

#No forks all written from scratch


########################################################################### enemy
#Units
def s_ghoul(lv):
    enemy = classes.enemy("ghoul",65+20*lv,(15+lv*4,20+lv*4),"alive",(40+lv*4,50+lv*4),(10+lv*3,15+lv*3),strength = 1, weakness = 3,loot = None)
    return (enemy)
def s_thief(lv):
    enemy = classes.enemy("thief",65+20*lv,(15+lv*4,20+lv*4),"alive",(40+lv*4,50+lv*4),(10+lv*3,15+lv*3),strength = 1, weakness = 2,loot = None)
    return (enemy)
def s_knight(lv):
    enemy = classes.enemy("undead_skeleton_knight",50+30*lv,(10+lv*4,20+lv*4),"undead",(35+lv*3,45+lv*3),(20+lv*3,30+lv*3),strength = 2, weakness = 3,loot = None)
    return (enemy)
def s_undead(lv):
    enemy = classes.enemy("undead_skeleton",45+15*lv,(5+lv*4,15+lv*4),"undead",(25+lv*2,35+lv*2),(15+lv*3,25+lv*3),strength = 3, weakness = 0,loot = None)
    return (enemy)
def s_spider(lv):
    enemy = classes.enemy("spider",45+20*lv,(5+lv*4,15+lv*4),"incect",(25+lv*2,35+lv*2),(15+lv*3,25+lv*3),strength = 1, weakness = 3,loot = None)
    return (enemy)
def m_spider(lv):
    enemy = classes.enemy("mother_spider",55+30*lv,(10+lv*4,15+lv*4),"incect",(25+lv*4,35+lv*4),(20+lv*3,27+lv*3),strength = 2, weakness = 0,loot = None)
    return (enemy)
def s_bat(lv):
    enemy = classes.enemy("bat",30+15*lv,(10+lv*4,20+lv*4),"alive",(15+lv*4,30+lv*4),(15+lv*2,25+lv*2),strength = 1, weakness = 2,loot = None)
    return (enemy)
def b_minotaur(lv):
    enemy = classes.enemy("minotaur",70+45*lv,(30+lv*4,35+lv*4),"alive",(35+lv*4,40+lv*4),(35+lv*3,40+lv*3),strength = 1, weakness = 0,loot = "Bull horn")
    return (enemy)
def b_skeleton_leader(lv):
    enemy = classes.enemy("undead_skeleton_leader",75+45*lv,(15+lv*4,25+lv*4),"undead",(35+lv*3,45+lv*3),(20+lv*3,30+lv*3),strength = 3, weakness = 0,loot = "Golden Skull")
    return (enemy)
def b_dragon(lv):
    enemy = classes.enemy("dragon",100+80*lv,(20+lv*7,30+lv*7),"alive",(35+lv*3,45+lv*3),(20+lv*5,30+lv*5),strength = 1, weakness = 0,loot = "Chalice")
    return (enemy)
def s_zombie(lv):
    enemy = classes.enemy("zombie",45+30*lv,(5+lv*4,15+lv*4),"undead",(25+lv*4,35+lv*5),(15+lv*3,25+lv*3),strength = 2, weakness = 0,loot = None)
    return (enemy)
def m_spitfire(lv):
    enemy = classes.enemy("spitfire",50+30*lv,(30+lv*4,30+lv*4),"undead",(25+lv*4,35+lv*5),(15+lv*4,25+lv*4),strength = 1, weakness = 0,loot = None)
    return (enemy)
###########################################
#level func
def level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp):
    while xp >= xp_base:
        print("You leveled up!!!!!")
        slow_print("You gained 10 more base hp",0.01,1,clear = False)
        slow_print("You gained 5 more atk dmg\n",0.01,1,clear = False)
        xp -= xp_base 
        xp_base = xp_base + 15
        dmg += 5
        lv += 1
        if armour_hp != 0:
            base_hp = base_hp + 10 - armour_hp
            armour_hp = int((base_hp/5)*armour_lv)
            base_hp = base_hp + armour_hp
        else:
            base_hp += 10
        hp += 10
        if lv == 3:
            slow_print(colorama.Fore.BLUE+"You gained a new ability! you now have healing magic. \nThis uses 1 mana pot but gets you to full hp\n",0.06,delay=3,clear = False)
        if lv == 6:
            slow_print(colorama.Fore.BLUE+"You gained a new ability! Using magic healing now stops all enemy pasives ex(poison,bleeding,burning,fear)\n"+ colorama.Fore.RESET+" ",0.06,delay=3,clear = False)
        if lv == 9:
            slow_print(colorama.Fore.BLUE+"You gained a new ability! you can now miss twice with the bow however your hit rate is lowered\n"+ colorama.Fore.RESET+" ",0.06,delay=3,clear = False)
        if lv == 12:
            slow_print(colorama.Fore.BLUE+"You gained a new ability! magic attack now does burn damage\n"+ colorama.Fore.RESET+" ",0.06,delay=3,clear = False)

    return (xp,dmg,base_hp,armour_hp,xp_base,lv,hp)



###############################################################################################
    
            
            
        
    
#Varible decleration
###########################################################################
while True:
    timeStart = time.time()
    kings_offer = ["handbook","armour","mana pots","healing pots","totem of undying","lucky coin","paper hat"]
    inventory = [] #default is none # testing "handbook","totem of undying","lucky coin","paper hat"
    gold = 50 #default is 50 # testing 500
    healing_pots = 2 #default is 2 # testing 50
    arrows = 15 #default is 10 # testing 500
    mana_pots = 1 #default is 1 # testing 50
    critrate = 0 #default is 0 
    base_hp = 100 #default is 100 # testing 50
    hp = base_hp 
    armour_hp = 0 #default is 0
    armour_lv = 0
    dmg = 10 #default is 10
    xp = 0 #default is 0 # testing = 900,1900,2800
    lv = 0 # default = 0
    xp_base = 20 # default is 20
    day = 0 #default is 0
    distance = 0 #default is 0  testing = 165,240
    rations = 3 #default is 3
    dead = False
    legit = 0
#Lore section
##########################################################################
    #These are for comenting out section when testing thing"""
    print("Disclaimer: The whole game may take a very long time you can start is second or third stage if you just want to do parts")
    print("You can answer any yes/no question with y/n if you want")
    lore = validate(["yes","no","y","n"],"Do you want to skip the lore?\n")
    cls()
    if lore in ["n","no"]:  
        slow_print(images.title,0.004,clear = False,audio = False)
        print("By Nathan")
        sleep(3)
        cls()
        
        slow_print("For years a great plague had been ravenging these lands.",0.06)
        
        print(images.king)
        
        slow_print("The king has tasked you with retrieving a golden chalice which can cure the sickness.\nHe demands you be swift(20days) as his family is sick!",0.06)
        
        print(images.mountains)
        
        slow_print("located In the Highlands, you deduct that this journey may take up to 25 days",0.06)
    
        slow_print("The king has granted you 3 rations of food \n50 gold shekels, \n5 arrows, \nand 3 items you can choose to take along with you.",0.06,5)
    print(kings_offer)
    print("\nHandbook: Gives enemy weaknesses, strengths, and abilities.")
    print("Armour: Adds 20% more hp on top of base hp")
    print("Mana pots: gives you 5 mana pots each pot allows the use of magic")
    print("healing pots: gives you 10 healing pots each pot regenerates 2/5 hp")
    print("Totem of undying: gives an extra life")
    print("Lucky coin: increases critrate and gold drops")
    print("Paper hat: just a cool hat\n\n")
    print("You can also chose nothing to make the game more difficult")
    for i in range(3):
        item_choice = validate(kings_offer,"What is item number " + str(i+1) + " you want:")
        if item_choice == "armour":
            armour_lv += 1
            base_hp -= armour_hp
            armour_hp = (base_hp//5)*armour_lv
            base_hp = int(base_hp + armour_hp)
            hp = base_hp
            slow_print("Armour has been added to your personel\n",0.03,clear=False)
            print("Armour_lv:",armour_lv)
            print(images.armour)
            sleep(1)
        elif item_choice == "mana pots":
            mana_pots+=5
            slow_print("mana pots have been added to your inventory\n",0.03,clear=False)
            print(images.mana_pots)
            sleep(1)
        elif item_choice == "healing pots":
            healing_pots+=9
            slow_print("Healing pots have been added to your inventory\n",0.03,clear=False)
            print(images.healing_pots)
            sleep(1)
        elif item_choice != None:
            add_to_inventory(item_choice,inventory,kings_offer)
            if item_choice == "handbook":
                print(images.handbook)
            elif item_choice == "paper hat":
                print(images.paper_hat)
            elif item_choice == "totem of undying":
                print(images.totem)
            elif item_choice == "horse":
                print(images.horse)
            elif item_choice == "lucky coin":
                print(images.lucky_coin)
        print(kings_offer)
    stall=input("Press enter to continue:")
    cls()
    
    stats(hp,base_hp,healing_pots,mana_pots,arrows,xp,xp_base,lv,gold,day,distance,rations,armour_lv,"Make the trek across the fields",150)
    
    stall=input("\nPress enter to continue:")
    
    weapons_guide = validate(["yes","no","y","n"],"Do you want A guide on how to play? ")
    if weapons_guide in ["yes","y"]:
        print("The sword does your current dmg and on a crit will do dmg*2.5. When the sword does not crit the crit rate will go up by 10% and on a crit it will go back to its base critrate")
        print("The bow will do a guaranteed dmg and has a 1/2 chnce of hitting again this is repeated till a miss")
        print("The Magic does a straight dmg*2.5.")
        stall=input("Press enter to continue:")
    cls()
    
    starter_kit = validate(["yes","no","y","n"],"Do you want a starter kit? \n")
    if starter_kit in ["yes","y"]:
        print("+50 gold \n+3 healing pots\n+5 arrows\n+2 mana pots\n+1 totem of undying\n+1 handbook")
        gold += 50
        healing_pots += 3
        arrows += 5
        mana_pots += 2
        inventory.append("totem of undying")
        inventory.append("handbook")
        rations = 5
        legit = 1

    slow_print("Before the trip you stop by the shop\n",0.02,clear = False)    
    gold,arrows,healing_pots,mana_pots,rations =shop(inventory,gold,arrows,healing_pots,mana_pots,rations)
    


        
    
    


##These are for comenting out section when testing thing"""




    
##########################################################################################################################################################################################################
    #this is a major while loop for the first 150 kms of the journy through a wasteland
    rest = True
    boss_killed = False # set to true for area skip / testing
    world_two = validate(["yes","no","y","n"],"Do you want a start in the second stage? \n")
    if world_two in ["yes","y"]:
        inventory.append("Golden Skull")
        boss_killed = True
        xp = 560
        gold = 420
        day = 10
        legit = 1
        distance = 165
    world_three = validate(["yes","no","y","n"],"Do you want a start in the third stage? \n")
    if world_three in ["yes","y"]:
        inventory.append("Bull horn")
        inventory.append("Golden Skull")
        boss_killed = True
        xp = 1360
        gold = 700
        day = 17
        legit = 1
        distance = 255 #255,270,285

        
    while boss_killed == False:
        if rest == True:
            day = day + 1
        
        
        if distance in range(0,76):
            mobs_perday = rand.randint(0,2)# how many mobs will be seen 0,1
        elif distance in range(76,140):
            mobs_perday = rand.randint(1,2)# how many mobs will be seen 0,2 
        elif distance >= 140:
            mobs_perday = 2
        stats(hp,base_hp,healing_pots,mana_pots,arrows,xp,xp_base,lv,gold,day,distance,rations,armour_lv,"Make the trek across the fields",150)
        print(inventory)

        #if merchant appears
        merchant_appear = 4
        if rest == True and distance != 0 and merchant_appear > 1:
            merchant =validate(["yes","no","y","n"],"\nYou stumble upon a wandering merchant would you like to shop?\n")
            if merchant in ["y","yes"]:
                gold,arrows,healing_pots,mana_pots,rations = shop(inventory,gold,arrows,healing_pots,mana_pots,rations)
            if armour_lv < 2:
                upgrade = validate(["yes","no","y","n"],"\nYou stumble upon an forgery would you like to upgrade your armour?\nCost:"+str(armour_lv*30+60)+"\n")
                if upgrade in ["y","yes"]:
                    gold,base_hp,armour_hp,lv,armour_lv,hp,inventory = armoury(gold,base_hp,armour_hp,lv,armour_lv,hp,inventory)
        
        else:
            stall=input("\nPress enter to continue:")
    
        
        #andering animation
        for i in range(9):
            cls()
            print(images.wandering[i%4])
            print(images.wasteland[distance%4])
            sleep(0.6)
    
        #checck point message
        if distance in range(75,90):
            print("You have made it to a more difficult part of the wastelad be careful for more mobs.\n You may have to fight two in the same day")
            stall=input("\nPress enter to continue:")
    
            #the fist 75 km mob rate
        if distance in range(0,76) and mobs_perday > 0:
            if mobs_perday > 1:
                mobs_perday -= 1
            while mobs_perday > 0:
                print("Possible mobs in the area",["undead_skeleton","undead_skeleton_knight"])
                encounter = rand.randint(0,11)#the chances of each enemy in the area 0-11
                sleep(3)

            
                if encounter in range(0,9):
                    undead_skeleton = s_undead(lv)#mob fight for mob
                    slow_print(colorama.Fore.RED+"You encounter a skeleton warrior the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: The undead are strong against magic and have an ability called rage(enemy damage is 150% when below half hp)")
                    print(images.skeleton)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(undead_skeleton,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.skeleton_attack,ability = rage_ability)
                    if dead == True:
                        break
                    
    
                        
                elif encounter in range(9,12):
                    undead_skeleton_knight = s_knight(lv)#mob fight for mob
                    slow_print(colorama.Fore.RED+"You encounter a skeleton knight the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: The undead knights are strong against bow and are weak against magic and have abilites called rage(enemy damage is 150% when below half hp) and charge(charge has a 1 in 6 chance each turn dealing 3*its dmg)")
                    print(images.skeleton_knight)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(undead_skeleton_knight,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.skeleton_attack,ability = rage_ability,ability2 = charge_ability)
                    if dead == True:
                        break
                mobs_perday -= 1
                xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
            if dead == True:
                        break
            

################################################################################################
            #the next mob rate
        elif distance in range(76,140) and mobs_perday > 0:
            while mobs_perday > 0:
                print("Possible mobs in the area",["undead_skeleton","undead_skeleton_knight"])
                encounter = rand.randint(0,11)#the chances of each enemy in the area 0-11
                  
                sleep(3)

            
                if encounter in range(0,5):
                    undead_skeleton = s_undead(lv)#mob fight for mob
                    slow_print(colorama.Fore.RED+"You encounter a skeleton warrior the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: The undead are strong against magic and have an ability called rage(enemy damage is 150% when below half hp)")
                    print(images.skeleton)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(undead_skeleton,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.skeleton_attack,ability = rage_ability)
                    if dead == True:
                        break
    
    
                        
                elif encounter in range(5,12):
                    undead_skeleton_knight = s_knight(lv)#mob fight for mob
                    slow_print(colorama.Fore.RED+"You encounter a skeleton knight the battle begins!"+colorama.Fore.RED,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: The undead knights are strong against bow and are weak against magic and have abilites called rage(enemy damage is 150% when below half hp) and charge(charge has a 1 in 6 chance each turn dealing 3*its dmg)")
                    print(images.skeleton_knight)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(undead_skeleton_knight,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.skeleton_attack,ability = rage_ability,ability2 = charge_ability)
                    if dead == True:
                        break

                        
                mobs_perday -= 1
                print("Mobs left:",mobs_perday)
                sleep(4)

                
                 # allows player to heal between battles
                xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
                if mobs_perday > 0 and healing_pots > 0:
                    print(colorama.Fore.GREEN + "Hp",hp,"/",base_hp,colorama.Fore.RESET+" ")
                    healing_pots,base_hp,hp = healing(healing_pots,base_hp,hp)
                    
                
            if dead == True:
                        break
            

###############################################################################################################################################################################
        #the last mob rate
        elif distance >= 140:
            while mobs_perday > 0:
                print("Possible mobs in the area",["undead_skeleton_knight","undead_skeleton_leader"])
                  
                sleep(3)

            
                if mobs_perday == 1:
                    undead_skeleton_leader = b_skeleton_leader(lv)#mob fight for mob
                    slow_print(colorama.Fore.RED+"You encounter The Skeleton Leader let the battle begins!"+colorama.Fore.RED,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: The undead_skeleton_leader is strong against magic and have abilites called rage(enemy damage is 150% when below half hp),charge(charge has a 1 in 6 chance each turn dealing 3*its dmg), and fear(has a 1/3 chance of lowering your dmg by 1/3 and has a 1/2 chanceof lasting each turn)")
                    print(images.skeleton_king)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(undead_skeleton_leader,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.skeleton_attack,ability = rage_ability,ability2 = charge_ability,ability3 = fear_ability)
                    if dead == True:
                        break
                    boss_killed = True
                    print("The undead_skeleton_leader dropped",undead_skeleton_leader.loot,"This is needed for armour-lv 5")
                    inventory.append(undead_skeleton_leader.loot)
        
    
                        
                elif mobs_perday == 2:
                    undead_skeleton_knight = s_knight(lv)#mob fight for mob
                    slow_print(colorama.Fore.RED+"You encounter a skeleton knight the battle begins!"+colorama.Fore.RED,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: The undead knights are strong against bow and are weak against magic and have abilites called rage(enemy damage is 150% when below half hp) and charge(charge has a 1 in 6 chance each turn dealing 3*its dmg), they have the bleed")
                    print(images.skeleton_knight)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(undead_skeleton_knight,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.skeleton_attack,ability = rage_ability,ability2 = charge_ability,ability3 = bleed_ability)
                    if dead == True:
                        break

                
                mobs_perday -= 1
                print("Mobs left:",mobs_perday)
                sleep(4)
                xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
                 # allows player to heal between battles
                if mobs_perday > 0 and healing_pots > 0:
                    healing_pots,base_hp,hp = healing(healing_pots,base_hp,hp)
                    
                
            if dead == True:
                        break
            
        
        
        elif mobs_perday == 0:
            slow_print("You encountered no mobs for the day..." ,0.06, clear = False)
            gold_found = rand.randint(10+lv*5,30+lv*5)
            gold += gold_found
            slow_print("Today you found " + str(gold_found) + " gold" ,0.06, clear = False)

        
        distance += 15
        #horse distance
        if "horse" in inventory:
            distance += 15
#horse rations
        if "horse" in inventory and rations >= 0:
            horse_eat = rand.randint(1,2)
            slow_print("Your horse ate "+ str(horse_eat)+ " rations",0.06, clear = False)
            rations -= horse_eat
        if rations >= 0:
            slow_print("You ate 1 ration\n",0.06, clear = False)
            rations -= 1
#starvation
        if rations < 0:
            rations = 0
            slow_print("You are dying of starvation! -half hp\n",0.06, clear = False)
            hp -= base_hp//2
        if hp<=0:
            dead = True
            break
        stats(hp,base_hp,healing_pots,mana_pots,arrows,xp,xp_base,lv,gold,day,distance,rations,armour_lv,"Make the trek across the fields",150)

        
        if day == 1: print("\nResting allows you to gain half hp and shop the next morning.\nHowever, you may encounter a thief at night and a day passes by.\n")
            #resting
        rest = validate(["yes","no","y","n"],"\nDo you want to sleep? ")
        
        if rest in ["y","yes"]:
            hp += base_hp//5
            rest = True
            print(images.night)
            sleep(4)
            if hp > base_hp: hp = base_hp
            
            theft = rand.randint(1,6)#theif
            if theft == 6 and not inventory == False:
                thief = s_thief(lv)
                slow_print("You wake up to the sound of rustling in your bag!",0.08,1,clear = False)
                slow_print(colorama.Fore.RED+"Its a thief he attemps to run away but he is cornered so he pulls out a shiv. The battle starts!"+colorama.Fore.RED,0.08,1,clear = False)
                if "handbook" in inventory:
                    print("\nHandbook: Thieves have no strenths and are weak against bow. Attacks done by the thief have a 1/2 chance of making you bleed they also have charge")
                print(images.thief)
                stall=input("\nPress enter to continue:")
                healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(thief,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.thief_attack,ability = bleed_ability, ability2 = charge_ability)
                if dead == True:
                    slow_print("You were unable to kill the thief...",0.08)
                    stolen = rand.choice(inventory)
                    inventory.remove(stolen)
                    slow_print("The thief took your" + stolen,0.08)
                    dead = False
                    hp = base_hp//3*2
                xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
                
            hp += base_hp//5
            if hp > base_hp: hp = base_hp
                    
                    
                
        
        
        
    
        cls()
    
    if dead == True:
        cls()
        print(images.death)
        timeEnd= time.time()
        timeTaken = timeEnd - timeStart
        print("That took: " + str(timeTaken) + "seconds")
        restart = validate(["yes","no","y","n"],"Do you want to try again?\n")
        if restart in ["yes","y"]: 
            cls()
            continue
        else: exit()
###############################################################################################################################################
            ############################################################################################
        ########################################################################################################
###############################################################################################################################################
            ############################################################################################
        ########################################################################################################
###############################################################################################################################################
            ############################################################################################
        ########################################################################################################
    if world_three in ["yes","y"]:
        rest = True
        boss_killed = True
        choice = "k"
    else:
        xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
        rest = True
        boss_killed = False
        print(images.caverns)
        lore = validate(["yes","no","y","n"],"Do you want to skip the lore?\n")
        cls()
        if lore in ["n","no"]: 
            slow_print("After defeating the Skeleton leader you have made it to the caverns",0.07,3)
            for i in range(5):
                print(images.loading[i%5])
                sleep(4)
                cls()
            print(images.cross_roads)
            slow_print("How ever you have came to a cross roads",0.06,3)
            print(images.mountain_path)
            slow_print("One path leads around the mountains to the other side",0.06,3)
            print(images.cave)
            slow_print("The other path leads towards the caverns going through the mountains",0.06,3)
        
            slow_print("Going in the caverns makes the trip shorter however the mob rate will be higher",0.06,clear = False)
            slow_print("Going around the mountains makes the trip long however the mob rate is reletively tame\n",0.06,clear = False)
        while True:
            print (["caverns","around","c","a"])
            choice = validate(["caverns","around","c","a"],"Do you chose to go in the caverns or around? \n")
            if choice in ["around","a"]:
                print("Your character ain't a scardy cat")
            else:
                break
##############################################################################################################################
    if choice in ["caverns","c"]:
        slow_print("You have decided to head to the caverns.\nThe caverns take 90 km",0.07,3)
        while boss_killed == False:
            if rest == True:
                day = day + 1
            
            #poison sting, bite regen dmg done, swarm multi hit like bow but with little spiders,blind makes dmg 0
            if distance in range(150,181):
                mobs_perday = rand.randint(0,2)# how many mobs will be seen 0,1 spider, bats
            elif distance in range(181,211):
                mobs_perday = rand.randint(0,3)# how many mobs will be seen 0,2 large spider, bats,spider
            elif distance in range(211,225):
                mobs_perday = rand.randint(4,5)# how many mobs will be seen 0,2 spider,large spider
            elif distance >= 240:
                mobs_perday = 1#minitor
            
            stats(hp,base_hp,healing_pots,mana_pots,arrows,xp,xp_base,lv,gold,day,distance,rations,armour_lv,"Travel through the caverns",240)
            print(inventory)
            #checck point message
            if distance in range(211,225):
                print("You have made it to a spider nest becarful for large amounts of mobs")
                
            merchant_appear = 3
            if rest == True and merchant_appear > 1:
                merchant =validate(["yes","no","y","n"],"\nYou stumble upon a magical shop would you like to shop?\n")
                if merchant in ["y","yes"]:
                    gold,arrows,healing_pots,mana_pots,rations = shop(inventory,gold,arrows,healing_pots,mana_pots,rations)
                if armour_lv < 4:
                    upgrade = validate(["yes","no","y","n"],"\nYou stumble upon an enchantery would you like to upgrade your armour?\nCost:"+str(armour_lv*30+60)+"\n")
                    if upgrade in ["y","yes"]:
                        gold,base_hp,armour_hp,lv,armour_lv,hp,inventory = armoury(gold,base_hp,armour_hp,lv,armour_lv,hp,inventory)
                
            else:
                stall=input("\nPress enter to continue:")
        
            
            #andering animation
            for i in range(9):
                cls()
                print(images.caverns_search[i%4])
                print(images.torch[i%4])
                sleep(0.6)
        
            
        
                
            if distance in range(150,181) and mobs_perday > 0:
                while mobs_perday > 0:
                    print("Possible mobs in the area",["s_spider","s_bat"])
                    encounter = rand.randint(0,11)#the chances of each enemy in the area 0-11
                      
                    sleep(3)
    
                
                    if encounter in range(0,6):
                        spider = s_spider(lv)
                        slow_print(colorama.Fore.RED+"You encounter a super spider the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                        if "handbook" in inventory:
                            print("\nHandbook: Spiders are strong against sword but are weak against magic, They have two abilities poison sting(poisons you) and bite(allows them to regen the damage they did to you)")
                        print(images.spider)
                        stall=input("\nPress enter to continue:")
                        healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(spider,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.spider_attack,ability = bite_ability,ability2 = poison_ability)
                        if dead == True:
                            break
                        
        
                            
                    elif encounter in range(6,12):
                        bat = s_bat(lv)
                        slow_print(colorama.Fore.RED+"You encounter a blood lusted bat the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                        if "handbook" in inventory:
                            print("\nHandbook: bats are strong against swords but are weak against bow they only attack using bite(which heals dmg done)")
                        print(images.bat)
                        stall=input("\nPress enter to continue:")
                        healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(bat,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.skeleton_attack,ability = b_bite_ability)
                        if dead == True:
                            break

                            
                    mobs_perday -= 1
                    xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
                    if mobs_perday > 0 and healing_pots > 0:
                        print(colorama.Fore.GREEN + "Hp",hp,"/",base_hp,colorama.Fore.RESET+" ")
                        healing_pots,base_hp,hp = healing(healing_pots,base_hp,hp)
                    
                if dead == True:
                            break
                
    
    ################################################################################################
                #the next mob rate
            elif distance in range(211,225) and mobs_perday > 0:
                while mobs_perday > 0:
                    print("Possible mobs in the area",["s_spider","m_spider"])
                    encounter = rand.randint(0,11)#the chances of each enemy in the area 0-11
                      
                    sleep(3)
    
                
                    if encounter in range(0,8):
                        spider = s_spider(lv)
                        slow_print(colorama.Fore.RED+"You encounter a super spider the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                        if "handbook" in inventory:
                            print("\nHandbook: Spiders are strong against bow, They have two abilities poison sting(poisons you) and bite(allows them to regen the damage they did to you)")
                        print(images.spider)
                        stall=input("\nPress enter to continue:")
                        healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(spider,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.spider_attack,ability = poison_ability,ability2 = bite_ability)
                        if dead == True:
                            break

                    if encounter in range(8,12):
                        big_spider = m_spider(lv)
                        slow_print(colorama.Fore.RED+"You encounter a Mother spider the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                        if "handbook" in inventory:
                            print("\nHandbook: Mother Spiders are strong against sword but are weak against magic, They have three abilities poison sting(poisons you) and bite(allows them to regen the damage they did to you),swarm(multi attack)")
                        print(images.spider)
                        stall=input("\nPress enter to continue:")
                        healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(big_spider,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.spider_attack,ability = swarm_ability,ability2 = poison_ability, ability3 = bite_ability)
                        if dead == True:
                            break
        
                        
    
                            
                    mobs_perday -= 1
                    print("Mobs left:",mobs_perday)
                    sleep(4)
    
                    
                     # allows player to heal between battles
                    xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
                    if mobs_perday > 0 and healing_pots > 0:
                        print(colorama.Fore.GREEN + "Hp",hp,"/",base_hp,colorama.Fore.RESET+" ")
                        healing_pots,base_hp,hp = healing(healing_pots,base_hp,hp)
                        
                    
                if dead == True:
                            break
                
    
    ###############################################################################################################################################################################
            #the other
            elif distance in range(181,211) and mobs_perday > 0:
                while mobs_perday > 0:
                    print("Possible mobs in the area",["s_spider","m_spider","s_bat"])
                    encounter = rand.randint(0,11)#the chances of each enemy in the area 0-11
                      
                    sleep(3)
    
                
                    if encounter in range(0,6):
                        spider = s_spider(lv)
                        slow_print(colorama.Fore.RED+"You encounter a super spider the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                        if "handbook" in inventory:
                            print("\nHandbook: Spiders are strong against sword but are weak against magic, They have two abilities poison sting(poisons you) and bite(allows them to regen the damage they did to you)")
                        print(images.spider)
                        stall=input("\nPress enter to continue:")
                        healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(spider,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.spider_attack,ability2 = poison_ability, ability3 = bite_ability)
                        if dead == True:
                            break

                    elif encounter in range(10,12):
                        big_spider = m_spider(lv)
                        slow_print(colorama.Fore.RED+"You encounter a Mother spider the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                        if "handbook" in inventory:
                            print("\nHandbook: Mother Spiders are strong against bow, They have three abilities poison sting(poisons you) and bite(allows them to regen the damage they did to you),swarm(multi attack)")
                        print(images.spider)
                        stall=input("\nPress enter to continue:")
                        healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(big_spider,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.spider_attack,ability = swarm_ability,ability2 = poison_ability, ability3 = bite_ability)
                        if dead == True:
                            break
        
                            
                    elif encounter in range(6,10):
                        bat = s_bat(lv)
                        slow_print(colorama.Fore.RED+"You encounter a blood lusted bat the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                        if "handbook" in inventory:
                            print("\nHandbook: bats are strong against swords but are weak against bow they only attack using bite(which heals dmg done)")
                        print(images.bat)
                        stall=input("\nPress enter to continue:")
                        healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(bat,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.skeleton_attack,ability = b_bite_ability)
                        if dead == True:
                            break
    
                            
                    mobs_perday -= 1
                    print("Mobs left:",mobs_perday)
                    sleep(4)
    
                    
                     # allows player to heal between battles
                    xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
                    if mobs_perday > 0 and healing_pots > 0:
                        print(colorama.Fore.GREEN + "Hp",hp,"/",base_hp,colorama.Fore.RESET+" ")
                        healing_pots,base_hp,hp = healing(healing_pots,base_hp,hp)
                         
                    
                if dead == True:
                            break
            ################################################################################################
                #the next mob rate
            elif distance >= 240 and mobs_perday > 0:
                while mobs_perday > 0:
                    print("Possible mobs in the area",["b_minotaur"])
                    encounter = 1#the chances of each enemy in the area 0-11
                      
                    sleep(3)
    
                
                    if encounter == 1:
                        minotaur = b_minotaur(lv)
                        slow_print(colorama.Fore.RED+"You encounter a boss MINOTAUR the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                        if "handbook" in inventory:
                            print("\nHandbook: Minotaur are strong against sword but are weak against nothing, They have three abilities rage,charge,and bleed")
                        print(images.minotaur)
                        stall=input("\nPress enter to continue:")
                        healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(minotaur,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.minotaur_attack,ability = rage_ability,ability2 = charge_ability,ability3 = bleed_ability)
                        if dead == True:
                            break
                        boss_killed = True
                        print("The minotaur dropped",minotaur.loot,"This is needed for armour-lv 5")
                        inventory.append(minotaur.loot)
        
            
                            
                    mobs_perday -= 1
                    print("Mobs left:",mobs_perday)
                    sleep(4)
    
                    
                     # allows player to heal between battles
                    xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
                    if mobs_perday > 0 and healing_pots > 0:
                        print(colorama.Fore.GREEN + "Hp",hp,"/",base_hp,colorama.Fore.RESET+" ")
                        healing_pots,base_hp,hp = healing(healing_pots,base_hp,hp)
                        
                    
                if dead == True:
                            break
            
            
            elif mobs_perday == 0:
                slow_print("You encountered no mobs for the day..." ,0.06, clear = False)
                gold_found = rand.randint(10+5*lv,30+5*lv)
                gold += gold_found
                slow_print("Today you found " + str(gold_found) + " gold" ,0.06, clear = False)
    
            
            distance += 15
            #horse distance
            if "horse" in inventory:
                distance += 15
    #horse rations
            if "horse" in inventory and rations >= 0:
                horse_eat = rand.randint(1,2)
                slow_print("Your horse ate "+ str(horse_eat)+ " rations",0.06, clear = False)
                rations -= horse_eat
            if rations >= 0:
                slow_print("You ate 1 ration\n",0.06, clear = False)
                rations -= 1
    #starvation
            if rations < 0:
                rations = 0
                slow_print("You are dying of starvation! -half hp\n",0.06, clear = False)
                hp -= base_hp//2
            if hp<=0:
                dead = True
                break
            stats(hp,base_hp,healing_pots,mana_pots,arrows,xp,xp_base,lv,gold,day,distance,rations,armour_lv,"Travel through the caverns",240)
    
            
                
            rest = validate(["yes","no","y","n"],"\nDo you want to sleep? ")
            
            if rest in ["y","yes"]:
                hp += base_hp//5 
                rest = True
                print(images.sleep)
                sleep(4)
                if hp > base_hp: hp = base_hp
                
                theft = rand.randint(1,4)
                if theft == 4 and not inventory == False:
                    ghoul = s_ghoul(lv)
                    slow_print("You wake up to the sound of rustling in your bag!",0.08,1,clear = False)
                    slow_print(colorama.Fore.RED+"Its a ghoul it attemps to run away but it is cornered in the mines. The battle starts!"+colorama.Fore.RED,0.08,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: Ghouls have no strenths and are weak against magic. Attacks done by the thief have a 1/2 chance of making you poisoned and 1/4 chance of making you blind")
                    print(images.ghoul)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(ghoul,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.ghoul_attack,ability2 = poison_ability, ability3 = blind_ability)
                    if dead == True:
                        slow_print("You were unable to kill the ghoul...",0.08)
                        stolen = rand.choice(inventory)
                        inventory.remove(stolen)
                        slow_print("The ghoul took your" + stolen,0.08)
                        dead = False
                        hp = base_hp//3*2
                    xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
                hp += base_hp//5 
                if hp > base_hp: hp = base_hp
                        
                        
                    
            
            
            
        
            cls()
        
        if dead == True:
            cls()
            print(images.death)
            timeEnd= time.time()
            timeTaken = timeEnd - timeStart
            print("That took: " + str(timeTaken) + "seconds")
            restart = validate(["yes","no","y","n"],"Do you want to try again?\n")
            if restart in ["yes","y"]: 
                cls()
                continue
            else: exit()





#############################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################

    rest = True
    boss_killed = False
    print(images.mountains)
    lore = validate(["yes","no","y","n"],"Do you want to skip the lore?\n")
    cls()
    if lore in ["n","no"]: 
        print(images.cave)
        slow_print("After passing through the caves you have made it to the highlands",0.07,3)
        for i in range(5):
            print(images.loading[i%5])
            sleep(2)
            cls()
        print(images.mountain_path)
        slow_print("Now you must take the path to the top\n",0.06,3)
##############################################################################################################################
    xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
    slow_print("Victory is almost near 45 km left",0.07,3)
    while boss_killed == False:
        if rest == True:
            day = day + 1
        
        #poison sting, bite regen dmg done, swarm multi hit like bow but with little spiders,blind makes dmg 0
        if distance == 255:
            mobs_perday = 8 # how many mobs will be seen 0,1 spider, bats, skeleton, zombie
            print("You have made to the basen you'll be fighting 8 medium mobs")
        elif distance == 270:
            mobs_perday = 4# how many mobs will be seen 0,2 large baby dragon, large spider, skeleton knight, minotaur
            #baby dragon rage and fire
            print("You have made it to the mountain side")
        elif distance == 285:
            mobs_perday = 1# how many mobs will be seen 0,2 dragon
            print("You have made tp the pedestal you'll be fighting THE DRAGON")#fire, arial dive does damage and lowers dmg by half, claw mui
        
        stats(hp,base_hp,healing_pots,mana_pots,arrows,xp,xp_base,lv,gold,day,distance,rations,armour_lv,"Travel through the highlands",285)
        print(inventory)
        #checck point message
            
            
        merchant_appear = 2
        if rest == True and merchant_appear > 1:
            merchant =validate(["yes","no","y","n"],"\nYou stumble upon a wrecked shop would you like to shop?\n")
            if merchant in ["y","yes"]:
                print(images.highland_shop)
                gold,arrows,healing_pots,mana_pots,rations = shop(inventory,gold,arrows,healing_pots,mana_pots,rations)
            if armour_lv < 5:
                upgrade = validate(["yes","no","y","n"],"\nYou stumble upon an mythical enchantery would you like to upgrade your armour?\nCost:"+str(armour_lv*30+60)+"\n")
                if upgrade in ["y","yes"]:
                    gold,base_hp,armour_hp,lv,armour_lv,hp,inventory = armoury(gold,base_hp,armour_hp,lv,armour_lv,hp,inventory)
            
        else:
            stall=input("\nPress enter to continue:")
    
        
        #andering animation
        for i in range(9):
            cls()
            print(images.highlands_search[i%4])
            print(images.highlands)
            sleep(0.3)
    
        
    
            
        if distance == 255 and mobs_perday > 0:
            counter = 7
            while mobs_perday > 0:
                print("Possible mobs in the area",["spider","bat","undead_skeleton","undead_zombie"])
                encounter = rand.randint(1,counter-1)#the chances of each enemy in the area 0-11
                  
                sleep(3)

            
                if encounter == 1:
                    spider = s_spider(lv)
                    slow_print(colorama.Fore.RED+"You encounter a super spider the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: Spiders are strong against sword but are weak against magic, They have two abilities poison sting(poisons you) and bite(allows them to regen the damage they did to you)")
                    print(images.spider)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(spider,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.spider_attack,ability = bite_ability,ability2 = poison_ability)
                    if dead == True:
                        break

                elif encounter == 2:
                    undead_skeleton = s_undead(lv)
                    slow_print(colorama.Fore.RED+"You encounter a skeleton warrior the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: The undead are strong against magic and have an ability called rage(enemy damage is 150% when below half hp)")
                    print(images.skeleton)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(undead_skeleton,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.skeleton_attack,ability = rage_ability)
                    if dead == True:
                        break
    
                        
                elif encounter == 3:
                    bat = s_bat(lv)
                    slow_print(colorama.Fore.RED+"You encounter a blood lusted bat the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: bats are strong against swords but are weak against bow they only attack using bite(which heals dmg done)")
                    print(images.bat)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(bat,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.skeleton_attack,ability = b_bite_ability)
                    if dead == True:
                        break

                elif encounter  in range(4,counter):
                    counter -= 1
                    zombie = s_zombie(lv)
                    slow_print(colorama.Fore.RED+"You encounter a plauge infected zombie the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: The zombie has no weaknesses and are strong against bow. They have the abilities poison and fear ")
                    print(images.zombie)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(zombie,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.zombie_attack,ability = poison_ability,ability2 = fear_ability)
                    if dead == True:
                        break

                        
                mobs_perday -= 1
                print("Mobs left:",mobs_perday)
                xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
                print()
                if mobs_perday > 0 and healing_pots > 0:
                    print(colorama.Fore.GREEN + "Hp",hp,"/",base_hp,colorama.Fore.RESET+" ")
                    healing_pots,base_hp,hp = healing(healing_pots,base_hp,hp)
                
            if dead == True:
                        break
            

################################################################################################
            #the next mob rate
        elif distance == 270 and mobs_perday > 0:
            while mobs_perday > 0:
                print("Possible mobs in the area",["mother_spider","undead_skeleton_knight","minotaur","spitfire"])
                  
                sleep(3)

                if mobs_perday == 1:
                    spitfire = m_spitfire(lv)
                    slow_print(colorama.Fore.RED+"You encounter a spitfire the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: Spitfire(baby dragons) are strong against sword but are weak against nothing, They have two abilities rage and fire")
                    print(images.baby_dragon)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(spitfire,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.baby_dragon_attack,ability = rage_ability,ability2 = fire_ability)
                    if dead == True:
                        break

                
                if mobs_perday == 2:
                    minotaur = b_minotaur(lv)
                    slow_print(colorama.Fore.RED+"You encounter a MINOTAUR the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: Minotaur are strong against sword but are weak against nothing, They have three abilities rage,charge,and bleed")
                    print(images.minotaur)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(minotaur,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.minotaur_attack,ability = rage_ability,ability2 = charge_ability,ability3 = bleed_ability)
                    if dead == True:
                        break

                elif mobs_perday == 3:
                    undead_skeleton_knight = s_knight(lv)
                    slow_print(colorama.Fore.RED+"You encounter a skeleton knight the battle begins!"+colorama.Fore.RED,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: The undead knights are strong against bow and are weak against magic and have abilites called rage(enemy damage is 150% when below half hp) and charge(charge has a 1 in 6 chance each turn dealing 3*its dmg) and fear")
                    print(images.skeleton_knight)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(undead_skeleton_knight,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.skeleton_attack,ability = rage_ability,ability2 = charge_ability,ability3 = fear_ability)
                    if dead == True:
                        break

                if mobs_perday == 4:
                    big_spider = m_spider(lv)
                    slow_print(colorama.Fore.RED+"You encounter a Mother spider the battle begins!"+colorama.Fore.RESET,0.06,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: Mother Spiders are strong against bow, They have three abilities poison sting(poisons you) and bite(allows them to regen the damage they did to you),swarm(multi attack)")
                    print(images.spider)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(big_spider,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.spider_attack,ability = swarm_ability,ability2 = poison_ability, ability3 = bite_ability)
                    if dead == True:
                        break
    
                    

                        
                mobs_perday -= 1
                print("Mobs left:",mobs_perday)
                sleep(2)

                
                 # allows player to heal between battles
                xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
                if mobs_perday > 0 and healing_pots > 0:
                    print(colorama.Fore.GREEN + "Hp",hp,"/",base_hp,colorama.Fore.RESET+" ")
                    healing_pots,base_hp,hp = healing(healing_pots,base_hp,hp)
                    
                
            if dead == True:
                        break
            

###############################################################################################################################################################################
        #the other
        elif distance == 285 and mobs_perday > 0:
            while mobs_perday > 0:
                print(images.right_there)
                slow_print("You are meters away from the golden chalice. you can finally end it all",0.07,3)
                print(images.flying_in)
                slow_print("Right as you are about to grab it a dragon sweaps in.",0.07,3)
                print(images.ready_yourself)
                slow_print("You ready yourself for the final battle\n",0.07,3)
                
                dragon = b_dragon(lv)
                if "handbook" in inventory:
                    print("\nHandbook: Dragons have no weakness and are strong against sword not much is know about their abilities")
                print(images.dragon)
                stall=input("\nPress enter to continue:")
                healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(dragon,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.dragon_attack,ability = dive_ability,ability2 = claw_ability, ability3 = fire_ability)
                
                if dead == True:
                    break

                print(images.dragon_dead)
                slow_print("You have slain the dragon it dropped the Chalice",0.07,3)
                print(images.you_won)
                slow_print("You take the chalice and celebrate",0.07,3)
                boss_killed = True
                if day > 20:
                    slow_print("How ever this celebration is short lived",0.07,3,clear=False)
                    slow_print("As you remember the kings words. \"My family is sick they will die in 20 days\"\n",0.07,3,clear=False)
                    print("You took",day,"days")
                    print(images.spoils)
                    slow_print("You'll be executed if you head back home so you decide to live a life of adventure taking the spoils for yorself",0.07,3,clear=False)
                    timeEnd= time.time()
                    timeTaken = timeEnd - timeStart
                    print("That took: " + str(timeTaken) + "seconds")
                    stall=input("\nPress enter to continue:")
                    break
                slow_print("You tame a dragon by inserting you dominace",0.07,3,clear=False)
                slow_print("As you fly home you think about the journy\n",0.07,3,clear=False)
                print("You took",day,"days")
                print(images.dragon_tame)
                slow_print("When you arrive home you are crowned as a hero. \nThe king allows you to marry his daughter and you are living the dream\n",0.07,3,clear=False)
                timeEnd= time.time()
                timeTaken = timeEnd - timeStart
                print("That took: " + str(timeTaken) + "seconds")
                stall=input("\nPress enter to continue:")
                break
                sleep(2)

                
        
                     
                
            if dead == True:
                        break
        ################################################################################################
            #the next mob rate
        if boss_killed == True:
            break
        

        
        distance += 15
        #horse distance
        if "horse" in inventory:
            distance += 15
#horse rations
        if "horse" in inventory and rations >= 0:
            horse_eat = rand.randint(1,2)
            slow_print("Your horse ate "+ str(horse_eat)+ " rations",0.06, clear = False)
            rations -= horse_eat
        if rations >= 0:
            slow_print("You ate 1 ration\n",0.06, clear = False)
            rations -= 1
#starvation
        if rations < 0:
            rations = 0
            slow_print("You are dying of starvation! -half hp\n",0.06, clear = False)
            hp -= base_hp//2
        if hp<=0:
            dead = True
            break
        stats(hp,base_hp,healing_pots,mana_pots,arrows,xp,xp_base,lv,gold,day,distance,rations,armour_lv,"Travel through the highlands",285)

        
            
        rest = validate(["yes","no","y","n"],"\nDo you want to sleep? ")
        
        if rest in ["y","yes"]:
            hp += base_hp//5 
            rest = True
            print(images.sleep)
            sleep(4)
            if hp > base_hp: hp = base_hp
            
            theft = rand.randint(1,2)
            if theft in range(1,3) and not inventory == False:
                if theft == 1:
                    ghoul = s_ghoul(lv)
                    slow_print("You wake up to the sound of rustling in your bag!",0.08,1,clear = False)
                    slow_print(colorama.Fore.RED+"Its a ghoul The battle starts!"+colorama.Fore.RED,0.08,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: Ghouls have no strenths and are weak against magic. Attacks done by the thief have a 1/2 chance of making you poisoned and 1/4 chance of making you blind")
                    print(images.ghoul)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(ghoul,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.ghoul_attack,ability2 = poison_ability, ability3 = blind_ability)
                    if dead == True:
                        slow_print("You were unable to kill the ghoul...",0.08)
                        stolen = rand.choice(inventory)
                        inventory.remove(stolen)
                        slow_print("The ghoul took your" + stolen,0.08)
                        dead = False
                        hp = base_hp//3*2
                if theft == 2:
                    thief = s_thief(lv)
                    slow_print("You wake up to the sound of rustling in your bag!",0.08,1,clear = False)
                    slow_print(colorama.Fore.RED+"Its a thief. he pulls out a shiv. The battle starts!"+colorama.Fore.RED,0.08,1,clear = False)
                    if "handbook" in inventory:
                        print("\nHandbook: Thieves have no strenths and are weak against bow. Attacks done by the thief have a 1/2 chance of making you bleed and they have charge ability")
                    print(images.thief)
                    stall=input("\nPress enter to continue:")
                    healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,dead = fight(thief,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,images.thief_attack,ability = bleed_ability, ability2 = charge_ability)
                    if dead == True:
                        slow_print("You were unable to kill the thief...",0.08)
                        stolen = rand.choice(inventory)
                        inventory.remove(stolen)
                        slow_print("The thief took your" + stolen,0.08)
                        dead = False
                        hp = base_hp//3*2
                xp,dmg,base_hp,armour_hp,xp_base,lv,hp=level_up(xp,dmg,base_hp,armour_hp,xp_base,lv,armour_lv,hp)
            hp += base_hp//5 
            if hp > base_hp: hp = base_hp
                    
                    
                
        
        
        
    
        cls()

    
    
    if dead == True:
        cls()
        print(images.death)
        timeEnd= time.time()
        timeTaken = timeEnd - timeStart
        print("That took: " + str(timeTaken) + "seconds")
        restart = validate(["yes","no","y","n"],"Do you want to try again?\n")
        if restart in ["yes","y"]: 
            cls()
            continue
        else: exit()

    print(legit)
    timeEnd= time.time()
    timeTaken = timeEnd - timeStart
    print("That took: " + str(timeTaken) + "seconds")
    restart = validate(["yes","no","y","n"],"Do you want to try your luck again?\n")
    if restart in ["yes","y"]: 
        cls()
        continue
    else: exit()
    
    

    