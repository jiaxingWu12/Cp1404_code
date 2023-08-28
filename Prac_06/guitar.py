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
