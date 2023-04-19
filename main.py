# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class FizzInt (int):
    def isMultipleOf(self, value):
        return self % value == 0

class Rules:
    def __init__(self):
        self.rules = []
        self.total = 100
    def makeRule(self, type, word, multiple, character=""):
        if type == 'normal':
            def newRule(final, num):
                if(num.isMultipleOf(multiple)):
                    final += word
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

def insertBeforeChar(character, oldWord, newWord):
    index = oldWord.find(character)
    if index == -1:
        return oldWord + newWord
    else:
        final = oldWord[:index] + newWord + oldWord[index:]
        return final

def fizzbuzz():
    rule = Rules()
    rule.makeRule("normal", "Haha", 4)
    rule.printResult()

    # Use a breakpoint in the code line below to debug your script.
    # total = FizzInt(input(f'Hi! Please input the number you wish to count up to:'))
    # for i in range(1, total + 1, 1):
    #     curr = FizzInt(i)
    #     final = ""
    #
    #     if curr.isMultipleOf(3):
    #         final += "Fizz"
    #
    #     if curr.isMultipleOf(5):
    #         final += "Buzz"
    #
    #     if curr.isMultipleOf(11):
    #         final = "Bong"
    #
    #     if curr.isMultipleOf(13):
    #         final = insertBeforeChar("B", final, "Fezz")
    #
    #     if curr.isMultipleOf(17):
    #         final = final[::-1]
    #
    #     if len(final) == 0:
    #         print(curr)
    #         continue
    #
    #     print(final)

    # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fizzbuzz()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
