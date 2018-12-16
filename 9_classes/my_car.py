from car import Car

my_tesla = Car('tesla' , 'model s' , 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


from car import Car

my_new_car = Car('audi', 'a4', 2015)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
