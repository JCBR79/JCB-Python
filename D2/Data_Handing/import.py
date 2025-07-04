import json
import datetime

#Create a Python dictionary representing product information
#The 'last updated' timestamp is generated dynamically  for demostration

product_data = {"products": [{
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
  }],
  "last_updated":datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

}
#Define the name of the JSON file
json_file_name="products.json"
print(f"Attemtingto write product date to {json_file_name}")
try:
    #open the JSON file in swite mode('w')
    #Using 'with' statement ensures the file is properly closed
    with open(json_file_name, mode='w', encoding='utf-8') as json_file:

        json.dump(product_data, json_file, indent=4)
        print(f"Successfully wrote product data to {json_file_name}")
except IOError as e:
    print(f"Error:Could not write to file '{json_file_name:{e}}")
except Exception as e:
    print(f"An unexpected error occured")
    print(f"\nPlease check the '{json_file_name}' file manually in a  test editor to verify its contect")
                                  


