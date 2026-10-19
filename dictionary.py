products = [
    {
        "name": "wood 1sqft",   
        "price": 0.99,
        "department": "building",
        "description": "high quality wood",
    },
    {
        "name": "20 steel screws",
        "price": 3.99,
        "department": "building",
        "description": "20 screws, heavy duty, works with most screwdrivers",
    }, 
    {
        "name": "plastic bucket",
        "price": 9.99,
        "department": "tools",
        "description": "big 10 gal bucket",
    },
]

print("Welcome to the store!")
cart = []
shopping = True

while shopping:
    print("\nAvailable Products:")
    for index, product in enumerate(products):
        print(f"{index + 1}. {product['name']} - ${product['price']} ({product['department']})") 
        print(f"   Description: {product['description']}") 

    cart_option = len(products) + 1
    exit_option = len(products) + 2

    print(f"{cart_option}. View Cart & Checkout")
    print(f"{exit_option}. Exit Store")

    choice = input("\nEnter the number of your choice: ")

    if choice.isdigit():
        choice_num = int(choice)
        
        if 1 <= choice_num <= len(products):
            selected_product = products[choice_num - 1]
            cart.append(selected_product)
            print(f"\n--> Added {selected_product['name']} to your cart!")

        elif choice_num == cart_option:
            print("\n--- Your Cart ---")
            if not cart:
                print("Your cart is empty.")
            else:
                total = 0
                for item in cart:
                    print(f"- {item['name']}: ${item['price']}")
                    total += item['price']
                print(f"Total: ${total:.2f}")
            shopping = False
            print("Thank you for shopping with us!")

        elif choice_num == exit_option:
            print("\nGoodbye! Come back soon.")
            shopping = False
            
        else:
            print("\nInvalid choice. Please choose a number from the menu.")
    else:
        print("\nInvalid input. Please enter a valid number.")
