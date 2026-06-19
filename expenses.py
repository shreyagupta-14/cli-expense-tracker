# =====================================================================
# CLI EXPENSE TRACKER - INITIAL ARCHITECTURE SPEC
# =====================================================================

# 1. INITIALIZE DATA STRUCTURES
# An empty list to hold our expense records. Each record will be a 
# dictionary: {"date": str, "category": str, "amount": float, "description": str}
#INITIALIZE expense_list AS AN EMPTY LIST
#INITIALIZE categories AS A LIST OF STRINGS ["Food", "Transport", "Leisure", "Bills", "Other"]

# 2. DEFINE CORE FUNCTIONS
'''
FUNCTION add_expense():
    PRINT "--- Add New Expense ---"
    INPUT amount AS FLOAT
    INPUT category AS STRING
    INPUT description AS STRING
    GET current_date AS STRING (or input manually)
    
    # Validation check
    IF category NOT IN categories:
        PRINT "Invalid category! Defaulting to 'Other'."
        SET category = "Other"
    
    # Create the record dictionary
    CREATE expense_record = {
        "date": current_date,
        "category": category,
        "amount": amount,
        "description": description
    }
    
    APPEND expense_record TO expense_list
    PRINT "Expense added successfully!"


FUNCTION view_expenses():
    PRINT "--- All Expense Records ---"
    IF expense_list IS EMPTY:
        PRINT "No expenses recorded yet."
        RETURN
        
    FOR each record IN expense_list:
        PRINT record["date"] | record["category"] | record["amount"] | record["description"]


FUNCTION calculate_total():
    INITIALIZE total = 0.0
    FOR each record IN expense_list:
        total = total + record["amount"]
    PRINT "Total Amount Spent: " + total


# 3. MAIN APPLICATION LOOP (CLI MENU INTERFACE)

LOOP FOREVER:
    PRINT "\n===== EXPENSE TRACKER MENU ====="
    PRINT "1. Add an Expense"
    PRINT "2. View All Expenses"
    PRINT "3. Show Total Spending"
    PRINT "4. Exit"
    
    INPUT user_choice AS STRING
    
    IF user_choice == "1":
        CALL add_expense()
    ELSE IF user_choice == "2":
        CALL view_expenses()
    ELSE IF user_choice == "3":
        CALL calculate_total()
    ELSE IF user_choice == "4":
        PRINT "Exiting application. Goodbye!"
        BREAK LOOP
    ELSE:
        PRINT "Invalid option selected. Please try again."
'''