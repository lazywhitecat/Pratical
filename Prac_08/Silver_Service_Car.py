from Prac_08.taxt_modification import Taxi

class silver_service_car(Taxi):
    flagfall = 4.5
    def __init__(self,name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        return '{}/km plus flagfall of {}'.format(self.price_per_km,self.flagfall)

    def get_fare(self):
        return self.flagfall + super().get_fare()

