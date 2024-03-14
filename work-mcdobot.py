# MCDOBOT
# Lucas Zhang
# Feb 22 2024

# Ask the user what do they want to have fries with their meals
food = input("Do you like fries with you meal? (Yes/No)")

# Respond
if food.lower().strip(" !,.><?@#$%^&*()_+=-/`~") == "yes":
    print("Here's your meal with fries!")
elif food.lower().strip(" !,.><?@#$%^&*()_+=-/`~") == "no":
    print("Here's your meal without fries!")
else:
    print(f"Sorry, I don't understand {food}.")

# ~ Finale ~