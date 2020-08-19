# Discussion Questions
# 2. Construct a class hierarchy for bank accounts

# My base account can hold all of the account behaviors
class BaseAccount:
    interest_rate = None

    def __init__(self, starting_deposit):
        self.balance = starting_deposit
    
    def calculate_monthly_interest(self):
        monthly_interest = self.balance * self.interest_rate
        return monthly_interest


# more specific accounts can hold th data that is unique to that account
class Checking(BaseAccount):
    # class attribute
    interest_rate = 0.1

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance


class Savings(BaseAccount):
    interest_rate = 1.0

    def withdraw(self, amount):
        if amount > 100: 
            return "Your withdraw cannot exceet 100" 
        self.balance = self.balance - amount
        return self.balance


checking = Checking(20)
savings = Savings(40)