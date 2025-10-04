from expense import Expense

def main():
    print("Welcome to expense tracker")
    expense_file_path = "expenses.csv"
    # get user input
    expense = user_input()
    print(expense)
    # write the input to a file
    write_input_file(expense, expense_file_path)
    # read the input from the file
    read_input(expense_file_path, budget = 2000)

def user_input():
    print("This is user input.")
    expense_name = input("What is it: ")
    expense_value = float(input("Amount used: "))
    
    expense_category = ['Food', 'Rent', 'Work', 'Fun', 'Misc']

    while True:
        print("Select a category:")
        for i, category_name in enumerate(expense_category, start=1):
            print(f"{i}. {category_name}")

        value = f"[1 - {len(expense_category)}]"
        selected_input = int(input(f"Enter a category {value}: "))

        # Check that user input is in 1..len
        if 1 <= selected_input <= len(expense_category):
            # convert to zero-based index
            selected_category = expense_category[selected_input - 1]
            new_expense = Expense(name=expense_name,
                                  category=selected_category,
                                  money=expense_value)
            return new_expense
        else:
            print("Invalid category, please try again.")

def write_input_file(expense: Expense, expense_file_path: str):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    # open in append mode
    with open(expense_file_path, "a") as f:
        # write without extra spaces after commas
        f.write(f"{expense.name},{expense.category},{expense.money}\n")

def read_input(expense_file_path: str, budget: float):
    print("Here we read value from the file.")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_money_str = line.strip().split(",")
            # Convert money to float
            expense_money = float(expense_money_str)
            line_expense = Expense(name=expense_name,
                                   category=expense_category,
                                   money=expense_money)
            expenses.append(line_expense)

    amount_by_category: dict[str, float] = {}
    for exp in expenses:
        key = exp.category
        if key in amount_by_category:
            amount_by_category[key] += exp.money
        else:
            amount_by_category[key] = exp.money

    print("Amount by category:", amount_by_category)

    total_spend = sum(x.money for x in expenses)
    print(f"Total spent: {total_spend}")
    rem_budget = budget - total_spend
    print(f"Remaining amount: {rem_budget:.2f}")

if __name__ == "__main__":
    main()
