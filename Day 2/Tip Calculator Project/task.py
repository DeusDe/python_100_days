print("Welcome to the tip calculator!")
bill = 150#float(input("What was the total bill? $"))
tip = 12#int(input("What percentage tip would you like to give? 10 12 15 "))
people = 5#int(input("How many people to split the bill? "))

tip_result = round( ( bill / people ) * (tip/100+1) ,2)

print(f'${tip_result}')