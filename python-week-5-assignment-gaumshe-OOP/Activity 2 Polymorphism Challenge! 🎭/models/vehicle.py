"""
Base Vehicle module that defines the common interface for all vehicles.
This serves as the parent class demonstrating polymorphism.
"""

class Vehicle:
    def __init__(self, brand: str, model: str, color: str):
        """
        Initialize a new vehicle.
        
        Args:
            brand (str): The manufacturer of the vehicle
            model (str): The model name
            color (str): The color of the vehicle
        """
        self.brand = brand
        self.model = model
        self.color = color
        self.is_moving = False
    
    def move(self) -> str:
        """
        Base movement method to be overridden by child classes.
        Each vehicle type will implement its own movement behavior.
        """
        raise NotImplementedError("Each vehicle must implement its own move method")
    
    def stop(self) -> str:
        """Stop the vehicle's movement."""
        if self.is_moving:
            self.is_moving = False
            return f"The {self.color} {self.brand} {self.model} comes to a stop."
        return f"The {self.color} {self.brand} {self.model} is already stopped."
