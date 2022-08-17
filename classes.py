class Cat: 
    lives = 9
Cat1 = Cat() 
Cat2 = Cat()
Cat2.lives = 8 
print(“Cat1 has”, Cat1.lives, “lives”) 
print(“Cat2 has”, Cat2.lives, “lives”)
class Chameleon: 
    invisible = False 
    def blend_in_with_background(self): 
        self.invisible = True
Chameleon1 = Chameleon() 
Chameleon2 = Chameleon() 
Chameleon1.blend_in_with_background() 
print(“Chameleon1 is invisible:”, Chameleon1.invisible) 
print(“Chameleon2 is invisible:”, Chameleon2.invisible)
class Dog: 
    def __init__(self, dogname):
        self.name = dogname
Dog1 = Dog(“Fido”) 
Dog2 = Dog(“Lassy”) 
print(“Dog1 has a name of”, Dog1.name) 
print(“Dog2 has a name of”, Dog2.name)
class House: 
    house_dog = Dog(“Doggy”) 
House1 = House() 
print(“The house dog’s name is”, House1.house_dog.name)
class Zoo: 
    def __init__(self, cat, chameleon, dog, city_name): 
        self.cat = cat 
        self.chameleon = chameleon 
        self.dog = dog 
        self.city_name = city_name 
    def print_animals(self): 
        print("The cat has", self.cat.lives, "lives") 
        print("The chameleon is invisible:", Chameleon1.invisible) 
        print("The dog has a name of", self.dog.name) 
    def print_zoo(self): 
        print("The", self.city_name, "Zoo has 3 animals") 
        print("Here is some information about them:") 
        self.print_animals()
