import os
import datetime

def add_expense(category, amount):
    timestamp=datetime.datetime.now().strftime("%Y-%m-%d-%H:%S")
    entry=f" {timestamp}| {category} | ${amount}\n"
    with open("expenses.txt", "a") as file: file.write(entry)
    print("Expense added successfully.")

    def view_expenses():
        try:
            with open ("expenses.txt", "r")as file:
                expenses=file.readlines()
                if not expenses:
                    print("No expenses recorded.")
                else:
                    print("Timestamp | category | Amount")
                print("------------------------------------------------------------------")
                for expense in expenses:
                    print(expense.rstrip())
        except FileNotFoundError:
                add_expense("Food",20)
                add_expense("Transportation", 30)
                view_expenses()    