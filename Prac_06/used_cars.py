"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, 'My car')
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("{} {}, {}".format(my_car.name,my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    #1. create new car object called limo and set the fuel to 100
    limo = Car(100,'limo')
    #2. add 20 more units of fuel to this new car object using the add method
    limo.add_fuel(20)
    #3. print the amount of fuel in the limo car
    print('limo fuel = ',limo.fuel)
    #4. attempt to drvie 115km
    limo.drive(115)
    #5. print the car's odometer reading
    print('limo odometer = ',limo.odometer)
    print(limo)

main()