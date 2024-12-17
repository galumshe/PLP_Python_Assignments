from models.xiaomi import XiaomiPhone
from models.iphone import iPhone

def main():
    # Create a Xiaomi Redmi Note 10
    redmi = XiaomiPhone(
        model="Redmi Note 10",
        storage=128,
        battery=5000,
        screen_size=6.43,
        miui_version=13.0
    )
    
    # Create an iPhone 13
    iphone = iPhone(
        model="iPhone 13",
        storage=256,
        battery=3240,
        screen_size=6.1,
        ios_version=16.0
    )
    
    # Demonstrate the functionality
    print("=== Xiaomi Redmi Note 10 ===")
    print(redmi.power_on())
    print(redmi.get_specs())
    print(redmi.enable_dark_mode())
    print()
    
    print("=== iPhone 13 ===")
    print(iphone.power_on())
    print(iphone.get_specs())
    print(iphone.toggle_face_id())

if __name__ == "__main__":
    main()