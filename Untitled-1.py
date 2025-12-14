
keep_running = "yes"

while keep_running.lower() == "yes":

        # display manu
        print("Menu")
        print("1. Add a new item")
        print("2. display the content of the shopping cart ")
        print("3. Remove an item")
        print("4. Compute the total price of items in the cart")
        print("5. Exit")

        # add a new item
        item_names = []
        item_prices = []

        while True:
            choice = input("Choose an option (1-5): ")
        
            if choice == "1":
                name = input("Enter the item name: ")
                price = int(input("Enter the item price: "))
                item_names.append(name)
                item_prices.append(price)
                print(f"'{name}' has been added to the cart.\n")
            #display the content of the shopping cart  
            elif choice == "2":
                if not item_names:
                    print("The shopping cart is empty.\n")
                else:
                    print("Items in the shopping cart:")
                    for i in range(len(item_names)):
                        print(f"{i + 1}. {item_names[i]} - ${item_prices[i]:.2f}")
                    print()
                # remove an item
            elif choice == "3":
                if not item_names:
                    print("The shopping cart is empty. Nothing to remove.\n")
                else:
                    item_to_remove = input("Enter the name of the item to remove: ")
                    if item_to_remove in item_names:
                        index = item_names.index(item_to_remove)
                        item_names.pop(index)
                        item_prices.pop(index)
                        print(f"'{item_to_remove}' has been removed from the cart.\n")
                    else:
                        print(f"'{item_to_remove}' not found in the cart.\n")
            # compute the total price of items in the cart
            elif choice == "4":
                total_price = sum(item_prices)
                print(f"The total price of items in the cart is: ${total_price:.2f}\n")
            elif choice == "5":
                print("Exiting the program. Goodbye!")
                keep_running = "no"
            else:
                print("Invalid choice. Please choose a valid option (1-5).\n")
                
                
                
                
             
        
        
        