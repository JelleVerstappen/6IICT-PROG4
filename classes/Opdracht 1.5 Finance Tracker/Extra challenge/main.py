# This file should be used to show the implementation of finance.py 
# For instructions read the README.md
import finance
from finance import create_spend_chart

hobby = finance.Grouping("hobby")
travel_expenses = finance.Grouping("Travel Expenses")
animals = finance.Grouping("animals")

hobby.deposit(500, "Initial deposit")
travel_expenses.deposit(1000, "Initial deposit")
animals.deposit(1500, "Initial deposit")

hobby.withdraw(100)
hobby.withdraw(200)
hobby.withdraw(300)

travel_expenses.withdraw(300, "Brussel")
travel_expenses.withdraw(150, "Maasmechelen")
travel_expenses.withdraw(800, "Parijs")

animals.withdraw(400, "Operatie van de kat, dit om zijn darmen na te kijken")
animals.withdraw(50, "Speciaal voer voor de kat om zijn darmen")

animals.transfer(500, travel_expenses)

travel_expenses.withdraw(800, "Parijs")
animals.withdraw(200, "Speciaal voer voor de hond")

print(hobby)
print(travel_expenses)
print(animals)

# print(create_spend_chart([hobby, travel_expenses, animals]))