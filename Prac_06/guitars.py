class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        current_year = 2023  # Update this as needed
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

# Example usage:

# Create a Guitar instance
guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

# Print the guitar details
print(guitar)

# Get the age of the guitar
age = guitar.get_age()
print(f"Age of the guitar: {age} years")

# Check if the guitar is vintage
is_vintage = guitar.is_vintage()
print(f"Is the guitar vintage? {'Yes' if is_vintage else 'No'}")

# Testing the methods
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 800.00)

print(f"{guitar1.name} get_age() - Expected 101. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected 10. Got {guitar2.get_age()}")
print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")

# Playing the Guitars
print("My guitars!")
guitars = []

# Uncomment these lines and comment the input lines for testing
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

while True:
    name = input("Name: ")
    if name == "":
        break
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.\n")

print("\nThese are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
