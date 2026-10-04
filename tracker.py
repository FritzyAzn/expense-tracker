#Project: Expense Tracker - Installment 3
#Author: Kezziah Faith C. Azaña
#Description: A simple landing page

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("[1] Add an expense\t\t(coming soon)")
print("[2] View all expenses\t\t(coming soon)")
print("[3] Show total spent\t\t(coming soon)")
print("[4] Exit\t\t\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

average = subtotal/2

tax_percent = int(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

amount1_text = f"${amount1:.1f}"
amount2_text = f"${amount2:.1f}"
subtotal_text = f"${subtotal:.1f}"
average_text = f"${average:.2f}"
tax_text = f"${tax:.1f}"
total_text = f"${total:.1f}"
left_text = f"${left:.1f}"


print(f"\n{"-" * 40}")
print("SUMMARY")
print(f"  -{item1:<20} {amount1_text}")
print(f"  -{item2:<20} {amount2_text}")
print(f"{"Subtotal:":<20}\t{subtotal_text}")
print(f"{"Average:":<20}\t{average_text}")
print(f"{"Tax (" + str(tax_percent) + "%):":<20}\t{tax_text}")
print(f"{"Grand Total:":<20}\t{total_text}")
print(f"{"Over budget?:":<20}\t{over_budget}")
print(f"{"Left in budget:":<20}\t{left_text}")
print("-" * 40)
print("Made by: Kezziah Faith C. Azaña | Installment 3")
