# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class xint (int):
    def isMultipleOf(self, value):
        return self % value == 0

def fizzbuzz():
    # Use a breakpoint in the code line below to debug your script.
    total = xint(input(f'Hi! Please input the number you wish to count up to:'))
    for i in range(1, total + 1, 1):
        curr = xint(i)
        if(curr.isMultipleOf(5)):
            print("Multiple Of 5")
        elif(curr.isMultipleOf(3)):
            print("Multiple Of 3")
        else:
            print(curr)

    # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fizzbuzz()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
