class Grouping:
    def __init__(self, name, ledger = [], balance = 0):
        self.name = name
        self.ledger = ledger
        self.balance = balance

    def __repr__(self):
        header = self.name.center(30, "*")
        trans = ""
        for dictionaries in self.ledger:
            for desc, value in dictionaries.items():
                trans += f"{desc[:22]: <22} {value: >6}\n"
        return f"{header}\n{trans}\nTotal: {self.balance}"
        

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True

    def deposit(self, amount, description):
        self.ledger.append({description : amount})
        self.balance = self.balance + amount
    
    def withdraw(self, amount, description="No description"):
        if amount <= self.balance:
            neg_amount = -amount
            self.ledger.append({description: -amount})
            self.balance = self.balance - amount
            return True
        if amount > self.balance:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            description_src = f"Transfer to {destination.name}"
            description_dest = f"Transfer from {self.name}"

            self.withdraw(amount, description_src)
            destination.deposit(amount, description_dest)
            return True
        return False
        

        

            

def create_spend_chart(groups):
    pass