"""
Plane module that implements specific airplane behavior.
Demonstrates polymorphism by implementing its own move method.
"""

from models.vehicle import Vehicle

class Plane(Vehicle):
    def __init__(self, brand: str, model: str, color: str, max_altitude: float):
        """
        Initialize a new plane.
        
        Args:
            brand (str): The manufacturer of the plane
            model (str): The model name
            color (str): The color of the plane
            max_altitude (float): Maximum flying altitude in feet
        """
        super().__init__(brand, model, color)
        self.max_altitude = max_altitude
    
    def move(self) -> str:
        """
        Implement plane-specific movement (flying).
        Overrides the base Vehicle.move() method.
        """
        self.is_moving = True
        return f"The {self.color} {self.brand} {self.model} is flying at {self.max_altitude} feet ✈️"
