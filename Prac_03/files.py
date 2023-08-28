# Question 1: Writing user's name to "name.txt"
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# Question 2: Reading and printing the name from "name.txt"
with open("name.txt", "r") as file:
    stored_name = file.read().strip()
print(f"Your name is {stored_name}")

# Question 3: Reading first two numbers from "numbers.txt" and adding them
with open("numbers.txt", "r") as file:
    number1 = int(file.readline().strip())
    number2 = int(file.readline().strip())
result = number1 + number2
print(f"The result of adding the first two numbers is {result}")

# Question 4: Reading and printing the total of all numbers in "numbers.txt"
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print(f"The total of all numbers in 'numbers.txt' is {total}")
