import csv
csv_file_name = "inventory.csv"
#Represents an inventory using a list of dictionaries.
#Each dictionery represents a product with keys like id, name, pricing and stock
inventory = [
    {
    "id": 1,
    "name": "Wireless Mouse",
    "price": 25.99,
    "stock": 150
  },
  {
    "id": 2,
    "name": "Mechanical Keyboard",
    "price": 79.99,
    "stock": 85
  },
  {
    "id": 3,
    "name": "HD Monitor",
    "price": 189.50,
    "stock": 60
  },
  {
    "id": 4,
    "name": "USB-C Hub",
    "price": 39.95,
    "stock": 200
  },
  {
    "id": 5,
    "name": "External SSD 1TB",
    "price": 119.00,
    "stock": 40
  }
]
print("---Initiaal Inventory---")
for product in inventory:
    print(f"ID: {product['id']}, Name:{product['name']}, Stock: {product['stock']}")
          
print("\n")
def update_stock(product_id, quantity):
    found = False
    for product in inventory:
        if product['id'] == product_id:
            #Ensure stock does not go below zero
            if product['stock'] >= 0:
                product['stock'] = product['stock'] + quantity
                print (f"Updated Stock for {product['name']} (ID: {product['id']})")
            else:
                print(f"Error: not enough stock for {product['name']}")
                found = True
                break
            if not found:
                print("Error: Product with '{product_id}' not Found in inventory")
def get_low_stock_products(threshold):
    """Args: 
        threshold (int): The stock level below which a product is 
    Retruns: 
        List: A list of names of products with low stocks"""
    low_stock_products=[]
    for product in inventory: 
        if product['stock']<=threshold:
            low_stock_products.append(product['name'])
    return low_stock_products

a = get_low_stock_products(100)
print(a)

fieldnames = ["name", "stock", "price", "id"]
print(f"Attemting to write employee data to 'csv_file_name' ...")
try:
    with open(csv_file_name, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        print("CSV headers written")

        writer.writerows(inventory)
        print(f"Successfully wrote {len(inventory)} employees records to {csv_file_name}")

except IOError as e:
    print(f"Error:Could not write to file'{csv_file_name}'. {e}")
except Exception as e:
    print(f"An unexpected error occured: {e}")
    