from asyncore import write
from distutils.command.check import check
from idlelib.debugger_r import restart_subprocess_debugger

MENU = {
    1:{
        "name":"espresso",
        "cost":1.5,
        "ingredients":{
            "water": 50,
            "coffee":18,
            "milk":0,
        }
    },
    2: {
        "name": "latte",
        "cost": 2.5,
        "ingredients": {
            "water": 200,
            "coffee": 150,
            "milk": 24,
        }
    },
    3: {
        "name": "cappuccino",
        "cost": 3,
        "ingredients": {
            "water": 250,
            "coffee": 100,
            "milk": 24,
        }
    }
}

class RessourceManager:
    def __init__(self, max_res,min_res,res_name, init_res):
        self.max_res = max_res
        self.min_res = min_res
        self.res_name = res_name
        self.res = init_res

    def get_res(self):
        return self.res

    def set_res(self,res):
        if res < self.min_res:
            return 0
        self.res = res

    def get_name(self):
        return self.res_name

    def set_name(self,name):
        self.res_name = name

    def is_reducable(self,red_amount):
        return self.res - red_amount >= self.min_res

    def is_increasable(self,inc_amount):
        return self.res + inc_amount <= self.max_res

    def increase(self,inc_amount):
        self.set_res(self.res + inc_amount)

    def reduce(self,red_amount):
        if self.is_reducable(red_amount):
            self.set_res(self.res-red_amount)

class MoneyManager(RessourceManager):
    def __init__(self):
        super().__init__(2000,0,'money',0)

    def return_change(self, change):
        quarters = int(change // 0.25)
        change -= quarters * 0.25

        dimes = int(change // 0.10)
        change -= dimes * 0.10

        nickels = int(change // 0.05)
        change -= nickels * 0.05

        pennies = int(round(change / 0.01))

        # Ergebnis ausgeben
        print(f"Return {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.")

    def insert_coins(self):
        quarter = int(input('Insert quarters:'))
        dime = int(input('Insert dimes:'))
        nickel = int(input('Insert nickels:'))
        pennies = int(input('Insert pennies:'))

        inserted_value = quarter * 0.25 + dime * 0.10 + nickel * 0.05 + pennies * 0.01

        return inserted_value

    def pay(self,price):
        inserted = self.insert_coins()

        if not inserted >= price:
            print("Not enough money")
            return False

        change = inserted - price
        self.increase(price)
        self.return_change(change)
        return True

class coffee_machine:
    def __init__(self,water,milk,coffee):
        self.ressources = {'water':RessourceManager(1000,0,'water',water),
                      'milk':RessourceManager(1000, 0, 'milk', milk),
                      'coffee':RessourceManager(1000, 0, 'coffee', coffee),
                      }
        self.money = MoneyManager()
        self.menu = MENU

    def menu_string(self):
        mstr = ""
        for order in self.menu:
            mstr += f"{self.menu[order]['name']} for {self.menu[order]['cost']}$\n"
        return mstr

    def ressources_report(self):
        for ressource in self.ressources:
            print(f"{ressource}: {self.ressources[ressource].get_res()}")
        print(f"money: {self.money.get_res()}€\n")

    def ressources_avaiable(self,ingredients):
        ret_val = True
        for ingredient in ingredients:
            if ingredient not in self.ressources:
                print("ingredient not in ressources")
                ret_val = False

            elif not self.ressources[ingredient].is_reducable(ingredients[ingredient]):
                print(f"not enough {ingredient} currently:{self.ressources[ingredient].get_res()} needed: {ingredients[ingredient]}")
                ret_val = False
        return ret_val

    def ressources_reduce(self,ingredients):
        for ingredient in ingredients:
            self.ressources[ingredient].reduce(ingredients[ingredient])


    def make_coffee(self,order):
        if order not in self.menu:
            print("Coffe is not in menu\n")
            return

        ingredients = self.menu[order]['ingredients']
        price = self.menu[order]['cost']

        if not self.ressources_avaiable(ingredients):
            return

        if not self.money.pay(price):
            return

        self.ressources_reduce(ingredients)

        print(f'Here is your {self.menu[order]["name"]}. Enjoy')

machine = coffee_machine(200,200,300)

while True:
    order = input(f"Which coffee would you like to order?\n{machine.menu_string()}")
    if order == "off":
        exit()
    elif order == "report":
        machine.ressources_report()
    else:
        machine.make_coffee(int(order))