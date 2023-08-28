def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
def main():
    # Get Celsius input from the user
    celsius_input = float(input("Enter temperature in Celsius: "))

    # Convert Celsius to Fahrenheit using the function
    fahrenheit_output = celsius_to_fahrenheit(celsius_input)
    print(f"{celsius_input} Celsius is equal to {fahrenheit_output:.2f} Fahrenheit.")

    # Get Fahrenheit input from the user
    fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius using the function
    celsius_output = fahrenheit_to_celsius(fahrenheit_input)
    print(f"{fahrenheit_input} Fahrenheit is equal to {celsius_output:.2f} Celsius.")


if __name__ == "__main__":
    main()
