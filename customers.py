
# module 11 lab 

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