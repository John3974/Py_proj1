# Basketball Player Performance Rating Program

# Step 1: Get input
score = float(input("Enter average points per game: "))

# Step 2: Determine base performance level
if score >= 30:
    level = "Superstar"
elif score >= 25:
    level = "Excellent"
elif score >= 20:
    level = "Good"
elif score >= 15:
    level = "Average"
else:
    level = "Needs Improvement"

# Step 3: Determine + or - sign
# (No + for Superstar, no signs for Needs Improvement)
sign = ""
decimal_part = score - int(score)

if level not in ["Superstar", "Needs Improvement"]:
    if decimal_part >= 0.7:
        sign = "+"
    elif decimal_part < 0.3:
        sign = "-"

# Step 4: Combine level and sign
performance = level + sign

# Step 5: Check All-Star qualification
if score >= 20:
    result = "Qualified for the All-Star team!"
else:
    result = "Not qualified for the All-Star team."

# Step 6: Display results
print(f"\nPerformance: {performance}")
print(f"Result: {result}")
