import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# I feel like the "resources" dict should be a constant and there for all caps.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0,
}

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino): ”
# Check the user’s input to decide what to do next.
# The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

DRINK = input("What would you like? (espresso/latte/cappuccino): ")
TOTAL_COST = 0.0


# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
# For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine.
# Your code should end execution when this happens.


def end_program(DRINK):
    turn_off = "off"
    if DRINK == turn_off:
        sys.exit()


# TODO: 3. Print report
# When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
# Example:
#   Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5


def display_resources(DRINK, TOTAL_COST):
    if DRINK == "report":
        print(
            f"Water: {resources['water']}ml"
        )
        print(
            f"Milk: {resources['milk']}ml"
        )
        print(
            f"Coffee: {resources['coffee']}g"
        )
        print(
            f"Money: ${TOTAL_COST}"
        )
    print(DRINK)


# TODO: 4. Check resources sufficient?
# When the user chooses a drink, the program should check if there are enough resources to make that drink.
# E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
# The same should happen if another resource is depleted, e.g. milk or coffee.


def check_resources():
    water = "water"
    milk = "milk"
    coffee = "coffee"

    if DRINK == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= \
                MENU["espresso"]["ingredients"]["coffee"]:
            return True
        elif resources["water"] <= MENU["espresso"]["ingredients"]["water"]:
            print(f"Sorry there is not enough {water}.")
        elif resources["coffee"] <= MENU["espresso"]["ingredients"]["coffee"]:
            print(f"Sorry there is not enough {coffee}.")
        else:
            return False

    if DRINK == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= \
                MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            return True
        elif resources["water"] <= MENU["latte"]["ingredients"]["water"]:
            print(f"Sorry there is not enough {water}.")
        elif resources["milk"] <= MENU["latte"]["ingredients"]["milk"]:
            print(f"Sorry there is not enough {milk}.")
        elif resources["coffee"] <= MENU["latte"]["ingredients"]["coffee"]:
            print(f"Sorry there is not enough {coffee}.")
        else:
            return False

    if DRINK == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] >= \
                MENU["cappuccino"]["ingredients"]["coffee"] and resources["coffee"] >= \
                MENU["cappuccino"]["ingredients"]["coffee"]:
            return True
        elif resources["water"] <= MENU["cappuccino"]["ingredients"]["water"]:
            print(f"Sorry there is not enough {water}.")
        elif resources["milk"] <= MENU["cappuccino"]["ingredients"]["milk"]:
            print(f"Sorry there is not enough {milk}.")
        elif resources["coffee"] <= MENU["cappuccino"]["ingredients"]["coffee"]:
            print(f"Sorry there is not enough {coffee}.")
        else:
            return False


# TODO: 5. Process coins
# If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
# Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


def process_coins(TOTAL_COST):
    if check_resources():
        print("Please insert coins.")
        TOTAL_COST += 0.25 * int(input("how many quarters?: "))
        TOTAL_COST += 0.1 * int(input("how many dimes?: "))
        TOTAL_COST += 0.05 * int(input("how many nickels?: "))
        TOTAL_COST += 0.01 * int(input("how many pennies?: "))
        return TOTAL_COST


# TODO: 6. Check transaction successful?
# Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.
# But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered.
# Example:
#   Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5
# If the user has inserted too much money, the machine should offer change.
# Example:
#   “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.


def check_transaction(DRINK, TOTAL_COST):
    espresso_cost = MENU["espresso"]["cost"]
    latte_cost = MENU["latte"]["cost"]
    cappuccino_cost = MENU["cappuccino"]["cost"]
    resource_money = float(resources["Money"])

    if DRINK == "espresso":
        if process_coins(TOTAL_COST) <= espresso_cost:
            print("Sorry that's not enough money. Money refunded.")
            new_drink = input("What would you like? (espresso/latte/cappuccino):† ")
            return new_drink
        else:

    if DRINK == "latte":
        if process_coins(TOTAL_COST) <= latte_cost:
            print("Sorry that's not enough money. Money refunded.")
            new_drink = input("What would you like? (espresso/latte/cappuccino): ")
            return new_drink
        else:

    if DRINK == "cappuccino":
        if process_coins(TOTAL_COST) <= cappuccino_cost:
            print("Sorry that's not enough money. Money refunded.")
            new_drink = input("What would you like? (espresso/latte/cappuccino): ")
            return new_drink
        else:

# TODO: 7. Make Coffee
# If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.

# Example (Report before purchasing latte):
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0

# Example (Report after purchasing latte):
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.














