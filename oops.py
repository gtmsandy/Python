# 1. Create a car with attributes like brand and model. 
# the create an instance of this class

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

# my_car=Car("Toyota","Corolla")
# print(my_car.brand, my_car.model)




# 2. Add a method to the Car class that displays
# the full name of the car

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

#     def full_name(self):
#         return f"{self.brand} {self.model}"

# my_car=Car("Toyota","Corolla")
# print(my_car.full_name())





# 3. (Inheritance) Create an ElectricCar class that inherits 
# from the Car class and has an additional attribute battery_size


class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)     #brand ra model feri nalekhnu paros 
        self.battery_size = battery_size

my_tesla=ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.model)
print(my_tesla.full_name())


