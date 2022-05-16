from datetime import datetime

class Grouping:
    def __init__(self, name, ledger=[]):
        self.name = name
        self.ledger = ledger
        self.balance = 0.0

    def __repr__(self):
        group = self.name.center(30, "*")
        new_line_group = f"{group} \n"
        bookings = ""
        for transactions in self.ledger:
            for descriptions in transactions:
                bookings += f"{descriptions[0:22]: <23} {transactions[descriptions] : >6} \n"
        total = f"Total: {self.balance}"
        return new_line_group + bookings + total

    def deposit(self, amount, description=""):
        self.ledger.append({description: amount})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.balance - amount >= 0:
            self.ledger.append({description: -1*amount})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category_instance):
        if self.withdraw(amount, f"To {category_instance.name}, {datetime.now()}"):
            category_instance.deposit(amount,  f"From {self.name}, {datetime.now()}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False
            

def create_spend_chart(groups):

    """
    Header
    """
    header = f"Percentage spent by category\n"

    """
    Chart
    """
    # Create list to store amount spent per group
    spent_amounts = []
    # Get total spent in each group
    for group in groups:
        spent = 0
        for transactions in group.ledger:
            for description in transactions:
                if transactions[description] < 0:
                    spent += abs(transactions[description])
        spent_amounts.append(round(spent, 2))

    # Calculate percentage rounded down to the nearest 10
    total = round(sum(spent_amounts), 2)
    spent_percentage = []
    for amount in spent_amounts:
        spent_percentage.append(int((amount/total)*100))

    # Add percentage spent to the chart
    chart = ""
    for current_percentage in range(100, -1, -10):
        chart += f"{current_percentage:3} |"
        for percent in spent_percentage:
            if percent >= current_percentage:
                chart += f" o "
            else:
                chart += f"   "
        chart += f" \n"

    """
    Seperator
    """
    length_footer_bar = 3*len(groups)+6
    seperator = f"{'     ':-<{length_footer_bar}}\n"

    """
    Footer
    """
    # Store names as characters in list of list
    names = []
    max_characters = 0
    for group in groups:
        characters = []
        max_characters = max(max_characters, len(group.name))
        for chars in group.name:
            characters.append(chars)
        names.append(characters)

    # Zip them together into new "words"
    zip = []
    for i in range(max_characters):
        zip_line = ""
        for name in names:
            if len(name) > i:
                zip_line += name[i]
                zip_line += "  "
            else:
                zip_line += "   " 
        zip.append(zip_line)

    # Adding footer
    footer = ""
    for word in zip:
        footer+=f"      {word}\n"

    return header + chart + seperator + footer