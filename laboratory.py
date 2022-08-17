class Player():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.position = None

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)

num19 = Player("Elliott", 18)

num19.print_name()