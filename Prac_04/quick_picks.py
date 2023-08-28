import random

# CONSTANTS
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_QUICK_PICK = 6

def main():
    num_quick_picks = int(input("How many quick picks? "))
    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)

def generate_quick_pick():
    """Generate a single quick pick with unique random numbers."""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_QUICK_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in quick_pick:
            quick_pick.append(num)
    return sorted(quick_pick)

def print_quick_pick(quick_pick):
    """Print the quick pick in a neat format."""
    for num in quick_pick:
        print(f"{num:2}", end=' ')
    print()

if __name__ == "__main__":
    main()
