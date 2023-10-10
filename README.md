# Inventory Management System for a shoe store

This Python program, `inventory.py`, is an inventory management system for a shoe store. It allows you to manage the inventory of shoes, perform various operations such as capturing new shoe data, viewing all shoes, restocking, searching for a specific shoe, calculating the value per item, finding the product with the highest quantity, and exiting the program.

## Usage
Capturing Shoes:

Select option 1 from the menu.
Enter the shoe details, including country, code, product name, cost, and quantity.
The shoe will be added to the inventory.
Viewing All Shoes:

Select option 2 from the menu.
It will display all the shoes in a tabular format.
Restocking Shoes:

Select option 3 from the menu.
The program will identify the shoe with the lowest quantity.
You can specify how many more shoes to add for restocking.
The quantity will be updated, and the changes will be saved to the inventory file.
Searching for a Shoe:

Select option 4 from the menu.
Enter the shoe code you want to search for.
The program will display the details of the matching shoe if found.
Value per Item:

Select option 5 from the menu.
The program will calculate and display the value (cost * quantity) for each shoe.
Product with the Highest Quantity:

Select option 6 from the menu.
The program will identify the shoe with the highest quantity and mark it as "for sale."
Exiting the Program:

Select option 7 from the menu.
The program will exit gracefully.

## File Structure

inventory.py: The main Python script containing the inventory management system.
inventory.txt: The data file containing information about the shoes in a CSV format (Country, Code, Product, Cost, Quantity).

## Data File Format

The inventory.txt file should have the following format:

Country,Code,Product,Cost,Quantity
South Africa,SKU44386,Air Max 90,2300,20
China,SKU90000,Jordan 1,3200,50
...

## Error Handling

The program includes error handling for various scenarios, such as invalid inputs and file reading errors. It will inform you about any issues encountered during execution.

## How to Run

To run the program, execute the following command:

python inventory.py

## Author

This inventory management system was created by Jinx606.
