"""Vehicle Selection - either a CAR or a BIKE"""
import itertools

class State(object):

    def selectNextVehicle(self):
        """
        Cycling through vehicles in a particular state
        """
        print("[+] Selecting vehicle... Vehicle is", next(self.vehicles), " - ",  self.name)


# State no. 1
class BikeState(State):
    def __init__(self, transport):
        self.transport = transport
        self.l = ["TVS", "Yamaha", "Duke", "Activa", "Bullet"]
        self.vehicles = itertools.cycle(self.l)
        self.name = "BIKE"

    def toggle_wheels(self):
        """
        Change state to CARS state
        """
        print("[*] Switching to CARS")
        self.transport.state = self.transport.carState

    def listVehicles(self):
        """
        List vehicles available in BIKE state
        """
        for i in range(len(self.l)):
            print(str(i+1) + ") " + self.l[i])


# State no. 2
class CarState(State):
    def __init__(self, transport):
        self.transport = transport
        self.l = ["Swift Dzire", "Verna", "Renault Kwid", "Nano", "Innova"]
        self.vehicles = itertools.cycle(self.l)
        self.name = "CAR"

    def toggle_wheels(self):
        """
        Change state to BIKE state
        """
        print("[*] Switching to BIKES")
        self.transport.state = self.transport.bikeState

    def listVehicles(self):
        """
        List vehicles available in CARS state
        """
        for i in range(len(self.l)):
            print(str(i+1) + ") " + self.l[i])



class Transport(object):

    def __init__(self):
        self.bikeState = BikeState(self)
        self.carState = CarState(self)
        # Set default state to BIKES
        self.state = self.bikeState

    def toggle_wheels(self):
        self.state.toggle_wheels()

    def selectNextVehicle(self):
        self.state.selectNextVehicle()

    def listVehicles(self):
        self.state.listVehicles()    