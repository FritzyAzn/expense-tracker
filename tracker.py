#Project: Expense Tracker - Installment 2
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

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total: float = amount1 + amount2
average = float(total)/2

amount1_text = f"${amount1:.1f}"
amount2_text = f"${amount2:.1f}"
total_text = f"${total:.1f}"
average_text = f"${average:.2f}"

print(f"\n{"-" * 40}")
print("SUMMARY")
print(f"{item1:<20}{amount1_text:>10}")
print(f"{item2:<20}{amount2_text:>10}")
print(f"{"Total spent:":<20}{total_text:>10}")
print(f"{"Average:":<20}{average_text:>10}")
print("-" * 40)
print("Made by: Kezziah Faith C. Azaña | Installment 2")
