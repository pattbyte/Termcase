import time
import os
import random

print("Termcase [v1.0]")
print("( www.github.com/pattbyte/termcase )")
print()
time.sleep(2.1)

print("Loading Termcase... [0.5%]")
time.sleep(0.1)
print("Installing from repository [5.2%]")
time.sleep(0.1)
print("Compiling from repository [23%%]")
time.sleep(0.1)
print("Installing from repository [26.3%]")
time.sleep(0.1)
print("Installing from repository [30.1%]")
time.sleep(0.03)
print("Copying code [35.8%]")
time.sleep(0.03)
print("Reading code [37.3%]")
time.sleep(0.03)
print("Loading repository [39.2%]")
time.sleep(0.03)
print("Copying code ( github ) [43%]")
time.sleep(0.03)
print("Copying code ( github ) [48%]")
time.sleep(0.02)
print("Extracting github.com/pattbyte/termcase")
time.sleep(0.02)
print("Extracting github.com/pattbyte/termcase")
time.sleep(0.02)
print("Extracting github.com/pattbyte/termcase")
time.sleep(0.02)
time.sleep(0.02)
print("Verifying github.com/pattbyte/termcase")
time.sleep(0.02)
print("Cloning github.com/pattbyte/termcase")
time.sleep(0.02)
print("Generating cache [80%]")
time.sleep(0.02)
print("Generating cache [84%]")
time.sleep(0.02)
print("Unpacking code [90.1%]")
time.sleep(0.02)
print("Downloading modules [93.3%]")
time.sleep(0.1)
print("Generating ascii art [98.5%]")
time.sleep(1.5)
print("Termcase succsefully installed")

if os.name =="nt":
        os.system("cls")
else:
        os.system("clear")

print("commands:\n[stats]: Shows your stats\n[qt/quit]: quits game\n[clear]: clears the screen\n[help]: displays commands")
print()
print("[ENTER] to roll !")
knives = ["★ Karambit","★ Butterfly Knife","★ Stiletto Knife","★ Talon Knife","★ Gut Knife","★ Navaja Knife","★ Huntsman Knife","★ Falchion Knife"]
uluck = ["Deagle | Tilted","Ak47 | Slate","Ak47 | Ice Coaled","USP-S | Jawbreaker","Ak47 | Fishing Net","AWP | Atheris","M4a1 | Emphorosaur-S","Glock18 | Weasel","Glock18 | Vogue","Glock18 | Candy Apple","M4a1 | Nightmare","m4a4 | Desolate Space","m4a1 | Fizzy Pop","AWP | Crakow!","Sawed off | Analog input","Sawed off | Apocalypto","Tec 9 | Avalanche"]

money = 0
count =0
gold = random.randint(1,384)

while True:
        roll = input("› ")
        if roll == "":
                count +=1
                rl = random.randint(1,384)
                if rl == gold:
                        knife = random.choice(knives)
                        float = random.uniform(0.05,0.85)
                        value = 0.55
                        n = 3

                        if float > 0.80:
                                n = 650
                        elif float > 0.60:
                                n = 750
                        elif float > 0.50:
                                n = 850
                        elif float > 0.40:
                                n = 900
                        elif float > 0.30:
                                n = 950
                        elif float > 0.15:
                                n = 1020
                        else:
                                n = 1100


                        price = random.randint(150,n)
                        print()
                        print(f"\033[33m| [!!] Unboxed: {knife}\033[0m")
                        print(f"|- [i] Float: {float}")
                        print(f"|- [$] Price: {price}€")
                        money+=price
                        print()
                elif rl != gold:
                        item = random.choice(uluck)
                        float = random.uniform(0.05,0.85)

                        if float > 0.80:
                                n = 15
                        elif float > 0.60:
                                n = 20
                        elif float > 0.50:
                                n = 30
                        elif float > 0.40:
                                n = 35
                        elif float > 0.30:
                                n = 45
                        elif float > 0.15:
                                n = 50
                        else:
                                n = 65
                        prc = random.randint(1,n)
                        money +=prc
                        print(f"\033[90m| [~] Unboxed: {item}\033[0m")
                        print(f"|- [info] Float: {float}")
                        print(f"|- [$] Price: {prc}€")
        elif roll.lower() == "stats":
                print(f"› Rolls : {count}")
                print(f"\033[32m› Wallet : {money}€\033[0m")

        elif roll.lower() == "quit":
                        print("bye! [Termcase quit succsessfully]")
                        break
        elif roll.lower() == "qt":
                        print("")
                        print("bye! [Termcase quit successfully]")
                        break
        elif roll.lower() == "clear":
                        os.system("clear")
        elif roll.lower() == "help":
                print()
                print("commands:\n[stats]: Shows your stats\n[qt/quit]: quits game\n[clear]: clears the screen\n[help]: displays commands")






























