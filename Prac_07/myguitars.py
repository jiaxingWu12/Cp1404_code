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

from guitar import Guitar

def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            year = int(year)
            cost = float(cost)
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars

def display_guitars(guitars):
    for i, guitar in enumerate(guitars, start=1):
        print(f"Guitar {i}: {guitar}")

def add_guitar(guitars):
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year the guitar was made: "))
    cost = float(input("Enter the cost of the guitar: "))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)

def save_guitars(filename, guitars):
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

def main():
    guitars = load_guitars("guitars.csv")
    guitars.sort(key=lambda x: x.year)  # Sort by year (oldest to newest)
    display_guitars(guitars)

    add_guitar(guitars)
    save_guitars("guitars.csv", guitars)

if __name__ == "__main__":
    main()
