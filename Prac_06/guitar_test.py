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


# Testing
def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 800.00)

    print(f"{guitar1} get_age() - Expected 101. Got {guitar1.get_age()}")
    print(f"{guitar2} get_age() - Expected 10. Got {guitar2.get_age()}")

    print(f"{guitar1} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2} is_vintage() - Expected False. Got {guitar2.is_vintage()}")

if __name__ == "__main__":
    main()

