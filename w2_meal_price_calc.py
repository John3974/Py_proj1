200# Meal Price Calculator

# the price of child's meal
CHILD_MEAL_PRICE = float(input("Enter the price of a child's meal: "))

# the price of adult meal
ADULT_MEAL_PRICE = float(input("Enter the price of an adult meal: "))

# number of children
num_children = int(input("Enter the number of children: "))

# number of adults
num_adults = int(input("Enter the number of adults: "))

# meal's subtotal for children
subtotal_children = CHILD_MEAL_PRICE * num_children
print(f"Subtotal for children's meals ({num_children} at ${CHILD_MEAL_PRICE} each): ${subtotal_children:.2f}")

# meal's subtotal for adults
subtotal_adults = ADULT_MEAL_PRICE * num_adults
print(f"Subtotal for adult's meals ({num_adults} at ${ADULT_MEAL_PRICE} each): ${subtotal_adults:.2f}")

# total meal's subtotal
total_subtotal = subtotal_children + subtotal_adults
print(f"Total meal subtotal: ${total_subtotal:.2f}")

# sales tax rate
SALES_TAX_RATE = 0.07

# total sales tax
total_sales_tax = total_subtotal * SALES_TAX_RATE
print(f"Total sales tax: ${total_sales_tax:.2f}")

# total meal cost
total_meal_cost = total_subtotal + total_sales_tax
print(f"Total meal cost: ${total_meal_cost:.2f}")

#  payment amount
payment_amount = float(input("Enter the payment amount: "))

# change
change = payment_amount - total_meal_cost
print(f"Change: ${change:.2f}")