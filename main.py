# python main.py normal-5-fezz normal-3-buzz override-7-bong insertBefore-11-gallow-b reverse-9

import sys
from utils import runDefaultRules, runCustomRules, printInstructions


def fizzbuzz():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Running Default Arguments :")
        print("normal-3-fizz normal-5-buzz normal-7-bang override-11-bong insertBefore-13-fezz-b reverse-17")
        ans = input("Are you sure you want to use default? [Y/N]")
        if ans == 'Y':
            runDefaultRules()
        else:
            print("GAME ABORTED")
    elif len(args) == 1 and args[0] == 'help':
        printInstructions()
    else:
        runCustomRules(args)
        print("END OF GAME")

if __name__ == '__main__':
    fizzbuzz()

