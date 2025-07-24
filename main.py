from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from task import is_resource_sufficient, process_coins

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
