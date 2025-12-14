##largest_num = numbers[0]
#for number in numbers:
            #
    #['chips',2.99],
    #


#max_price = -1 
#product_name = ""
#for item in shopping_cart:
    #product_name = item [0]
    #price = item [1]
    #if price > max_price:
    #  max_price = price
#print(f'The maximum price is:{max_price}')
#print(f"The product with maximaum price is {product_name}")

    
        
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# Start our youngest_age variable at 
youngest_age = 9999

# This will keep track of the person with the youngest age
youngest_name = ""

# Go through each person in the list
for person_line in people:

    parts = person_line.split() # by default this will split on the space

    # Set variables for the two different parts
    name = parts[0]
    age = int(parts[1])

    # Check to see if this current person is younger than the youngest
    # that we have seen so far
    if age < youngest_age:
        # This person is the new "youngest"

        # Save their age as the new youngest
        youngest_age = age

        # Save their name as the youngest name
        youngest_name = name

# Outside of the loop, so we are all done now
print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")



