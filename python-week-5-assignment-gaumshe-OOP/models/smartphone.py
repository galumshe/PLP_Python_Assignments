class Smartphone:
    """
    Base class representing a generic smartphone with common attributes and behaviors.
    This class serves as a parent class for specific smartphone brands.
    """
    
    def __init__(self, model: str, storage: int, battery: int, screen_size: float):
        """
        Initialize a new smartphone.
        
        Args:
            model (str): The model name of the smartphone
            storage (int): Storage capacity in GB
            battery (int): Battery capacity in mAh
            screen_size (float): Screen size in inches
        """
        self.model = model
        self.storage = storage
        self.battery = battery
        self.screen_size = screen_size
        self.is_powered_on = False
    
    def power_on(self) -> str:
        """Turn on the smartphone."""
        if not self.is_powered_on:
            self.is_powered_on = True
            return f"{self.model} is now powered on"
        return f"{self.model} is already on"
    
    def power_off(self) -> str:
        """Turn off the smartphone."""
        if self.is_powered_on:
            self.is_powered_on = False
            return f"{self.model} is now powered off"
        return f"{self.model} is already off"
    
    def get_specs(self) -> str:
        """Return the specifications of the smartphone."""
        return f"""
        Model: {self.model}
        Storage: {self.storage}GB
        Battery: {self.battery}mAh
        Screen Size: {self.screen_size} inches
        Power Status: {'On' if self.is_powered_on else 'Off'}
        """