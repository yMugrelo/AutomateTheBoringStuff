stuff = {'rope' : 1, 'torch' : 6, 'gold coin' :  42, 'dagger' : 1, 'arrow' : 12}
#Learning  how to show items in a dictionary! 
def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k,v in inventory.items():
        item_total += v
    print(f"Total number of items: {item_total}")

displayInventory(stuff)