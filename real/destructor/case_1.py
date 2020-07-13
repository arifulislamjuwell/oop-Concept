class Vehicle:

    def __init__(self):
        self.name= 'motorbike'
        super().__init__()
    
    def __del__(self):
        print('destroy object')

object_1= Vehicle()

#A reference to objects is also deleted when the object goes out of reference or when the program ends.
del object_1
object_2= Vehicle()