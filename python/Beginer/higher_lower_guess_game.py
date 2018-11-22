""" A sample game to guess a number between 1 and 100 """
import random

rules = """
=========================================================================================================
=                   Hi, Below are the rules of the game !!!!                                            =
= 1. At the Start of the game, Program will take a random number between 1 and 100.                     =
= 2. Then program will ask player to guess the number. You have to input the number you have guessed.   =
= 3. Program will then show you the results, if your guess is higher or lower.                          =
=========================================================================================================
"""
message = {'success': 'Congratulations !!!, You have guess it right',
           'high': 'You have guessed a higher value.',
           'low': 'Oops !! You have guess a lower value'}

end_credits = """ Thanks for Playing !!! """

# Display the rules
print rules

play = input("Press 1 to Play the game\n")
# Continue playing till user gives the input
while play == 1:
    num = random.randint(1, 100)
    guess = input("\tEnter the number you have guessed : \t")

    msg = "\tProgram's Number : {} ,".format(num)
    if guess < num:
        print msg + message['low']
    elif guess > num:
        print msg + message['high']
    else:
        print msg + message['success']

    # Check with User if he wants to play again
    play = input("\n\tPress 1 to Play again.\t")

print(end_credits)
