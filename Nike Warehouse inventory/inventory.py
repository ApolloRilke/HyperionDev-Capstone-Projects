# L1T29: Capstone Project IV. 


class Shoes:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __repr__(self):
        return (f"{self.country} {self.code} {self.product} {self.cost} "
                f"{self.quantity}")


def read_shoes_data():
    """Opens the file inventory.txt and reads the data 
    from this file the create shoes object and append 
    this object into the shoes list.
    """
    shoes_list = []
    with open("inventory.txt", "r", encoding="UTF-8") as f:
        # Prints error if the inventory file is not found. 
        try: 
            inventory = open("inventory.txt", "r")
        except FileNotFoundError:
            print("This file was not found in the directory.")
        else:
            pass
        
        # Puts all the items in the file into a list.
        for i in f:
            line = i.strip()  # Removes "\n"
            log_shoe = line.split(",")  # Split items via comma.
            
            try:
                # Make Shoe object
                log_shoe = Shoes(log_shoe[0], log_shoe[1], log_shoe[2],
                            log_shoe[3], log_shoe[4])
            
            # If there is an entry missing in one of the lines
            except IndexError:
                print(f"There was an error found while compiling the from "
                    f" the inventory.txt file. Line {i} has an entry error")
            
            # If the file is formatted as expected: append to list.
            else:
                shoes_list.append(log_shoe)
            #print(shoes_list[count])
    return shoes_list


def view_all():
    """Display all the objects in the Shoe class"""
    shoes_list = read_shoes_data()

    for i in range(0,len(shoes_list)-1):
        display_data = ("{:<15} {:<11} {:<22} {:<10} {:<15}"\
                        .format(shoes_list[i].country,
                                shoes_list[i].code,
                                shoes_list[i].product,
                                ("$" + str(shoes_list[i].cost)),
                                shoes_list[i].quantity))
        print(display_data)  # Data.


def re_stock():                         
    """View and restock lowest quantity in warehouse"""
    # Get the lowest quantity item:
    # Ensure using updated shoes list
    shoes_list = read_shoes_data()

    low_stock = []  # Quanity values list.
    # Loop through shoelist and add all the quanities in a list.
    # Range at 1 to skip the heading line. 
    for item in range(1,len(shoes_list)):
        quantity_number = (shoes_list[item].quantity)
        low_stock.append(int(quantity_number))

    # Find the index of the lowest quanity.
    index = [index for index, low in enumerate(low_stock) 
                if low == min(low_stock)]

    # Adding +1 to account for the heading in the inventory file,
    # index[0] is used if lowest quantity value is found more than once,
    # in that case, choose the first item to restock.          
    index = int(index[0]) + 1  

    # Print out the details of the lowest stocked item.
    print("This is the warehouse with the lowest stock:")
    # Put up heading.
    display = ("{:<15} {:<15} {:<22} {:<15} {:<15}"\
                .format("Country",
                    "Code",
                    "Product",
                    "Cost",
                    "Quantity"))
    print(display)  # Headings.

    # Put up lowest quantity item data.
    display_data = ("{:<15} {:<15} {:<22} {:<15} {:<15}"\
                    .format(shoes_list[index].country,
                            shoes_list[index].code,
                            shoes_list[index].product,
                            ("$"+shoes_list[index].cost),
                            shoes_list[index].quantity))
    print(display_data)  # Data.
    print()

    # Allow user to update the stock order, or go back to menu.
    while True:
        add_choice = input("Choose to update quantity now?"
                    "\n y - yes, update quanity order now."
                    "\n n - no, go back to menu\n").lower()  
        
        # User wants to update quantity with new order now.
        if add_choice == "y":
            # Get the quanitity of stock to be added from user.
            add = int(input("Enter the quanity order of these shoes "
                        "to update the stock.\n"))
            
            # Add the new quanity to the old quantity.
            stock_update = int(shoes_list[index].quantity) + add

            # Replace in the file in inventory. 
            new_inventory = []
            replace_inventory = []
            with open('inventory.txt', 'r+', encoding='utf-8') as file:
                # Reads all lines in inventory sans \n.
                data = file.read().splitlines()

                # Separate items in data into list items. 
                for items in data:
                    line = items.strip() 
                    log_shoe = line.split(",")  # Split items via comma.            
                    replace_inventory.append(log_shoe)
                
                # Replace the old quantity with the updated inventory.
                replace_inventory[index][4] = str(stock_update)
                
                # Reformat list to write to inventory.txt.
                for the_items in replace_inventory:
                    inventory_replace = ",".join(the_items)
                    new_inventory.append(inventory_replace)

            # Write the new inventory to the inventory file. 
            with open('inventory.txt', 'w', encoding='utf-8') as file:
                file.write("\n".join(new_inventory))
            
            # Confirmation message to user about inventory update.
            print("\nThis was updated in inventory.txt")
            break

        # Return to menu.
        elif add_choice == "n":
            break

        # User invalid menu choice, try again.
        else:
            print("Incorrect choice")
            continue


