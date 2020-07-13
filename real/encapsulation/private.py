class Vehicle:
    def __private(self):
        print("private")

    def _protected(self):
        print("protected")

    def public(self):
        self.__private()
        self._protected()

class MotorBike(Vehicle):


    #private is a private method, only the object itself 
    #could use it, there is no naming conflict for a private method.
    def __private(self):
        print("subclass")

    def _protected(self):
        print("subclass")

a= MotorBike()
a.public()
print(dir(a))