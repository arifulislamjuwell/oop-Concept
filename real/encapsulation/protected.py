class Vehicle:
    def __init__(self):
        self._wheel= 2


class Motorbike(Vehicle):

    def __init__(self):
        super().__init__()
        print(self._wheel)

a= Vehicle()
print(a._wheel)

b= Motorbike()

