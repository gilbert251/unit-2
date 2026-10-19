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

print("welcome to store")
cart = []
shopping = True
print("\nAvailable Products:")
while shopping:
 for index, product in enumerate(products):
    
    print(f"{index + 1}. {product['name']} - ${product['price']} ({product['department']})") 
    print(f"   Description: {product['description']}") 

 cart_option = len(products) + 1
 exit_option = len(products) + 2

 print(f"{len(products) + 1}. View Cart & Checkout")
 print(f"{len(products) + 2}. Exit Store")

choice = input("\nEnter the number of your choice: ")
elif choice == str(cart_option):

if choice.isdigit() and 1 <= int(choice) <= len(products):
    selected_product = products[int(choice) - 1]
    cart.append(selected_product)
    print(f"\n--> Added {selected_product['name']} to your cart!")

elif choice == str(len(products) + 1):
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

elif choice == str(len(products) + 2):
    print("\nGoodbye! Come back soon.")
    shopping = False
        
else:
    print("\nInvalid choice. Please try again.")
