import random

total_score = 0
rolls = 3

aside = [None,None,None]

spare_one = aside[0]
spare_two = aside[1]
spare_three = aside[2]

usedOptions = []

optionList = {
              1: "Ones",
              2: "Twos",
              3: "Fours",
              4: "Fives",
              5: "Sixes",
              6: "Full House",
              7: "Four-Of-A-Kind",
              8: "Little Straight",
              9: "Big Straight",
              10: "Choice",
              11: "Yacht"
              }


def showoptions():
    options = [
        "Name:                    Description:                                 Score:",
        "======================================================================================================= ",
        "|(1) Ones:              | Any combination                          | The sum of dice with the 1 face |",
        "|(2) Twos:              | Any combination                           | The sum of dice with the 2 face |",
        "|(3) Fours:             | Any combination                           | The sum of dice with the 4 face |",
        "|(4) Fives:             | Any combination                           | The sum of dice with the 5 face |",
        "|(5) Sixes:             | Any combination                           | The sum of dice with the 6 face |",
        "|(6) Full House:        | Three of one same face and two of another | Sum of all dice                 |",
        "|(7) Four-Of-A-Kind:    | At least four dice showing the same face  | Sum of those four dice          |",
        "|(8) Little Straight:   | 1-2-3-4-5                                 | 30                              |",
        "|(9) Big Straight:      | 2-3-4-5-6                                 | 30                              |",
        "|(10) Choice:           | Any combination                           | Sum of all dice                 |",
        "|(11) Yacht:            | All five dice showing the same face       | 50                              |",
        "======================================================================================================="
    ]

    for i in options:
        print(i)


def diceroll():
    dicelist = []

    min = 1
    max = 6

    for i in range(5):
        roll = random.randint(min, max)
        dicelist.append(roll)
    
    return dicelist


def taketurn(dicelist, total_score):
    dice = dicelist
    score = 0
    user_option = ""
    
    input("Press enter to see the move set!\n")
    showoptions()
    print(f"You rolled {dice}")

    while True:
        try:
            user_option = int(input("Please Select Your Option!"))
            if user_option not in range(11):
                print("Invalid Option! Please Try Again!")
            else:
                break
        except ValueError:
            print("That was not a number, Please input a number")
            continue

    if user_option in usedOptions:
        name = optionList.get(user_option)
        print(f"You have chosen {name} Before, Please select a different move!")
        taketurn(dicelist, total_score)
    else:
        pass

    if user_option == 1:
        ones = []
        for i in dice:
            if i == 1:
                ones.append(1)

        if len(ones) == 0:
            print("You had no ones in your dice roll set\nScore this round is 0")
            usedOptions.append(user_option)

        else:
            score = len(ones) * 1
            total_score = total_score + score
            print(
                f"You had {len(ones)} ones in your dice roll set\nScore this round is {score}\nTotal Score: {total_score}")
            usedOptions.append(user_option)


    elif user_option == 2:
        twos = []
        for i in dice:
            if i == 2:
                twos.append(2)

        if len(twos) == 0:
            print(f"You had no twos in your dice rolls set\nScore this round is 0\nTotal Score: {total_score}")
            usedOptions.append(user_option)

        else:
            score = len(twos) * 1
            total_score = total_score + score
            print(
                f"You had {len(twos)} twos in your dice roll set\nScore this round is {score}\nTotal Score: {total_score}")
            usedOptions.append(user_option)

    elif user_option == 3:
        fours = []
        for i in dice:
            if i == 4:
                fours.append(4)

        if len(fours) == 0:
            print(f"You had no fours in your dice rolls set\nScore this round is 0\nTotal Score: {total_score}")
            usedOptions.append(user_option)

        else:
            score = len(fours) * 1
            total_score = total_score + score
            print(
                f"You had {len(fours)} fours in your dice roll set\nScore this round is {score}\nTotal Score: {total_score}")
            usedOptions.append(user_option)


    elif user_option == 4:
        fives = []
        for i in dice:
            if i == 5:
                fives.append(5)

        if len(fives) == 0:
            print(f"You had no fives in your dice rolls set\nScore this round is 0\nTotal Score: {total_score}")
            usedOptions.append(user_option)

        else:
            score = len(fives) * 1
            total_score = total_score + score
            print(
                f"You had {len(fives)} fives in your dice roll set\nScore this round is {score}\nTotal Score: {total_score}")
            usedOptions.append(user_option)

    elif user_option == 5:
        sixes = []
        for i in dice:

            if i == 6:
                sixes.append(6)

        if len(sixes) == 0:
            print(f"You had no sixes in your dice rolls set\nScore this round is 0\nTotal Score: {total_score}")
            usedOptions.append(user_option)

        else:
            score = len(sixes) * 1
            total_score = total_score + score
            print(
                f"You had {len(sixes)} sixes in your dice roll set\nScore this round is {score}\nTotal Score: {total_score}")
            usedOptions.append(user_option)

    elif user_option == 6:

        dice = sorted(dice)
        print(dice)

        result = False

        if dice[0] == dice[1] and dice[0] == dice[2]:
            if dice[3] == dice[4]:
                result = True
        elif dice[0] == dice[1]:
            if dice[2] == dice[3] and dice[2] == dice[4]:
                result = True
        else:
            pass

        if result:
            score = sum(dice)
            total_score = total_score + score
            print(f"You rolled a Full House!\nScore this round is {score}\nTotal Score: {total_score}")
            usedOptions.append(user_option)
        else:
            print(f"You did not roll a Full house!\nScore this round is {score}\nTotal Score: {total_score}")

    elif user_option == 7:

        result = dice.count(dice[0]) == 4
        if not result:
            result = dice.count(dice[1]) == 4
        else:
            result = result

        if result:
            score = dice[0] * 4
            print(f"You rolled four of the same dice\nScore this round is {score}\nTotal Score: {total_score}")

        else:
            print(f"You did not roll four of the same dice\nScore this round is {score}\nTotal Score: {total_score}")



    elif user_option == 8:
        list = [1, 2, 3, 4, 5]

        result = dice == list

        if result:
            score = 30
            total_score = total_score + score
            print(f"You rolled 1-2-3-4-5! Score this round is {score}\nTotal Score: {total_score}")
            usedOptions.append(user_option)
        else:
            print(f"You did not roll 1-2-3-4-5 Score this round is 0\nTotal Score: {total_score}")


    elif user_option == 9:
        list = [2, 3, 4, 5, 6]

        result = dice == list

        if result:
            score = 30
            total_score = total_score + score
            print(f"You rolled 2-3-4-5-6 Score this round is {score}\nTotal Score: {total_score}")
        else:
            print(f"You did not roll 2-3-4-5-6 Score this round is 0\nTotal Score: {total_score}")

    elif user_option == 10:
        score = sum(dice)
        total_score = total_score + score
        print(f"You rolled {str(dice)} Score this round is {score}\nTotal Score: {total_score}")


    elif user_option == 11:
        result = True
        first_element = dice[0]
        for num in dice:
            if first_element != num:
                result = False
                print(f"Your dice rolls are not all equal!\nScore this round is 0\nTotal Score:{total_score}")
            else:
                result = True
            if result:
                score = 50
                total_score = total_score + score
                print(f"All your dice rolls are the same!\nScore this round is {score}\nTotal Score:{total_score}")


    else:
        print("[!] Something went wrong!")


