class Vehicle:

    def __init__(self):
        print('parent class vehicle')

class Roads:
    
    def __init__(self):
        print('parent class road')

#multiple inheritance
class Truck(Vehicle, Roads):

    def __init__(self):
        Vehicle.__init__(self)
        Roads.__init__(self)



obj= Truck()
