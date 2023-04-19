# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
import sys


class FizzInt (int):
    def isMultipleOf(self, value):
        return self % value == 0


class Rules:
    def __init__(self):
        self.rules = []
        self.total = 100

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


def fizzbuzz():
    args = sys.argv[1:]
    rule = Rules()

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
    # rule = Rules()
    # rule.makeRule("normal", 4, "Haha")
    # rule.makeRule("override", 9, "Override")
    # rule.makeRule("insertBefore", 7, "Newbie", "O")
    # rule.makeRule("reverse", 13)
    # rule.printResult()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fizzbuzz()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
