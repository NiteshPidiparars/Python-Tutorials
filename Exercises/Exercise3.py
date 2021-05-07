# You have to build a "Number Guessing Game," in which a winning number is set to some integer value.
# The Program should take input from the user, and if the entered number is less than the winning number,
# a message should display that the number is smaller and vice versa.

# Instructions:
# 1. You are free to use anything we've studied till now.
# 2. The number of guesses should be limited, i.e (5 or 9).
# 3. Print the number of guesses left.
# 4. Print the number of guesses he took to win the game.
# 5. “Game Over” message should display if the number of guesses becomes equal to 0.


# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n = 18
number_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses <= 9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 18:
        print("you enter less number please input greater number.\n")
    elif guess_number > 18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses, "no.of guesses he took to finish.")
        break
    print(9-number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses > 9):
    print("Game Over")
