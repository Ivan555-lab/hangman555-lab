class Cat:
    Name_Class = "Cats"
    def __init__(self, wool_color, eyes_color, name):
        self.wool_color = wool_color
        self.eyes_color = eyes_color
        self.name = name

my_Cat = Cat('W', 'G', 'M')
my_Cat.name = 'Gregory Andelov'
my_Cat.wool_color = 'B'
print("Cl name - ", my_Cat.Name_Class)
print("Here is our Cat:", my_Cat.name)
print("W col- ", my_Cat.wool_color)
print('Y-', my_Cat.eyes_color)