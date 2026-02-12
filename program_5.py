# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
   total_expenses = 0.0

    monthly_budget = float(input("Enter your monthly budget: "))
    number_of_expenses = int(input("Enter the number of expenses: "))

    for i in range(1, number_of_expenses + 1):
        expense = float(input(f"Enter expense #{i}: "))
        total_expenses += expense

    print("\n------------------------------")

    if total_expenses > monthly_budget:
        difference = total_expenses - monthly_budget
        print(f"You are OVER budget by ${difference:.2f}")
    elif total_expenses < monthly_budget:
        difference = monthly_budget - total_expenses
        print(f"You are UNDER budget by ${difference:.2f}")
    else:
        print("You met your budget exactly!")

    print("------------------------------")
    ######################


if __name__ == '__main__':
    main()
