"""
    1. Inheritance is nothing but acquiring properties of parent class to child class.
    2. We need to import the required class from the file it is defined to access the properties of the parent class.
    3. To access the properties of parent class WO creating an object to it, we need to give parent class name as an
       argument to the child class.(line 12)
    4. If any constructor defined in parent class, then we need to create the same in child class too.
"""

from base_car import BaseCarModel


class Altroz(BaseCarModel):
    print("This is Alroz car")

    def base_car_specs(self):
        list_specs = [self.seats, self.air_bags, self.gears]
        return list_specs

    def altroz_car_specs(self):
        print("Doors open till 90 degrees of angle.")


car_obj = Altroz()
print(car_obj.base_car_specs())
car_obj.altroz_car_specs()
