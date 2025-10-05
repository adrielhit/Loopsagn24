def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")

menu_items = ["Taco", "Burrito", "Nachos", "Drink"]
prices = [3.00, 4.50, 5.25, 1.75]

ordered = []
total = 0.0

print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

while True:
    print_menu()
    choice = int(input("Your selection: "))
    if choice == 5:
        break
    elif 1 <= choice <= 4:
        print("You selected a " + menu_items[choice - 1])
        ordered.append(menu_items[choice - 1])
        total += prices[choice - 1]

if ordered:
    if len(ordered) == 1:
        print(f"You ordered a {ordered[0]}. Your total is ${total:.2f}")
    else:
        print(f"You ordered a {', '.join(ordered[:-1])} and a {ordered[-1]}. Your total is ${total:.2f}")
else:
    print("No items ordered. Goodbye!")
