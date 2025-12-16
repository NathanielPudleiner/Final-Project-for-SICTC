#function to check if value if an integer and to return false if not an integer
def intchecker(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
#main menu loop
menu = """
What would you like to do?
(1) = Read the Menu
(2) = Create Order Cart
(3) = Examine Cart
(4) = Proceed to Checkout
(5) = Modify Cart
(6) = Exit
"""
#List that stores all items and their prices
foodItems= ["kp", "kpc", "dkp", "dkpc", "tkp", "tkpc", "cbs", "cbm", "cbl", "kr", "sls", "ks", "sfs", "sfm", "sfl", "km", "dkm", "tkm", "ssd", "fl", "ss", "gl", "gls"]
prices = [0.25, 1.50, 2.00, 2.25, 3.00, 3.25, 1.00, 1.25, 1.50, 1.50, 0.50, 2.00, 1.00, 1.25, 1.50, 3.50, 3.75, 4.00, 1.25, 2.00, 3.00, 2.00, 2.50]

#List that stores orders
orderitem = [[]]
orderprice = [[]]
ui = 0
#iterator for order number
i = 0
while(ui!="6"):
    #Main control loop
    ui = input(menu)
    if ui == "1":
        #menu printing
        print("""
                        GALLEY GRUB:
        (kp) Krabby Patty - $1.25             (km) Krabby Meal - $3.50
            (kpc) w/ sea cheese - $1.50       (dkm) Double Krabby Meal - $3.75
        (dkp) Double Krabby Patty - $2.00     (tkm) Triple Krabby Meal - $4.00
            (dkpc) w/ sea cheese - $2.25      (ssd) Salty Sea Dog - $1.25
        (tkp) Triple Krabby Patty - $3.00     (fl) Footlong - $2.00
            (tkpc) w/ sea cheese - $3.25      (ss) Sailors Surprise - $3.00
                                              (gl) Golden Loaf - $2.00
                                                (gls) w/ sauce - $2.50

        Coral Bits:                           (ks) Kelp Shake - $2.00
            (cbs) Small - $1.00
            (cbm) Medium - $1.25              Seafoam Soda:
            (cbl) Large - $1.50                   (sfs) Small - $1.00
                                                  (sfm) Medium - $1.25
        (kr) Kelp Rings - $1.50                   (sfl) Large - $1.50
            (sls) salty sauce - $0.50
        """)
        
    elif ui == "2":
        #continorder controls the order continuation and while loop
        #newordercheck checks if user wants to add a new list to list of lists
        print("Make sure you have examined the menu to know what you want to order!")
        continorder = "yes"
        while(continorder!="no"):
            newordercheck = "no"
            newordercheck = input("Do you want to create a new order? ")
            if newordercheck == "yes":
                orderitem.append([])
                orderprice.append([])
                i += 1
            else:
                pass
            userorder = input("What would you like to order? ")
            #Checks main item index to check if userorder exist in the menu list
            if userorder not in foodItems:
                #Operates if item doesn't exit in menu list
                print("Order something actually from the menu! Re-examine the menu if you have too")
            elif userorder in foodItems:
                #Operates if item exists in menu list
                orderitem[i].append(userorder)
                orderprice[i].append(prices[foodItems.index(userorder)])
                print(orderitem[i])
                print(orderprice[i])
            else:
                #Displays if conditional didn't work properly
                print("Error! Conditional statement not handled! ")
            continorder = input("Do you want to add to your order? ")



    elif ui == "3":
        #prints out specified list
        ordertypeexamine = input("Which order do you want to view? ")
        if intchecker(ordertypeexamine):
            print(orderitem[int(ordertypeexamine)])
            print(orderprice[int(ordertypeexamine)])
        else:
            break
    elif ui == "4":
        subtotal = 0
        tax = .07
        #checks the range of the main list containing all of the orders
        for ordi in range(len(orderitem)):
            print(f"Order {ordi}")
            for itemi in range(len(orderitem[ordi])):
                #prints every order in the range of the main list
                print(f"    {orderitem[ordi][itemi]} = {orderprice[ordi][itemi]}")
            order_total = sum(orderprice[ordi])
            print(f"    {order_total}")
            subtotal += order_total
        #Calculations for the main order
        print(f"Your subtotal is: ${subtotal}")
        total = subtotal + (subtotal * tax)
        print(f"Your Bikini Bottom tax is: ${tax}")
        print(f"Your total is: ${total}")
    elif ui == "5":
        confirmrem = "yes"
        while(confirmrem!="no"):
            #asks for which list to modify
            ordertype = input("Which order do you want to change? ")
            #checks if user input is a number
            if intchecker(ordertype):
                i = int(ordertype)
            else:
                break
            #prints the list of items
            print(orderitem[int(ordertype)])
            remitem = input("""What item would you like to remove?
            (Note) - Make sure to type the position number in the list
            (Note) - First position on list is 0
            """)
            if intchecker(remitem):
                #converts remitem to an int value then pops the index pos of both price and item list
                orderitem[int(ordertype)].pop(int(remitem))
                orderprice[int(ordertype)].pop(int(remitem))
                print(orderitem[int(ordertype)])
                print(orderprice[int(ordertype)])
                confirmrem = input("Do you want to continue? ")
            else:
                print("Type a valid index position!")
                confirmrem = input("Do you want to continue? ")
    elif ui == "6":
        break
    else:
        #handler for if the user types in nonsense
        break
