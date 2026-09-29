#July_27_RobuxSystem

menu = """What do you want to do: 
0. Exit
1. Buy hat 100 Robux
2. Buy hair 150 Robux
3. VIP Server 500 Robux
4. Add more Robux

Enter your selection: """

robux = 300

inventory = []

def buy_thing(item, price):
    global robux
    global inventory
    
    if robux >= price:
        robux -= price
        inventory.append(item)
        print(f"\n{item} was added to your inventory\n")
    else:
        print("\nYou don\'t have the robux\n")

while True:
    print(f"You have ${robux} robux")
    user_input = input(menu)
    if user_input == "0":
        break
    elif user_input=="1":
        buy_thing("hat", 100)
    elif user_input == "2":
        buy_thing("hair", 150)
    elif user_input == "3":
        buy_thing("VIP server", 500)
    elif user_input == "4":
        #Ask the user how much robux to add
        robux_to_add = input("how much robux do you want to add?")
        
        #Ask the user for their credit card number
        input("Enter your credit card number: ")
        
        #We need to add that robux to the robux variable
        robux += int(robux_to_add)

for i in range(len(inventory)):
    print(f"{i +1}. {inventory[i]}")