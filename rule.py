import re
class FizzInt(int):
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

    def reverse(self, final):
        arr = re.findall('.[^A-Z]*', final)
        if len(arr) <= 1:
            return final
        else:
            arr.reverse()
            return ''.join(arr)

    def makeRule(self, ruleType, multiple, word="", character=""):
        def newRule(final, num):
            if num.isMultipleOf(multiple):
                if ruleType == 'normal':
                    final += word
                elif ruleType == 'insertBefore':
                    final = self.insertBeforeChar(character, final, word)
                elif ruleType == 'reverse':
                    final = self.reverse(final)
                elif ruleType == 'override':
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