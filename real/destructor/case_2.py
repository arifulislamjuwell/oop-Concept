class Vehicle:

    def __init__(self):
        self.name= 'motorbike'
        super().__init__()
    
    def __del__(self):
        print('destroy object')
        
#The destructor was called after the program ended   
object_1= Vehicle()