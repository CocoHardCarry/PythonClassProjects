#July_25_ShoppingCartSystem

#Create our menu

menu = """What do you want to buy:
\t1. I am done, checkout please
\t2. Milk - $5
\t3. Ice Cream - $4
\t4. Bread - $6
\t5. Soup - $3

Enter your selection:"""

answer = input(menu)

total_cost = 0
shopping_cart = []
frozen_foods = ["Milk","Ice Cream"]

def purchase_item(item, cost):
    global total_cost
    global shopping_cart
    #Add a specific item to your shopping cart list
    #increase the total cost by the cost
    total_cost += cost
    shopping_cart.append(item)
    print(f"\nYou have bought some {item}\n")

while True:
    answer = input(menu)
    if answer == "1":
        break
    elif answer == "2":
        purchase_item("Milk",5)
    elif answer == "3":
        purchase_item("Ice Cream",4)        
    elif answer == "4":
        purchase_item("Bread",6)    
    elif answer == "5":
        purchase_item("Soup",3) 

#Down here, loop through the shopping cart and print each item out in a list
#Hint 1, use a for loop
#Hint 2, use a Range for loop
#Do this on your own 5 minutes

print("\nHere is your Shopping Cart: ")
for index in range(len(shopping_cart)):
    if shopping_cart[index] in frozen_foods:
        #Print something
        print(f"\t{index+1}. {shopping_cart[index]} - Needs To Be Frozen")
    else:
        print(f"\t{index+1}. {shopping_cart[index]}")

print(f"Your total cost is: ${total_cost}")
