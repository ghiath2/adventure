import sys
import os
import random
import time


class Game:

    def print_slow(self, str, delay=0.1):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print("\n")


    def reset_console(self):
        print("\n")
        os.system('cls||clear')


    def fprint(self, str, delay=0):
        print("\n" + str)
        time.sleep(delay)


    def sprint(self, str, delay=0):
        print(str)
        time.sleep(delay)


class World:

    def entry(self):
        hero.location = "entry"
        print(f"\nHealth: {hero.health}")
        game_functions.fprint("You are in a dark cave. The entry has been sealed by fallen rocks. There is no way out.", 2)
        print("Ahead, you can see a cavern. Will you continue?")
        print("Enter 'yes' or 'no'.")
        self.check_medkit()
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.cavern()
            elif action == "no":
                game_functions.fprint(
                    "A bat flies over your head and you hear screetches in the distance.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You sit in total darkness wondering if there's a way out.")

    def cavern(self):
        hero.location = "cavern"
        print(f"\nHealth: {hero.health}")
        game_functions.fprint("You stumble into a dimly lit cavern.", 2)
        print("You cannot go right or left but the cave continues ahead. Will you go on?")
        print("Enter 'yes' or 'no'.")
        self.check_bat_attack()
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.hallway()
            elif action == "no":
                game_functions.fprint("You sit down and eat some food you brought with you.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You shiver from the cold.")