from Prac_08.Silver_Service_Car import silver_service_car

def main():
    silverservicecar = silver_service_car('Hummer',200,4.5)
    silverservicecar.drive(100)
    print(silverservicecar)
    print(silverservicecar.get_fare())

main()