from datetime import datetime
now = datetime.now()
import random

'''
create a class with two attributes, balance and interest rate. the newly 'opened' account will default to zero with an interest rate of 0.l%. implement the initializer as well as the functions.
'''


class ATM:

    def __init__(self, balance=0.0, rate=0.01):
        self.balance = balance
        self.rate = rate
        self.history = []

    def check_balance(self):
        return self.balance

    def deposit(self, input_deposit):
        self.balance += input_deposit
        self.history.append(f"You deposited {input_deposit} on {now.strftime('%Y-%m-%d at %H:%M:%S')}.")
        return self.balance

    def check_withdrawal(self, input_withdrawal):

        if self.balance >= input_withdrawal:
            self.balance -= input_withdrawal
            self.history.append(f"You withdrew {input_withdrawal} on {now.strftime('%Y-%m-%d at %H:%M:%S')}.")
        else:
            print('You don\'t have enough money in your account for this transaction. :( \n')

    def calc_interest(self):
        self.balance += self.balance * self.rate
        self.history.append(f"You calculated interest on {now.strftime('%Y-%m-%d at %H:%M:%S')}.")
        return self.balance

    def history(self):
        print('Account History:')
        for item in self.history:
            return '\t', item

    def rps():

        cpu = ['rock', 'paper', 'scissors']
        computer = random.choice(cpu)
        player = 'win'

        while player == 'win':

            player = input('Rock, paper or scissors? \n> ').lower()

            if player == computer:
                print('Its a Tie!')

            elif player == 'rock':
                if computer == 'paper':
                    print('You lose,', computer, 'covers', player)
                elif computer == 'scissors':
                    print('You win,', player, 'smashes', computer)

            elif player == 'paper':
                if computer == 'scissors':
                    print('You lose,', computer, 'cuts', player)
                else:
                    print('You win,', player, 'covers', computer)

            elif player == 'scissors':
                if computer == 'rock':
                    print('You lose,', computer, 'smashes', player)
                else:
                    print('You win,', player, 'cuts', computer)

            else:
                print('You must have entered something wrong. Please, try again!')

            player = False
            computer = random.choice(cpu)


def main():
    atm = ATM()

    print('''Please select one. Before any transaction can be made, 
    we must play a game of Rock, Paper, Scissors. If you win, proceed 
    with your transaction. If you lose, this ATM will charge you a $5 'fee'.
    
    1. check balance
    2. deposit
    3. withdraw
    4. calculate interest
    5. print history
    6. exit''')

    answer = input('What would you like to do? \n > ')

    while True:
        if answer == '1':

            rps()

            if player == win:
                print(atm.balance)
            else:
                balance -= 5

        elif answer == '2':
            input_deposit = float(input('How much would you like to deposit? \n > '))
            atm.deposit(input_deposit)
            print(f'Balance: {atm.balance}')

        elif answer == '3':
            input_withdrawal = float(input('How much would you like to withdraw? \n > '))
            atm.check_withdrawal(input_withdrawal)
            print(f'New balance: {atm.balance}')

        elif answer == '4':
            atm.calc_interest()
            print(f'At the current interest rate of 1%, your new balance is {atm.balance} in interest.')

        elif answer == '5':
            print(f'These are your past transactions:\n\t' + '\n\t'.join(atm.history))

        elif answer == '6':
            print('Exit')
            exit(0)

        else:
            print('Please input a valid response')

        answer = input('What would you like to do? \n > ')


main()