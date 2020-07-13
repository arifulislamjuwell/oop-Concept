class Vehicle:

    def __init__(self):
        self.horn= 'po po po'
        print('parent class vehicle')

class Roads:
    
    def __init__(self):
        print('parent class road')

#multiple inheritance
class Truck(Vehicle, Roads):

    def __init__(self):
        Vehicle.__init__(self)
        Roads.__init__(self)
        

#multi level
class Tyre(Truck):

    def __init__(self):
        Truck.__init__(self)

    def get_horn(self):
        a= self.horn
        return a

obj= Tyre()
print(obj.get_horn())