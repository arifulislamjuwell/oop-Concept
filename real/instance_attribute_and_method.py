class Dog:

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

    def prefix_fun(self):
        if hasattr(self, '_prefix'):
            return self._prefix
        
        prefix= self.name+str(self.age)
        self._prefix= prefix
        return prefix
    
    def act(self):
        return self._prefix+' its work'


#object create
dog_1= Dog('pussu', 4)
dog_2= Dog('mickey', 7 )

print("the name of two {}  {}".format(dog_1.name, dog_2.name))

def get_biggest_number(self, *args):
    return max(args)

if dog_1.species == 'mammal':
    print('class property working')

print('maximum age is {} years old'.format(get_biggest_number(dog_1.age, dog_2.age)))

print(dog_1.description())
print(dog_1.speak('gheuuu'))


print(dog_1.act())