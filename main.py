# python main.py normal-5-fezz normal-3-buzz override-7-bong insertBefore-11-gallow-b reverse-9

import re
import sys


class FizzInt (int):
    def isMultipleOf(self, value):
        return self % value == 0


class Rules:
    def __init__(self, totalNum):
        self.rules = []
        self.total = totalNum

    def insertBeforeChar(self, character, oldWord, newWord):
        index = oldWord.find(character)
        if index == -1:
            return oldWord + newWord
        else:
            final = oldWord[:index] + newWord + oldWord[index:]
            return final

    def reverse(self, word):
        arr = re.findall('.[^A-Z]*', word)
        if len(arr) == 0:
            return ""
        else:
            return arr.reverse().join("")

    def makeRule(self, ruleType, multiple, word="", character=""):
        def newRule(final, num):
            if(num.isMultipleOf(multiple)):
                if(ruleType == 'normal'):
                    final += word
                elif(ruleType == 'insertBefore'):
                    final = self.insertBeforeChar(character, final, word)
                elif(ruleType == 'reverse'):
                    final = self.reverse(word)
                elif(ruleType == 'override'):
                    final = word
            return final
        self.rules.append(newRule)

    def runRules(self, curr):
        final = ""
        for i in self.rules:
            final = i(final, curr)
        return final

    def printResult(self):
        for i in range(1, self.total + 1, 1):
            final = self.runRules(FizzInt(i))
            if len(final) == 0:
                print(i)
            else:
                print(final)


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
            return
    else:
        runCustomRules(args)
    print("END OF GAME")


if __name__ == '__main__':
    fizzbuzz()

