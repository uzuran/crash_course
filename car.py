class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def get_descriptive_name(self):
        log_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return log_name.title()

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cant roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self,):
        print('This car have a ' + str(self.battery_size) + 'kWh battery')

    def get_range(self):
        global rrange
        if self.battery_size == 70:
            rrange = 240
        elif self.battery_size == 85:
            rrange = 270

        message = 'This car go approximately ' + str(rrange)
        message += ' miles on a full charge'
        print(message)

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 's', 2106,)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()



my_new_car = Car('audi', 'a4',  2016)
print(my_new_car.get_descriptive_name())
print(my_new_car.odometer_reading)
my_new_car.odometer_reading = 23
print(my_new_car.odometer_reading)

my_new_car.update_odometer(500)
my_new_car.read_odometer()

my_used_car = Car('subaru', 's14', 2000)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(5000)
my_used_car.increment_odometer(5000)
my_used_car.read_odometer()
