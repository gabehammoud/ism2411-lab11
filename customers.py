
# module 11 lab 

# reflection
# 1.
# I would use .get() when a key might be missing because it prevents errors
# I would use bracket notation when I know the key exists and need its value

# 2.
# Exercise 8 reminds me of using a PivotTable in Excel to summarize data
# Python is more useful for large datasets because it can automate calculations
# and process information without manually updating spreadsheets

# exercise 1

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1500
}
print("Exercise 1:")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# exercise 2 

print("\nExercise 2:")
customer["phone"] = "555-123-4567"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# exercise 3

print("\nExercise 3:")
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError:
    print("KeyError caught: email does not exist in the dictionary.")

# exercise 4

print("\nExercise 4:")
for key, value in customer.items():
    print(f"{key}: {value}")
# using .items() returns both the key and its value
# iterating without .items() returns only the key
print("\nIterating without .items():")
for key in customer:
    print(key)

# exercise 5 

print("\nExercise 5:")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}
tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
purchase_price = 200
final_price = purchase_price * (1 - discount_rate)
print("Tier:", tier)
print("Discount rate:", f"{discount_rate:.0%}")
print("Final price: $", f"{final_price:.2f}", sep="")

# exercise 6

print("\nExercise 6:")
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]
for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(f"{name} ({tier}): ${discount_amount:.2f} discount")

# exercise 7 

print("\nExercise 7:")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}
for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} remaining")

# exercise 8 

print("\nExercise 8:")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]
regional_sales = {}
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    regional_sales[region] = regional_sales.get(region, 0) + amount
for region in sorted(regional_sales):
    print(f"{region}: ${regional_sales[region]}")