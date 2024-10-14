from art import logo

def add(x_i, y_i):
    return x_i + y_i

def subtract(x_i, y_i):
    return x_i - y_i

def multiply(x_i, y_i):
    return x_i * y_i

def divide(x_i, y_i):
    return x_i / y_i



calculations = {'+':add,'-':subtract,'*':multiply,'/':divide}
x = 0
print(logo)
while True:

    op = input("+,-,*,/ :")
    if x == 0:
        x = int(input("x: "))
    y = int(input("y: "))
    res = 0

    if op in calculations:
        res = calculations[op](x, y)

    print(res)

    choice = input("Do you want to continue using the result as x (y,n)?")
    if choice == 'y':
        x = res
    elif choice == 'n':
        x = 0

