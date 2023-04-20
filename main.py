# python main.py normal-5-fezz normal-3-buzz override-7-bong insertBefore-11-gallow-b reverse-9

import re
import sys
from rule import Rules, FizzInt

def runDefaultRules():
    totalNum = input("What is the number you wish to count up to?")
    rule = Rules(int(totalNum))
    rule.makeRule("normal", 3, "Fizz")
    rule.makeRule("normal", 5, "Buzz")
    rule.makeRule("normal", 7, "Bang")
    rule.makeRule("override", 11, "Bong")
    rule.makeRule("insertBefore", 13, "Fezz", "B")
    rule.makeRule("reverse", 17)
    rule.printResult()

def runCustomRules(args):
    totalNum = input("What is the number you wish to count up to?")
    rule = Rules(int(totalNum))
    for arg in args:
        ruleArr = arg.split('-')
        for i in range(len(ruleArr), 4):
            ruleArr.append("")
        ruleType, multiple, word, insertBeforeChar = ruleArr

        multiple = int(multiple)
        word = word.capitalize()
        insertBeforeChar = insertBeforeChar.upper()

        rule.makeRule(ruleType, multiple, word, insertBeforeChar)
    rule.printResult()

def printInstructions():
    commands = [
        ['TYPE', 'EXAMPLE', 'EXPLANATION'],
        ['normal', 'normal-4-fizz', 'For multiples of 4, add "Fizz" to output'],
        ['override', 'override-3-bong', 'For multiples of 3, output "Bong" ONLY'],
        ['insertBefore', 'insertBefore-7-fezz-h', 'For multiples of 7, add "Fezz" to output, immediately before "H"'],
        ['reverse', 'reverse-11', 'For multiples of 11, reverse output'],

    ]
    examples = [
        ['COMMAND', 'NUMBER', 'RESULT'],
        ['normal-3-fizz normal-5-buzz', '15', 'FizzBuzz'],
        ['normal-2-fizz override-7-bong', '42', 'Bong'],
        ['normal-3-buzz insertBefore-7-fezz-b', '21', 'FezzBuzz'],
        ['normal-5-fizz normal-7-buzz reverse-10', '70', 'BuzzFizz'],
    ]

    print("\n\nInstructions: List out commands in the following format: [type]-[number]-[word]-[character]")
    print("** Note that the rules generated will be carried out in sequence,from left to right \n")
    widths = [max(map(len, col)) for col in zip(*commands)]
    for row in commands:
        print("  ".join((val.ljust(width) for val, width in zip(row, widths))))

    print("\n\nSome Examples: \n")
    widths = [max(map(len, col)) for col in zip(*examples)]
    for row in examples:
        print("  ".join((val.ljust(width) for val, width in zip(row, widths))))

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

