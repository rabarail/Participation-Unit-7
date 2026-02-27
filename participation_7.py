""" Rajani Baraili, February 27th 2026
loop that prompts user to enter series of pizza toppings until they enter quit value """

topping = []
Pizza_layer = True

while Pizza_layer: 
    user_input = input("Enter the topping of your liking (or 'quit'): ")

    if user_input == "quit":
        Pizza_layer = False

    topping.append(user_input)
    if user_input != "quit":
            print("l'll add", user_input, "to your pizza")
