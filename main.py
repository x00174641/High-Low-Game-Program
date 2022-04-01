import random

min_range = 1 # minimum value
max_range = 10 # maximum value
total_guesses =  0  # total user guesses
total_allowed_guess = 5 # total allowed guesses per game
def menu(): # menu function
    print("Type [1] - Start game:")
    print("Type [2] - To end the program")

def start_game(): # start number guessing game function
    global total_guesses 
    answer = random.randint(min_range,max_range) # generates a random number from our min and max range stated above
    user_guess = int(input("Your Guess: ")) # user inputs their guess in the command line
    while True: # loop
        # if the guess is equal to the correct number generated then print a congratulations message
        if user_guess == answer:
            print("Congratulations, You guessed the right number: " , answer , "\nYou guessed ", total_guesses , " time(s). ")
            break
        # if the total guess is equal to the total allowed guess then print, loose message then stop the program.
        elif total_guesses == total_allowed_guess - 1:
            print("Your guess's has ran out unfortunately, Please re-run the program!\nThe Answer was:" , answer)
            break
        # if the users guess is lower than the randomly generated then print guess higher message and adds 1 to the users total guesses.
        elif user_guess < answer:
            total_guesses += 1
            print("Your guess is to low! Try guessing higher!\nYou have ", total_allowed_guess - total_guesses  , " guesses left!")
            user_guess = int(input("Guess Again: "))
            print()
        # if the users guess is higher than the randomly generated then print guess lower message and adds 1 to the users total guesses.
        else:
            total_guesses += 1
            print("Your guess is to high! Try guessing lower!\nYou have ", total_allowed_guess  - total_guesses , " guesses left!")
            user_guess = int(input("Guess Again: "))
            print()
# calls the menu function
menu()
# user enters 1 or 2 options
menu_option = int(input("Enter your menu option: "))
# loop
while menu_option != 2:
    # if user types 1 then the start_game function is called.
    if menu_option == 1:
        start_game()
        break
    else:
        # invalid option supplied by the user
        menu_option = int(input("Invalid menu option: Enter menu option 1 or 2: "))



