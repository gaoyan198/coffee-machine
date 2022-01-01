from static import MENU, resources

off = False
moneyInMachine = 0

while not off:
    customerInput = input("What would you like to have? (espresso/latte/cappuccino): ")
    if customerInput == "espresso":
        notEnoughWater = MENU["espresso"]["ingredients"]["water"] > resources["water"]
        notEnoughCoffee = MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]
        if notEnoughWater:
            print("Sorry, there is not enough water")
        elif notEnoughCoffee:
            print("Sorry, there is not enough coffee")
        else:
            numOfTenCentCoins = int(input("How many 10c coins put in: "))
            numOfTwentyCentCoins = int(input("How many 20c coins put in: "))
            numOfFiftyCentCoins = int(input("How many 50c coins put in: "))
            numOfDollarCoins = int(input("How many $1 coins put in?"))

            amountInserted = numOfTenCentCoins * 0.1 + numOfTwentyCentCoins * 0.2 + numOfFiftyCentCoins * 0.5 + numOfDollarCoins
            espressoCost = MENU["espresso"]["cost"]

            if amountInserted < espressoCost:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                moneyInMachine += espressoCost
                resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]

                if amountInserted > espressoCost:
                    change = amountInserted - espressoCost
                    change = str(round(change, 2))
                    print("Here is ${} dollars in change".format(change))
                
                print("Here is you espresso☕️. Enjoy!")

    elif customerInput == "latte":
        notEnoughWater = MENU["latte"]["ingredients"]["water"] > resources["water"]
        notEnoughMilk = MENU["latte"]["ingredients"]["milk"] > resources["milk"]
        notEnoughCoffee = MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]

        if notEnoughWater:
            print("Sorry, there is not enough water")
        elif notEnoughMilk:
            print("Sorry, there is not enough milk")
        elif notEnoughCoffee:
            print("Sorry, there is not enough coffee")
        else:
            numOfTenCentCoins = int(input("How many 10c coins put in: "))
            numOfTwentyCentCoins = int(input("How many 20c coins put in: "))
            numOfFiftyCentCoins = int(input("How many 50c coins put in: "))
            numOfDollarCoins = int(input("How many $1 coins put in: "))

            amountInserted = numOfTenCentCoins * 0.1 + numOfTwentyCentCoins * 0.2 + numOfFiftyCentCoins * 0.5 + numOfDollarCoins
            latteCost = MENU["latte"]["cost"]

            if amountInserted < latteCost:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                moneyInMachine += latteCost
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]

                if amountInserted > latteCost:
                    change = amountInserted - latteCost
                    change = str(round(change, 2))
                    print("Here is ${} dollars in change".format(change))

                print("Here is you latte☕️. Enjoy!")

    elif customerInput == "cappuccino":
        notEnoughWater = MENU["cappuccino"]["ingredients"]["water"] > resources["water"]
        notEnoughMilk = MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]
        notEnoughCoffee = MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]

        if notEnoughWater:
            print("Sorry, there is not enough water")
        elif notEnoughMilk:
            print("Sorry, there is not enough milk")
        elif notEnoughCoffee:
            print("Sorry, there is not enough coffee")
        else:
            numOfTenCentCoins = int(input("How many 10c coins put in: "))
            numOfTwentyCentCoins = int(input("How many 20c coins put in: "))
            numOfFiftyCentCoins = int(input("How many 50c coins put in: "))
            numOfDollarCoins = int(input("How many $1 coins put in: "))

            amountInserted = numOfTenCentCoins * 0.1 + numOfTwentyCentCoins * 0.2 + numOfFiftyCentCoins * 0.5 + numOfDollarCoins
            cappuccinoCost = MENU["cappuccino"]["cost"]

            if amountInserted < cappuccinoCost:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                moneyInMachine += cappuccinoCost
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]

                if amountInserted > cappuccinoCost:
                    change = amountInserted - cappuccinoCost
                    change = str(round(change, 2))
                    print("Here is ${} dollars in change".format(change))

                print("Here is you cappuccino☕️. Enjoy!")

    elif customerInput == "report":
        print("Water: " + str(resources["water"]) + "ml")
        print("Milk: " + str(resources["milk"]) + "ml")
        print("Coffee: " + str(resources["coffee"]) + "g")
        print("Money: $" + str(moneyInMachine))
    elif customerInput == "off":
        print("Shutting down machine.")
        off = True
    else:
        "Invalid input. Please try again."
