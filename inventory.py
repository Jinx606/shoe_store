from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
    
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.'''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    # Add the code to return the cost of the shoe in this method.    
    def get_cost(self):
        return self.cost

    # Add the code to return the quantity of the shoes.
    def get_quantity(self):
        return int(self.quantity)

    # Add a code to returns a string representation of a class.
    def __str__(self):
        return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============

'''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
'''
def read_shoes_data(file_path):
    with open(file_path, "r") as file1:
        next(file1) # Skip the fist line
        
        for line in file1:
            try:
                data = line.strip().split(",")
                country = data[0]
                code = data[1]
                product = data[2]
                cost = data[3]
                quantity = data[4]
                
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
            except (IndexError, ValueError) as e:
                print(f"\nError while processing line: {line.strip()}")
                print(f"\nError details: {str(e)}")
                
'''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
'''    
def capture_shoes():
    print("\n")
    country = input("Enter the country: ")
    code = input("Enter the shoe code: ")
    product = input("Enter the product/shoe name: ")
    cost = (input("Enter the shoe cost: "))
    quantity = int(input("Enter the quantity of this shoe: "))
    
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

'''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
'''
def view_all():
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    table = []
    
    for shoe in shoe_list:
        row = [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
        table.append(row)
    
    print("\n")
    print(tabulate(table, headers=headers, tablefmt="grid"))

'''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
'''
def re_stock(file_path):
    min_quantity = float("inf")
    min_shoe = None

    # Finding shoe with lowest quantity
    for shoe in shoe_list:
        if shoe.get_quantity() < min_quantity:
            min_quantity = shoe.get_quantity()
            min_shoe = shoe
        
    if min_shoe is None:
        print("\nNo shoes found for restocking.")
        return
    
    print(f"\nLowest quantity shoe: {min_shoe}")
    add_quantity = int(input("Enter the quantity to add for restocking: "))
    confirm_add_quantity = input(f"Do you want to add {add_quantity} shoes for restocking? Y/N: ")
    
    if confirm_add_quantity.lower() == "y":
        #Updating in the shoe object
        min_shoe.quantity = str(int(min_shoe.quantity) + add_quantity)
        
        # Update in the file
        with open(file_path,"r") as file2:
            lines = file2.readlines()
            
        for i, line in enumerate(lines):
            data = line.strip().split(",")
            if data[1] == min_shoe.code:
                data[4] = str(min_shoe.quantity)
                lines[i] = ",".join(data) + "\n"
        
        with open(file_path, "w") as file2:
            file2.writelines(lines)
            
        print("\nRestocking successful.")
    else:
        print("\nRestocking has been cancelled")

'''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
'''
def search_shoe(code):
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe
    
    return None

'''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
'''
def value_per_item():
    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)
        print(f"\nItem: {shoe.product}\nValue: {value}\n")
        print("-" * 20)
    
'''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
'''
def highest_qty():
    max_qty = 0
    max_shoe = None
    
    for shoe in shoe_list:
        if shoe.get_quantity() > max_qty:
            max_qty = shoe.get_quantity()
            max_shoe = shoe
    
    if max_shoe is not None:
        print(f"\nProduct with the highest quantity: {max_shoe.product} | Quantity: {max_shoe.quantity}\n\nThis shoe is for sale!")
    else:
        print("\nNo shoes found.")
    

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
inventory_file = "inventory.txt"
read_shoes_data(inventory_file)

while True:
    print('''Menu\n
1. Capture Shoes
2. View All
3. Restock
4. Search Shoe
5. Value per Item
6. Product with the Highest Quantity
7. Exit\n''')
    
    choice = input("Enter your choice from 1 to 7: ")
    if choice == "1":
        capture_shoes()
        print("\n")
    elif choice == "2":
        view_all()
        print("\n")
    elif choice == "3":
        re_stock(inventory_file)
        print("\n")
    elif choice == "4":
        search_code = input("\nEnter the shoe code to search: ")
        found_shoe = search_shoe(search_code)
        if found_shoe:
            print(found_shoe + "\n")
        else:
            print("\nShoe not found.\n")
    elif choice == "5":
        value_per_item()
        print("\n")
    elif choice == "6":
        highest_qty()
        print("\n")
    elif choice == "7":
        print("\nYou are exiting the program. Goodbye\n")
        break
    else:
        print("\nInvalid choice. Please try again.\n")