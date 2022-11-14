class Bike:
    def __init__(self,drive,rate):
        self.rate = rate
        self.drive = drive


    def get_fare(self,distance):
        return distance * self.rate

class Car:
    def __init__(self,driver,rate) -> None:
        self.driver = driver
        self.rate = rate
    def get_fare(self,distance):
        return distance * self.rate 

class CNG:
    def __init__(self,mama,rate) -> None:
        self.driver = mama
        self.rate = rate
    
    def get_fare(self,distance):
        return distance * self.rate

        


def Factory(vhicle_type):
    vheicles = {
        'car': Car,
        'bike': Bike,
        'cng': CNG
    }
    return vheicles[vhicle_type]()


# b1 = Bike('masud',5)
# c1 = Car('mahbub',10)
# g1 = CNG('karim',6)

# customers = [20,14,16]
# for distance in customers:

#     print(b1.get_fare(distance))
#     print(c1.get_fare(distance))
#     print(g1.get_fare(distance))


