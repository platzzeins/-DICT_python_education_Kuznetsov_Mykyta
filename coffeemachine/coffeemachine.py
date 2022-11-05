class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 75
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.status = "Waiting"

    def coffee_check(self, water_need, beans_need, milk_need, price):
        if (self.water >= water_need) and (self.beans >= beans_need) \
                and (self.milk >= milk_need) and (self.cups >= 1):
            print("I have enough resources, making you a coffee!")
            self.water -= water_need
            self.beans -= beans_need
            self.milk -= milk_need
            self.money += price
        else:
            if self.water <= water_need:
                print("Sorry, not enough water")
            elif self.beans <= beans_need:
                print("Sorry, not enough beans")
            elif self.milk <= milk_need:
                print("Sorry, not enough milk")
            elif self.cups <= 1:
                print("Sorry, not enough cups")

    def espresso(self):
        water_need = 250
        beans_need = 16
        milk_need = 0
        price = 4
        self.coffee_check(water_need, beans_need, milk_need, price)

    def latte(self):
        water_need = 350
        milk_need = 75
        beans_need = 20
        price = 7
        self.coffee_check(water_need, beans_need, milk_need, price)

    def cappuccino(self):
        water_need = 200
        milk_need = 100
        beans_need = 12
        price = 6
        self.coffee_check(water_need, beans_need, milk_need, price)

    def print_current(self):
        print(f"""\nThe coffee machine has:
    {self.water} of water
    {self.milk} of milk
    {self.beans} of coffee beans
    {self.cups} of disposable cups
    {self.money} of money""")

    def all_staff(self, user_action):
        if user_action == "buy":
            choose = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
            if choose == 1:
                self.espresso()
            elif choose == 2:
                self.latte()
            elif choose == 3:
                self.cappuccino()
            else:
                print("You have typed incorrect value")
            self.status = "Bought coffee"
        elif user_action == "fill":
            try:
                self.water += int(input("Write how many ml of water you want to add:\n>"))
                self.milk += int(input("Write how many ml of milk you want to add:\n>"))
                self.beans += int(input("Write how many grams of coffee beans you want to add:\n>"))
                self.cups += int(input("Write how many disposable coffee cups you want to add:\n>"))
            except ValueError:
                print("Please, enter only numbers")
            self.status = "Fill status"
        elif user_action == "take":
            print(f"I gave you {self.money}")
            self.money = 0
            self.status = "Gave money"
        elif user_action == "remaining":
            self.print_current()
            self.status = "Remaining status"
        elif user_action == "exit":
            self.status = "Exit"
        else:
            print("You have typed incorrect value")


def main():
    coffeemachine = CoffeeMachine()
    while True:
        user_action = (input("Write action (buy, fill, take, remaining, exit):\n>")).lower()
        coffeemachine.all_staff(user_action)
        if user_action == "exit":
            break


if __name__ == "__main__":
    main()

# DeFakto
