from abc import ABC,abstractmethod
class Person:
    _id=''
    _name=''
    _passengerType=''

    def Person(self):
        return None
    def __init__(self,id,name,passengerType):
        self._name=name
        self._id=id
        self._passengerType=passengerType
    def __str__(self):
        print("Passenger Id :"+str(self._id))
        print("Passenger Name :"+str(self._name))
        print("Passenger Type :"+str(self._passengerType))

    @abstractmethod
    def display(self):
        return None
