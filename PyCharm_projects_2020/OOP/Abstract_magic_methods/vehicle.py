class Vehicle():
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @staticmethod
    def air_condition():
        pass

    def drive(self, distance):
        pass

    def refuel(self, litters):
        pass

class Car(Vehicle):
    def air_condition(self):
        return 0.9

    def drive(self, distance):
        if distance * (self.fuel_consumption + self.air_condition()) < self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + self.air_condition())
            return self.fuel_quantity
        else:
            return self.fuel_quantity

    def refuel(self, litters):
        self.fuel_quantity += litters
        return self.fuel_quantity

class Truck(Vehicle):
    def air_condition(self):
        return 1.6

    def drive(self, distance):
        if distance * (self.fuel_consumption + self.air_condition()) < self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + self.air_condition())
            return self.fuel_quantity
        else:
            return self.fuel_quantity

    def refuel(self, litters):
        self.fuel_quantity += litters * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
print()
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)