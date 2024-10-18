age = input("How old are you?")
try:
    age = int(age)
except ValueError:
    print("Please enter an integer")
    exit()
if age >= 18:
    print(f"You can drive at age {age}.")
