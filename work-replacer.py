# REPLACER
# Lucas Zhang
# Feb 27 2024

# Create a function called replacer
# Accpets a string
# Replace all 100 with 💯
# Replace all noodles with 🍜
# Return the result
def translate(text):
    text = text.replace("100","💯")
    text = text.replace("noodles","🍜")
    return text

# Create a function called main
# Prompt the user  to type something in
# Use the translate on the user input
# Print the result
def main():
    user_input = input("Enter your text: ")
    translated_text = translate(user_input)
    print("Translated_Text: ",translated_text)


# Test
