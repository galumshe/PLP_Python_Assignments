def calculate_discount(item, price, discount_percent):
    if discount_percent < 20:
        print("your discount is below 20%")
        return price
    print(f"This {item} is selling for ${price}")
    print(f"We are offering {discount_percent}% for the {item}")
    return discount_percent*price/100
    
  
  
# calculate_discount("Lenovo ideapad L14", ""Lenovo ideapad L14"", "25")

def calculate_discountPrice():
    item = input("Enter the name of the item: ")
    original_price = int(input("Enter product price: "))
    discount = int(input("Enter the discout to be applied: "))
    discount_price =  calculate_discount(item, original_price, discount)
    print(f"your discount is ${discount_price} ")
    # if discount < 20:
    #     return original_price
calculate_discountPrice()

