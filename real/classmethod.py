from datetime import date 
  
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    
    def test(self):
        return 'hi'
    # a class method to create a  
    # Person object by birth year. 
    @classmethod    
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
      
    # a static method to check if a 
    # Person is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 18

class People(Person):
    
    @classmethod
    def fromBirthYear(cls, name, year):
        return 'hellow'
  
p = People('juwel', 12)
print(People.fromBirthYear('juwel', 243))  

# person1 = Person('mayank', 21) 
# person2 = Person.fromBirthYear('juwel', 1974)
  
# print (person1.age) 
# print (person2.age) 
# print(person1.fromBirthYear('juwel', 1994).age)

# print(Person.test(Person))