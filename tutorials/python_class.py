from abc import ABCMeta, abstractmethod

class Vehicle(object) :
    """A vehicle for sale.
attrs: wheels, miles, make, model, year, soldOn"""
    
    __metaclass__ = ABCMeta
    
    base_sale_price = 0
    wheels = 0

    def __init__(self,miles, make, model, year, sold_on) :
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self) :
        """return sale price as float"""
        if self.sold_on is not None :
            return 0.0 # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self) :
        """return standard price to purchase"""
        if self.sold_on is not None :
            return 0.0 # Already sold
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self) :
        """return string of what type this vehicle is"""
        pass

class Car(Vehicle) :
    """a car for sale"""

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        return 'car'

class Truck(Vehicle):
    """a truck for sale"""

    base_sale_price = 10000
    wheels = 16

    def vehicle_type(self):
        return 'truck'


ford_mustang = Car(53671, 'Ford', "Mustang", 1959, None)

print(ford_mustang)
print(ford_mustang.wheels)

