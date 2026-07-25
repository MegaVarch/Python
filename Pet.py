

class Pet:
    def __init__(self, name, species, age, color):
        self.name = name
        self.species = species
        self.age = age
        self.color = color

    def display_profile(self):
        print("----- Pet Profile -----")
        print("Name    :", self.name)
        print("Species :", self.species)
        print("Age     :", self.age)
        print("Color   :", self.color)
        print()



pet1 = Pet("Buddy", "Dog", 4, "Brown")
pet2 = Pet("Whiskers", "Cat", 2, "White")
pet3 = Pet("Coco", "Parrot", 3, "Green")

pet1.display_profile()
pet2.display_profile()
pet3.display_profile()