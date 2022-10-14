def hi():
    return "Hi y"


def doSomethingBeforeHi(func):
    print("I am doing")
    print(func())

doSomethingBeforeHi(hi)