def reroll(dice):

    print("====================")
    print(f"Rolls left: {rolls}")
    print("====================")
    print(f""
          f"\nStored Dice One: [{spare_one}]"
          f"\nStored Dice Two: [{spare_two}]"
          f"\nStored Dice Three: [{spare_three}]"
          f"\n")
    print("====================")


    while True:
        try:
            choice = int(input("Please Select an option!"
                             "\n(1) Re roll a dice"
                             "\n(2) Set aside a dice"
                             "\n(3) Select a stored dice"))

            if choice not in range(3):
                print("Invalid Choice, Try again!")
                continue
            else
                break

        except ValueError:
            print("That was not a number! Please try again")
            continue

        except Exception as err:
            print(f"Something went wrong! >>> {err}")

    if choice == 1:
        print(f"You rolled {dice}")
        selection = int(input("Please select the dice number you would like to re-roll"))






def play():
    print("Welcome to the Yacht game! The aim of the game is to roll sets of 5 dice in order to score points in "
          "accordance with the 12 available moves, each move may only be used once so pick carefully")
    print("")
    print("You may re-roll any dice up to 3 times! You may also set aside dice and re-roll. These set aside dice"
          "may be accessed later one!")

    input("Press ENTER to roll the dice!")




    print("Rolling the first set of dice...")
    dice = diceroll()
    print(f"You rolled {dice}")

    while True:
        try:
            choice = int(input("Would you like to re-roll, set aside or access set aside dice?"
                           "\n(1) >>> YES"
                           "\n(2) >>> NO\n"))

            if choice not in range(3):
                print("Invalid Choice! Please try again!")
                continue

            elif choice == 1:
                reroll(dice)
                break

            elif choice == 2:
                taketurn(dice,total_score)
                break


        except ValueError:
            print("That was not a number! Try again!")
            continue

        except Exception as err:
            print(f"Something Went Wrong! >>> {err}")



if __name__ == "__main__":
    play()
