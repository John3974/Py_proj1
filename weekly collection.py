# small Business Tracker:Sales,credits,expenses,profits,losses,debits

from datetime import datetime

# businesss setup
business_name = "Matire Small Business"
business_address = "Denkell, rooftop"
business_contact = "info@matirebusiness.com"
business_phone = "0759984237"
business_owner = "John otieno"
business_start_date = "2023-01-01"
business_currency = "USD"
business_tax_id = "TAX123456"

SELLING_PRICE = 85.0   # per joint
COST_PRICE = 35.0      # per joint(target cost )
DAILY_SALES_TARGET = 50 # joints evry 4-5 days
 

sold_joints = input("Enter number of joints sold this week: ")
try:
    sold_joints = int(sold_joints)

except Exception as e:
    print(f"An error occurred: {e}")
    
if sold_joints == "":
    sold_joints = 0
elif sold_joints <= 0:
    print("Invalid input. Please enter a positive number.")
    sold_joints = 0


        

# Transaction records: credits, debits, expenses, profits, losses, sales
# Existing transactions list
transactions = []

# --- Interactive section ---
print("=== Weekly Business Tracker ===")
while True:
    name = input("Enter name (person or company): ")
    amount = float(input("Enter amount (Ksh): "))
    t_type = input("Type of transaction (credit/debit): ").lower()
    category = input("Category (profit/loss/sale/expenditure): ").lower()
    description = input("Short description: ")

    # Automatically save today's date
    date = datetime.now().strftime("%Y-%m-%d")

    transactions.append({
        "date": date,
        "name": name,
        "type": t_type,
        "amount": amount,
        "category": category,
        "description": description
    })

    another = input("Add another transaction? (yes/no): ").lower()
    if another != "yes":
        break

# computing weekly revenue and costs

revenue = sum(t["amount"] for t in transactions if t["type"] == "sale")
costs = sum(t["amount"] for t in transactions if t["type"] in ["expense", "debit", "loss"])
profits = sum(t["amount"] for t in transactions if t["type"] == "profit")
credits = sum(t["amount"] for t in transactions if t["type"] == "credit")
debits = sum(t["amount"] for t in transactions if t["type"] == "debit")
net_income = revenue + credits - costs - debits
# weekly summary report
print(f"Weekly Summary Report for {business_name}")
print(f"Address: {business_address}")
print(f"Contact: {business_contact} | Phone: {business_phone}")
print(f"Owner: {business_owner}")
print(f"Week Ending: {datetime.now().strftime('%Y-%m-%d')}")
print("-" * 40)
print(f"Total Revenue: ${revenue:.2f}")
print(f"Total Costs: ${costs:.2f}")
print(f"Total Profits: ${profits:.2f}")
print(f"Total Credits: ${credits:.2f}")
print(f"Total Debits: ${debits:.2f}")
print(f"Net Income: ${net_income:.2f}")

# list detailed 
print("\nPeople who owe me money:")
for t in transactions:
    if t["type"] == "credit":
        print(f"{t['name']} owes ${t['amount']:.2f} for {t['description']} on {t['date']}")
print("\nPeople I owe money to:")
for t in transactions:
    if t["type"] == "debit":
        print(f"I owe {t['name']} ${t['amount']:.2f} for {t['description']} on {t['date']}")
        print("*" * 30)
    elif t["type"] == "loss":
        print(f"Lost ${t['amount']:.2f} due to {t['description']} on {t['date']}")
    elif t["type"] == "profit":
        print(f"Profit of ${t['amount']:.2f} from {t['description']} on {t['date']}")
    elif t["type"] == "expense":
        print(f"Expense of ${t['amount']:.2f} for {t['description']} on {t['date']}")
    elif t["type"] == "sale":
        print(f"Sold ${t['amount']:.2f} to {t['name']} on {t['date']}")
        
    
        
        
print(".................")
print(".................")
total_revenue = sold_joints * SELLING_PRICE
print(f"Total Joints Sold This Week: {sold_joints:.2f} joints")
print(f"Total Revenue This Week: ${total_revenue:.2f}")

total_week_balance = net_income - (COST_PRICE * sold_joints)
print(f"Total Weekly Balance After Costs: ${total_week_balance:.2f}")
# calculate weekly balance after costs
weekly_costs = COST_PRICE * sold_joints
print(f"Total Weekly Costs: ${weekly_costs:.2f}")
if total_week_balance >= 0:
    print(f"you made a profit of ${total_week_balance:.2f} this week.")
else:
    print(f"you incurred a loss of ${-total_week_balance:.2f} this week.")

# how much more to sell to meet target

target_sales = DAILY_SALES_TARGET * 7 / 5  # weekly target based on 4-5 days

joints_needed = target_sales - sold_joints

if joints_needed > 0:
    additional_revenue_needed = joints_needed * SELLING_PRICE
    print(f"Additional Revenue Needed to Meet Target: ${additional_revenue_needed:.2f}")
elif joints_needed >= 10:
    print("you need to step up your sales game!")
else:
    print("Congratulations! You've met your sales target for the week.")
    print("Keep up the great work!")
print(".................")
    
