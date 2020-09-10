from Prac_08.taxi import Taxi


def main():
    my_taxi = Taxi('Prius 1',100,1.23)
    my_taxi.drive(40)
    print(my_taxi)
    print('Taxi Details:{}, current fare:${}'.format(my_taxi.name,my_taxi.current_fare_distance))
    my_taxi.start_fare()
    my_taxi.drive(100)
    print('Taxi Details:{}, current fare:${}'.format(my_taxi.name,my_taxi.current_fare_distance))
    print(my_taxi)

main()