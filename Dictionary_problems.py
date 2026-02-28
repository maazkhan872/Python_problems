# How to Create a dictionary:
empty = {}
student = dict(name="Ali", age=22)

# Creating Dictionary
user = {
    "name": "Maaz",
    "age": 25,
    "role": "AI Engineer",
    "salary": 150000
}
print(user)

# Accessing Values
print(user["name"])  # Maaz

print(user.get("salary"))        # None
print(user.get("salary", 0))     # default value

# Adding / Updating
user["salary"] = 100000
user["age"] = 26

user.pop("role")
del user["age"]

# keys()
print(user.keys())

# values()
print(user.values())

# items()
for key, value in user.items():
    print(key, value)

user.update({"city": "Karachi"})

# Dictionary Comprehension
squares = {x: x*x for x in range(5)}
print(squares)