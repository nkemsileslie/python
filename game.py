import random
class NumberGuessingGame:

    def __init__(self):
        ## define the range
        self.Lowest_num = 1
        self.Highest_num = 10
        self.Endgame_max= 0

    # method to generate the random number
    def get_random_number(self):
        return random.randint(self.Lowest_num, self.Highest_num)

    ## game start method
    def start(self):
        ## generating the random number
        random_number = self.get_random_number()

        print(
            f"To begin guess the randomly generated number between {self.Lowest_num} to {self.Highest_num}")

        ## heart of the game
        Starting_Score= 5
        while True:
            user_number = int(input("Enter the guessed number: "))
            if user_number == random_number:
                print(
                    f"-> Hurray! You got it in  your Starting_Scoreis {Starting_Score+ 1} . {'' if Starting_Score> 1 else ''}!")
                break
            elif user_number > random_number:
                print(" Your number is less than the random number -1 from your guess")
            else:
                print("Your number is greater than the random number +1 to your guess")
            Starting_Score-= 1

            if Starting_Score== self.Endgame_max:
                print(" ")
                print(" ")
                print("Sorry! You lost the game.")
                print(f"Your Score is {Starting_Score}")
                break
                
## instantiating and starting the game
numberGuessingGame = NumberGuessingGame()
numberGuessingGame.start()