def search_shoe():
    """User can search shoe object using the SKU number"""
    # Ensure to get updated shoes_list.
    shoes_list = read_shoes_data()

    # Get product code from user to search:
    search_code = input("Enter the SKU product code: ")

    # Find index of the matching SKU number in the shoes_list.
    index = [index for index, item in enumerate(shoes_list) 
                if item.code == search_code]
    
    # Return the matching object.
    # Put up heading.
    display = ("{:<15} {:<15} {:<22} {:<15} {:<15}"\
                .format("Country",
                    "Code",
                    "Product",
                    "Cost",
                    "Quantity"))
    print(display)  # Headings.

    # Put searched for item.
    display_data = ("{:<15} {:<15} {:<22} {:<15} {:<15}"\
                    .format(shoes_list[index[0]].country,
                            shoes_list[index[0]].code,
                            shoes_list[index[0]].product,
                            ("$"+shoes_list[index[0]].cost),
                            shoes_list[index[0]].quantity))
    print(display_data)  # Data.

    # Allow user to peruse sale infor before having menu pop up.
    input("Press enter when to return to menu.")


def highest_qty(): 
    """Takes highest quanity item and displays it on sale"""
    # Ensure to get updated shoes_list.
    shoes_list = read_shoes_data()
    highest_stock = []  # Quanity values list.

    # Loop through shoelist and add all the quanities in a list.
    # Range at 1 to skip the heading line. 
    for item in range(1, len(shoes_list)):
        quantity_number = (shoes_list[item].quantity)
        highest_stock.append(int(quantity_number))

    # Find the index of the highest quanity.
    index = [index for index, high in enumerate(highest_stock) 
                if high == max(highest_stock)]

    # Adding +1 to account for the heading in the inventory file:            
    index = int(index[0]) + 1  

    # The sale display
    print(f"{shoes_list[index].product} in "
        f"{shoes_list[index].country} IS ON SALE!"
        f"\nThe SKU number is: {shoes_list[index].code}! Get it before its"
        f" all gone!")

    # Allow user to peruse sale infor before having menu pop up.
    input("Press enter when to return to menu.")


def value_per_item():
    """Gets value per item, and displays along the item info"""
    # Ensure updates shoes_list is used.
    shoes_list = read_shoes_data()

    # Isolate and prepare cost values for calucaltion.
    cost_list = []  # Cost values list.

    # Append all cost items to a list.
    [cost_list.append(shoes_list[i].get_cost())    
        for i in range(1, len(shoes_list))]

    # Convert all cost values to integers.
    cost_list = [int(cost) for cost in cost_list]

    # Isolate and prepare quantity values for calculation.
    qty_list = []  # Quantity values list

    # Append all quantity values to a list.
    [qty_list.append(shoes_list[i].get_quantity()) 
        for i in range(1, len(shoes_list))]

    # Convert all quantity values to integers. 
    qty_list = [int(quanity) for quanity in qty_list]

    # Perform calculation of value of item.
    value_list = []
    for i in range(0, len(qty_list)):
        value_value = qty_list[i] * cost_list[i]
        value_list.append(value_value)  # Add value in list.

    # Display the headings.
    display = ("{:<15} {:<11} {:<22} {:<15}"\
                .format("Country",
                    "Code",
                    "Product",
                    "Value"))
    print(display)  # Headings.

    # Display the data.
    for i in range(0,len(shoes_list)-1):
        display_data = ("{:<15} {:<11} {:<22} {:<15}"\
                        .format(shoes_list[i+1].country,
                                shoes_list[i+1].code,
                                shoes_list[i+1].product,
                                ("$"+str(value_list[i]))))
        print(display_data)  # Data.

    # Allow user to peruse sale infor before having menu pop up.
    input("Press enter when to return to menu.")


print("THIS IS THE NIKE WAREHOUSE.")
menu = ""
while menu != "q":
    menu = input("\nChoose a menu item:"
                "\n a - view all in stock"
                "\n r - restrock the lowest quantity in warehouse"
                "\n s - search for shoe using SKU number"
                "\n l - look at our items on sale"
                "\n v - get the value per item"
                "\n e - exit \n").lower()

    # To see the inventory in full.
    if menu == "a":
        print()
        view_all()

    # User wishes to see lowest quantity item and potentially.
    # add new stock order.
    elif menu == "r":
        print()
        re_stock()
    
    # Search for the object using the SKU number.
    elif menu == "s":
        print()
        search_shoe()

    # Check the sale item.
    elif menu == "l":
        print()
        highest_qty()
    
    # Get a list of the total value per item.
    elif menu == "v":
        print()
        value_per_item()
    
    # User exits the program.
    elif menu == "e":
        print()
        print("Goodbye. \n'Just do it'")
        exit()

    # User enters invalid menu entry.
    else:
        print("Incorrect entry. Try again.")