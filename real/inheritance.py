
class Dog():

    #class attribute
    species = 'mammal'

    #instance attribute
    def __init__(self, name, age):
        self.name= name
        self.age= age

    #instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)    

    #instance method
    def speak(self, sound):
        return "{} speak like {}".format(self.name, sound)

#Child class (inherits from Dog class)
class RusselTerrior(Dog):
    def run(self, speed):
        return "{} speed is {}".format(self.name, speed)

    def chage_class_property(self, value):
        self.species= value

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {} km per hours".format(self.name, speed)

jim= Bulldog('jim', 6)
print(jim.run(10))

suju= RusselTerrior('suju', 7)
suju.chage_class_property('hey')

kim= Dog('kim', 7)
kim.species= 'new'

sahi= Dog()
print(sahi.species)