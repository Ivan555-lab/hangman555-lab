class Cat:
    Name_Class = "Cats"
    def __init__(self, wool_color, eyes_color, name):
        self.wool_color = wool_color
        self.eyes_color = eyes_color
        self.name = name

my_Cat = Cat('W', 'G', 'M')
print("Cl name - ", my_Cat.Name_Class)
print("Here is our Cat:")
print("W col- ", my_Cat.wool_color)