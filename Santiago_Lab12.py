# the menu with food items and their prices
menu = {
    1: {"name": "Cordon Blue", "price": 85.00},
    2: {"name": "Carbonara", "price": 120.00},
    3: {"name": "Cheesecake", "price": 95.00},
    4: {"name": "Chicken Curry", "price": 170.00},
    5: {"name": "Croissant", "price": 50.00},
    6: {"name": "Cheese Bread", "price": 35.00},
}

# this is fuction to display menuu
def show_menu():
    print("=== Ian's Best Seller Menu ===")
    for key, item in menu.items():
        print(f"{key}. {item['name']} --- ₱{item['price']:.2f}")

# main ordering function
def place_order():
    # Display the menu
    show_menu()
    
    # this will get the users food choice
    while True:
        try:
            choice = int(input("\nEnter the number of the item you want to order: "))
            if choice in menu:
                selected_item = menu[choice]
                break
            else:
                print("Please choose a number from the menu, thank you!")
        except ValueError:
            print("Please enter a valid number :)")
    
    # this code calculates the total
    total_cost = selected_item['price']
    print(f"\nYou selected: {selected_item['name']}")
    print(f"Total cost: ₱{total_cost:.2f}")
    
    # this is the payment processing
    while True:
        try:
            cash_rendered = float(input("Enter the amount of cash you're paying with: ₱"))
            
            # this code checks if payment is sakto
            if cash_rendered >= total_cost:
                change = cash_rendered - total_cost
                print(f"\nPayment accepted")
                print(f"Your change is: ₱{change:.2f}")
                break
            else:
                print(f"your payment is not enough... you need to pay at least ₱{total_cost:.2f}")
        except ValueError:
            print("Please enter another amount you will pay...")
    
    print("\nThank you for your order! come again here pls :D")

# this will run the ordering system
if __name__ == "__main__":
    place_order()