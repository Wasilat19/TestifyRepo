import abc

class Vehicle(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_drive_direction(self):
        pass


class Car(Vehicle):

    def get_drive_direction(self):
        return "Drive forward"   


class Plane(Vehicle):
    def get_drive_direction(self):
        return "Drive Upward"


car = Car()
print(car.get_drive_direction())

plane = Plane()
print(plane.get_drive_direction())
