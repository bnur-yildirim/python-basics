# function that checks the stocks for the items customer wants,
# if stock isn't enough, amount in the shopping list is updated 
# to the highest amount possible
def check_stock(inventory, SList):
    newList = []
    for key in inventory:
        for item, amount in SList:
            if item == key:
                if inventory[key][1] == 0:
                    continue
                elif amount > inventory[key][1]:
                    newList.append((item, inventory[key][1]))
                else:
                    newList.append((item, amount))
    return newList

#inventory of the online shop
# inventory = {"item name":[price, stock, "section the item belongs"]}
inventory = {"Laptop":[1200.00, 10, "Electronics"],
             "Coffee Maker":[50.99, 20, "Appliances"],
             "Running Shooes":[79.95, 30, "Clothing"],
             "Smartphone":[899.99, 15, "Electronics"],
             "Cookware Set":[129.50, 25, "Kitchen"],
             "Backpack":[34.99, 40, "Accessories"],
             "LED TV":[799.00, 8, "Electronics"],
             "T-Shirt":[19.99, 10, "Clothing"]}

# shopping list of the customer
# shopping_list = [("item name", amount)]
shoppingList = [("Laptop", 1), ("Coffee Maker", 2), ("Smartphone", 1),
                ("Cookware Set", 1), ("Backpack", 90), ("LED TV", 1),
                ("T-Shirt", 3)]
print(shoppingList)
shoppingList = check_stock(inventory, shoppingList)
print(shoppingList)
