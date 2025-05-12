# Demonstrate potymorphism by demng a method fuel_type in both Car 
# and ElectricCar classes, but different behaviors.
# euta kura le anek kaam garna milne

class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model

    def get_brand(self):
        return self.__brand + " ! " #__brand means it is private

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)     #brand ra model feri nalekhnu paros 
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_tesla=ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.fuel_type())
# print(my_tesla.model)
# print(my_tesla.get_brand())

Safari = Car("Tata", "Safari")
print(Safari.fuel_type())