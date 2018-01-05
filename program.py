import random

import time

from actors import Wizard, Creature

def main():
    #print welcome screen
    print_header()
    game_loop()


def print_header():
    print('------------------------------------')
    print('      WIZARD BATTTTTTTLE            ')
    print('------------------------------------')
    print()


def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000),
    ]

    hero = Wizard('Gandalf', 75)

    #print(creatures)



    while True:

        active_creature = random.choice(creatures) #randomly select a creature
        print("A {} of level {} has appeared from a dark and foggy forest ..."
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature,):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides, taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == 'r':
            print('runnnnaway!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'
                  .format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('Ok, exiting game ... bye!')
            break

        print()

if __name__ == '__main__':
    main()
