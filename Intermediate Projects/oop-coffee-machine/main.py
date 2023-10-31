from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"what would you like? ({options})")

    try:
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            enough_resources = coffee_maker.is_resource_sufficient(drink)
            payment_successful = money_machine.make_payment(drink.cost)
            if enough_resources and payment_successful:
                coffee_maker.make_coffee(drink)
    except AttributeError:
        print("Invalid choice. Please select a valid drink, or input 'off', or 'report'.")
