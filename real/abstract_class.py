from abc import ABC, abstractmethod,abstractstaticmethod

class Animal(ABC): 

    @abstractmethod
    def move(self): 
        pass
    
    @abstractmethod
    def stop(self):
        pass


class Human(Animal): 
    
    def move(self): 
        print("I can walk and run") 

    def stop(self):
        print('hi')
  
c=Human()
print(c.stop())
