class VendingMachine:
    def __init__(self):
        self.balance = 0
        self.amount = 0
        self.transactions = []
        self.items = []
        self.codes = {}

    def insert_money(self, money):
        self.balance += money
        return self.balance




m = VendingMachine()
print(m.balance)

m.insert_money(10)
m.insert_money(10)

print(m.balance)