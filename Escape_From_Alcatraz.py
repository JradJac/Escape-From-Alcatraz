#Final Version
import sys
import time
from colorama import Fore, Style, init
init()


print("Hello, and welcome to Prison Escape. \n This is a horror game where your goal is to escape Alcatraz.\n Good luck!")

print("\n (－_－) zzZ \n You have awoken in a prison cell with no recollection as to how you got there. \n What do you want to do?")

def chapter1():
    while True:
        print("\n1: Look around the cell. "
              "\n2: Check for items. "
              "\n3: Quit. ")
        choice = input("Please make a selection.\n")
    
        if choice == "1":
            time.sleep(0.5)
            pick = input("You found a large hole behind the toilet. Go inside?\n 1 for Yes.\n 2 for No.\n")
            while True:
                if pick == "1":
                    time.sleep(0.5)
                    print("You have lost your head!\n ( ҂ × ཀ × ) \n Someone set a trap for you. Try again.")
                else:
                    pick == "2"
                break       
        elif choice == "2":
            time.sleep(0.5)
            print("You have found the keys to the cell and have escaped! Ⓞ═╦╗")
            chapter2()
        else:
            choice == "3"
            time.sleep(0.5)
            print("Bye. ( ・_・)ノ")
            sys.exit()
            
def chapter2():
    while True:
        time.sleep(1)
        print("\nYou have found yourself in hallway. \nYou hear sounds coming from the LEFT and see stairs to the RIGHT."
              "\nDo you go LEFT or RIGHT?")
        time.sleep(1)
        print("\n1: Go LEFT. (⸝⸝⸝O﹏ O⸝⸝⸝) "
              "\n2: Go RIGHT. ಠ_ʖಠ"
              "\n3: Quit. ")
        choice = input("Please make a selection.\n")

        if choice == "1":
            time.sleep(0.5)
            pick = input("You have found a room and hear movement inside. Go inside?\n 1 for Yes.\n 2 for No.\n")
            while True:
                if pick == "1":
                    time.sleep(0.5)
                    print("You have been stabbed!\n ( ҂ × ཀ × ) \nYou startled an inmate and he shanked you (*ﾟ∀ﾟ)つ＝lニニフ."
                          "Try again.")
                else:
                    pick == "2"
                break       
        elif choice == "2":
            time.sleep(0.5)
            print("You have found a staircase that leads to the first floor!"
                  "\n￣￣┗┓"             
                  "\n￣￣￣┗┓"
                  "\n￣￣￣￣┗┓"
                  "\n￣￣￣￣￣┗┓")
            chapter3()
        else:
            choice == "3"
            time.sleep(0.5)
            print("Bye. ( ・_・)ノ")
            sys.exit()
            
def chapter3():
    while True:
        time.sleep(0.5)
        print("\nAt the bottom of the stairs you enter the cafeteria. ( ˘▽˘)っ♨"
              "\nYou see the door for the Emergency Exit and the door to the kitchen."
              "\nWhich door do you choose?")
        time.sleep(0.5)
        print("\n1: Go into Kitchen. "
              "\n2: Use Emergency Exit. "
              "\n3: Quit. ")
        choice = input("Please make a selection.\n")
    
        if choice == "1":
            time.sleep(0.5)
            pick = input("You enter the kitchen and find the chef standing at the stove."
                         "\nDo you want to talk to him?\n 1 for Yes.\n 2 for No.\n")
            while True:
                if pick == "1":
                    time.sleep(0.5)
                    print("The Chef turns to you and stabs you in the heart (*ﾟ∀ﾟ)つ＝lニニフ🤍."
                          "\nYou are dead. ( ´ཀ` ) Try again.")
                    break
                else:
                    pick == "2"
                    time.sleep(0.5)
                    print("You have made it past the chef and through the back door!")
                chapter4()       
        elif choice == "2":
            time.sleep(0.5)
            print("You run towards the Emergency Exit. You trip over a wire and fall."
                  "\nA giant pane of glass falls from the ceiling crushing you. ┻━┻ ︵ \(Ò_Ó \). Try again.")
        else:
            choice == "3"
            time.sleep(0.5)
            print("Bye. (￣ｰ￣)ﾉ")
            sys.exit()
            
def chapter4():
    while True:
        time.sleep(0.5)
        print("\nWalking through the backdoor you find yourself in an empty gated parking lot."
              "There is only one vehicle in the parking lot. A garbage truck."
              "\n What do you want to do?")
        time.sleep(0.5)
        print("\n1: Get into garbage truck. "
              "\n2: Try to climb fence. "
              "\n3: Look for items. "
              "\n4: Quit.")
        choice = input("Please make a selection.\n")
    
        if choice == "1":
            time.sleep(0.5)
            print("You get into the garbage truck and find the keys. You start the truck and drive toward the gate."
                  "\nAs you line up with the gate you floor it! You hit the gate hard and the truck explodes!(●～*"
                  "\nYou died ( ҂ × ཀ × ). Try again")
                  
        elif choice == "2":
            time.sleep(0.5)
            print("You run over to the fence, jump up to climb over it...but unbeknownst to you it is electrified ⦙⦙⦙⦙⦙⌁⌁⌁."
                  "\n You died ( ҂ ⌁ ཀ ⌁ ) Try again.") 
        elif choice == "3":
            time.sleep(0.5)
            print("You quickly walk around the parking lot looking for anything that might help you."
                  "\nYou come across a set of keys Ⓞ═╦╗! They appear to go to a boat."
                  "\nRight next to them you find a hole in the fence ⦙⦙⦙⦙⦙ and escape the parking lot.")
            chapter5()
        else:
            choice == "4"
            time.sleep(0.5)
            print("Bye. (￣ｰ￣)ﾉ")
            sys.exit()
            
def chapter5():
    while True:
        time.sleep(0.5)
        print("\nAfter slipping through the hole in the fence you find yourself near a lighted path. You see 3 possible routes to take."
              "\nWhich one you choose?")
        time.sleep(0.5)
        print("\n1: Use main path.. "
              "\n2: Go to pier. "
              "\n3: Go to lighthouse. "
              "\n4: Quit.")
        choice = input("Please make a selection.\n")
    
        if choice == "1":
            time.sleep(0.5)
            print("You start walking down the main path. ꆜꆜꆜ When all of a sudden you see the chef! He runs at you with a knife."
                  "\nYou trip when you try to run away. He catches you and stabs you to death."
                  "\n(*ﾟ∀ﾟ)つ＝lニニフ ( ´ཀ` ). Try again.")
        elif choice == "2":
            time.sleep(0.5)
            print("You start walking towards the pier. It is very quiet and dark. You make it to the peir and find a boat!"
                  "\nYou try the keys you found in the parking lot. They fit! You turn the key...BOOM (●～* the boat explodes 🛥"
                  "\nYou are dead. ( ´ཀ` ) Try again.") 
        elif choice == "3":
            time.sleep(0.5)
            print("Through the woods you see a lighthouse ⛯. You make your way through the trees ⍋⍋⍋."
                  "\nWhen you finally get there you noticed there is boat. You get on the boat and the keys Ⓞ═╦╗ are still in it!"
                  "\nYou try to start the boat and it fires right up!"
                  "\nYou have successfully escaped Alcatraz!")
            time.sleep(2)
            print("\nGame over. Thank you for playing.")
            sys.exit()
        else:
            choice == "4"
            time.sleep(0.5)
            print("Bye. (￣ｰ￣)ﾉ")
            sys.exit()
chapter1()
chapter2()
chapter3()
chapter4()
chapter5()
