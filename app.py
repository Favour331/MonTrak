from datetime import date

from database import insertTable,retriveMonth,retriveDate,createTables


print("Welcome. What do you want to do today")
keeprunning = True
while (keeprunning):
    try:
        createTables()
        print("Enter 1 to record an expense")
        print("Enter 2 to see monthly expense")
        print("Enter 3 to check a specific date")
        print("Enter 4 to quit")
        reply = int(input("Enter your answer here: "))
        if reply == 1:
            reply2 = int(input("Enter the amount made: "))
            reply3 = int(input("Enter the amount spent: "))
            if reply2 and reply3:
                insertTable(reply2,reply3)
                print("Expense saved to database\n")
            else:
                print("Field cannot be empty")
        elif  reply == 2:
            month_reply = int(input("Enter month in digit: "))
            if 1 <= month_reply <= 12:
                expenses = retriveMonth(month_reply)
                if expenses:
                    print("Monthly expenses:")
                    for expense in expenses:
                        print(
                            f"Date: {expense['date']} | "
                            f"Money made: {expense['Money_made']} | "
                            f"Money spent: {expense['Money_spent']}"
                        )
                else:
                    print("No expenses found for that month.")
            else:
                print("Month must be a number from 1 to 12.")
        elif reply == 3:
            mon_reply = int(input("Enter month in digit: "))
            date_reply = int(input("Enter date: "))
            if 1 <= mon_reply <= 12:
                selected_date = date(date.today().year, mon_reply, date_reply)
                expenses = retriveDate(selected_date)
                if expenses:
                    print(f"Expenses for {selected_date}:")
                    for expense in expenses:
                        print(
                            f"Money made: {expense['Money_made']} | "
                            f"Money spent: {expense['Money_spent']}"
                        )
                else:
                    print("No expenses found for that date.")
            else:
                print("Month must be a number from 1 to 12.")
        elif reply == 4:
            print("...Goodbye!!!...\n")
            break

        else:
            break
    except Exception as e:
        print(e)