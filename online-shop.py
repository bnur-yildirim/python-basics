# function that checks the stocks for the items customer wants,
# if stock isn't enough, amount in the shopping list is updated 
# to the highest amount possible
def check_stock(inventory, shopping_list):
    new_list = []
    for item, amount in shopping_list:              # item = item name, amount = amount customer wants
        stock = inventory[item][1]
        if item in inventory:                       # if we find item in the inventory
            if stock == 0:                          # if stock of the item is zero
                continue
            elif amount > stock:                    # if stock is not enough
                new_amount = int(input(f"Stock of {item} is only {stock}.\nEnter a new amount: "))

                # make sure new amount is entered correctly
                while new_amount < 0 or new_amount > stock:
                    new_amount = int(input(f"Amount should be between (0 - {stock}).\nEnter a new amount: ")) 
                if new_amount == 0:               # if customer doesn't want the item anymore
                    continue                      # this line will remove it from the shopping list
                else:
                    new_list.append((item, new_amount))
            else:
                new_list.append((item, amount))                                   
    return new_list

#calculate the total bill
def compute_bill(inventory, shopping_list):
    bill = 0
    for item, amount in shopping_list:           # go through each item in the shopping list
        bill += inventory[item][0] * amount      
    return bill

def update_stock(inventory, shopping_list):
    for item, amount in shopping_list:
        inventory[item][1] -= amount            # decrease the stock with the amount purchased
    return inventory

#inventory of the online shop
# inventory = {"item name":[price, stock, "section the item belongs"]}
inventory = {"Laptop":[1200.00, 10, "Electronics"],
             "Coffee Maker":[50.99, 20, "Appliances"],
             "Running Shoes":[79.95, 30, "Clothing"],
             "Smartphone":[899.99, 15, "Electronics"],
             "Cookware Set":[129.50, 25, "Kitchen"],
             "Backpack":[34.99, 40, "Accessories"],
             "LED TV":[799.00, 8, "Electronics"],
             "T-Shirt":[19.99, 10, "Clothing"]}

# shopping list of the customer
# shopping_list = [("item name", amount)]
shopping_list = [("Laptop", 1), ("Coffee Maker", 30), ("Smartphone", 1),
                ("Cookware Set", 1), ("Backpack", 2), ("LED TV", 1),
                ("T-Shirt", 3)]

shopping_list = check_stock(inventory, shopping_list)
print(f"Your updated shopping list is:\n{shopping_list}\n")

bill = compute_bill(inventory, shopping_list)
print(f"Total price: $ {bill:.2f}\n")

inventory = update_stock(inventory, shopping_list)
print(f"The inventory has been updated:\n{inventory}\n")