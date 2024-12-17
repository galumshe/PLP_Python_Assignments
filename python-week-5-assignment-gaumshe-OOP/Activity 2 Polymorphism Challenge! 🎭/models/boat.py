"""
Boat module that implements specific boat behavior.
Demonstrates polymorphism by implementing its own move method.
"""

from models.vehicle import Vehicle

class Boat(Vehicle):
    def __init__(self, brand: str, model: str, color: str, has_sail: bool = False):
        """
        Initialize a new boat.
        
        Args:
            brand (str): The manufacturer of the boat
            model (str): The model name
            color (str): The color of the boat
            has_sail (bool): Whether the boat has a sail, defaults to False
        """
        super().__init__(brand, model, color)
        self.has_sail = has_sail
    
    def move(self) -> str:
        """
        Implement boat-specific movement (sailing/motoring).
        Overrides the base Vehicle.move() method.
        """
        self.is_moving = True
        movement_type = "sailing" if self.has_sail else "motoring"
        return f"The {self.color} {self.brand} {self.model} is {movement_type} across the water ⛵"
