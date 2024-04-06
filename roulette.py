# Roulette game

import joblib
from random import randint
from time import sleep
from typing import Literal

class Roulette:

    # initialize the roulette object
    def __init__(self, initial_fund: int, numbers_path='data/numbers.joblib'):
        # initialize attributes
        self.result = None
        self.numbers = joblib.load(numbers_path)
        self.last_fund = initial_fund
        self.fund = initial_fund

    # simulate spinning the roulette wheel
    def __spin(self):
        self.win_position = randint(0, len(self.numbers)-1) # select a random position
        self.result = self.numbers[self.win_position] # determine the winning number

        # show a spin animation
        spin = self.numbers*3 + self.numbers[:self.win_position+1]

        for number in spin:
            print(f'{number:<6}', end='\r')
            sleep(0.12) # speed that the numbers change

        print(f'Winning number is {self.result}')
        print('='*50, end='\n\n')

    # place a bet on a specific number
    def bet_on_number(self, number:int, amount: int, appelativ='Gentleman'):
        # check if the bet amount exceeds the available funds
        if amount > self.fund:
            print("Insufficient funds.")
            return
        self.__spin() # spin the roulette wheel
        winning_number = self.result.split('_')[0] # extract the winning number
        winning_number = int(winning_number)

        # check if the bet is successful
        if number == winning_number:
            prize = amount * 36
            self.fund += prize - amount
            print(f'{appelativ} is a winner for betting {amount} dollars on number {number}! You won {prize} dollars!')
        else:
            self.fund -= amount
            print(f'{appelativ} is not a winner. Winning number is {self.result}. You lost {amount} dollars.')

    # place a bet on a specific color
    def bet_on_color(self, color:str, amount: int, appelativ='Gentleman'):
        # check if the bet amount exceeds the available funds
        if amount > self.fund:
            print("Insufficient funds.")
            return
        self.__spin() # spin the roulette wheel
        winning_color = self.result.split('_')[1] # extract the winning color
        color = color[0].upper()
        color_dictionary = dict(BLACK='B', B='B', R='R', RED='R')
        color = color_dictionary[color]

        # check if the bet is successful
        if color == winning_color:
            prize = amount * 2
            self.fund += prize - amount
            print(f'{appelativ} is a winner for betting {amount} dollars on color {color}! You won {prize} dollars!')
        else:
            self.fund -= amount
            print(f'{appelativ} is not a winner. Winning number is {self.result}. You lost {amount} dollars.')

    # place a bet if number is odd or even
    def bet_on_odd_even(self, odd_even:Literal['odd', 'even'], amount: int, appelativ='Gentleman'):
        # check if the bet amount exceeds the available funds
        if amount > self.fund:
            print("Insufficient funds.")
            return
        self.__spin() # spin the roulette wheel
        winning_number = self.result.split('_')[0] # extract the winning number
        winning_number = int(winning_number)

        # check if the bet is successful
        if (odd_even == 'odd' and winning_number % 2 == 1) or (odd_even == 'even' and winning_number % 2 == 0):
            prize = amount * 2
            self.fund += prize - amount
            print(f'{appelativ} is a winner for betting {amount} dollars on {odd_even} numbers! You won {prize} dollars!')
        else:
            self.fund -= amount
            print(f'{appelativ} is not a winner. Winning number is {self.result}. You lost {amount} dollars.')

    # show current and last funds
    def show_fund(self):
        print('='*50, end='\n\n')
        print(f"Your current fund is: {self.fund} dollars")
        print(f"Your last fund was: {self.last_fund} dollars")
        print('='*50, end='\n\n')

    # update the last fund
    def update_last_fund(self):
        self.last_fund = self.fund

    # start playing the game
    def play(self):
        while True:
            # ask the player to continue or stop playing
            choice = input("Enter 'yes' to play or 'no' to stop: ")
            if choice.lower() == 'no':
                break
            elif choice.lower() == 'yes':
                self.show_fund() # show current fund
                # ask the player the type of bet 
                bet_type = input("Enter 'number', 'color', or 'odd_even' to choose the type of bet: ")
                amount = int(input("Enter the amount you want to bet: "))
                
                # place the bet based on the choosen type
                if bet_type == 'number':
                    number = int(input("Enter the number you want to bet on: "))
                    self.bet_on_number(number, amount)
                elif bet_type == 'color':
                    color = input("Enter the color you want to bet on (B for Black, R for Red): ")
                    self.bet_on_color(color, amount)
                elif bet_type == 'odd_even':
                    odd_even = input("Enter 'odd' or 'even' for the type of numbers you want to bet on: ")
                    self.bet_on_odd_even(odd_even, amount)
                else:
                    print("Invalid bet type.")
            else:
                print("Invalid choice.")

# First page of the game
print('='*50, end='\n\n')
print('''
                       _      _   _       
                | |    | | | |      
 _ __ ___  _   _| | ___| |_| |_ ___ 
| '__/ _ \| | | | |/ _ \ __| __/ _ \\
| | | (_) | |_| | |  __/ |_| ||  __/
|_|  \___/ \__,_|_|\___|\__|\__\___|
                                    
''')
print('='*50, end='\n\n')

# Example usage:
initial_fund = int(input("How much you want to play with: "))
roulette = Roulette(initial_fund=initial_fund)
roulette.play()
