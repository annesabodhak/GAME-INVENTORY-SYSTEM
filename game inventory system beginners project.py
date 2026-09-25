#### 🎮 Mini Project Challenge — Inventory System

#*Create a Python program for a game character that stores items in a dictionary as `item: (category, quantity)` and allows the user to view the inventory, add an item, use an item, search for an item, remove an item, and see the total number of items through a menu-driven program.**
d=inventory = {
    "sword": ("weapon", 1),
    "potion": ("health", 5),
    "coins": ("currency", 100),
    "shield": ("armor", 1)
}
for key, value in d.items():
    print(key , ':', value)
print('welcome to the inventory system!')

#TO ADD AN ITEM IN INVENTORY 
a= input('Enter the item name to add: ')
b= input('Enter the item category: ')
c= int(input('Enter the item quantity: '))
if a in d: 
    
    print('Item already exists in inventory. Updating quantity.')
    d[a] = (b, d[a][1] + c)  # Update quantity if item exists
else:
    d[a] = (b, c)  # Add new item to inventory
print('Item added/updated successfully!')
print(d)


#to take input from user and check the quantity of the item in inventory and display the remaining quantity after using the item
e= input('Enter the item name to use: ')
f= int(input('no. of quantity you want to use:'))
if e in d:
    q=d[e][1]
    if q>0: 
        s=q-f
        if s>0:
            print('Remaining quantity of', e, 'is:', s)
        else:
            print ('you dont have enough quantity of', e, 'to use. Remaining quantity is:', q)
    else:
        print('quantity is zero')
#to search for an item in inventory and display the category and quantity of the item
g= input('Enter the item name to search: ')
if g in d: 
    print ('item found:', g , 'category:', d[g][0] ,  'quantity:', d[g][1])
else: 
    print('item not found in inventory')

#to take an input from user to remove item from the inventory 
s1= input('Enter the item name to remove: ')
if s1 in d:
    del d[s1]
    print(d , 'item removed successfully!')
else: 
    print('item not found in inventory')

#count the total number of items in the inventory and display it by their category 
y= sum(value[1] for value in d.values())
print('Total number of items in inventory:', y)
for key, values in d.items():
    print(key, ':', values[1])


print('Thank you for using the inventory system! SEE YOU NEXT TIME!')



        
        
