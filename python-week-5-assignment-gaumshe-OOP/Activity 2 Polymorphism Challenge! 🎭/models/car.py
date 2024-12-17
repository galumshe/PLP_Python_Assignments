"""
Car module that implements specific car behavior.
Demonstrates polymorphism by implementing its own move method.
"""

from models.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand: str, model: str, color: str, num_wheels: int = 4):
        """
        Initialize a new car.
        
        Args:
            brand (str): The manufacturer of the car
            model (str): The model name
            color (str): The color of the car
            num_wheels (int): Number of wheels, defaults to 4
        """
        super().__init__(brand, model, color)
        self.num_wheels = num_wheels
    
    def move(self) -> str:
        """
        Implement car-specific movement (driving).
        Overrides the base Vehicle.move() method.
        """
        self.is_moving = True
        return f"The {self.color} {self.brand} {self.model} is driving on {self.num_wheels} wheels 🚗"
