def hi(name= "y"):
    def greet():
        return "you inside greet()"

    def welcome():
        return "y in welcome()"

    if name == "y":
        return greet
    else:
        return welcome


a = hi()
print(a)
print(a())
