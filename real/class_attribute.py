class Person:
    pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

jane = Person()
bob = Person()

jane.add_pet("cat")
print(jane.pets)
print(bob.pets) # oops!


class Person1:
    TITLES = ['Dr', 'Mr', 'Mrs', 'Ms']

    def __init__(self, title, name, surname, allowed_titles=TITLES):
        allowed_titles.append('New')
        if title not in allowed_titles:
            raise ValueError("%s is not a valid title." % title)

        self.title = title
        self.name = name
        self.surname = surname
p = Person1('New',' asdfasf','sdfasdf')
print(p)
p = Person1('Dr' ,'asdfasf','sdfasdf')
print(p.TITLES)



class Smith:
    surname = "Smith"
    profession = "smith"

    def __init__(self, name, profession=None):
        self.name = name
        if profession is not None:
            self.profession = profession

sm= Smith('smith', profession='driver')
print(sm.profession)

sn= Smith('smith')
print(sn.profession)
