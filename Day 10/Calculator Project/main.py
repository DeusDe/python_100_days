def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2



calculations = {'+':add,'-':subtract,'*':multiply,'/':divide}

u_i = input("Gib was ein")
n1 = int(input("Zahl 1"))
n2 = int(input("Zahl 2"))
erg = 0

if u_i in calculations:
    erg = calculations[u_i](n1, n2)


print(erg)