#Made by Sam D'Agostino
#Game -- "MINERS for MINORS"

import random
from colorama import Fore as f

tool = "Sticky Stick"
money = 0
MineRepeats = 1



Inventory = []

SellValues = {
    f"{f.LIGHTWHITE_EX}Dirt{f.RESET}": 1,
    f"{f.LIGHTBLACK_EX}Rock{f.RESET}": 5,
    f"{f.LIGHTYELLOW_EX}Good Stick{f.RESET}": 12,
    f"{f.BLACK}Coal{f.RESET}": 36,
    f"{f.WHITE}Iron{f.RESET}": 70,

    f"{f.MAGENTA}Amethyst{f.RESET}": 45,
    f"{f.YELLOW}Gold Ore{f.RESET}": 135,
    f"{f.GREEN}Emerald{f.RESET}": 330,
    f"{f.CYAN}Diamond{f.RESET}": 890,
    f"{f.RED}Netherite{f.RESET}": 16000,

    f"{f.BLUE}Bad Stick{f.RESET}": 9999 ** 2,
}


Shoplist_real = {
    "Sticky Stick": 0,
    "Stone Pickaxe": 500,
    "Polished Pickaxe": 1500,
    "Jackhammer": 6400,
    "Excavator": 11400,
    "Company Drill": 75500,
    "The Holy Grail for Miners": 160000
}

def Shop():
    global money
    global tool
    print(f"{f.LIGHTWHITE_EX}----SHOP----{f.RESET} Money : {money}")
    for ShopList in Shoplist_real:
        if ShopList == tool:
            Shoplist_real[ShopList] = "OWNED"
        print(f"{ShopList} : {Shoplist_real.get(ShopList)}")


    print(f"{f.LIGHTWHITE_EX}-------------{f.RESET}")
    ShopAction = input("What would you like to do? --> [Buy (item), Sell All, Back]: ")
    if ShopAction[0:3] == "Buy":
        if Shoplist_real.get((ShopAction[4:len(ShopAction)])):
            if Shoplist_real[ShopAction[4:len(ShopAction)]] == "OWNED":
                print(f"{f.GREEN}You already own that item doofus.{f.RESET}")
                Shop()
            else:
                if money >= Shoplist_real[ShopAction[4:len(ShopAction)]]:
                    print(f"{f.GREEN}Purchase successful!{f.RESET}")
                    money = money - Shoplist_real[ShopAction[4:len(ShopAction)]]
                    tool = ShopAction[4:len(ShopAction)]
                    Shop()
                else:
                    print(f"{f.RED}You don't have enough money bozo, L poor. Get a job fatty{f.RESET}")
                    Shop()
        else:
            print(f"{f.RED}That item is not in the shop small brain. Open yur eyes 0-0{f.RESET}")
            Shop()
    elif ShopAction[0:4] == "Sell":
        #print(ShopAction[5:len(ShopAction)])
       # print(Inventory)
        if ShopAction[5:len(ShopAction)] in Inventory:
            print(f"Successfully sold {ShopAction[5:len(ShopAction)]}(s)")
            while ShopAction[5:len(ShopAction)] in Inventory:
                Inventory.remove(ShopAction[5:len(ShopAction)])
                money = money + SellValues[ShopAction[5:len(ShopAction)]]
        elif ShopAction[5:len(ShopAction)] == "All":
            while len(Inventory) > 0:
                money = money + SellValues[Inventory[0]]
                Inventory.pop(0)

            Shop()
        else:
            print(f"{f.RED}StOOpid. YOu DoOn'T hAAve THAt. Sell smth else Dumbo.{f.RESET}")
            Shop()
    elif ShopAction[0:4] == "Back" or ShopAction[0:4] == "back" or ShopAction[0:1] == "b":
        Action()
    else:
        print(f"{f.RED}INVALID ACTION{f.RESET}")
        Shop()

def ShowInventory():
    print(f"{f.LIGHTWHITE_EX}--INVENTORY--{f.RESET}  Tool : {tool}" )
    Inventory_real = {}

    for Thing in Inventory:
        if Thing in Inventory_real.keys():
            Inventory_real[Thing] = Inventory_real[Thing] + 1
        else:
            Inventory_real[Thing] = 1
    for items in Inventory_real:
        print(f"{items} x{Inventory_real[items]}")
    print(f"{f.LIGHTWHITE_EX}-------------{f.RESET}")

def Mine():
    global rareJewel
    global RNG

    EPICmineRNG = random.randint(1, 12000)
    rareMineRNG = random.randint(1, 100)
    RNG = random.randint(1, 100)
    Jewel = " "
    if RNG == 100:
        Jewel = f"{f.WHITE}Iron{f.RESET}"
    elif RNG < 100 and RNG >= 90:
        Jewel = f"{f.BLACK}Coal{f.RESET}"
    elif RNG < 90 and RNG >= 70:
        Jewel = f"{f.LIGHTYELLOW_EX}Good Stick{f.RESET}"
    elif RNG < 70 and RNG >= 50:
        Jewel = f"{f.LIGHTBLACK_EX}Rock{f.RESET}"
    elif RNG < 50 and RNG >= 1:
        Jewel = f"{f.LIGHTWHITE_EX}Dirt{f.RESET}"
    print(f"You Mined: {Jewel}")
    Inventory.append(Jewel)

    if rareMineRNG == 100:
        RNG = random.randint(1, 100)
        rareJewel = " "
        if RNG <= 100 and RNG >= 100:
            rareJewel = f"{f.RED}Netherite{f.RESET}"
        elif RNG < 100 and RNG >= 90:
            rareJewel = f"{f.CYAN}Diamond{f.RESET}"
        elif RNG < 90 and RNG >= 70:
            rareJewel = f"{f.GREEN}Emerald{f.RESET}"
        elif RNG < 70 and RNG >= 50:
            rareJewel = f"{f.YELLOW}Gold Ore{f.RESET}"
        elif RNG < 50 and RNG >= 1:
            rareJewel = f"{f.MAGENTA}Amethyst{f.RESET}"
        print(f"Yoooooo coool You Mined: {rareJewel}")
        Inventory.append(rareJewel)

    if EPICmineRNG == 48000:
        RNG = random.randint(1, 10)
        EpicJewel = " "
        #if RNG == 10 - 1:
        EpicJewel = f"{f.BLUE}Bad Stick{f.RESET}"

        print(f"WOOAHHHH!1!!11! YOUU MIIEENED: {EpicJewel}")
        Inventory.append(EpicJewel)



def Action():
    TheAction = input("What Would you like to do? [Inv, Mine, Shop]: ")

    if TheAction == "Inv" or TheAction == "inv" or TheAction == "i":
        ShowInventory()
        Action()
    elif TheAction == "Mine" or TheAction == "mine" or TheAction == "m":
        if tool == "Sticky Stick":
            MineRepeats = 1
        if tool == "Stone Pickaxe":
            MineRepeats = random.randint(2, 4)
        if tool == "Polished Pickaxe":
            MineRepeats = random.randint(5, 10)
        if tool == "Jackhammer":
            MineRepeats = random.randint(11, 16)
        if tool == "Excavator":
            MineRepeats = random.randint(18, 28)
        if tool == "Company Drill":
            MineRepeats = random.randint(35, 50)
        if tool == "The Holy Grail for Miners":
            MineRepeats = 100

        i = 0
        while i < MineRepeats:
            i += 1
            Mine()


        Action()
    elif TheAction == "Shop" or TheAction == "shop" or TheAction == "s":
        Shop()
    else:
        print(f"{f.RED}INVALID ACTION{f.RESET}")
        Action()



Action()
