from models.smartphone import Smartphone

class iPhone(Smartphone):
    """
    Class representing iPhones, inheriting from the base Smartphone class.
    Includes iPhone-specific features like iOS version and Face ID functionality.
    """
    
    def __init__(self, model: str, storage: int, battery: int, screen_size: float, ios_version: float):
        """
        Initialize a new iPhone.
        
        Args:
            model (str): The model name of the iPhone
            storage (int): Storage capacity in GB
            battery (int): Battery capacity in mAh
            screen_size (float): Screen size in inches
            ios_version (float): Version of iOS operating system
        """
        super().__init__(model, storage, battery, screen_size)
        self.ios_version = ios_version
        self.face_id_enabled = True
    
    def get_specs(self) -> str:
        """Return the specifications of the iPhone, including iOS version."""
        base_specs = super().get_specs()
        return f"{base_specs}\n        iOS Version: {self.ios_version}\n        Face ID: {'Enabled' if self.face_id_enabled else 'Disabled'}"
    
    def toggle_face_id(self) -> str:
        """Toggle Face ID functionality."""
        if self.is_powered_on:
            self.face_id_enabled = not self.face_id_enabled
            status = "enabled" if self.face_id_enabled else "disabled"
            return f"Face ID is now {status} on {self.model}"
        return f"Cannot toggle Face ID: {self.model} is powered off"