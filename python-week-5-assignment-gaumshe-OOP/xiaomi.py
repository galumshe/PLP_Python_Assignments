from models.smartphone import Smartphone

class XiaomiPhone(Smartphone):
    """
    Class representing Xiaomi smartphones, inheriting from the base Smartphone class.
    Includes Xiaomi-specific features like MIUI version and fast charging capabilities.
    """
    
    def __init__(self, model: str, storage: int, battery: int, screen_size: float, miui_version: float):
        """
        Initialize a new Xiaomi smartphone.
        
        Args:
            model (str): The model name of the smartphone
            storage (int): Storage capacity in GB
            battery (int): Battery capacity in mAh
            screen_size (float): Screen size in inches
            miui_version (float): Version of MIUI operating system
        """
        super().__init__(model, storage, battery, screen_size)
        self.miui_version = miui_version
        self.fast_charging = True
    
    def get_specs(self) -> str:
        """Return the specifications of the Xiaomi smartphone, including MIUI version."""
        base_specs = super().get_specs()
        return f"{base_specs}\n        MIUI Version: {self.miui_version}\n        Fast Charging: {'Yes' if self.fast_charging else 'No'}"
    
    def enable_dark_mode(self) -> str:
        """Enable MIUI dark mode."""
        if self.is_powered_on:
            return f"Dark mode enabled on {self.model} with MIUI {self.miui_version}"
        return f"Cannot enable dark mode: {self.model} is powered off"