print("Hello, welcome to Peak Coffee!!")

name = input("What's your name ?\n-> ")
print("Hey! "+ name + ", thank you so much for coming in today!")

menu = "1.Black Coffee,\n2.Espresso,\n3.Latte,\n4.Cappucino"
print(name + "What would you like from out menu today? Here is what we are serving.\n" + menu )
order = print(input( "->")) # for now dont use any integers

price = 5
# bc = 5, es = 10, lat = 4, cap = 7
quantity = int(input("How many coffees would you like?"))
print(input( "->"))
total = quantity * price
print("Thank you. Your total amount is: $" + str(total))

print("Sounds good " + name + ", we'll have that " + order + " ready for you in a moment.")
