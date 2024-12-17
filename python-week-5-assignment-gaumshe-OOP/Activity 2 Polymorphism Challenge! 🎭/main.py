"""
Main module demonstrating polymorphism with different vehicle types.
Shows how the same method name (move) behaves differently for each vehicle.
"""

from models.car import Car
from models.plane import Plane
from models.boat import Boat

def main():
    # Create different types of vehicles
    car = Car("Toyota", "Supra", "red", num_wheels=4)
    plane = Plane("Boeing", "747", "white", max_altitude=35000)
    boat = Boat("Yamaha", "242X", "blue", has_sail=True)
    
    # Store all vehicles in a list to demonstrate polymorphism
    vehicles = [car, plane, boat]
    
    # Demonstrate polymorphic behavior
    print("=== Vehicle Movement Demonstration ===")
    for vehicle in vehicles:
        # The same method call (move) behaves differently for each vehicle type
        print(vehicle.move())
        print(vehicle.stop())
        print()

if __name__ == "__main__":
    main()
