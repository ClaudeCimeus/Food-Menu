# Claude Cimeus
# 2/7/15
# Restaurant

### End of header ###

### Dictionary that holds the values of the menu ###

menuitem = {
    "Chicken Strips": 3.50,
    "French Fries": 2.50,
    "Hamburger": 4.00,
    "Hotdog": 3.50,
    "Large Drink": 1.75,
    "Medium Drink": 1.50,
    "Milk Shake": 2.25,
    "Salad": 3.75,
    "Small Drink": 1.25,
    "Cheese Burger": 4.50,
    "Steak": 7.60,
    "Fried Rice": 6.50
}
### End of Dictionary ###


### Functions that hold the values of the Specials ###
def special1(food1):
        return ("Steak")
        return ("Salad")
        return ("Small Drink")


def special2(food2):
    if food2 in special2(food2) == menuitem:
        print (menuitem["Cheese Burger"])
        print (menuitem["French Fries"])
        print(menuitem["Medium Drink"])
    else:
        print ("This food is not available")

def special3(food3):
    if food3 in special3(food3) == menuitem:
        print (menuitem["Milk Shake"])
        print (menuitem["French Fries"])
    else:
        print ("This food is not available")
### End of functions ###



### Greetings and user interaction ###
print ("Welcome to Restaurant! Where you can order virtually! Press Enter to continue.")

input()

userInput = input("Enter your preferred Special or Would you like to sit in? (Enter 'Sit in')")

if userInput == "Special 1":
    print (special1)

if userInput == "Special 2":
    print (special2)

if userInput == "Special 3":
    print (special3)

elif userInput == ("Sit in"):
    print ("Great! Here's the general menu ")

print (menuitem)


### End of greetings and user interaction ###
















