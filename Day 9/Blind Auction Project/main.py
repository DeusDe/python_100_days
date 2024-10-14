# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bidders_list = {}
next_bidder = True
def clear_screen():
    print("\n" * 20)

while next_bidder:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    if name in bidders_list:
        print("name already exists")
        continue
    else:
        bidders_list[name] = bid
    if 'y' == input("Would you like to add another bidder? (y/n): "):
        clear_screen()
    else:
        next_bidder = False

highest_bidder = ""
highest_amount = 0
for bidder in bidders_list:
    if bidders_list[bidder] > highest_amount:
        highest_amount = bidders_list[bidder]
        highest_bidder = bidder

print(f'{highest_bidder} has the highest bid amount {highest_amount}')