
class Vehicle:
    color =['black', 'white']
    wheel= 4

    def description(self):
        return 'vehicle color available {}, and wheel must be {}'.format(len(self.color), self.wheel)

object_1= Vehicle()
print(object_1.description())

print(Vehicle.color)
print(object_1.color)