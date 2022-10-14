def hi(name= "y"):
    def greet():
        return "you inside greet()"

    def welcome():
        return "y in welcome()"

    if name == "y":
        return greet
    else:
        return welcome
# new_feature1

a = hi()
print(a)
print(a())
