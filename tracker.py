#Project: Expense Tracker - Installment 5
#Author: Kezziah Faith C. Azaña

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

name = input("\nWhat's your name? ")
tax_percent = int(input("Tax rate %? "))
budget = float(input("Your budget? "))

print(f"Welcome, {name}!")

subtotal = 0
expense_count = 0

print("\nMAIN MENU")
print("[1] Add an expense")
print("[2] View all expenses (coming soon)")
print("[3] Show total spent")
print("[4] Exit")

while True:
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        expense_count += 1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left = budget - total

        print("\nSUMMARY")
        print(f"{"Expenses: "}{expense_count:>0}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax ({tax_percent}%): ${tax:.2f}")
        print(f"Grand total: ${total:.2f}")

        if total > budget:
           over = total - budget
           print(f"Over budget by ${left:.1f} left.")
        elif total > budget * 0.90:
            print(f"Careful: only ${left:.1f} left.")
        else:
            print(f"Within budget. ${left:.1f} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: Kezziah Faith C. Azaña | Installment 5")
        print("-" * 40)
        break

    else:
        print("Please choose 1, 2, 3, or 4.") 