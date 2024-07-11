class Vehicle:
    def _init_(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def _str_(self):
        return f"Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}"


class Car(Vehicle):
    def _init_(self, registration_number, make, model, number_of_seats):
        super()._init_(registration_number, make, model)
        self.number_of_seats = number_of_seats

    def _str_(self):
        return f"{super()._str_()}, Number of Seats: {self.number_of_seats}"


class Truck(Vehicle):
    def _init_(self, registration_number, make, model, cargo_capacity):
        super()._init_(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def _str_(self):
        return f"{super()._str_()}, Cargo Capacity: {self.cargo_capacity} kg"


class Motorcycle(Vehicle):
    def _init_(self, registration_number, make, model, engine_capacity):
        super()._init_(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def _str_(self):
        return f"{super()._str_()}, Engine Capacity: {self.engine_capacity} cc"


class Fleet:
    def _init_(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.registration_number} added successfully.")

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles found.")
        else:
            for vehicle in self.vehicles:
                print(vehicle)

    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                print(f"Vehicle found: {vehicle}")
                return vehicle
        print(f"No vehicle found with registration number {registration_number}.")
        return None


def main():
    fleet = Fleet()

    while True:
        print("\nTransport Fleet Management System")
        print("1. Add a new vehicle")
        print("2. Display all vehicles")
        print("3. Search for a vehicle by registration number")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            vehicle_type = input("Enter vehicle type (car/truck/motorcycle): ").lower()
            registration_number = input("Enter registration number: ")
            make = input("Enter make: ")
            model = input("Enter model: ")

            if vehicle_type == 'car':
                number_of_seats = int(input("Enter number of seats: "))
                vehicle = Car(registration_number, make, model, number_of_seats)
            elif vehicle_type == 'truck':
                cargo_capacity = float(input("Enter cargo capacity (kg): "))
                vehicle = Truck(registration_number, make, model, cargo_capacity)
            elif vehicle_type == 'motorcycle':
                engine_capacity = int(input("Enter engine capacity (cc): "))
                vehicle = Motorcycle(registration_number, make, model, engine_capacity)
            else:
                print("Invalid vehicle type.")
                continue

            fleet.add_vehicle(vehicle)
        elif choice == '2':
            fleet.display_vehicles()
        elif choice == '3':
            registration_number = input("Enter registration number: ")
            fleet.search_vehicle(registration_number)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if _name_ == "_main_":
    main()