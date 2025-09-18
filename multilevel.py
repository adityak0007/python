class car:
    def __init__(self,name,year):
        self.name = name
        self.yrs = year

    def fuel(self):
        print("diesel")


class aeroplane:
    def __init__(self,power,capacity):
        self.pow = power
        self.cap = capacity

    def fuel(self):
        print("jet fuel")


class boat:
    def __init__(self,size,distance):
        self.size = size
        self.dist = distance

    def fuel(self):
        print("heavy fuel oil")


car1 = car("toyota", "2023")
aero1 = aeroplane("90000 hp", "500")
boat1 = boat("medium", "1000 nm")

for x in [car1, aero1, boat1]:
    x.fuel()
