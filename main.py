from menu import MENU, COINS
from sys import exit

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def display_menu():
    menu = ""
    for coffee in MENU:
        coffee_price = MENU[coffee]["cost"]
        if menu:
            menu += "/"
        menu += f"{coffee} (${coffee_price/100:.2f})"
    return menu


# TODO 2: Implement off switch that finishes code execution
def check_killswitch(user_input):
    """\
    Attached to user input validation function.
    Exits the program if "OFF" is input at any point where input is required.
    """
    if user_input.upper() == "OFF":
        exit()


def validate_input(user_input, options):
    """\
    :param user_input: Input provided by the user at any point where input is required.
    :param options: Iterable of options available for each given input.
    :return: True if input provided by the user is found in the available options.
    """
    check_killswitch(user_input)
    return True if user_input in options else False


def print_report():
    """\
    Prints available resources for making coffee as well as money currently in the machine.
    """
    for resource in resources:
        print(f"{resource.capitalize()}:\t{resources[resource]}")
    print(f"Money:\t${money/100:.2f}")


def check_ingredients(target_coffee):
    """\
    :param target_coffee: Coffee type selected by user
    :return: True/False depending on whether there are resources to prepare given coffee type
    """
    coffee_ingredients = MENU[target_coffee]["ingredients"]
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, we're missing {ingredient} at the moment. Try again later!")
            return False
    return True


def update_ingredients(target_coffee):
    """\
    :param target_coffee: Coffee type selected by the user.
    :return: Updates the ingredient list by removing ingredients of coffee chosen by the user.
    """
    coffee_ingredients = MENU[target_coffee]["ingredients"]
    print(coffee_ingredients)
    for ingredient in coffee_ingredients:
        resources[ingredient] -= coffee_ingredients[ingredient]


def get_money():
    """\
    :return: Total value of coins inserted into the machine.
    Asks for coins with different values (pennies, nickels, dimes, and quarters).
    """
    total_inserted = 0
    # TODO 5.1: Ask for each coin separately
    for coin in COINS:
        raw_coin_number = input(f"How many {coin}?\t")
        coin_number = int(raw_coin_number)
        total_inserted += coin_number * COINS[coin]
    return total_inserted


def check_money(coffee, inserted_money):
    """\
    :param coffee: Coffee selected by the user
    :param inserted_money: Coins currently being inserted into the coffee machine.
    :param machine_money: Sum of coins currently in the machine, updated in the transaction.
    :return: True if inserted coins match or exceed price of coffee, otherwise False.
    """
    coffee_price = MENU[coffee]["cost"]
    if inserted_money == coffee_price:
        print("All good!")
        return True
    elif inserted_money > coffee_price:
        # TODO 5.2: Give change if paid too much
        print(f"All good! Here's your change: ${(inserted_money - coffee_price)/100:.2f}")
        return True
    else:
        print(f"Sorry, that's not enough money. Returning: ${inserted_money/100:.2f}")
        return False

if __name__ == "__main__":
    # TODO 1: Ask user what kind of coffee they would like (espresso/latte/cappucino)
    brewing = True
    while brewing:
        print("Hello and welcome!")
        # TODO 3: Print report showing resource values
        print_report()

        coffee_selection = ""
        coffee_validator = False
        while not coffee_validator:
            coffee_selection = input(f"What kind of coffee would you like? {display_menu()}\n").lower()
            coffee_validator = validate_input(coffee_selection, MENU)


        # TODO 4: Check if there are sufficient resources to make the given coffee
        if not check_ingredients(coffee_selection):
            break

        # TODO 5: Process coins and check if there are enough to make the given coffee
        cash = get_money()
        sufficient_cash = check_money(coffee_selection, cash)
        if not sufficient_cash:
            break

        update_ingredients(coffee_selection)
        money += MENU[coffee_selection]["cost"]
        print("Making coffee…")

        # TODO 6: Make the coffee, update resources and print report; give the user a goodbye message
        print(f"Here's your {coffee_selection}, have a great day!")
