class Vehicle:
    def drive(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

# Subclasses
class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike"

class Bus(Vehicle):
    def drive(self):
        return "Driving a bus"
    
class VehicleFactory:
    def create_vehicle(vehicle_type: str) -> Vehicle:
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "bus":
            return Bus()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
        

# Client code
vehicles_to_create = ["car", "bike", "bus", "car"]

for v_type in vehicles_to_create:
    vehicle = VehicleFactory.create_vehicle(v_type)
    print(vehicle.drive())