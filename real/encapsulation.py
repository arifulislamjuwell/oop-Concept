class Robot(object):
    def __init__(self):
      self.__c = 123
    
    def get_value(self):
        return self.__c
    
    def set_value(self, value):
        self.__c= value

class Leg(Robot):
    def test(self):
        self.set_value(34)
        value= self.get_value()
        return value

obj = Robot()
obj.set_value(67)
print(obj.get_value())

obj1= Leg()
print(obj1.test())
