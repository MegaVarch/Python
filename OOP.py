class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Declined: insufficient funds")
        else:
            self.balance -= amount
        
    def show(self):
        print(f"{self.owner}: {self.balance}")

class Savings_Account(Account):
    def __init__(self, owner, balance=0, rate=0.05):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.balance += self.balance * self.rate

    def withdraw(self, amount):
        super().withdraw(amount + 2)

class CurrentAccount(Account):
    def withdraw(self, amount):
        if self.balance - amount < -500:
            print("Declined: overdraft limit")
        else:
            self.balance -= amount
        

a = Account("Ravi", 500)
a.show()
a.deposit(200)
a.show()
a.withdraw(900)
a.show()
a.deposit(300)
a.show()

s=Savings_Account("Priya", 1000)
s.show()
s.add_interest()
s.show()
s.withdraw(100)
s.show()

c = CurrentAccount("Amit", 100)
c.withdraw(500)
c.show()
c.withdraw(500)
c.show()

accounts = [a, s, c]

for acc in accounts:
    acc.show()

for acc in accounts:
    acc.deposit(100)
    acc.show()

b = Account("Test", 100)

while b.balance > 0:
    b.withdraw(30)
    b.show()

while b.balance >= 30:
    b.withdraw(30)
    b.show()