import colorama
import images
import sys
import os 
import random as rand
from time import sleep 

cls = lambda: os.system('cls')

#prints words in a way that makes user interested
def slow_print(words,speed,delay=1,clear=True,audio = True):
    print(colorama.Fore.RESET + "\n_______________________________________________________")
    #if speed < 0.06 and audio == True:
    #    replit.audio.play_file('sussy.wav')
    for char in words:
        sleep(speed)#lowerd in testing so faster
        #if speed >= 0.05 and char != " ":
        #    replit.audio.play_file('suslow.wav')
        sys.stdout.write(char)
        sys.stdout.flush()
        
        #if speed >= 0.05 and char == ".":
        #    sleep(0.06)
        
    sleep(delay)
    if clear == True:
        cls()


#max min input for shops
def number_minmax(min,max,msg):
    while True:
        try:
            user_num = int(input(msg))
            if user_num in range(min,max+1):
                return user_num
            else:
                print("Inputs must be between the values ", min , " and ",max )
        except:
            print("Input must be of type interger")

            
#valadates user input
def validate(valid_list,msg):
    while True:
        the_line = input(msg).lower()
        if the_line in valid_list:
            return the_line
        elif the_line in ["nothing","none","n"]:
            return None
        else:
            print("That is not a VALID answer")


            
#adds to inventory
def add_to_inventory(item,inventory,stock):
    inventory.append(item)
    stock.remove(item)
    slow_print(item+ " has been added to your inventory!",0.02,clear=False)


#displays stats
def stats(hp,base_hp,healing_pots,mana_pots,arrows,xp,xp_base,lv,gold,day,distance,rations,armour_lv,objective,out_of):
    print(colorama.Fore.GREEN + "Hp",hp,"/",base_hp)
    print(colorama.Fore.MAGENTA +"Healing pots:", healing_pots)
    print(colorama.Fore.CYAN + "Mana pots:", mana_pots)
    print(colorama.Fore.RESET +"Arrows:", arrows)
    print(colorama.Fore.BLUE + "Xp:", xp,"/",xp_base)
    print("Lv:",lv)
    print("armour lv:",armour_lv)
    print(colorama.Fore.YELLOW + "\nGold amount:", gold)
    slow_print(colorama.Fore.RESET +"Day: "+ str(day),0.02,clear = False)
    slow_print("Distance traveled: "+ str(distance)+"/"+str(out_of),0.,clear = False) 
    slow_print("Rations left: "+ str(rations),0.02,clear = False)
    slow_print("Current objective: "+ objective+ "\n",0.04,clear = False)


