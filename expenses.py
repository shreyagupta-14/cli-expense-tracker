import json
import os

from datetime import datetime
#Blueprint for single item
class Expense:
    def __init__(self,expense_id, name, amount , category, date = None):
        self.expense_id = expense_id
        self.name= name
        self.category = category
        self.amount = amount
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def to_dict(self):
        # Convert this object's data into a standard Python dictionary
        return {
            "id" : self.expense_id,
            "name" : self.name,
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        } 

#Manager - manages collection of expenses
class ExpenseTracker:
    def __init__(self, filename= "expenses.json"):
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, 'w')as file:
                json.dump([], file)
    
    def load_raw_data(self):
        with open (self.filename, 'r') as file:
            return json.load(file)
    
    def save_raw_data(self, data):
        with open (self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def add_expense( self, name, amount, category):
        data= self.load_raw_data()
        
        if len(data) == 0:
            next_id =1
        else:
            next_id = data[-1]['id'] + 1

        # Creating new instance of Expense
        new_expense = Expense(next_id, name, amount, category) 
        data.append(new_expense.to_dict())

        self.save_raw_data(data)
        print(f"💰 Expense added successfully! (ID: {next_id})")
    
    def view_expense(self, category = None):
        data = self.load_raw_data()

        for item in data:
            if item['category'] == category.lower:
                return(item)
            
    def get_total(self, month = None):
        data= self.load_raw_data()
        total_amount = 0
        
        month_map = {
            "january": "-01-", "february": "-02-", "march": "-03-", 
            "april": "-04-", "may": "-05-", "june": "-06-", 
            "july": "-07-", "august": "-08-", "september": "-09-", 
            "october": "-10-", "november": "-11-", "december": "-12-"
        }

        target_pattern = None
        if month:
            target_pattern = month_map.get(month.lower())
            if not target_pattern:
                print(f"⚠️ Warning: '{month}' is not a valid month name.")
                return 0
            
        for item in data:
            if target_pattern is None:
                total_amount += item['amount']
            else:
                if target_pattern in item['date']:
                    total_amount += item['amount']
        return total_amount
    
    def delete_expense(self, expense_id):
        data= self.load_raw_data()

        id_exists = any(item['id'] == expense_id for item in data)

        if not id_exists:
            print(f"❌ Error: ID {expense_id} doesn't exist.")
            return
        
        updated_data = (item for item in data if item['id'] != expense_id) 
        self.save_raw_data(updated_data)
        print(f"🗑️ Expense ID {expense_id} deleted successfully!")


