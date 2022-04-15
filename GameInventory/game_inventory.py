inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    for i in inventory:
        print(f"{i}: {inventory[i]}")

def add_to_inventory(inventory, added_items):
    used = []
    for i in added_items:
        if i not in used:
            if i in inventory:
                inventory[i] += added_items.count(i)
                used.append(i)
            else:
                inventory.update({i:added_items.count(i)})
                used.append(i)
    display_inventory(inv)

def print_table(inventory, order):
    s1 = ""
    s2 = ""
    s3 = ""
    print("-----------------\nitem name | count\n-----------------")
    if order == "count,desc":
         for key, value in sorted(inventory.items(), key=lambda kv: kv[1], reverse=True):
             s1 = key + " |"
             s1 = s1.rjust(11)
             s2 = " " + str(value)
             s2 = s2.rjust(6)
             s3 = s1 + s2
             print(s3)
    elif order == "count,asc":
        for key, value in sorted(inventory.items(), key=lambda kv: kv[1]):
             s1 = key + " |"
             s1 = s1.rjust(11)
             s2 = " " + str(value)
             s2 = s2.rjust(6)
             s3 = s1 + s2
             print(s3)

def Item_Count(item, filename):
    count = 0
    with open(filename) as f:
        for i in f:
            i = i[:-1]
            if i == item:
                count += 1
    return count

def import_inventory(inventory, filename):
    used = []
    with open(filename) as file:
        for i in file:
            i = i[:-1]
            if i not in used:
                if i in inventory:
                    inventory[i] += Item_Count(i, filename)
                    used.append(i)
                else:
                    inventory.update({i:Item_Count(i, filename)})
                    used.append(i)
    print_table(inventory, "count,desc")
    export_inventory(inv, "export_inventory.csv")

def export_inventory(inventory, filename):
     with open(filename, "w") as file:
         for i in inventory:
             file.write(i + ": " + str(inventory[i]) + "\n")
             
add_to_inventory(inv, dragon_loot)
import_inventory(inv, "import_inventory.csv")