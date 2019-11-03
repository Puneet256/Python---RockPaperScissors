from random import randint

choices = {
    1:"rock",
    2:"paper",
    3:"scissors"
}

comp_choice = randint(1,3)

print("++++ Welcome To Rock Paper Scissors+++\nWhat's your choice? Enter\n1 for Rock\n2 for Paper\n3 for Scissors")
user_choice = int(input())

print("\nYou Chose: %s\nThe CPU Chose:  %s" % (choices[user_choice], choices[comp_choice]))

if user_choice == 1:
    if comp_choice == 1:
        print("TIE")
    if comp_choice == 2:
        print("CPU Wins")
    if comp_choice == 3:
        print("You Win")

if user_choice == 2:
    if comp_choice == 1:
        print("You Win")
    if comp_choice == 2:
        print("TIE")
    if comp_choice == 3:
        print("CPU Wins")

if user_choice == 3:
    if comp_choice == 1:
        print("CPU Wins")
    if comp_choice == 2:
        print("You Win")
    if comp_choice == 3:
        print("TIE")
