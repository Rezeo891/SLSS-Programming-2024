# String Methods
# Lucas
# Feb 22 2024

# Type Python3 in terminal to enter special mode to check codes & more

# Ask the user what the weather is like
weather = input("What's the weather like?")

# If they reply rainy
    # Bring an umbrella
if weather.lower().strip("!.?, ") == "rainy":
    print("You will need an umberlla.")
else:
    print("Sorry, I don't understand.")
