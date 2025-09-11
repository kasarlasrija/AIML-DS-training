from abc import ABC, abstractmethod
class Vehicle:
    def __init__(self, license, name):
        self.__license = license
        self.__name = name
    def get_license(self):
        return self.__license
    def get_name(self):
        return self.__name
    def display(self):
        print(f"License Plate: {self.__license}, Owner: {self.__name}")
    def parking_fee(self, hours):
        pass
class Bike(Vehicle):
    def __init__(self, license, name, helmet=True):
        super().__init__(license, name)
        self.helmet = helmet
    def display(self):
        super().display()
        print("Vehicle Type: Bike | Helmet Required:", self.helmet)
    def parking_fee(self, hours):
        return 20 * hours
class Car(Vehicle):
    def __init__(self, license, name, seats=4):
        super().__init__(license, name)
        self.seats = seats
    def display(self):
        super().display()
        print("Vehicle Type: Car | Seats:", self.seats)
    def parking_fee(self, hours):
        return 50 * hours
class SUV(Vehicle):
    def __init__(self, license, name, four_wheel=True):
        super().__init__(license, name)
        self.four_wheel = four_wheel
    def display(self):
        super().display()
        print("Vehicle Type: SUV | 4WD:", self.four_wheel)
    def parking_fee(self, hours):
        return 70 * hours
class Truck(Vehicle):
    def __init__(self, license, name, max_load=10000):
        super().__init__(license, name)
        self.max_load = max_load
    def display(self):
        super().display()
        print("Vehicle Type: Truck | Max Load:", self.max_load, "kg")
    def parking_fee(self, hours):
        return 100 * hours
class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size
        self.__status = "free"
        self.__vehicle = None
    def get_status(self):
        return self.__status
    def get_vehicle(self):
        return self.__vehicle
    def assign_vehicle(self, vehicle):
        if self.__status == "occupied":
            print(f"Spot {self.spot_id} is already occupied.")
            return False
        if not self.__compatible(vehicle):
            print(f"Vehicle type not allowed in spot size {self.size}")
            return False
        self.__vehicle = vehicle
        self.__status = "occupied"
        print(f"Vehicle parked at Spot {self.spot_id}")
        return True
    def remove_vehicle(self):
        if self.__status == "free":
            print(f"Spot {self.spot_id} is already empty.")
            return None
        vehicle = self.__vehicle
        self.__vehicle = None
        self.__status = "free"
        print(f"Vehicle removed from Spot {self.spot_id}")
        return vehicle
    def __compatible(self, vehicle):
        if isinstance(vehicle, Bike) and self.size in ["S", "M", "L", "XL"]:
            return True
        elif isinstance(vehicle, Car) and self.size in ["M", "L", "XL"]:
            return True
        elif isinstance(vehicle, SUV) and self.size in ["L", "XL"]:
            return True
        elif isinstance(vehicle, Truck) and self.size == "XL":
            return True
        return False
    def display(self):
        print(f"Spot {self.spot_id} | Size: {self.size} | Status: {self.__status}")
class ParkingLot:
    def __init__(self):
        self.spots = []
    def add_spot(self, spot):
        self.spots.append(spot)
    def show_spots(self):
        for spot in self.spots:
            spot.display()
    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.get_status() == "free":
                if spot.assign_vehicle(vehicle):
                    return spot
        print("No suitable spot available.")
        return None
    def unpark_vehicle(self, license_plate, hours):
        for spot in self.spots:
            vehicle = spot.get_vehicle()
            if vehicle and vehicle.get_license() == license_plate:
                spot.remove_vehicle()
                fee = vehicle.parking_fee(hours)
                print(f"Parking Fee for {hours} hours: ₹{fee}")
                return fee
        print("Vehicle not found in any spot.")
        return 0
class Payment(ABC):
    @abstractmethod
    def payment(self, amount):
        pass
class CashPayment(Payment):
    def payment(self, amount):
        print(f"Paid ₹{amount} in cash.")
class CardPayment(Payment):
    def payment(self, amount):
        print(f"Paid ₹{amount} using credit/debit card.")
class UPIPayment(Payment):
    def payment(self, amount):
        print(f"Paid ₹{amount} using UPI.")
if __name__ == "__main__":
    lot = ParkingLot()
    lot.add_spot(ParkingSpot("S1", "S"))
    lot.add_spot(ParkingSpot("S2", "M"))
    lot.add_spot(ParkingSpot("S3", "L"))
    lot.add_spot(ParkingSpot("S4", "XL"))
    vehicles = [
        Bike("KA01AB1234", "Ravi"),
        Car("KA02XY7890", "Asha"),
        SUV("KA03ZZ4321", "John"),
        Truck("KA04TR0001", "Logistics Ltd.")
    ]
    print("\nParking Vehicles")
    for v in vehicles:
        v.display()
        lot.park_vehicle(v)
    print("\nParking Lot Status")
    lot.show_spots()
    print("\nUnparking Vehicle")
    license_to_unpark = input("Enter license plate to unpark: ").strip()
    hours_parked = int(input("Enter number of hours parked: "))
    fee = lot.unpark_vehicle(license_to_unpark, hours_parked)
    if fee == 0:
        print("No payment needed.")
    else:
        print("\nProcessing Payment")
        valid_choices = {"1": CashPayment, "2": CardPayment, "3": UPIPayment}
        while True:
            print("Choose payment method: 1. Cash  2. Card  3. UPI")
            choice = input("Enter choice (1/2/3): ").strip()
            if choice in valid_choices:
                payment = valid_choices[choice]()
                break
            else:
                print("Invalid choice. Please try again.")
        payment.payment(fee)
