# is this program I will build a basic automation system to manage a coffee shop.
# I will be doing it using maximum fundamentals. So that it will be easy to revise the fundamentals.

VIP = {
    "VIP1" : "Ahnaf"
}

print("Hello, welcome to Peak Coffee!!")
name = input("What's your name?\n-> ")
print("Hey! " + name + ", thank you so much for coming in today!")

# Menu display with better formatting
menu = """Please select a coffee (1-4):
1. Black Coffee  - $5
2. Espresso     - $10
3. Latte        - $4
4. Cappuccino   - $7"""

print(menu)

# Simple input validation using while loop
while True:
    try:
        order = int(input("-> "))
        if 1 <= order <= 4:
            break
        print("Please enter a number between 1 and 4")
    except ValueError:
        print("Please enter a valid number")

# Fix quantity input
print("How many coffees would you like?")
while True:
    try:
        quantity = int(input("-> "))
        if quantity > 0:
            break
        print("Please enter a positive number")
    except ValueError:
        print("Please enter a valid number")

# Simple price calculation
prices = [5, 10, 4, 7]  # prices for each coffee type
total = prices[order - 1] * quantity

# VIP check
if name == "Ahnaf":
    print("VIP discount applied!")
    total = total * 0.8  # 20% discount

print("Thank you. Your total amount is: $" + str(total))
print("Sounds good " + name + ", we'll have your coffee ready in a moment.")
