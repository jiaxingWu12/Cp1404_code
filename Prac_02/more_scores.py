import random

def determine_result(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 50:
        return "Passable"
    elif score > 90:
        return "Excellent"
    elif score < 50:
        return "Bad"


def generate_random_scores(num_scores):
    scores = []
    for _ in range(num_scores):
        score = random.randint(0, 100)
        scores.append(score)
    return scores


def write_results_to_file(scores):
    with open("results.txt", "w") as file:
        for score in scores:
            result = determine_result(score)
            file.write(f"{score} is {result}\n")


def main():
    num_scores = int(input("Enter the number of scores: "))
    if num_scores <= 0:
        print("Invalid number of scores. Please enter a positive integer.")
        return

    random_scores = generate_random_scores(num_scores)
    write_results_to_file(random_scores)
    print(f"{num_scores} random scores have been written to results.txt")


if __name__ == "__main__":
    main()
