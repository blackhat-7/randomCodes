
class ATM:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.history = []

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.history.append('Deposited $'+str(deposit_amount))
        print("Deposited $"+str(deposit_amount))

    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount
        self.history.append('Withdrew $'+str(withdraw_amount))
        print("Withdrew $"+str(withdraw_amount))

    def check_balance(self):
        print("Your current balance is:", self.balance)

    def check_history(self):
        print('History:')
        print(self.history)

hsbc_atm = ATM(initial_balance=1000)

hsbc_atm.withdraw(withdraw_amount=100)
hsbc_atm.check_balance()
hsbc_atm.deposit(deposit_amount=300)
hsbc_atm.withdraw(withdraw_amount=1000)
hsbc_atm.check_balance()
hsbc_atm.check_history()
hsbc_atm.withdraw(withdraw_amount=500)
hsbc_atm.check_history()


'''
Outputs:

You deposited $1000.
You withdrew $100.
Your current balance is: 900
You deposited $300.
You withdrew $1000.
Your current balance is: $200
Your history:
Deposited $1000, Withdrew $100, Deposted $300, Withdrew $1000
Insufficient funds. Your current balance is $200 only.
Deposited $1000, Withdrew $100, Deposted $300, Withdrew $1000

'''
