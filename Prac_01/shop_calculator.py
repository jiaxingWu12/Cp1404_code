numbers_of_item = int(input("How many items? "))
if numbers_of_item < 0:
    print("invalid number of items, pleas try again")


for i in range(1, numbers_of_item+1):
    print("what is the price for the items")
    price = float(input("$"))
    total_price = total_price + price

if total_price > 100:
    price * 0.9

print("Total price of", "numbers_of_item", "items is ${:2f}". format(total_price) )





