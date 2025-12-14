# -----------------------------------------------------------
# SHOPPING CART PROGRAM
# Creativity Addition:
# I added a QUANTITY feature so the user can specify how many
# units of each item they want. The cart displays aligned
# prices and calculates totals using item quantities.
# -----------------------------------------------------------

print("Welcome to the Shopping Cart Program!\n")

# Lists to store data
item_names = []
item_prices = []
item_quantities = []   # <-- CREATIVE FEATURE

while True:

    # Display menu
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    choice = input("Please enter an action: ")

    # -------------------------------------------------------
    # 1. ADD ITEM
    # -------------------------------------------------------
    if choice == "1":
        name = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{name}'? "))
        quantity = int(input(f"How many '{name}' would you like to add? "))  # creative feature

        item_names.append(name)
        item_prices.append(price)
        item_quantities.append(quantity)

        print(f"'{name}' has been added to the cart.\n")

    # -------------------------------------------------------
    # 2. VIEW CART
    # -------------------------------------------------------
    elif choice == "2":
        if len(item_names) == 0:
            print("Your shopping cart is empty.\n")
        else:
            print("The contents of the shopping cart are:")
            for i in range(len(item_names)):
                name = item_names[i]
                price = item_prices[i]
                quantity = item_quantities[i]

                # Align prices using formatting
                print(f"{i+1}. {name:<12} - ${price:.2f}  (Qty: {quantity})")

            print()  # blank line

    # -------------------------------------------------------
    # 3. REMOVE ITEM
    # -------------------------------------------------------
    elif choice == "3":
        if len(item_names) == 0:
            print("Your shopping cart is empty. Nothing to remove.\n")
        else:
            print("The contents of the shopping cart are:")
            for i in range(len(item_names)):
                print(f"{i+1}. {item_names[i]} - ${item_prices[i]:.2f} (Qty: {item_quantities[i]})")

            remove = int(input("\nWhich item would you like to remove? "))

            # convert to 0-based index
            index = remove - 1

            # verify valid index
            if 0 <= index < len(item_names):
                item_names.pop(index)
                item_prices.pop(index)
                item_quantities.pop(index)
                print("Item removed.\n")
            else:
                print("Sorry, that is not a valid item number.\n")

    # -------------------------------------------------------
    # 4. COMPUTE TOTAL
    # -------------------------------------------------------
    elif choice == "4":
        total = 0
        for i in range(len(item_prices)):
            total += item_prices[i] * item_quantities[i]
        print(f"The total price of the items in the shopping cart is ${total:.2f}\n")

    # -------------------------------------------------------
    # 5. QUIT
    # -------------------------------------------------------
    elif choice == "5":
        print("Thank you. Goodbye.")
        break

    # -------------------------------------------------------
    # INVALID OPTION
    # -------------------------------------------------------
    else:
        print("Invalid choice. Please try again.\n")
        
