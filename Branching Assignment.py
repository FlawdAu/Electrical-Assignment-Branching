# Electric Bill Calculator

# Get input
kw_hours = int(input("Enter the KW hours used: "))

# Calculate amount owed
if kw_hours <= 1000:
    amount = kw_hours * 0.07633
else:
    amount = (1000 * 0.07633) + ((kw_hours - 1000) * 0.09259)

# Display result
print("Amount owed is $", amount, sep="")