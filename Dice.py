import random


def main():
    min = 1
    max = 6
    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        print("Rolling the die...")
        print("The values are....")
        print("Die 1 rolled:" + str(random.randint(min, max)))
        print("Die 2 rolled:" + str(random.randint(min, max)))

        roll_again = input("Roll the dices again?")



main()
