products = [
{
    "name": "wood 1lb",   
    "price": 2.99,
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

while shopping:
  print("\nAvailable Products:")
for index, product in enumerate(products):
    print(
        f"{index + 1}. {product['name']} - ${product['price']} ({product['department']})"

    print(f"   Description: {product['description']}") 

    print(f"{len(products) + 1}. View Cart & Checkout")
    print(f"{len(products) + 2}. Exit Store")

    choice = input("\nEnter the number of your choice: ")