# upgrading armour
def armoury(gold,base_hp,armour_hp,lv,armour_lv,hp,inventory):
    while True:
        cost = armour_lv*30+60
        if armour_lv == 4 and "Golden Skull" in inventory and "Bull horn" in inventory:
            slow_print("Your armour is being enchanted with Golden Skull and Bull horn\n",0.05,clear=False)
            inventory.remove("Bull horn")
            inventory.remove("Golden Skull")
            armour_lv += 1
            base_hp -= armour_hp
            armour_hp = (base_hp//5)*armour_lv
            base_hp = int(base_hp + armour_hp)
            print(images.forge)
            slow_print("Your armour has been upgraded\n",0.05,clear=False)
            gold -= cost
            hp = base_hp
            print("-",cost,"Gold")
            print("Armour_lv:",armour_lv)
            return gold,base_hp,armour_hp,lv,armour_lv,hp,inventory
        elif cost > gold:
            slow_print("You do not have enough to upgrade your armour!",0.06)
        elif armour_lv < 4:
            armour_lv += 1
            base_hp -= armour_hp
            armour_hp = (base_hp//5)*armour_lv
            base_hp = int(base_hp + armour_hp)
            print(images.forge)
            slow_print("Your armour has been upgraded\n",0.05,clear=False)
            gold -= cost
            hp = base_hp
            print("-",cost,"Gold")
            print("Armour_lv:",armour_lv)
            sleep(1)
        cost = armour_lv*30+60
        print("Cost:",cost)
        continue_shoping = validate(["yes","no","y","n"],"Do you want to continue upgrading?\n")
        cls()
        if continue_shoping in ["n","no"]:
            return gold,base_hp,armour_hp,lv,armour_lv,hp,inventory


        
#shop func this is the shop system
def shop(inventory,gold,arrows,healing_pots,mana_pots,rations):
    # shop prices and stock
    shop_inventory = {"arrows" : [rand.randint(3,8),rand.randint(15,30),"3 per"], "mana pots": [rand.randint(1,5),rand.randint(30,40)], "healing pots" : [rand.randint(4,8),rand.randint(15,25)], "lucky coin": [rand.randint(0,1),rand.randint(125,150)], "rations" : [rand.randint(2,5),rand.randint(10,20)]}
    #the shops fluctuaition to see if good price
    print(""" "arrows" : (15-30), "mana pots": (30-40)], "healing pots" :(15-25), "lucky coin": (125-150), "rations" : [10-20]" """)
    if "totem of undying" not in inventory:
        shop_inventory["totem of undying"] = [rand.randint(1,1),rand.randint(200,250)]
    while True:
        print("Here is the shops current stock the first number is stock and the second is price. \nType 'n' if you dont buy")
        print(shop_inventory)
        print(colorama.Fore.YELLOW + "\nGold amount:", gold)
        selected_item = validate(shop_inventory,colorama.Fore.RESET+"Select which item you would want to buy: ")
        if selected_item == None:
            pass
        elif shop_inventory[selected_item][0] == 0:
            print("That item is out of stock")
            continue
        else:
            while True:
                amount = number_minmax(0,shop_inventory[selected_item][0],"How many "+ selected_item +" do you want?\n")
                if amount*shop_inventory[selected_item][1] > gold:
                    print("You do not have the suficient funds to puchase that amount!")
                    continue 
                else:
                    # I could have just added another thing to the dictionary showing what varrible it affected but im lazy
                    gold -= amount*shop_inventory[selected_item][1]
                    if selected_item == "rations":
                        print("You purchased ",amount, selected_item)
                        rations += amount
                        print("Minus", amount*shop_inventory[selected_item][1],"Gold")
                        shop_inventory[selected_item][0] = shop_inventory[selected_item][0] - amount
                    if selected_item == "arrows":
                        print("You purchased ",amount, selected_item)
                        arrows += 3 * amount
                        print("Minus", amount*shop_inventory[selected_item][1],"Gold")
                        shop_inventory[selected_item][0] = shop_inventory[selected_item][0] - amount
                    elif selected_item == "mana pots":
                        mana_pots += amount
                        print("You purchased",amount, selected_item)
                        print("Minus", amount*shop_inventory[selected_item][1],"Gold")
                        shop_inventory[selected_item][0] = shop_inventory[selected_item][0] - amount
                    elif selected_item == "healing pots":
                        print("You purchased ",amount, selected_item)
                        print("Minus", amount*shop_inventory[selected_item][1],"Gold")
                        healing_pots += amount
                        shop_inventory[selected_item][0] = shop_inventory[selected_item][0] - amount
                    elif selected_item == "lucky coin":
                        print("You purchased ",amount, selected_item)
                        print("Minus", amount*shop_inventory[selected_item][1],"Gold")
                        inventory.append("lucky coin")
                        shop_inventory[selected_item][0] = shop_inventory[selected_item][0] - amount
                    elif selected_item == "totem of undying":
                        print("You purchased ",amount, selected_item)
                        print("Minus", amount*shop_inventory[selected_item][1],"Gold")
                        inventory.append("totem of undying")
                        shop_inventory[selected_item][0] = shop_inventory[selected_item][0] - amount
                    break
            #still shop?
        continue_shoping = validate(["yes","no","y","n"],colorama.Fore.RED+"\n\nDo you want to continue shopping?"+ colorama.Fore.RESET + " \n")
        cls()
        if continue_shoping in ["n","no"]:
            return (gold,arrows,healing_pots,mana_pots,rations)
    cls()
################################################################################
def healing(healing_pots,base_hp,hp):
    healing = validate(["yes","no","y","n"],"Do you want to use a healing pot? \n")
    if healing in ["y","yes"]:
        healing_pots -= 1
        healing_amount = base_hp//3
        hp += healing_amount
        if hp > base_hp: hp = base_hp
        print("You used a healing potion!")
        print("+",healing_amount,"hp")
        print(colorama.Fore.GREEN +"Hp",hp,"/",base_hp)
        print(colorama.Fore.RESET)
    return healing_pots,base_hp,hp


#magic spell attack
def magic_attack(enemy,dmg,mana_pots,inventory):
    print(images.magic)
    if enemy.weakness == 3:
        dmg = dmg//4*5
    if enemy.strength == 3:
        dmg = dmg//4*3
    print("You used magic attack!!")
    print("The attack hits dealing",dmg//2*5,"dmg")
    enemy.hp -= dmg//2*5
    mana_pots -=1
    return mana_pots



#sword attack
def sword_attack(enemy,dmg,critrate,inventory):
    print(images.sword)
    print("You swung the sword!!")
    get_rand = rand.randint(1,10)
    if enemy.weakness == 1:
        dmg = dmg//4*5
    if enemy.strength == 1:
        dmg = dmg//4*3
    if get_rand <= critrate:
        print("You end up hitting a crit dealing",dmg//2*5,"dmg!!")
        print(images.crit)
        enemy.hp -= dmg//2*5
        critrate = inventory.count("lucky coins")*2
        print("Critrate:",critrate*10,"%")
    elif get_rand == 10:
        print("You missed the enemy critrate increased by 20%")
        critrate += 2
        print("Critrate:",critrate*10,"%")
    elif get_rand in range(0,10):
        print("You swung the sword striking the opponent for",dmg,"dmg!!")
        enemy.hp -= dmg
        critrate += 1
        print("Critrate:",critrate*10,"%")
    return critrate


#bow attack
def bow_attack(enemy,dmg,arrows,lv):
    print(images.archery)
    get_rand = 4
    if lv >= 9:
        get_rand = 3
    i = 0
    total_dmg = 0
    missed = 0
    if enemy.weakness == 2:
        dmg = dmg//4*5
    if enemy.strength == 2:
        dmg = dmg//4*3
    while arrows !=0 and enemy.hp > 0:
        i += 1
        if lv >= 9:
            if get_rand <= 8:
                print("\nShot number", i ,"hit!")
                print(images.hit)
                enemy.hp -= dmg
                total_dmg += dmg
                print(enemy.name,"took",dmg,"dmg")
                arrows -= 1
                sleep(1)
            elif missed < 1:
                print("\nShot missed!")
                print(images.miss)
                missed +=1
            else:
                missed +=1
                print("\nShot missed!")
                print(images.miss)
                print("You did a total of",total_dmg,"dmg")
                return arrows
        elif get_rand > 3:
            print("\nShot number", i ,"hit!")
            print(images.hit)
            enemy.hp -= dmg
            total_dmg += dmg
            print(enemy.name,"took",dmg,"dmg")
            arrows -= 1
            sleep(1)
        elif get_rand <= 3:
            arrows-=1
            missed +=1
            print("\nShot missed!")
            print(images.miss)
            print("You did a total of",total_dmg,"dmg")
            return arrows
        if lv >= 9:
            get_rand = rand.randint(1,23) #default 1,5
        else:
            get_rand = rand.randint(1,6)
    if arrows == 0: 
        print("You ran out of arrows")
        print("You did a total of",total_dmg,"dmg")
        return arrows
    else:
        print("You did a total of",total_dmg,"dmg")
        return arrows



        
#####################################################################################################

#these are indivisual enemy abilities
#poison sting, bite regen dmg done, swarm multi hit like bow but with little spiders,blind makes dmg 0
def fire_ability(enemy,critrate,hp,dmg,usage,passive,dmg_base,attack_after,base_hp):
    burned = rand.randint(1,2)
    if passive == True:
        still_burning = rand.randint(1,8)
        if still_burning > 1:
            dealing = base_hp//5//4*2
            print(colorama.Fore.RED+"You are burning -"+str(dealing),"hp")
            print("You are burning your critrate is still 0 and your dmg is still 4/5")
            hp -= dealing
            critrate = 0
        else:
            print("The fire wore off you are no longer burning. Your crit rate will no longer be 0 dmg is restored")
            dmg = dmg_base
            passive = False
            
    elif burned == 2:
        dealing = rand.randint(enemy.attackmin,enemy.attackmax)//4*3
        print(images.fire_attack)
        print("The",enemy.name,"spts fire at you",dealing,"dmg")
        hp -= dealing
        sleep(1)
        print("The burning weakens you. Crit rate is 0")
        dmg = dmg//5 *4
        passive = True
        attack_after = False
        sleep(3)
        cls()
    return (critrate,hp,dmg,usage,passive,attack_after)
    
def claw_ability(enemy,critrate,hp,dmg,usage,passive,dmg_base,attack_after,base_hp):
    claw = rand.randint(1,5) # default 1,6
    if claw == 5:
        print(images.dragon_slash)
        slow_print("The "+enemy.name+" swoops down to slash you with claws\n",0.06,clear = False)
        get_rand = 4
        i = 0
        total_dmg = 0
        while hp > 0:
            i += 1
            if get_rand > 1:
                print("The slash", i ,"hit you!")
                hp -= enemy.attackmax//3
                total_dmg += enemy.attackmax//3
                print("You took",enemy.attackmax//3,"dmg")
                sleep(1.2)
            elif get_rand <= 1:
                print("You block the",i,"slash!")
                break
            get_rand = rand.randint(1,5) #default 1,7
        print( enemy.name,"did a total of",total_dmg,"dmg")
        attack_after = False
        usage = True
    return (critrate,hp,dmg,usage,passive,attack_after)
    
def dive_ability(enemy,critrate,hp,dmg,usage,passive,dmg_base,attack_after,base_hp):
    dive = rand.randint(1,4) # default 1,6
    if enemy.charge == 1:
        print("Your dmg is still lowerd")
        enemy.charge = 2
    elif enemy.charge == 2:
        print("Your dmg is still lowerd")
        enemy.charge = 3
    elif enemy.charge == 3:
        print("Your dmg is restored")
        dmg = dmg_base
        enemy.charge = 0
    elif dive == 4:
        print("The",enemy.name,"uses desolate dive")
        slow_print("The "+enemy.name+" hit you dealing " + str(enemy.attackmin*2) +" dmg\n",0.06,clear = False)
        slow_print("The enemies dive injurss you lowering your dmg to 2/3 for 2 turns\n",0.06,clear = False)
        hp -= enemy.attackmin*2
        dmg = dmg//3*2
        sleep(1)
        enemy.charge = 1
        usage = True
        attack_after = False
    return (critrate,hp,dmg,usage,passive,attack_after)

def blind_ability(enemy,critrate,hp,dmg,usage,passive,dmg_base,attack_after,base_hp):
    blind = rand.randint(1,4) # default 1,4
    if enemy.charge == 1:
        slow_print("The blindness wore off and your dmg is back to base",0.06,clear = False)
        dmg = dmg_base
        usage = True
        attack_after = True
    elif blind == 4:
        print("The",enemy.name,"blinds you")
        slow_print("The your dmg is now 0 for one turn and your critrate is back at 0\n",0.06,clear = False)
        dmg = 0
        sleep(1)
        usage = True
        attack_after = False
        enemy.charge = 1
    return (critrate,hp,dmg,usage,passive,attack_after)

def swarm_ability(enemy,critrate,hp,dmg,usage,passive,dmg_base,attack_after,base_hp):
    swarm = rand.randint(1,5) # default 1,6
    if swarm == 5:
        print(images.spider_swarm)
        slow_print("The "+enemy.name+" is swarming you with spiders\n",0.06,clear = False)
        get_rand = 4
        i = 0
        total_dmg = 0
        while hp > 0:
            i += 1
            if get_rand > 1:
                print("Spider", i ,"bit you!")
                hp -= enemy.attackmax//2
                total_dmg += enemy.attackmax//2
                print("You took",enemy.attackmax//2,"dmg")
                sleep(1.2)
            elif get_rand <= 1:
                print("You shook of the spiders!")
                break
            get_rand = rand.randint(1,5) #default 1,7
        print("They did a total of",total_dmg,"dmg")
        attack_after = False
        usage = True
    return (critrate,hp,dmg,usage,passive,attack_after)

def b_bite_ability(enemy,critrate,hp,dmg,usage,passive,dmg_base,attack_after,base_hp):
    print("The",enemy.name,"bit you")
    amount = rand.randint(enemy.attackmax,enemy.attackmax)
    slow_print("The "+enemy.name+" bit you dealing " + str(amount) +" dmg\n",0.06,clear = False)
    hp -= amount
    slow_print("The "+enemy.name+" regens " + str(amount//3) +" hp\n",0.06,clear = False)
    enemy.hp += amount//3
    sleep(1)
    usage = True
    attack_after = False
    return (critrate,hp,dmg,usage,passive,attack_after)


def bite_ability(enemy,critrate,hp,dmg,usage,passive,dmg_base,attack_after,base_hp):
    bite = rand.randint(1,3) # default 1,4
    if bite == 3:
        print("The",enemy.name,"bit you")
        slow_print("The "+enemy.name+" hit you dealing " + str(enemy.attackmax) +" dmg\n",0.06,clear = False)
        hp -= enemy.attackmax
        slow_print("The "+enemy.name+" regens " + str(enemy.attackmax//3) +" hp\n",0.06,clear = False)
        enemy.hp += enemy.attackmax//3
        sleep(1)
        usage = True
        attack_after = True
    return (critrate,hp,dmg,usage,passive,attack_after)



def poison_ability(enemy,critrate,hp,dmg,usage,passive,dmg_base,attack_after,base_hp):
    poisoned = rand.randint(1,3)
    if passive == True:
        still_poisened = rand.randint(1,5)
        if still_poisened > 1:
            dealing = base_hp//5//4*2
            print(colorama.Fore.RED+"You are poisened -"+str(dealing),"hp")
            print("You are poisened your dmg is still lowered")
            hp -= dealing
        else:
            print("The poison wore off you are no longer poisoned and your dmg is restored")
            dmg = dmg_base
            passive = False
            
    elif poisoned == 3:
        dealing = rand.randint(enemy.attackmin,enemy.attackmax)//4*3
        print(images.poison)
        print("The",enemy.name,"poisens you",dealing,"dmg")
        hp -= dealing
        sleep(1)
        print("The poison weakens you. dmg is lowered by 1/5")
        dmg = dmg//5 *4
        passive = True
        attack_after = False
        sleep(3)
        cls()
    return (critrate,hp,dmg,usage,passive,attack_after)

        
def bleed_ability(enemy,critrate,hp,dmg,usage,passive,dmg_base,attack_after,base_hp):
    if passive == True:
        still_bleeding = rand.randint(1,5)
        if still_bleeding > 1 or enemy.charge == 1:
            dealing = base_hp//5//4*3
            print("You are bleeding -"+str(dealing),"hp")
            hp -= dealing
            enemy.charge = 0
        else:
            print("The bleeding wore off you are no longer bleeding")
            passive = False
    else:
        dealing = rand.randint(enemy.attackmin,enemy.attackmax)
        print(images.thief_attack)
        print("The",enemy.name,"slashes you dealing",dealing,"dmg")
        hp -= dealing
        sleep(1)
        if dealing > (enemy.attackmax - enemy.attackmin)/2 + enemy.attackmin:
            print("The slash causes you to bleed")
            passive = True
        attack_after = False
        sleep(3)
        cls()
        enemy.charge = 1
    return (critrate,hp,dmg,usage,passive,attack_after)



        
def rage_ability(enemy,critrate,hp,dmg,usage,passive,dmg_base,attack_after,base_hp):
    if passive == True:
        print("The",enemy.name,"is still enranged, increasing its dmg.")
    elif enemy.hp < enemy.base_hp//2:
        print("The",enemy.name,"is enraged its attack dmg has been raised!!!!!")
        print(images.rage)
        sleep(1)
        enemy.attackmax = enemy.attackmax + enemy.attackmax//2 # default 2
        enemy.attackmin = enemy.attackmin + enemy.attackmin//2 # default 2
        usage = False
        passive = True
        sleep(3)
        cls()
    return (critrate,hp,dmg,usage,passive,attack_after)




def charge_ability(enemy,critrate,hp,dmg,usage,passive,dmg_base,attack_after,base_hp):
    charge = rand.randint(1,5) # default 1,6
    if charge == 5:
        print("The",enemy.name,"charges at you")
        slow_print("The "+enemy.name+" hit you dealing " + str(enemy.attackmin*3) +" dmg\n",0.06,clear = False)
        hp -= enemy.attackmin*3
        sleep(1)
        usage = False
        attack_after = False
    return (critrate,hp,dmg,usage,passive,attack_after)




    
def fear_ability(enemy,critrate,hp,dmg,usage,passive,dmg_base,attack_after,base_hp):
    if passive == True:
        fear = rand.randint(1,5)
        if fear > 1:
            print("You are still afraid!")
            dmg = dmg_base//3*2
            sleep(2)
            return (critrate,hp,dmg,usage,passive,attack_after)
        else:
            print("The fear wore off. You are back at full damage")
            dmg = dmg_base
            usage = True
            passive = False
            sleep(3)
            return (critrate,hp,dmg,usage,passive,attack_after)
    fear = rand.randint(1,3) # default 1,3
    if fear == 3:
        print("The makes you cower in fear dmg is lowerd by 1/3")
        dmg -= dmg//3
        sleep(1)
        usage = True
        passive = True
        sleep(3)
    return (critrate,hp,dmg,usage,passive,attack_after)


#####################################################################################################
def fight(enemy,healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg,xp,gold,inventory,lv,attack_image,ability = None,ability2 = None,ability3 = None):
    #varrible decloration
    dmg_base = dmg
    dead = False
    cls()
    possible_acctions = ["attack","heal","a","h","nothing"]
    attacks = ["sword","bow","magic","s","b","m"]
    heals = ["heal","magic heal","h","m"]
    ability_usage = True
    ability_usage2 = True
    ability_usage3 = True
    critrate = inventory.count("lucky coin")*2
    passive = False
    passive2 = False
    passive3 = False
    burn = False
    burn_total = 0
    if lv < 3:
        heals.remove("m")
        heals.remove("magic heal")
    attack_after = True
    attack_after2 = True
    attack_after3 = True
    
    while enemy.hp >= 0:
        #checks if the enemy has any effects on the player
        if passive == True:
            critrate,hp,dmg,ability_usage,passive,attack_after = ability(enemy,critrate,hp,dmg,ability_usage,passive,dmg_base,attack_after,base_hp)
        if passive2 == True:
            critrate,hp,dmg,ability_usage2,passive2,attack_after2 = ability2(enemy,critrate,hp,dmg,ability_usage,passive2,dmg_base,attack_after2,base_hp)
        if passive3 == True:
            critrate,hp,dmg,ability_usage3,passive3,attack_after3 = ability3(enemy,critrate,hp,dmg,ability_usage,passive3,dmg_base,attack_after3,base_hp)

        #if you die to an effect
        if hp <= 0 and "totem of undying" in inventory and enemy.name not in ["thief","ghoul"]: 
            slow_print("You have died in combat- ",0.1,3,clear = False)
            print("\nBut with the totem of undying you are reborn!")
            hp = base_hp
            print("-1 totem of undying")
            inventory.remove("totem of undying")
        elif hp <= 0 and enemy.name == "thief" :
            slow_print("You have fainted in combat- ",0.1,3)
            stall = input("Press enter to continue:")
            dead = True
            return healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg_base,xp,gold,dead
        elif hp <= 0 :
            slow_print("You have died in combat- ",0.1,3)
            stall = input("Press enter to continue:")
            dead = True
            return healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg_base,xp,gold,dead
            
        attack_after = True
        attack_after2 = True
        attack_after3 = True

        #looks for what the player wants to do 
        if arrows == 0 and "b" in attacks:
            attacks.remove("b")
            attacks.remove("bow")
        if mana_pots == 0 and "m" in attacks:
            attacks.remove("m")
            attacks.remove("magic")
            if lv >= 3:
                heals.remove("m")
                heals.remove("magic heal")
        if healing_pots == 0 and "h" in heals:
            heals.remove("h")
            heals.remove("heal")
        if not heals and "h" in possible_acctions:
            possible_acctions.remove("heal")
            possible_acctions.remove("h")
        
        print(colorama.Fore.GREEN +"Hp",hp,"/",base_hp)
        print(colorama.Fore.MAGENTA +"Healing pots:", healing_pots)
        print(colorama.Fore.CYAN+ "Mana pots:", mana_pots)
        print(colorama.Fore.RESET +"Arrows:", arrows)
        print(colorama.Fore.BLUE + "Lv:",lv)
        print(colorama.Fore.RED + enemy.name, "hp:",enemy.hp,"/",enemy.base_hp)
        print(colorama.Fore.RESET + "Critrate:",critrate*10,"%")
        print(colorama.Fore.MAGENTA + "Dmg:",dmg,"/",dmg_base)
        print (colorama.Fore.RESET +"Possible actions:",possible_acctions)
        action = validate(possible_acctions,"What do you choose to do: ")


        #grabing user actions and running them
        if action in ["attack","a"]:
            print ("Possible actions:",attacks)
            action = validate(attacks, "What weapon do you want to use: ")
            if action in ["bow","b"]:
                arrows = bow_attack(enemy,dmg,arrows,lv)
            elif action in ["sword","s"]:
                critrate = sword_attack(enemy,dmg,critrate,inventory)
            elif action in ["magic","m"]:
                if lv >= 12: 
                    print(colorama.Fore.RED + "They're burning")
                    print(images.fire_attack)
                    print(colorama.Fore.RESET+" ")
                    burn = True
                mana_pots = magic_attack(enemy,dmg,mana_pots,inventory)

                
        elif action in ["heal","h"]:
            print ("Possible actions:",heals)
            action = validate(heals, "What heal do you want to use: ")
            if action in ["heal","h"]:
                healing_pots -= 1
                healing_amount = base_hp//5*2
                hp += healing_amount
                if hp > base_hp: hp = base_hp
                print("You used a healing potion!")
                print("+",healing_amount,"hp")
                print(colorama.Fore.GREEN +"Hp",hp,"/",base_hp)
            if action in ["magic heal","m"]:
                mana_pots -= 1
                healing_amount = base_hp - hp
                hp += healing_amount
                print(images.magic_healing)
                if hp > base_hp: hp = base_hp
                print("You used healing magic!")
                print("+",healing_amount,"hp")
                print("-1 mana pots")
                print(colorama.Fore.GREEN +"Hp",hp,"/",base_hp)
                if lv >= 6: 
                    dmg = dmg_base
                    print("Efects cleared")
                    passive = False
                    passive2 = False
                    passive3 = False

            
            
        if enemy.hp <=0:
            break
        #enemies turn
        print(enemy.name,colorama.Fore.RED + "hp:",enemy.hp,"/",enemy.base_hp)
        slow_print(colorama.Fore.RESET + "Your turn is over its the enemies turn.",0.03,4,clear = False)
        cls()

        if burn == True:
            burning = rand.randint(1,5)
            if burning > 1:
                amount = dmg//3
                print(colorama.Fore.RED + "The enemy takes burn damage dealing",amount,"dmg",colorama.Fore.RESET +" \n\n")
                enemy.hp -= amount
                burn_total += amount
            else:
                print("The enemy is no longer burning. The burning did a total of",burn_total,"dmg\n\n")
                burn == False
                burn_total = 0
            if enemy.hp <= 0: break

        # if the enemy has abilities
        if ability != None and ability_usage != False and passive == False:
            critrate,hp,dmg,ability_usage,passive,attack_after = ability(enemy,critrate,hp,dmg,ability_usage,passive,dmg_base,attack_after,base_hp)
        if ability2 != None and ability_usage2 != False and passive2 == False and attack_after == True and attack_after2 == True:
            critrate,hp,dmg,ability_usage2,passive2,attack_after2 = ability2(enemy,critrate,hp,dmg,ability_usage,passive2,dmg_base,attack_after2,base_hp)
        if ability3 != None and ability_usage3 != False and passive3 == False and attack_after == True and attack_after2 == True and attack_after3 == True:
            critrate,hp,dmg,ability_usage3,passive3,attack_after3 = ability3(enemy,critrate,hp,dmg,ability_usage,passive3,dmg_base,attack_after3,base_hp)

        #enemy base attack
        if attack_after == True and attack_after2 == True and attack_after3 == True:
            enemy_dmg = enemy.attack()
            hp -= enemy_dmg
            print(attack_image)
            print("The enemy attacks dealing",enemy_dmg,"dmg")

        #if you have second chance
        if hp <= 0 and "totem of undying" in inventory and enemy.name not in ["thief","ghoul"]: 
            slow_print(colorama.Fore.RED+"You have died in combat- ",0.1,3,clear = False)
            print(colorama.Fore.GREEN+"\nBut with the totem of undying you are reborn!")
            hp = base_hp
            print(colorama.Fore.RESET + "-1 totem of undying")
            inventory.remove("totem of undying")
        elif hp <= 0 and enemy.name == "thief" :
            slow_print("You have fainted in combat- ",0.1,3)
            dead = True
            return healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg_base,xp,gold,dead
        elif hp <= 0 :
            slow_print("You have died in combat- ",0.1,3)
            stall = input("Press enter to continue:")
            dead = True
            return healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg_base,xp,gold,dead
        
        print("The enemies turn is over!")
        stall=input("Press enter to continue:")
        cls()
# if its the last boss
    if enemy.name == "dragon":
        return healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg_base,xp,gold,dead
    #gold drops
    slow_print("You have defeated the " + enemy.name,0.07,1,clear = False)
    gold_drop = rand.randint(enemy.golddropmin,enemy.golddropmax)
    xp_drop = rand.randint(enemy.xpmin,enemy.xpmax)
    if "lucky coin" in inventory:
        lucky_add = gold_drop//5*inventory.count("lucky coin")
        gold += lucky_add

    # what the enemy dropped
    gold += gold_drop
    xp += xp_drop
    slow_print("The enemy gave " + str(xp_drop) + " xp",0.05,1,clear = False)
    slow_print("The enemy dropped " + str(gold_drop) + " coins",0.05,1,clear = False)
    if "lucky coin" in inventory:
        slow_print("The lucky coin(s) granted an additional " + str(lucky_add) + " coins\n",0.05,1,clear = False)
    stall=input("\nPress enter to continue:")
    cls()
    return healing_pots,arrows,mana_pots,critrate,hp,base_hp,dmg_base,xp,gold,dead


