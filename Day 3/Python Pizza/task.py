print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25

if extra_cheese == "Y":
    price += 1


if pepperoni == "Y" and size == "S":
    price += 2
elif pepperoni == "Y":
    price += 3

print(f'Your final bill is: ${price}.')